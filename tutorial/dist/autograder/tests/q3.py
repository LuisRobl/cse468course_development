OK_FORMAT = True

test = {   'name': 'q3',
    'points': None,
    'suites': [   {   'cases': [   {'code': ">>> len(data['flavor'].unique()) == 4\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> for l in ['chocolate', 'vanilla', 'strawberry', 'mint']:\n...     assert l in data['flavor'].unique()\n", 'hidden': False, 'locked': False},
                                   {'code': '>>> assert type(price_by_flavor) == pd.Series\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert len(price_by_flavor) == 4\n', 'hidden': False, 'locked': False},
                                   {'code': ">>> np.isclose(price_by_flavor['chocolate'], 3.33333333)\nTrue", 'hidden': True, 'locked': False},
                                   {'code': ">>> np.isclose(price_by_flavor['mint'], 4.5)\nTrue", 'hidden': True, 'locked': False},
                                   {'code': ">>> np.isclose(price_by_flavor['strawberry'], 3)\nTrue", 'hidden': True, 'locked': False},
                                   {'code': ">>> np.isclose(price_by_flavor['vanilla'], 1.75)\nTrue", 'hidden': True, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
