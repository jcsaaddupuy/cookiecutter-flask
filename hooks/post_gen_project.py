# coding: utf-8
import os

project_directory=os.path.realpath(os.path.curdir)
project_name="{{cookiecutter.repo_name}}"


TO_REMOVE={
'celery': [
        os.path.join(project_directory, 'src', project_name, 'tasks.py'),
    ]
,'git': [
        os.path.join(project_directory, 'gitignore'),
    ]
,'sqlalchemy': [
        os.path.join(project_directory, 'src', project_name, 'models.py'),
    ]
}

TO_MOVE={
'git': [
        (os.path.join(project_directory, 'gitignore'), os.path.join(project_directory, '.gitignore')),
    ]
}

def remove_files(files):
    for f in files:
        os.unlink(f)

def move_files(files):
    for from_, to_ in files:
        os.rename(from_, to_)

if "{{ cookiecutter.use_celery}}" != 'yes':
    # remove celery files
    remove_files(TO_REMOVE['celery'])

if "{{ cookiecutter.use_sql_alchemy}}" != 'yes':
    # remove celery files
    remove_files(TO_REMOVE['sqlalchemy'])


if "{{ cookiecutter.use_git}}" != 'yes':
    remove_files(TO_REMOVE['git'])
else:
    move_files(TO_MOVE['git'])

