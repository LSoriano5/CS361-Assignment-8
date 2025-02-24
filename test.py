import requests

url = "http://localhost:5001/recommend"


while True:
    print("Please select a choice for song recommendations:")
    print("1. Genre")
    print("2. Mood")
    print("3. Activity")
    print("4. All 3")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

   # initializing parameters.
    genre = ""
    mood = ""
    activity = ""

    # user selection.
    if choice == "1":
        genre = input("Enter genre (e.g., Rock, Rap): ")
        mood = ""  # Empty for mood and activity
        activity = ""
    elif choice == "2":
        genre = ""  # Empty for genre and activity
        mood = input("Enter mood (e.g., Energetic, Chill): ")
        activity = ""
    elif choice == "3":
        genre = ""  # Empty for genre and mood
        mood = "" 
        activity = input("Enter activity (e.g., Workout, Cooking): ")
    elif choice == "4":
        genre = input("Enter genre (e.g., Rock, Rap): ")
        mood = input("Enter mood (e.g., Energetic, Chill): ")
        activity = input("Enter activity (e.g., Workout, Cooking): ")
    elif choice == "5":
        print("Goodbye!")
        break  
    else:
        print("Invalid choice. Please select a valid option.")
        continue  

    # Prepare parameters for the request, sending info back to the microservice.
    params = {
        "genre": genre,
        "mood": mood,
        "activity": activity
    }

    # Send GET request to the microservice
    response = requests.get(url, params=params)

    # Handle the response from the microservice, parses and prints songs
    if response.status_code == 200:
        data = response.json() 
        print("Recommended Songs:")
        for song in data["songs"]:
            print(f"- {song}")
        if "note" in data:
            print(f"Note: {data['note']}")
    else:
        print("Error:", response.json().get("error", "Unknown Error"))

    # Ask the user if they want to make another selection
    another_choice = input("Do you want to select another option? (yes/no): ").lower()
    if another_choice != "yes":
        print("Thanks for using, see you again!")
        break   