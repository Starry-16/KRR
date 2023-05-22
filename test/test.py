import os
from pyltp import Segmentor, Postagger, Parser

# 加载LTP模型
LTP_DATA_DIR = 'D:/desktop/KRR/myself/model/ltp_data_v3.4.0'  # LTP模型文件所在的文件夹路径

cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为cws.model
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为pos.model
par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为parser.model

segmentor = Segmentor(cws_model_path)  # 加载分词模型
postagger = Postagger(pos_model_path)  # 加载词性标注模型
parser = Parser(par_model_path)  # 加载依存句法分析模型



# 定义事件规则
rules = [
    {
        'pattern': '<S-NP>*<S-VP>',  # 规则1：以名词短语开头，以动词短语结尾
        'args': [
            {'type': 'ORG', 'pos': ['ni', 'nh', 'nt', 'nz']},  # 组织机构
            {'type': 'PER', 'pos': ['nh', 'ni']},  # 人名
            {'type': 'DATE', 'pos': ['nt']}  # 日期
        ]
    },
    {
        'pattern': '<S-NP>*<S-VP>',  # 规则2：以名词短语开头，以动词短语结尾
        'args': [
            {'type': 'LOC', 'pos': ['ns']},  # 地名
            {'type': 'DATE', 'pos': ['nt']}  # 日期
        ]
    }
]

# 中文事件提取函数
def extract_event(text):
    words = segmentor.segment(text)  # 分词
    postags = postagger.postag(words)  # 词性标注
    arcs = parser.parse(words, postags)  # 依存句法分析

    events = []
    for r in rules:
        pattern = r['pattern']
        args = r['args']
        for i in range(len(words)):
            # 从每个词开始，尝试匹配规则
            if pattern.startswith(postags[i]):
                j = i
                k = 0
                while j < len(words) and k < len(pattern):
                    # 按规则模板匹配
                    if pattern[k].startswith('<'):
                        t = pattern[k][1:-1].split('-')
                        s = ''
                        for m in range(j, len(words)):
                            s += postags[m] + '/'
                            if s.startswith(t[1] + '-'):
                                if t[0] == 'S':
                                    break
                                elif s.startswith(t[0] + '-'):
                                    if k == len(pattern) - 1:
                                        events.append({'type': args[0]['type'], 'text': words[i:j+1]})
                                    else:
                                        break
                            elif s.startswith(t[0] + '-'):
                                break
                        j = m + 1
                        k += 1
                    else:
                        if words[j] != pattern[k]:
                            break
                        j += 1
                        k += 1

    return events



# 使用示例
text = '北京时间2023年5月18日，人工智能在医疗行业的一项研究成果于5月18日发表在《Nature》杂志上。该项研究表明，使用人工智能辅助医生诊断'
events = extract_event(text)
print(events)

# 释放LTP模型
segmentor.release()
postagger.release()
parser.release()