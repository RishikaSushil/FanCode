#!/usr/bin/python3

import requests

def isInFanCode(geo):
    if float(geo['lat']) > -40 and float(geo['lat']) < 5 and float(geo['lng']) > 5 and float(geo['lng']) < 100:
        return True
    return False

def percentTasksCompleted(todos):
    completed = 0
    for todo in todos:
        if todo['completed']:
            completed += 1
    return (completed / len(todos)) * 100

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    user_count = 1
    user_data = requests.get(url + '/users/' + str(user_count)).json()

    while user_data:
        if isInFanCode(user_data['address']['geo']):
            print("This user is in FanCode! User ID: " + str(user_count))
        user_count += 1
        user_data = requests.get(url + '/users/' + str(user_count)).json()

