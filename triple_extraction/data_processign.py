import csv
import json


'''数据处理：清除空列表，将列表转化为字典存在json文件中'''
def data_process(extractor):
    with open('./data/csv/total.csv', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        list1=[]
        for row in csv_reader:
            svos = extractor.triples_main(row[0])
            if len(svos)==1:
                list1.append(svos[0])
            elif len(svos)>1:
                for item in svos:
                    list1.append(item)

        with open('./data/json/primary_data.json', 'w',encoding='utf-8') as f:
            for data in list1:
                dict1={"triple": data}
                json.dump(dict1, f, ensure_ascii=False)
                f.write('\n')


# with open('./data/json/primary_data2.json', mode='r', encoding='utf-8') as f:
#     content = f.readlines()
#     json_data_list = []
#     buffer = ""
#     for line in content:
#         print(line)
#         json_data_list.append(line)
#         buffer = ""
#         print(json_data_list)

    
