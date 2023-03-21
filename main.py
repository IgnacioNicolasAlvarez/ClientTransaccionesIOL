from src.tasks.consume_api import task_consume_api, task_transform

if __name__ == "__main__":
    raw = task_consume_api()
    task_transform(raw=raw)
