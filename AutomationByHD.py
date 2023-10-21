import json
import requests

def my_test_function():
    my_test = "Hello, Hang."
    print(my_test)

print("Stop here foer debugging.")
my_test_function()

def my_scrapping():
    r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

    # check status code for response received
    # success code - 200
    print(r)

    # print content of request
    print(r.content)
