from sunny import Solr
import pytest


@pytest.fixture(scope="function")
def solr():
    return Solr('http://localhost:13022/solr')


@pytest.fixture(scope='function')
def ex_params():
    return {'q': 'office',
            'facet': 'on',
            'facet.field': ['network', 'runtime']}


def test_dict_support(solr, ex_params):
    res = solr.query(ex_params)
    assert len(res['response']['docs']) == 7
    assert len(res['facet_counts']['facet_fields']) == 2
