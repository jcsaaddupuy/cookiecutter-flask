# coding: utf-8
import os

project_directory=os.path.realpath(os.path.curdir)
project_name="{{cookiecutter.repo_name}}"

TO_REMOVE={
'celery': [
        os.path.join(project_directory, project_name, 'tasks.py'),
    ]
}

def remove_files(files):
    for f in files:
        os.unlink(f)

if "{{ cookiecutter.use_celery}}" != 'yes':
    # remove celery files
    remove_files(TO_REMOVE['celery'])


