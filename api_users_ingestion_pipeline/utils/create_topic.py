from confluent_kafka.admin import AdminClient
from confluent_kafka.admin import NewTopic
import socket

bootstrap_servers = 'localhost:9092'
client_id = socket.gethostname()

server_basic_config = {'bootstrap.servers': bootstrap_servers, 'client.id': client_id}

admin_client = AdminClient(server_basic_config)

topic_name = 'users'
num_partitions = 1
replication_factor=1
topic = NewTopic(topic=topic_name, num_partitions=num_partitions, replication_factor=replication_factor)

futures = admin_client.create_topics([topic])

for topic, future in futures.items():
    try: 
        future.result()
        print(f"Topic: {topic} - Created sucessfully!")
    except Exception as e:
        print(f"Topic: {topic} - Creation fail due to {e}")

