from py2neo import Graph, NodeMatcher, RelationshipMatcher 

graph = Graph('http://localhost:7474', auth=("neo4j", "123456"))

# 创建 NodeMatcher 和 RelationshipMatcher 对象
node_matcher = NodeMatcher(graph)
rel_matcher = RelationshipMatcher(graph)

exit = 0

while(exit != 1):
    print("--------------------------------------------------------")
    print("请输入你要查询的方式：\n")
    print("1. 输入头节点和关系，  查询尾节点\n")
    print("2. 输入关系和尾节点，  查询头节点\n")
    print("3. 输入头节点和尾节点，查询关系\n")

    mode = eval(input("请输入1或2或3:"))
    
    if mode == 1:
        print("--------------------------------------------------------")
        head = str(input("请输入你要查询的头节点："))
        relation = str(input("请输入你要查询的关系："))
        
        head_node = node_matcher.match("head", name=head).first()
        if head_node:
            relations = rel_matcher.match((head_node, None))
            for rel in relations:
                if rel['type'] == relation:
                    tail_name = rel.end_node['name']
                    rel_type = rel['type']
                elif type(rel).__name__ == "BELONGS_TO":   
                    tail_name = rel.end_node['name'] 
                    rel_type = "属于"
                print("--------------------------------------------------------")    
                print(head_node['name'], rel_type, tail_name)
        
        print("--------------------------------------------------------")
        exit = int(input("是否退出，若是输入1，否则输入0:"))
    elif mode == 2:
        print("--------------------------------------------------------")
        tail = str(input("请输入你要查询的尾节点："))
        relation = str(input("请输入你要查询的关系："))
        
        tail_node = node_matcher.match("tail", name=tail).first()
        if tail_node:
            relations = rel_matcher.match((None, tail_node))
            for rel in relations:
                if rel['type'] == relation:
                    head_name = rel.start_node['name']
                    rel_type = rel['type']
                    print("--------------------------------------------------------")    
                    print(head_name, rel_type, tail_node['name'])
        
        print("--------------------------------------------------------")
        exit = int(input("是否退出，若是输入1，否则输入0:"))
    elif mode == 3:
        print("--------------------------------------------------------")
        head = str(input("请输入你要查询的头节点："))
        tail = str(input("请输入你要查询的尾节点："))
        
        head_node = node_matcher.match("head", name=head).first()
        tail_node = node_matcher.match("tail", name=tail).first()
        if head_node and tail_node:
            relations = rel_matcher.match((head_node, tail_node))
            for rel in relations:
                head_name = head_node['name']
                tail_name = tail_node['name']
                rel_type = rel['type']
                print("--------------------------------------------------------")    
                print(head_name, rel_type, tail_name)
        
        print("--------------------------------------------------------")
        exit = int(input("是否退出，若是输入1，否则输入0:"))
    else:
        print("--------------------------------------------------------")
        mode = eval(input("请输入1或2或3:"))
