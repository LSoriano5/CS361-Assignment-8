# How to request data from the Microservice
To be able to request data from the microservice, the user has to select one of the given parameters of (Genre, Mood, Activity, or all 3) then it will make a GET request to the /recommend endpoint of the microservice. An example call for this would be:

    URL = "http://localhost:5001/recommend" (endpoint can be anything)

    params = {your 3 given parameters}
    
    userResponse = requests.get(url, params=params)

    if the response is valid:
      print (the recommended songs)
    else:
      print(Error!)

that way whatever user input was given, it will send the request to whatever endpoint you want to give the microservice. I gave it /recommend.

# How to receive data from the Microservice
Once a request was made to the url enpoint, it will run through the function to read the parameters selected, create a ceate based on what parameters are choosen and loop to check each key and compare it to the key made from user input. If the request was successful and keys match, the microservice will send over the recommended songs based on the selected parameters. An example call for this would look 

      for existing key in song_database
          set match to true
          if genre is not empty and genre!= existing key
              match = false
          if mood is not empty and mood!= existing key
              match = false
          if activity is not emtpy and activity!= existing key
              match = false
          if match
              return recommended songs


# UML Sequence Diagram

      https://github.com/user-attachments/assets/e1edfee8-5e21-45b8-a5b8-c550c0c072ea




