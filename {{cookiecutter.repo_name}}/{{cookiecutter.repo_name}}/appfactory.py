# coding: utf-8
from __future__ import unicode_literals

from flask import Flask


def create_app():
    app = Flask()

def configure_all(app):
    configure_loggers(app)

def configure_loggers(app):
    pass

def register_all(app):
{% if cookiecutter.use_sql_alchemy %}
    register_db(app)
{% endif %}
{% if cookiecutter.use_celery %}
    register_celery(app)
{% endif %}
    register_blueprints(app)

def register_blueprints(app):
    pass

{% if cookiecutter.use_sql_alchemy %}
def register_db(app):
    pass
{% endif %}

{% if cookiecutter.use_celery %}
def register_celery(app):
    app.celery = None # TODO
{% endif %}
