from confluent_kafka import Producer
import api_users_ingestion_pipeline.services.api_data_handling_service as api_data_handling_service
from datetime import datetime
import socket
import json
import pytz

body = {
    "mappings": {
        "properties": {
            "full_name": {"type": "text"},
            "email": {"type": "text"},
            "age": {"type": "integer"},
            "dob": {"type": "date"},
            "address": {
                "properties": {
                        "street": {
                            "properties": {
                                "number": {"type": "text"},
                                "name": {"type": "text"}
                            }
                        },
                    "city": {"type": "text"},
                    "state": {"type": "text"},
                    "country": {"type": "text"},
                    "postcode": {"type": "text"}
                },
            },
            "phones": {"type": "keyword"}
        }
    }
}

def produce_message(response):
    return json.dumps({'full_name': f'{api_data_handling_service.get_name_from_response_json(response)} {api_data_handling_service.get_last_name_from_response_json(response)}',
                       'email': api_data_handling_service.get_email_from_response_json(response),
                       "dob": api_data_handling_service.get_dob_from_response_json(response),
                       "address": {
                            "street": {
                                "number": api_data_handling_service.get_location_street_number_from_response_json(response),
                                "name": api_data_handling_service.get_location_street_name_from_response_json(response) 
                            },
                            "city": api_data_handling_service.get_location_city_from_response_json(response),
                            "state": api_data_handling_service.get_location_state_from_response_json(response),
                            "country": api_data_handling_service.get_location_country_from_response_json(response),
                            "postcode": api_data_handling_service.get_location_postcode_from_response_json(response) 
                        }
                       }
                    ).encode('utf-8')




def callback(error, message):
    if error is not None:
        print("------> Error <------")
        print(f"Failure to send: {message.key().decode('utf-8')}")
    else: 
        timestamp_dt = datetime.fromtimestamp(message.timestamp()[1] / 1000.0, tz=pytz.utc)

        print("------> Sucessfull Message <------")
        print(f'Message Value: {message.value()}')
        print(f"Message Topic: {message.topic()}")
        print(f"Message Partition: {message.partition()}")
        print(f"Message Offset: {message.offset()}")
        print(f"Message Key: {message.key().decode('utf-8')}")
        print(f"Message Moment: {timestamp_dt}")