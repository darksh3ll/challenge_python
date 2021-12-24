foo = [{
    'name': 'LKS',
    'value': '10d19ecbf05bbb668c1fd2724ca6b693',
    'path': '/',
    'domain': '.ecojoko.com',
    'secure': True,
    'httpOnly': False,
    'sameSite': 'None'
}, {
    'name': 'tdw',
    'value': '77ae39c158209caf09397a380488ff8c',
    'path': '/',
    'domain': '.ecojoko.com',
    'secure': True,
    'httpOnly': False,
    'expiry': 1642936760,
    'sameSite': 'None'
}]
print(foo[0].get('value'))
