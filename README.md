Get exchange rates from [ECB](https://data.ecb.europa.eu/) via [pandaSDMX](https://pandasdmx.readthedocs.io/en/v1.0/), send the data to [RabbitMQ](https://www.rabbitmq.com/) and log to [Elasticsearch](https://www.elastic.co/de/elasticsearch) via [fluentd](https://github.com/fluent/fluentd).

# pre reqs

- running RabbitMQ service with an exchange and queue

# get it running

```sh
docker-compose up -d --build --recreate
docker exec -it fluent-exchangerates-elasticsearch-1 bin/elasticsearch-create-enrollment-token -s kibana
```

# TODO 
- https://www.elastic.co/guide/en/elasticsearch/reference/current/index-lifecycle-management.html


