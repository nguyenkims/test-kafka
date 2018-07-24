Instal [kafka-python](https://github.com/dpkp/kafka-python):
> pip install kafka-python

Run zookeeper and kafka:

> docker-compose up

Produce some messages:

> python producer.py

Check offset using [kt](https://github.com/fgeller/kt)
> kt group -topic tt

The offset should be 100

Run the consumer

> python consumer.py

