# coding: utf-8


class Config(object):
    DEBUG = False
    TESTING = False
{% if cookiecutter.use_sql_alchemy == 'yes' %}
    SQLALCHEMY_DATABASE_URI = 'sqlite://:memory:'
{% endif %}
{% if cookiecutter.use_celery== 'yes' %}
    # Configure celery to use redis a broker
    CELERY_BROKER_URL='redis://localhost:6379',
    # Configure celery to use redis result backend
    CELERY_RESULT_BACKEND='redis://localhost:6379'
    # Configure celery to only use json
    CELERY_ACCEPT_CONTENT = ['json',]
    CELERY_TASK_SERIALIZER = 'json'
    # compress messages
    CELERY_MESSAGE_COMPRESSION='gzip'
{% endif %}
