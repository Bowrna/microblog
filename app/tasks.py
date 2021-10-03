import time
from rq import get_current_job
from app import app

app.app_context().push()

def example(seconds):
    print('Starting task')
    job = get_current_job()
    for i in range(seconds):
        job.meta['progress'] = 100 * i / seconds
        job.save_meta()
        print(i)
        time.sleep(1)
    job.meta['progress'] 
    job.save_meta()
    print('Task completed')

def _set_task_progress(progress):
    job = get_current_job()
    if job:
        job.meta['progress'] = progress
        job.save_meta()
        task = Task.query.get(job.get_id())
        task.user.add_notification('task_progress', {'task_id': job.get_id(),
                                                     'progress': progress})
        if progress >= 100:
            task.complete = True
        db.session.commit()