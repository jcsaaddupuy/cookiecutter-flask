import os
import unittest
import tempfile
from  {{cookiecutter.repo_name | lower}} import appfactory

from {{cookiecutter.repo_name | lower}}.models import Base



# find abs path to this script
root_dir = os.path.abspath(os.path.dirname(__file__))
ENV_VAR_NAME="{{cookiecutter.repo_name|upper}}_SETTINGS"

SETTINGS_TESTS_CFG=os.path.join(
        root_dir,
        '..',
        '{{cookiecutter.repo_name|lower}}',
        'settings',
        'tests.cfg'
)

DEFAULT_CONFIG_OBJ='{{cookiecutter.repo_name}}.settings.defaults'


class BaseTestCase(unittest.TestCase):
    TMP_DB = os.path.join(tempfile.gettempdir(), "{{cookiecutter.repo_name}}-tmp.db")

    def setUp(self):
        # remove tmp db if exists
        if os.path.exists(self.TMP_DB):
            os.unlink(self.TMP_DB)

        # app configuration
        config_obj = '{{cookiecutter.repo_name | lower}}.settings.defaults'
        os.environ[ENV_VAR_NAME]=SETTINGS_TESTS_CFG

        app = appfactory.create_app(__name__)
        appfactory.configure_app(app, from_default_obj=config_obj, from_envvar=ENV_VAR_NAME)
{%- if cookiecutter.use_sql_alchemy == 'yes' %}
        # use a persistent file temporary database
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///%s" %self. TMP_DB
{%- endif %}
        appfactory.register_all(app)
{%- if cookiecutter.use_sql_alchemy == 'yes' %}
        # Create models
        Base.metadata.create_all(app.db.engine)
{%- endif %}

        self.app = app
        self.client = app.test_client()


{%- if cookiecutter.use_sql_alchemy == 'yes' %}
    def tearDown(self):
        # cleanup temp db
        if os.path.exists(self.TMP_DB):
            os.unlink(self.TMP_DB)
{%- endif %}


if __name__ == '__main__':
    unittest.main()
