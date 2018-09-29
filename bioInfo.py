import requests
from flask import Flask,render_template
app = Flask(__name__)

linked_client_id ='78goqqwig5hwzc'
linked_client_secret='zJp4N571RpMQGPeW'


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/gettorrebio')
def get_torrebio():
    resp = requests.get('https://torre.bio/api/people/sandralancheros')
    if resp.status_code != 200:
        return "error"
    else:
        return str(resp.json())

@app.route('/bio')
def get_bio():
    resp = requests.get('https://torre.bio/api/people/sandralancheros')
    if resp.status_code != 200:
        return "error"
    else:
        user = resp.json()['publicId']
        name = resp.json()['name']
        return render_template('index.html', author=author, name=name)


@app.route('/linkedIn/Oauth', methods=['POST'])
def linked_authorization():
    resp = requests.get('https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id='+linked_client_id+'&redirect_uri=http%3A%2F%2F34.207.142.147%2F&state=987654321&scope=r_basicprofile')
    if resp.status_code != 200:
        return "error"
    else:
        return str(resp.json())



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
