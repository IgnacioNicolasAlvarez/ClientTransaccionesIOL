from prefect import flow
from src.etl.api import task_consume_api, task_transform, task_load
from prefect.task_runners import SequentialTaskRunner


@flow(task_runner=SequentialTaskRunner())
def ingest_api():
    raw = task_consume_api()
    processed = task_transform(raw=raw)
    task_load(orders=processed)

# prefect deployment build main.py:ingest_api -n etl --cron "0 18 * * 1-5"
