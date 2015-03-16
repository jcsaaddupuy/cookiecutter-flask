# coding: utf-8


class Config(object):
    DEBUG = False
    TESTING = False
{% if cookiecutter.use_sql_alchemy == 'yes' -%}
    SQLALCHEMY_DATABASE_URI = 'sqlite://:memory:'
{% endif -%}
