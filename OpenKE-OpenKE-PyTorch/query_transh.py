from openke.config import Trainer,Tester
from openke.module.model import TransH
from openke.module.loss import MarginLoss
from openke.module.strategy import NegativeSampling
from openke.data import TrainDataLoader, TestDataLoader
import numpy as np
import random

entity = []
relation = []
with open('./benchmarks/mydata/data.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        list_l = eval(line)
        entity.append(list_l[0])
        entity.append(list_l[2])
        relation.append(list_l[1])
        
entity_clean = list(set(entity))
relation_clean = list(set(relation))
entity_clean.sort(key=entity.index)
relation_clean.sort(key=relation.index)
entity_enc = dict() 
relation_enc = dict() 
for idx, e in enumerate(entity_clean):
    entity_enc[e] = idx
for idx, r in enumerate(relation_clean):
        relation_enc[r] = idx

train_dataloader = TrainDataLoader(
	in_path = './benchmarks/mydata/', 
	nbatches = 100,
	threads = 8, 
	sampling_mode = "normal", 
	bern_flag = 1, 
	filter_flag = 1, 
	neg_ent = 25,
	neg_rel = 0,
)
test_dataloader = TestDataLoader("./benchmarks/mydata/", "link") 

transh = TransH(
	ent_tot = train_dataloader.get_ent_tot(),
	rel_tot = train_dataloader.get_rel_tot(),
	dim = 200, 
	p_norm = 1, 
	norm_flag = True)

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
        
        head_index = entity_enc.get(head)
        relation_index = relation_enc.get(relation)
        tail_index = random.randint(0, len(entity_enc))

        with open("./benchmarks/mydata/test2id.txt", "w") as f:
            f.write(str(1) + '\n')
            f.write(str(head_index) + ' ' + str(tail_index) + ' ' + str(relation_index))
        with open("./benchmarks/mydata/valid2id.txt", "w") as f:
            f.write(str(1) + '\n')
            f.write(str(head_index) + ' ' + str(tail_index) + ' ' + str(relation_index))
        
        test_dataloader = TestDataLoader("./benchmarks/mydata/", "link") 
        transh.load_checkpoint('./checkpoint/transh.ckpt')
        tester = Tester(model = transh, data_loader = test_dataloader, use_gpu = True)
        score_tail_index = tester.tail_query(type_constrain = False)

        print("--------------------------------------------------------")    
        print(head, relation, entity_clean[score_tail_index[0][0]])
        
        print("--------------------------------------------------------")
        exit = int(input("是否退出，若是输入1，否则输入0:"))
    elif mode == 2:
        print("--------------------------------------------------------")
        tail = str(input("请输入你要查询的尾节点："))
        relation = str(input("请输入你要查询的关系："))
        
        head_index = 0
        relation_index = relation_enc.get(relation)
        tail_index = entity_enc.get(tail)

        with open("./benchmarks/mydata/test2id.txt", "w") as f:
            f.write(str(1) + '\n')
            f.write(str(head_index) + ' ' + str(tail_index) + ' ' + str(relation_index))
        with open("./benchmarks/mydata/valid2id.txt", "w") as f:
            f.write(str(1) + '\n')
            f.write(str(head_index) + ' ' + str(tail_index) + ' ' + str(relation_index))
        
        test_dataloader = TestDataLoader("./benchmarks/mydata/", "link") 
        transh.load_checkpoint('./checkpoint/transh.ckpt')
        tester = Tester(model = transh, data_loader = test_dataloader, use_gpu = True)
        score_head_index = tester.head_query(type_constrain = False)

        print("--------------------------------------------------------")    
        print(entity_clean[score_head_index[0][0]], relation, tail)

        print("--------------------------------------------------------")
        exit = int(input("是否退出，若是输入1，否则输入0:"))
    elif mode == 3:
        print("--------------------------------------------------------")
        head = str(input("请输入你要查询的头节点："))
        tail = str(input("请输入你要查询的尾节点："))
        
        head_index = entity_enc.get(head)
        relation_index = 0
        tail_index = entity_enc.get(tail)
        
        with open("./benchmarks/mydata/test2id.txt", "w") as f:
            f.write(str(1) + '\n')
            f.write(str(head_index) + ' ' + str(tail_index) + ' ' + str(relation_index))
        with open("./benchmarks/mydata/valid2id.txt", "w") as f:
            f.write(str(1) + '\n')
            f.write(str(head_index) + ' ' + str(tail_index) + ' ' + str(relation_index))
        
        test_dataloader = TestDataLoader("./benchmarks/mydata/", "link") 
        transh.load_checkpoint('./checkpoint/transh.ckpt')
        tester = Tester(model = transh, data_loader = test_dataloader, use_gpu = True)
        score_rel_index = tester.rel_query(type_constrain = False)

        print("--------------------------------------------------------")    
        print(head, relation_clean[score_rel_index[0][0]], tail)
        
        print("--------------------------------------------------------")
        exit = int(input("是否退出，若是输入1，否则输入0:"))
    else:
        print("--------------------------------------------------------")
        mode = eval(input("请输入1或2或3:"))
