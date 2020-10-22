from flask import Flask, abort
import requests
import os
import random

app = Flask('gateway')
service = os.environ['SERVICE_ADDRESS']

@app.route('/')
def index():
    r = requests.get(service + '/random')
    print(f'Got a {r.text} from the service')
    return r.text

@app.route('/health')
def health():
    r = random.randint(1,1000)
    if r == 1:
        print(f'error: {random.randint(500,599)}')
        abort(500)
    return '', 200
