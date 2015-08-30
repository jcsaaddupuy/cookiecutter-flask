# coding: utf-8
import os

from flask.ext.script import Manager
from {{cookiecutter.repo_name}}.app import app

{% if cookiecutter.use_sql_alchemy == 'yes' -%}
from flask.ext.migrate import Migrate, MigrateCommand
{% endif -%}

manager = Manager(app)
root_directory = os.path.abspath(os.path.dirname(__file__))


{% if cookiecutter.use_sql_alchemy == 'yes' -%}
# trick for using db maagement command from amywhere
migration_directory=os.path.join(root_directory, 'migrations')
migrate = Migrate(app, app.db, directory=migration_directory)
manager.add_command('db', MigrateCommand)
{% endif -%}


def main():
    manager.run()

if __name__ == "__main__":
    main()

