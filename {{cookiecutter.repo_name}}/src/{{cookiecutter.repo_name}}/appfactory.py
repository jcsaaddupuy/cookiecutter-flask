# coding: utf-8
from __future__ import unicode_literals

from flask import Flask

import flask_appconfig

import os
import logging
import logging.config


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
    # Override config from environment
    prefix = "{app_name}_SETTINGS_".format(app_name = app.name.upper())
    flask_appconfig.env.from_envvars( app.config, prefix=prefix )

def configure_loggers(app):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logging.config.fileConfig(os.path.join(current_dir, 'logging.conf'))
    if app.debug:
        map(lambda handler: handler.setLevel(logging.DEBUG), app.logger.handlers)


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
