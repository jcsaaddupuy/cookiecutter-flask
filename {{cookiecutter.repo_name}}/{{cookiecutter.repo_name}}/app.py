# coding: utf-8
from __future__ import unicode_literals
import appfactory


def make_app():
    app = appfactory.create_app()
    appfactory.configure_all(app)
    appfactory.register_all(app)

app = make_app()
{%- if cookiecutter.use_celery %}
celery = app.celery
{%- endif %}
