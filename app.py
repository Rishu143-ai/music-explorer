from flask import Flask, render_template, request
import requests as req

app = Flask(__name__)

def get_songs(query):
    result = req.get("https://saavn.sumit.co/api/search/songs",
                     params={
                         "query": query,
                         "page": "0",
                         "limit": "20"
                     })
    all_json = result.json()
    songs = all_json['data']['results']
    return songs

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template('index.html', songs=[])
    elif request.method == "POST":
        query = request.form.get('song-search', '')
        try:
            songs = get_songs(query)
            return render_template("index.html", songs=songs)
        except Exception as e:
            return render_template("index.html", songs=[], error="Failed to fetch songs. Please try again.")

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

