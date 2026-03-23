import json

import requests

def print_status_code(r):
    """
    Prints the status code

    Arguments
    r: HTTP response
    """

    print(f"Status Code: {r.status_code}")


def print_response_output(r):
    """
    Prints the output of the HTTP request by taking the returned JSON output,
    converting it to a Python dictionary and printing it in the format
    Key: Value

    Arguments
    r: HTTP response
    """

    response = json.loads(r.text)
    response = list(response.items())
    k, v = zip(*response)
    for i in range(0, len(k)):
        print(f"{k[i].capitalize()}: {v[i]}")


# send a GET using the URL http://127.0.0.1:8000
r = requests.get("http://127.0.0.1:8000")

# print the status code
print_status_code(r)

# print the welcome message
print_response_output(r)


data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# send a POST using the data above
r = requests.post("http://127.0.0.1:8000/data", data=json.dumps(data))

# print the status code
print_status_code(r)

# print the result
print_response_output(r)
