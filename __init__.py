import requests
global username, token

def setup(usernameIn, tokenIn):
    global username, token
    username, token = usernameIn, tokenIn


def api_request(path, method, **data):
    global username, token
    if method=="post":
        run = requests.post
    elif method=="get":
        run = requests.get
    elif method=="put":
        run = requests.put
    elif method=="delete":
        run = requests.delete
    response = run(
    'https://www.pythonanywhere.com' + path.replace("[username]", username),
    headers={'Authorization': 'Token {token}'.format(token=token)},
    data=data
    )
    return response
