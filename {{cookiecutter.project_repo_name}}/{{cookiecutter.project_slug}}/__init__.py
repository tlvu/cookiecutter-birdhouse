# -*- coding: utf-8 -*-

"""Top-level package for {{ cookiecutter.project_name }}."""

from .__version__ import __author__, __email__, __version__  # noqa: F401

from pywps.application import make_app

application = make_app()
