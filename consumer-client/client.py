#!/usr/bin/env python3
import logging
from kafka import KafkaConsumer

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    consumer = KafkaConsumer("test", bootstrap_servers="kafka:9092")
    for msg in consumer:
        logging.info("Received message: %s", msg)
