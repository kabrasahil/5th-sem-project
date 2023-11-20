import Levenshtein

# Sample MusicBrainz database (song titles and artists)
musicbrainz_database = [
    ("I Wanna Hold Your Hand", "The Beatles"),
    ("Yesterday", "The Beatles"),
    ("Let It Be", "The Beatles"),
    ("I Know", "Travis Scott"),
    ("Drip too hard", "Gunna"),
    ("LOnely", "Akon"),
    ("Scared to be lonely", "Martin Garrix"),
    ("7 Years", "Lukas Graham"),
    ("Mr Bombastic", "Mr Bean"),
    ("Guten Tag", "Dave"),
    ("Attention", "Charlie Puth"),
    # Add more entries as needed
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

# Main program
if __name__ == "__main__":
    input_lyrics = input("Enter lyrics to search for a song: ")

    matching_songs = search_song_by_lyrics(input_lyrics, musicbrainz_database)

    if not matching_songs:
        print("No matching songs found.")
    else:
        print("Matching songs (sorted by Levenshtein distance):")
        for i, (title, artist, distance) in enumerate(matching_songs):
            if i >= 10:  # Limit to 10 results
                break
            print(f"{i+1}. Song: {title}, Artist: {artist}, Levenshtein Distance: {distance}")
