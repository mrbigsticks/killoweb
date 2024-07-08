

import requests

flag = True

url = 'http://www.momommommom.com'


data = {'a': 'fakeemail@fe.com', 'az': 'fake password',
}

while flag:
    response = requests.post(url, data=data)
    print(response.status_code)


