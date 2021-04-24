from flask import Flask, render_template
from secrets import API_KEY
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    header = "Welcome"
    return f'<h1> {header}! </h1>'

@app.route('/name/<nm>')
def name(nm):
    return render_template('name.html', name=nm)

@app.route('/headlines/<nm>')
def headlines(nm):
    results = requests.get(BASE_URL + endpoint).json()['results']
    tech_headlines = {}
    for result in results:
        title = result['title']
        section = result['section']
        url = result['url']
        if section == 'technology':
            #print(section, title)
            #print('-------------------------------')
            tech_headlines[title] = url
    return render_template('headlines.html', headlines=tech_headlines, name=nm)

BASE_URL = 'https://api.nytimes.com/svc/topstories/v2/'
endpoint = 'technology.json' + '?api-key=' + API_KEY

def write_response_to_json(results, file_name):
    with open(file_name, 'w') as f:
        json.dump(results, f)

if __name__ == '__main__':
    app.run(debug=True)

    #write_response_to_json(results, 'get_tech_headlines_response.json')
