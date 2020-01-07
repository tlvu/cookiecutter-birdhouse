from pywps import Service
from pywps.tests import client_for

from .common import CFG_FILE
from {{ cookiecutter.project_slug }}.processes import processes


def test_wps_caps():
    client = client_for(Service(processes=processes, cfgfiles=[CFG_FILE]))
    resp = client.get('?service=wps&request=GetCapabilities&version=1.0.0')
    names = resp.xpath_text('/wps:Capabilities'
                            '/wps:ProcessOfferings'
                            '/wps:Process'
                            '/ows:Identifier')
    assert sorted(names.split()) == [
        'hello',
    ]
