# Title2Event
This is the dataset for the paper [Title2Event: Benchmarking Open Event Extraction with a Large-scale Chinese Title Dataset](https://arxiv.org/abs/2211.00869) \
[[webpage]](https://open-event-hub.github.io/title2event/) [[github]](https://github.com/open-event-hub/title2event_baselines)

## Format
The dataset is provided in both `csv` and `json` format, but currently the baseline code reads `csv` files by default. \
You can also find `tagging_train.csv`,`tagging_dev.csv` ,`tagging_test.csv`, these files contain the `BIO` labels needed to train tagging-based models, and are used by the `SeqTag` model.
### csv example

```csv
title_id,title,topic,event1_trigger,event1_triple,event2_trigger,event2_triple,event3_trigger,event3_triple,event4_trigger,event4_triple,event5_trigger,event5_triple,event6_trigger,event6_triple
28363,盗掘古墓葬、古文化遗址！七人被望江检察院提起公诉,社会,盗掘,"('七人', '盗掘', '古墓葬、古文化遗址')",被提起公诉,"('七人', '被提起公诉', '望江检察院')",,,,,,,,
```
with `BIO` labels:
```
title_id,title,topic,event1_trigger,event1_triple,event2_trigger,event2_triple,event3_trigger,event3_triple,event4_trigger,event4_triple,event5_trigger,event5_triple,event6_trigger,event6_triple,tokens,trg_tags,event1_arg_tags,event2_arg_tags,event3_arg_tags,event4_arg_tags,event5_arg_tags,event6_arg_tags
28363,盗掘古墓葬、古文化遗址！七人被望江检察院提起公诉,社会,盗掘,"('七人', '盗掘', '古墓葬、古文化遗址')",被提起公诉,"('七人', '被提起公诉', '望江检察院')",,(),,(),,(),,(),"['盗', '掘', '古', '墓', '葬', '、', '古', '文', '化', '遗', '址', '！', '七', '人', '被', '望', '江', '检', '察', '院', '提', '起', '公', '诉']","['B-T1', 'I-T1', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-T2', 'O', 'O', 'O', 'O', 'O', 'I-T2', 'I-T2', 'I-T2', 'I-T2']","['O', 'O', 'O', 'I-obj', 'I-obj', 'I-obj', 'I-obj', 'I-obj', 'I-obj', 'I-obj', 'I-obj', 'O', 'B-sbj', 'I-sbj', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']","['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'B-sbj', 'I-sbj', 'O', 'B-obj', 'I-obj', 'I-obj', 'I-obj', 'I-obj', 'O', 'O', 'O', 'O']",,,,
```

### json example
```json
{
    "title_id": "28363",  #an unique string for each document
    "title": "盗掘古墓葬、古文化遗址！七人被望江检察院提起公诉", 
    "topic": "社会",     
    "event_info": [ # A list, the event info from the title.
        {
            "event1_trigger": "盗掘", 
            "event1_triple": "'七人', '盗掘', '古墓葬、古文化遗址'" # a string, the triple of the event, joining by comma ,
        }, 
        {
            "event2_trigger": "被提起公诉", 
            "event2_triple": "'七人', '被提起公诉', '望江检察院'"
        }
    ]
}

```
