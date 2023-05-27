#### 查询tail

MATCH (head)-[rel]->(tail)
WHERE head.name = "'威少和湖人'" AND rel.type = "说"
RETURN head, rel, tail

####  查询head

MATCH (head)-[rel]->(tail)
WHERE tail.name = " '大雾黄色预警'" AND rel.type = '解除'
RETURN head, rel, tail

#### 查询关系

MATCH (head)-[rel]->(tail)
WHERE tail.name = " '勇士'" AND head.name = "'湖人'"
RETURN head, rel, tail