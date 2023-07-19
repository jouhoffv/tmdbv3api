from tmdbv3api import TMDb, Person, Movie
import csv
import argparse

# Create an instance of TMDb
tmdb = TMDb()

# Function to read the API key from .secrets/rootkey.csv
def read_api_key():
    with open('.secrets/rootkey3.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            return row[0]  # Assuming the API key is in the first column (modify as per your CSV structure)

# Set the API key
tmdb.api_key = read_api_key()

# Function to get the filmography details for a person
def get_person_filmography(person_id):
    person = Person()
    filmography = person.movie_credits(person_id).cast
    return filmography

# Function to get the genre names for a movie ID
def get_movie_genres(movie_id):
    movie = Movie()
    movie_details = movie.details(movie_id)
    genres = movie_details.genres
    return genres

# Function to add the film IDs, names, release years, and genres to columns 5, 6, and additional columns
def add_filmography_details(person_id):
    filmography = get_person_filmography(person_id)

    # Collect unique genre names from the filmography
    unique_genres = set()
    for film in filmography:
        movie_id = film['id']
        genres = get_movie_genres(movie_id)
        for genre in genres:
            unique_genres.add(genre['name'])

    # Prepare CSV header
    header = ['IMDB', 'TMDB', 'TITLE', 'DATE']
    genre_columns = list(unique_genres)
    header.extend(genre_columns)

    # Prepare data rows
    rows = []
    for film in filmography:
        movie_id = film['id']
        imdb_id = get_imdb_id(movie_id)
        film_name = film['title']
        release_year = film['release_date'].split('-')[0] if film['release_date'] else 'N/A'
        genres = get_movie_genres(movie_id)

        row = [imdb_id, movie_id, film_name, release_year]
        for genre_column in genre_columns:
            if any(genre['name'] == genre_column for genre in genres):
                row.append('X')
            else:
                row.append('')

        rows.append(row)

    # Write the filmography details to a CSV file
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)  # Write header row
        writer.writerows(rows)  # Write data rows

    print("Filmography details have been written to output.csv")

# Function to get the IMDb ID for a movie ID
def get_imdb_id(movie_id):
    movie = Movie()
    movie_external_ids = movie.external_ids(movie_id)
    return movie_external_ids.get('imdb_id', 'N/A')

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Script to retrieve filmography details and genres for a person")
parser.add_argument("--genre", action="store_true", help="Include genres in output")
parser.add_argument("-t", "--testing", action="store_true", help="Enable testing mode")
args = parser.parse_args()

# Example usage
if args.testing:
    person_id = '17838'  # Testing mode using ID 17838
else:
    person_id = input("Enter the person ID: ")

add_filmography_details(person_id)
