from flask import Flask, render_template, request,redirect
import requests as req
app = Flask(__name__)
import io

def get_songs(query):
    result = req.get("https://saavn.sumit.co/api/search/songs",
                     params={
                         "query": query,
                         "page": "0",
                         "limit": "20"
                     })
    all_json = result.json()
    songs = all_json['data']['results']
    # song_names = []

    # for song in songs:
    #     song_names.append(song['name'])
    return songs

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == "GET":    
        return render_template('home.html', songs=[])
    elif request.method == "POST":
        query = request.form['song-search']
        
        return render_template("home.html",songs=get_songs(query))
    


    
@app.route('/about',methods=['GET','POST'])
def about():
    return render_template('about.html')

app.run(debug=True)

