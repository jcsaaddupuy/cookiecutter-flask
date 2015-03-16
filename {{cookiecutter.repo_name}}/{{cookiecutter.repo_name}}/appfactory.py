# coding: utf-8
from __future__ import unicode_literals

from flask import Flask
import logging


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
    if not app.debug:
        # In production mode, add log handler to sys.stderr.
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.INFO)


def register_all(app):
{%- if cookiecutter.use_sql_alchemy == 'yes' %}
    register_db(app)
{%- endif %}
{%- if cookiecutter.use_celery == 'yes' %}
    register_celery(app)
{%- endif%}
    register_blueprints(app)


def register_blueprints(app):
    from {{cookiecutter.repo_name}}.apps.default import views as default_views
    app.register_blueprint(default_views.blueprint, url_prefix='/')

{%- if cookiecutter.use_sql_alchemy == 'yes' %}
def register_db(app):
    from flask.ext.sqlalchemy import SQLAlchemy
    db = SQLAlchemy(app)
    app.db = db
{%- endif%}

{%- if cookiecutter.use_celery == 'yes' %}
def register_celery(app):
    app.celery = None
{%- endif %}
