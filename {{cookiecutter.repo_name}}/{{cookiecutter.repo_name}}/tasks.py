# coding: utf-8
from celery import Celery

# hack to be able to user {{cookiecutter.repo_name}}.tasks.celery in views
# without cyclic dependancies
celery = None

def make_celery(app):
    global celery
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    app.celery=celery
    return celery

