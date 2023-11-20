from flask import Flask, request, jsonify, render_template
import Levenshtein

app = Flask(__name__)  # Use __name__ instead of _name_

# Sample MusicBrainz database (song titles and artists)
musicbrainz_database = [
    ("I Wanna Hold Your Hand", "The Beatles"),
    # ... rest of the database entries ...
]

def search_song_by_lyrics(input_lyrics, database):
    # Initialize a list to store matching songs and their Levenshtein distances
    matches = []

    # Calculate the Levenshtein distance between input lyrics and song titles in the database
    for title, artist in database:
        distance = Levenshtein.distance(input_lyrics.lower(), title.lower())
        matches.append((title, artist, distance))

    # Sort the matches by Levenshtein distance (lower distance means a better match)
    matches.sort(key=lambda x: x[2])

    return matches

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    input_lyrics = request.form['lyricsInput']
    matching_songs = search_song_by_lyrics(input_lyrics, musicbrainz_database)

    # Return the matching songs as JSON
    return jsonify(matching_songs[:10])  # Limit to 10 results

if __name__ == '__main__':  # Use double underscores and '__main__'
    app.run(debug=True)
