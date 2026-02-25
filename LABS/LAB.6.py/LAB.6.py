# Exercise 1: Music Library Manager

# 1. Initialize Data Structures
music_library = []


# 2. Function to Add Music
def add_song(library, title, artist, genre, duration):
    # Validation
    if not title or not artist or not genre:
        print("Error: Title, artist, and genre cannot be empty.")
        return

    try:
        duration = float(duration)
        if duration <= 0:
            print("Error: Duration must be positive.")
            return
    except ValueError:
        print("Error: Duration must be a number.")
        return

    song = {
        "title": title,
        "artist": artist,
        "genre": genre,
        "duration": duration
    }

    library.append(song)
    print(f"'{title}' by {artist} added successfully!")


# 3. Function to Display Music Library
def display_library(library, filter_artist=None, filter_genre=None):

    if not library:
        print("Music library is empty.")
        return

    filtered = library

    if filter_artist:
        filtered = [song for song in filtered if song["artist"].lower() == filter_artist.lower()]

    if filter_genre:
        filtered = [song for song in filtered if song["genre"].lower() == filter_genre.lower()]

    if not filtered:
        print("No songs found with given filter.")
        return

    print("\n--- Music Library ---")
    for i, song in enumerate(filtered, 1):
        print(f"{i}. Title: {song['title']}")
        print(f"   Artist: {song['artist']}")
        print(f"   Genre: {song['genre']}")
        print(f"   Duration: {song['duration']} minutes")
        print("----------------------")


# 4. Main Program Loop
while True:
    print("\nMusic Library Menu:")
    print("1. Add a new song")
    print("2. View all songs")
    print("3. Filter songs by artist")
    print("4. Filter songs by genre")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        title = input("Enter title: ")
        artist = input("Enter artist: ")
        genre = input("Enter genre: ")
        duration = input("Enter duration (minutes): ")

        add_song(music_library, title, artist, genre, duration)

    elif choice == '2':
        display_library(music_library)

    elif choice == '3':
        artist = input("Enter artist name to filter: ")
        display_library(music_library, filter_artist=artist)

    elif choice == '4':
        genre = input("Enter genre to filter: ")
        display_library(music_library, filter_genre=genre)

    elif choice == '5':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

