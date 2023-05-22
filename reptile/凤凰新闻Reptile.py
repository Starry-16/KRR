from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

def get_response(url,tag):
    response=urlopen(url)
    soup=BeautifulSoup(response.read(),"lxml")
    result=soup.find_all(tag)
    data=list()
    for a in result:
        if a:
            if a.text and len(a.text)>3: #过滤导航栏
                row=dict()
                row['title']=a.text
                row['href']=a.get('href')
                data.append(row)
    return data


def export_excel(data):
    # 将字典转换为DataFrame
    pf=pd.DataFrame(data)
    order=['title','href']
    pf=pf[order]

    # 将列名替换为中文
    columns_map={
        'title':'标题',
        'href':'链接'
    }
    pf.rename(columns=columns_map,inplace=True)
    # 指定生成的Excel表格名称
    file_path='./data/csv/凤凰新闻.csv'
    # 替换空单元格s
    pf.fillna('',inplace=True)
    # 输出
    pf.to_csv(file_path, index=False, encoding='utf-8-sig')  # 设置编码为 utf-8-sig 避免中文乱码


if __name__ == "__main__":
    url='https://www.ifeng.com/'
    tag='a'

    data=get_response(url,tag)
    export_excel(data)