from fastapi import FastAPI

from tasks import celery, square_root

app = FastAPI()


@app.post('/square_root')
def process(num: float):
    task = square_root.delay(num)
    return {'taskId': task.id}


@app.get('/status/{task_id}')
def status(task_id: str):
    task = celery.AsyncResult(task_id)
    if task.ready():
        return {'status': 'DONE', 'result': task.get()}
    else:
        return {'status': 'IN_PROGRESS'}
