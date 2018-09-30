import requests
from flask import Flask,render_template
app = Flask(__name__)

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
        photo = resp.json()['picture']
        headline = resp.json()['professionalHeadline']
        return render_template('index.html', user=user, name=name, photo=photo, headline = headline)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
