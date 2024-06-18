#!/usr/bin/python3

import requests

def isInFanCode(geo):
    if geo['lat'] > -40 and geo['lat'] < 5 and geo['lng'] > 5 and geo['lng'] < 100:
        return True
    return False

def percentTasksCompleted(todos):
    completed = 0
    for todo in todos:
        if todo['completed']:
            completed += 1
    return (completed / len(todos)) * 100

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/1'
    print(requests.get(url).json())
