from sunny import Solr, normalize_params


def test_normalize_params_dict():
    """
    Order is not guaranteed with dictionaries, so we cannot make an
    equality assertion on the output.
    """
    dct = {'q': 'office',
           'facet': 'on',
           'facet.field': ['network', 'runtime']}
    tuples = normalize_params(dct)
    assert len(tuples) == 4
    assert ('q', 'office') in tuples
    assert ('facet', 'on') in tuples
    assert ('facet.field', 'network') in tuples
    assert ('facet.field', 'runtime') in tuples


def test_normalize_params_omdict():
    """
    Order is guaranteed for omdicts.
    """
    from orderedmultidict import omdict
    dct = omdict()
    dct['q'] = 'office'
    dct['facet'] = 'on'
    dct.add('facet.field', 'network')
    dct.add('facet.field', 'runtime')
    tuples = normalize_params(dct)
    assert tuples == [('q', 'office'),
                      ('facet', 'on'),
                      ('facet.field', 'network'),
                      ('facet.field', 'runtime')]


def test_simple_real_world():
    """
    This really only works on my computer, sorry.  /Deniz
    """
    res = Solr('http://localhost:13022/solr').\
        query({'q': 'office',
               'facet': 'on',
               'facet.field': ['network', 'runtime']})
    assert len(res['response']['docs']) == 7
    assert len(res['facet_counts']['facet_fields']) == 2
