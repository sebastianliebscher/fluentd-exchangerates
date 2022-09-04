Get exchange rates from ECB via pandasdmx, send data to RabbitMQ and log to fluentd.

# pre reqs

- running RabbitMQ service with an exchange and queue

# get it running

```sh
docker-compose up -d --build --recreate
docker exec -it fluent-exchangerates-elasticsearch-1 bin/elasticsearch-create-enrollment-token -s kibana
```

# TODO 
- https://www.elastic.co/guide/en/elasticsearch/reference/current/index-lifecycle-management.html


