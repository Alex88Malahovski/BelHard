import requests
from time import time

URL = 'https://roadres.com/images/top/audi/a7-sportback-ii.jpg'

def get_file():
    response = requests.get(URL)
    return response

def write_file(response):
    filename = response.url.split('/')[-1]
    with open('homework/' + filename, 'wb') as file:
        file.write(response.content)

def main():
    t0 = time()
    for i in range(10):
        write_file(get_file())
    print(time() -t0)

if __name__=='__main__':
    main()
