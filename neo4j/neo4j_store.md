#### 导入数据库

CALL apoc.load.json("file:///all.json") YIELD value AS data
UNWIND data AS eventData
MERGE (t:Topic {name: eventData.topic})

CALL apoc.load.json("file:///all.json") YIELD value AS data
UNWIND data.event_info AS event
WITH event, data.topic AS topic
WHERE event.event1_triple IS NOT NULL
WITH split(toString(event.event1_triple), ',') AS parts, event.event1_trigger AS trigger, topic
MERGE (n1:head {name: COALESCE(parts[0], '')}) 
MERGE (n2:tail {name: COALESCE(parts[2], '')}) 
MERGE (n1)-[:relation {type: trigger}]->(n2)
ON CREATE SET n1.name = COALESCE(parts[0], ''), n2.name = COALESCE(parts[2], '')
WITH n1, n2, topic
MATCH (t:Topic {name: topic})
MERGE (n1)-[:BELONGS_TO]->(t)

CALL apoc.load.json("file:///all.json") YIELD value AS data
UNWIND data.event_info AS event
WITH event, data.topic AS topic
WHERE event.event2_triple IS NOT NULL
WITH split(toString(event.event2_triple), ',') AS parts, event.event2_trigger AS trigger, topic
MERGE (n1:head {name: COALESCE(parts[0], '')}) 
MERGE (n2:tail {name: COALESCE(parts[2], '')}) 
MERGE (n1)-[:relation {type: trigger}]->(n2)
ON CREATE SET n1.name = COALESCE(parts[0], ''), n2.name = COALESCE(parts[2], '')
WITH n1, n2, topic
MATCH (t:Topic {name: topic})
MERGE (n1)-[:BELONGS_TO]->(t)

CALL apoc.load.json("file:///all.json") YIELD value AS data
UNWIND data.event_info AS event
WITH event, data.topic AS topic
WHERE event.event3_triple IS NOT NULL
WITH split(toString(event.event3_triple), ',') AS parts, event.event3_trigger AS trigger, topic
MERGE (n1:head {name: COALESCE(parts[0], '')}) 
MERGE (n2:tail {name: COALESCE(parts[2], '')}) 
MERGE (n1)-[:relation {type: trigger}]->(n2)
ON CREATE SET n1.name = COALESCE(parts[0], ''), n2.name = COALESCE(parts[2], '')
WITH n1, n2, topic
MATCH (t:Topic {name: topic})
MERGE (n1)-[:BELONGS_TO]->(t)

CALL apoc.load.json("file:///all.json") YIELD value AS data
UNWIND data.event_info AS event
WITH event, data.topic AS topic
WHERE event.event4_triple IS NOT NULL
WITH split(toString(event.event4_triple), ',') AS parts, event.event4_trigger AS trigger, topic
MERGE (n1:head {name: COALESCE(parts[0], '')}) 
MERGE (n2:tail {name: COALESCE(parts[2], '')}) 
MERGE (n1)-[:relation {type: trigger}]->(n2)
ON CREATE SET n1.name = COALESCE(parts[0], ''), n2.name = COALESCE(parts[2], '')
WITH n1, n2, topic
MATCH (t:Topic {name: topic})
MERGE (n1)-[:BELONGS_TO]->(t)

CALL apoc.load.json("file:///all.json") YIELD value AS data
UNWIND data.event_info AS event
WITH event, data.topic AS topic
WHERE event.event5_triple IS NOT NULL
WITH split(toString(event.event5_triple), ',') AS parts, event.event5_trigger AS trigger, topic
MERGE (n1:head {name: COALESCE(parts[0], '')}) 
MERGE (n2:tail {name: COALESCE(parts[2], '')}) 
MERGE (n1)-[:relation {type: trigger}]->(n2)
ON CREATE SET n1.name = COALESCE(parts[0], ''), n2.name = COALESCE(parts[2], '')
WITH n1, n2, topic
MATCH (t:Topic {name: topic})
MERGE (n1)-[:BELONGS_TO]->(t)

CALL apoc.load.json("file:///all.json") YIELD value AS data
UNWIND data.event_info AS event
WITH event, data.topic AS topic
WHERE event.event6_triple IS NOT NULL
WITH split(toString(event.event6_triple), ',') AS parts, event.event6_trigger AS trigger, topic
MERGE (n1:head {name: COALESCE(parts[0], '')}) 
MERGE (n2:tail {name: COALESCE(parts[2], '')}) 
MERGE (n1)-[:relation {type: trigger}]->(n2)
ON CREATE SET n1.name = COALESCE(parts[0], ''), n2.name = COALESCE(parts[2], '')
WITH n1, n2, topic
MATCH (t:Topic {name: topic})
MERGE (n1)-[:BELONGS_TO]->(t)
