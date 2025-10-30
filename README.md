End-to-End API Ingestion Pipeline:

Um pipeline ETL que extrai dados de uma API, envia para o Kafka através de um processo producer e consome os dados por meio de um processo consumer para indexá-los no Elasticsearch. 
Este projeto implementa um pipeline completo de ingestão de dados, cobrindo todas as etapas do fluxo de dados:

-Extração (Extract): coleta dados de uma API externa.

-Transformação e Envio (Transform & Load): envia as mensagens para um topic no Apache Kafka.

-Consumo e Indexação (Consume & Index): consome os dados do Kafka e os indexa no Elasticsearch.

-O objetivo é permitir ingestão em tempo real ou quase em tempo real de dados de APIs em uma camada de busca eficiente.

Principai dependências:

-Python 3.x

-Apache Kafka 

-Elasticsearch 
