from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Hardcoded song database for you to input your own.
song_database = {
    ("Rock", "Energetic", "Workout"): [
        "Thunderstruck - AC/DC", "Livin on a Prayer - Bon Jovi", "Eye of the Tiger - Survivor", "Welcome to the Jungle - Guns N' Roses", "We Will Rock You - Queen"
    ],
    ("Rap", "Chill", "Cooking"): [
        "Kick, Push - Lupe Fiasco", "Soundtrack 2 My Life - Kid Cudi", "Still Not a Player - Big Pun", "Just a Friend - Biz Markie", "Good Life - Kanye West"
    ],
}

# flask will run the app when a GET requestis made to /recommend URL from main service
@app.route('/recommend', methods=['GET']) 
# how you get pararmeters from the request, defualt to empty string if a parameter isnt given
def recommend_songs():
    genre = request.args.get('genre', '')
    mood = request.args.get('mood', '')
    activity = request.args.get('activity', '')

    # create a key based on what pararmeters are chosen.
    key = tuple(val for val in [genre, mood, activity] if val)

    if len(key) == 0:
        return jsonify({"error": "At least one parameter (genre, mood, activity) must be provided."}), 400

    # loop to check each key and compare it to the key made from user input
    for existing_key in song_database.keys():
        match = True
        if genre and genre.lower() != existing_key[0].lower():
            match = False
        if mood and mood.lower() != existing_key[1].lower():
            match = False
        if activity and activity.lower() != existing_key[2].lower():
            match = False
        # once matched, list of songs will be selected based on the parameters given
        if match:
            songs = random.sample(song_database[existing_key], min(5, len(song_database[existing_key])))
            return jsonify({"songs": songs})

    return jsonify({"error": "No matching songs found. Please check your input."}), 404

# running the flask app.
if __name__ == '__main__':
    app.run(port=5001, debug=False)
