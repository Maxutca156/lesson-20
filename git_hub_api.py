import pprint

import requests

url = "https://api.github.com/search/code?q=addClass+in:file+language:python+user:Maxutca156"
token = "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"
#result = requests.get(url, auth=('Maxutca156', token))

headers = {
    'Autorization': f'tokenP{token}'
}

result = requests.get(url, headers=headers)

#session = requests.session()
#session.auth = ('Maxutca156', token)
#result = session.get(url)

#url = 'https://api.github.com/search/repositories?q=tetris+language:assembly&sort=stars&order=desc'
#result = session.get(url)
pprint.pprint(result.json())
