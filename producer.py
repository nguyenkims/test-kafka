from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

for i in range(100):
    producer.send('tt', f'myvalue-{i}'.encode())

producer.flush()