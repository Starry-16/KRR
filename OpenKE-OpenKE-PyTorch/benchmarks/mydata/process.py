with open("./entity2id.txt", "r") as f:
    
    data = []
    for line in f:
        # 假设文件中的每行数据有两个字段，用空格分隔
        items = line.strip().split(" ")
        data.append((items[0], int(items[1])))

    for item in data:
        print(f"{item[0]:<30}{item[1]}")