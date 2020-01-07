.. _installation:

Installation
============

.. contents::
    :local:
    :depth: 1

Install from Conda
------------------

.. warning::

   TODO: Prepare Conda package.

Install from GitHub
-------------------

Check out code from the {{ cookiecutter.project_name }} GitHub repo and start the installation:

.. code-block:: console

   $ git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_repo_name }}.git
   $ cd {{ cookiecutter.project_slug }}

Create Conda environment named `{{ cookiecutter.project_slug }}`:

.. code-block:: console

   $ conda env create -f environment.yml
   $ source activate {{ cookiecutter.project_slug }}

Install {{ cookiecutter.project_name }} app:

.. code-block:: console

  $ pip install -e .
  OR
  make install

For development you can use this command:

.. code-block:: console

  $ pip install -e .[dev]
  OR
  $ make develop

Start PyWPS service
-------------------

After successful installation you can start the service using the ``pywps`` command-line.

.. code-block:: console

  # show help
  $ pywps -h

  # start service with default configuration (pywps.cfg)
  $ pywps -c pywps.cfg start

The deployed WPS service is by default available on:

http://localhost:{{ cookiecutter.http_port }}/wps?service=WPS&version=1.0.0&request=GetCapabilities.

Check the log files for errors:

.. code-block:: console

   $ tail -f pywps.log

... or do it the lazy way
+++++++++++++++++++++++++

You can also use the ``Makefile`` to start service:

.. code-block:: console

  $ make start
  $ tail -f pywps.log


Run {{ cookiecutter.project_name }} as Docker container
-{{ '-' * (cookiecutter.project_name|count + 23) }}

You can also run {{ cookiecutter.project_name }} as a Docker container.

.. warning::

  TODO: Describe Docker container support.

Use Ansible to deploy {{ cookiecutter.project_name }} on your System
-{{ '-' * (cookiecutter.project_name|count + 36) }}

Use the `Ansible playbook`_ for PyWPS to deploy {{ cookiecutter.project_name }} on your system.


.. _Ansible playbook: http://ansible-wps-playbook.readthedocs.io/en/latest/index.html
