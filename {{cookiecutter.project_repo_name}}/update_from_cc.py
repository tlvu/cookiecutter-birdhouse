"""
This script replays the cookiecutter repository creation with the original values.

The intended use is to inject template changes into an existing repo.

How-to
======
* Make sure that there are no files left uncommitted.
* Check out the commit right after the repo creation by cookiecutter
  and create a new branch that will hold the template modifications.
* Clean the repo
* Run this script from the parent directory
* Commit all files that were created or modified
* Checkout a new branch from master
* Merge the modifications made to the original version
* Fix the conflicts and merge

.. code:: bash

    git checkout -b orig_cc_update <SHA>
    git clean -fxd
    cd ..
    python {{ cookiecutter.project_slug }}/update_from_cc.py
    cd {{ cookiecutter.project_slug }}
    git add * */.*
    git commit -m 'update from cookiecutter template'
    git rebase master

"""

from cookiecutter.main import cookiecutter

if __name__ == "__main__":


    cookiecutter('cookiecutter-birdhouse',
                 no_input=True,
                 overwrite_if_exists=True,
                 extra_context={
                     "full_name": "{{ cookiecutter.full_name }}",
                     "email": "{{ cookiecutter.email }}",
                     "github_username": "{{ cookiecutter.github_username }}",
                     "project_name": "{{ cookiecutter.project_name }}",
                     "project_slug": "{{ cookiecutter.project_slug }}",
                     "project_repo_name": "{{ cookiecutter.project_repo_name }}",
                     "project_short_description": "{{ cookiecutter.project_short_description }}",
                     "version": "{{ cookiecutter.version }}",
                     "open_source_license": "{{ cookiecutter.open_source_license }}",
                     "http_port": "{{ cookiecutter.http_port }}",
                     "timestamp": "{{ cookiecutter.timestamp }}"
                 }
                 )
