.. _configuration:

Configuration
=============

Use a custom configuration file
-------------------------------

You can overwrite the default `PyWPS`_ configuration by providing your own
PyWPS configuration file.
Use one of the existing ``pywps.cfg`` file as example and copy it to ``custom.cfg``.

For example change the hostname (*demo.org*) and logging level:

.. code-block:: console

   $ cd {{ cookiecutter.project_slug }}
   $ cp pywps.cfg custom.cfg
   $ vim custom.cfg
   $ cat custom.cfg
   [server]
   url = http://demo.org:{{ cookiecutter.http_port }}/wps
   outputurl = http://demo.org:{{ cookiecutter.http_port }}/outputs

   [logging]
   level = DEBUG

Start the service with your custom configuration:

.. code-block:: console

   # start the service with this configuration
   $ pywps -c custom.cfg start

.. _PyWPS: http://pywps.org/
