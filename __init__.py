import requests
global username, token

def setup(usernameIn, tokenIn):
    global username, token
    username, token = usernameIn, tokenIn


def api_request(path, **data):
    global username, token
    response = requests.post(
    'https://www.pythonanywhere.com' + path.format(
        username=username,
        id=id
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)},
    data=data
    )