import time

from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'tt',
    bootstrap_servers='localhost:9092',
    group_id='gg',
    enable_auto_commit=False,
    auto_offset_reset='earliest'
)
# consumer.commit()

for msg in consumer:
    print(f'key:{msg.key} value:{msg.value} '
          f'offset:{msg.offset} partition:{msg.partition}')
    
    consumer.commit()
    time.sleep(10)
