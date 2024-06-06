from fastapi import APIRouter

from tasks import celery, square_root

router = APIRouter()


@router.post('/square_root')
def process(num: float):
    task = square_root.delay(num)
    return {'taskId': task.id}


@router.get('/status/{task_id}')
def status(task_id: str):
    task = celery.AsyncResult(task_id)
    if task.ready():
        return {'status': 'DONE', 'result': task.get()}
    else:
        return {'status': 'IN_PROGRESS'}
