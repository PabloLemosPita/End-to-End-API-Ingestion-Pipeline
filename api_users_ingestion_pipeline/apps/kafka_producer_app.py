from api_users_ingestion_pipeline.services.api_data_handling_service import request_randomuser_from_api
from api_users_ingestion_pipeline.services.message_service import produce_message
from api_users_ingestion_pipeline.services.message_service import callback
from confluent_kafka import Producer
import socket

bootstrap_servers = 'localhost:9092'
client_id = socket.gethostname() 

producer_config = {'bootstrap.servers': bootstrap_servers, 'client.id': client_id}

topic_name = 'users'
key = 'users_partition'
producer = Producer(producer_config)

while(True):
    response = request_randomuser_from_api()
    
    message = produce_message(response)
    producer.produce(topic=topic_name,
                     key=key,
                     value=message,
                     on_delivery=callback
                    )
    producer.flush()
    print()