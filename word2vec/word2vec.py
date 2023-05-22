from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import pandas as pd
import jieba
import gensim
import sys
sys.stdout.reconfigure(encoding='utf-8')

df = pd.read_csv('./data/csv/total.csv')
df.info()

with open('./data/txt/data.txt','+w',encoding='utf-8') as f:
    for sentence in df['title']:
        sentence_list = jieba.cut(sentence, cut_all = False)
        word = " ".join(sentence_list)
        f.writelines(word + '\n')

model = Word2Vec(
    LineSentence(open('./data/txt/data.txt', 'r', encoding='utf8')),
    sg = 0,
    vector_size = 100,
    window = 3,
    min_count = 5,
    workers=8
)
 
# 词向量保存
model.wv.save_word2vec_format('./vector/data.vector', binary=False)
 
# 模型保存
model.save('./model/test.model')

# 1 通过模型加载词向量(recommend)
model = gensim.models.Word2Vec.load('./model/test.model')

dic = model.wv.index_to_key
print(dic)
print(len(dic))
print(model.wv.vectors.shape)

# print(model.wv['提供'])
print(model.wv.most_similar('乌克兰', topn=10))