from openke.config import Trainer,Tester
from openke.module.model import TransE
from openke.module.loss import MarginLoss
from openke.module.strategy import NegativeSampling
from openke.data import TrainDataLoader, TestDataLoader
import numpy as np
# print(1)
# dataloader for training
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

# dataloader for test
test_dataloader = TestDataLoader("./benchmarks/mydata/", "link") 

transe = TransE(
	ent_tot = train_dataloader.get_ent_tot(),
	rel_tot = train_dataloader.get_rel_tot(),
	dim = 200, 
	p_norm = 1, 
	norm_flag = True)


# define the loss function
model = NegativeSampling(
	model = transe, 
	loss = MarginLoss(margin = 5.0),
	batch_size = train_dataloader.get_batch_size()
)

# train the model
# trainer = Trainer(model = model, data_loader = train_dataloader, train_times = 1000, alpha = 1.0, use_gpu = True)
# trainer.run()
# transe.save_checkpoint('./checkpoint/transe.ckpt')

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
    
# test the model
transe.load_checkpoint('./checkpoint/transe.ckpt')
tester = Tester(model = transe, data_loader = test_dataloader, use_gpu = True)
score_tail_index = tester.tail_query(type_constrain = False)
score_head_index = tester.head_query(type_constrain = False)
score_rel_index = tester.rel_query(type_constrain = False)
# print(score_head_index)
# print(entity_clean[score_head_index[0][0]])
print(score_tail_index)
print(entity_clean[score_tail_index[0][0]])
# print(score_rel_index)
# print(relation_clean[score_rel_index[0][0]])
# score_index = tester.rel_query(type_constrain = False)
# score_index = (tester.head_query(type_constrain = False))
# print(score_index[0][0])
# print(type(score_index))
# # for idx in score_index:
# print(relation_clean[score_index[0][0]])
# score_index = tester.tail_query(type_constrain = False)

# print(score_index)


