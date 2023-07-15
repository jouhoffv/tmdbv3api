from tmdbv3api import TMDb, Movie
import csv

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

# Function to get the cast details for a movie
def get_movie_cast(movie_id):
    movie = Movie()
    cast = movie.credits(movie_id).cast
    return cast

# Function to add the cast IDs and full names to columns 3 and 4
def add_cast_details(movie_id):
    cast = get_movie_cast(movie_id)
    cast_ids = [member['id'] for member in cast]
    cast_names = [member['name'] for member in cast]

    # Add the cast details to columns 3 and 4 (modify as per your needs)
    for i in range(len(cast_ids)):
        # Replace the following line with your desired method of adding the cast details to columns
        print(f"Column 3: {cast_ids[i]}, Column 4: {cast_names[i]}")

# Example usage
movie_id = input("Enter the movie ID: ")
add_cast_details(movie_id)
