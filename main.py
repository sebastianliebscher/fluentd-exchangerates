import json
from datetime import datetime
import schedule
import time
import logging
import pandasdmx as sdmx
from kombu import Connection, Exchange

logging.getLogger('pandasdmx.reader.sdmxml').setLevel(logging.ERROR)

logging.basicConfig(
    level=logging.WARNING,
    format='{"time":"%(asctime)s", "name":"%(name)s", "level":"%(levelname)s", "message":"%(message)s" }'
)
logger = logging.getLogger('exchangerates')
logger.setLevel(level=logging.INFO)


def get_exchange_rates():
    # https://pandasdmx.readthedocs.io/en/stable/walkthrough.html
    # https://sdw.ecb.europa.eu/datastructure.do?conceptMnemonic=EXR_SUFFIX&datasetinstanceid=120
    ecb = sdmx.Request('ECB')
    key = dict(CURRENCY=['CHF'], CURRENCY_DENOM='EUR', FREQ='M', EXR_SUFFIX='A')
    params = dict(startPeriod='2022-01', endPeriod=datetime.today().strftime('%Y-%m-%d'))
    data_response = ecb.data('EXR', key=key, params=params)

    data = data_response.data[0]
    df = sdmx.to_pandas(data)
    return df


def publish(message):
    rmq_exchange = Exchange(name='exchange_rates', durable=True)

    result = message.to_json(orient="values")
    parsed = json.loads(result)

    with Connection('amqp://guest:guest@rmq//') as conn:
        # produce
        producer = conn.Producer(serializer='json')
        producer.publish(body=parsed, exchange=rmq_exchange, routing_key='exchange_rates')
    logger.info(f"sent: {parsed}")


def main():
    publish(get_exchange_rates())


if __name__ == '__main__':
    schedule.every(5).seconds.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)
