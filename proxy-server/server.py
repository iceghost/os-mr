#!/usr/bin/env python3
import logging
import sys
from kafka import KafkaProducer
from flask import Flask, request

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


@app.post("/statements")
def statements():
    logging.info("Received statements")
    statements = request.get_data()
    global producer
    producer.send("saturday test", statements)
    return "Okay"


producer = KafkaProducer(bootstrap_servers="kafka:9092")
if __name__ == "__main__":
    app.run(debug=True, port=int(sys.argv[1]))
