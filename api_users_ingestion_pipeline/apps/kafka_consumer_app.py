from confluent_kafka import Consumer
from confluent_kafka import KafkaError
from elasticsearch import Elasticsearch
from elasticsearch import helpers

import time
import json

# Elasticsearch Config
es_host = "https://localhost:9200"
es_user = "your_elasticsearch_user"
es_password = "your_elastic_password"
index_name = 'users'
es = Elasticsearch(es_host, basic_auth=(es_user, es_password), verify_certs=False, ssl_show_warn=False)

try:
    info = es.info()
    print("Successfully elasticsearch connection!")
    print()
except Exception as e:
    print(f"Error to connect with elasticsearch: {e}")


# Kafka Config
consumer_config = {'bootstrap.servers': 'localhost:9092',
                    'group.id': 'users_consumers',
                    'auto.offset.reset': 'earliest',
                    'enable.auto.commit': True,
                    'auto.commit.interval.ms': 5000
                    }
    

topic_name = 'users'
consumer = Consumer(consumer_config)
consumer.subscribe([topic_name])

while(True):
    try:
        batch_to_index = []
        rounds_without_consume = 0
        while(len(batch_to_index) != 100):
            message = consumer.poll(1.0)

            if rounds_without_consume == 10:
                print("Early batch indexing...")
                print()
                break

            if message is None:
                print("There are no messages for now... WAITING...")
                rounds_without_consume += 1
                continue
            
            message_error = message.error()
            if message_error:
                
                if message_error.code() == KafkaError._PartitionEOF:
                    print(f"End of partition reached. Waiting for new messages...")
                    print()
                    break
                else:
                    print(f"FATAL ERROR: {message_error} - exiting...")
                    print()
                    break

            try:
                message_value = message.value()
                decoded_message = message_value.decode('utf-8')
                _source = json.loads(decoded_message)
                print("Sucessfull Consumed Message")
                print(f"Valor (Raw): {decoded_message}")
                # print(f"Tipo: {type(_source)}")
                print()
                rounds_without_consume = 0
                batch_to_index.append({'_index': index_name, '_source': _source})

            except:
                print(f"Bad formated message! Not added to batch... Please check message producer process.")
                print()
                continue

    except Exception as e:
        print(f"Erro: {e}")
    
    if len(batch_to_index) > 0:
        helpers.bulk(es, batch_to_index)
        print(f"{len(batch_to_index)} - USERS SUCCEFULLY INDEX!")
        print()
    
    print(f"STARTING BATCH BUILDING AGAIN...")
    print()



