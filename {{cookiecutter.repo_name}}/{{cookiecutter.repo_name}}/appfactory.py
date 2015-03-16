# coding: utf-8
from __future__ import unicode_literals

from flask import Flask


def create_app(name):
    app = Flask(name)
    return app


def configure_all(app, from_default_obj, from_envvar=None):
    configure_app(app, from_default_obj, from_envvar)
    configure_loggers(app)

def configure_app(app, from_default_obj, from_envvar=None):
    app.config.from_object(from_default_obj)
    if from_envvar:
        app.config.from_envvar(from_envvar)

def configure_loggers(app):
    pass


def register_all(app):
{%- if cookiecutter.use_sql_alchemy %}
    register_db(app)
{%- endif %}
{%- if cookiecutter.use_celery %}
    register_celery(app)
{%- endif%}
    register_blueprints(app)


def register_blueprints(app):
    pass

{%- if cookiecutter.use_sql_alchemy %}
def register_db(app):
    from flask.ext.sqlalchemy import SQLAlchemy
    db = SQLAlchemy(app)
    app.db = db
{%- endif%}

{%- if cookiecutter.use_celery %}
def register_celery(app):
    app.celery = None
{%- endif %}
