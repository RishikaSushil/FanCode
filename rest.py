#!/usr/bin/python3

import requests

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/1'
    print(requests.get(url).json())
