from elasticsearch import Elasticsearch

# Elasticsearch config

es_host = "https://localhost:9200"
es_user = "your_elasticsearch_user"
es_password = "your_elastic_password"

es = Elasticsearch(es_host, basic_auth=(es_user, es_password), verify_certs=False, ssl_show_warn=False)

try:
    es.info()
    print("Successfully elasticsearch connection!")
except Exception as e:
    print(f"Error to connect with elasticsearch: {e}")

body = {
    "mappings": {
        "properties": {
            "full_name": {"type": "text"},
            "email": {"type": "text"},
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

index_name = "users"

if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name, body=body)
    print(f"Index: {index_name} - Succesfully created!")
else:
    print(f"Index: {index_name} - Already exists!")