import os
from pyltp import Segmentor, Postagger, Parser, NamedEntityRecognizer, SementicRoleLabeller


class LtpParser:
    def __init__(self):
        LTP_DIR = "./model/ltp_data_v3.4.0"
        self.segmentor = Segmentor(os.path.join(LTP_DIR, "cws.model"))

        self.postagger = Postagger(os.path.join(LTP_DIR, "pos.model"))

        self.parser = Parser(os.path.join(LTP_DIR, "parser.model"))

        self.recognizer = NamedEntityRecognizer(os.path.join(LTP_DIR, "ner.model"))

        self.labeller = SementicRoleLabeller(os.path.join(LTP_DIR, 'pisrl.model'))  #快
        # self.labeller = SementicRoleLabeller(os.path.join(LTP_DIR, 'pisrl_win.model'))  #慢

    '''语义角色标注'''
    def format_labelrole(self, words, postags):
        arcs = self.parser.parse(words, postags)
        roles = self.labeller.label(words, postags, arcs)
        roles_dict = {}
        for role in roles:
            roles_dict[role.index] = {arg[0]:[arg[0],arg[1][0], arg[1][1]] for arg in role[1]}
        return roles_dict

    '''句法分析---为句子中的每个词语维护一个保存句法依存儿子节点的字典'''
    def build_parse_child_dict(self, words, postags, arcs):
        child_dict_list = []
        format_parse_list = []

        for index in range(len(words)):
            child_dict = dict()
            for arc_index in range(len(arcs)):
                if arcs[arc_index][0] == index+1:   #arcs的索引从1开始
                    if arcs[arc_index][1] in child_dict:
                        child_dict[arcs[arc_index][1]].append(arc_index)
                    else:
                        child_dict[arcs[arc_index][1]] = []
                        child_dict[arcs[arc_index][1]].append(arc_index)
            child_dict_list.append(child_dict)
        rely_id = [arc[0] for arc in arcs]  # 提取依存父节点id
        relation = [arc[1] for arc in arcs]  # 提取依存关系
        heads = ['Root' if id == 0 else words[id - 1] for id in rely_id]  # 匹配依存父节点词语
        for i in range(len(words)):
            # ['ATT', '李克强', 0, 'nh', '总理', 1, 'n']
            a = [relation[i], words[i], i, postags[i], heads[i], rely_id[i]-1, postags[rely_id[i]-1]]
            format_parse_list.append(a)

        return child_dict_list, format_parse_list

    '''parser主函数'''
    def parser_main(self, sentence):
        words = list(self.segmentor.segment(sentence))
        postags = list(self.postagger.postag(words))
        arcs = self.parser.parse(words, postags)
        child_dict_list, format_parse_list = self.build_parse_child_dict(words, postags, arcs)
        roles_dict = self.format_labelrole(words, postags)
        return words, postags, child_dict_list, roles_dict, format_parse_list


if __name__ == '__main__':
    parse = LtpParser()
    sentence = '李克强总理今天来我家了,我感到非常荣幸'
    words, postags, child_dict_list, roles_dict, format_parse_list = parse.parser_main(sentence)
    print(words, len(words))
    print(postags, len(postags))
    print(child_dict_list, len(child_dict_list))
    print(roles_dict)
    print(format_parse_list, len(format_parse_list))