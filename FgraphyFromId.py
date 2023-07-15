from tmdbv3api import TMDb, Person
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

# Function to get the filmography details for a person
def get_person_filmography(person_id):
    person = Person()
    filmography = person.movie_credits(person_id).cast
    return filmography

# Function to add the film IDs and names to columns 5 and 6
def add_filmography_details(person_id):
    filmography = get_person_filmography(person_id)
    film_ids = [film['id'] for film in filmography]
    film_names = [film['title'] for film in filmography]

    # Add the filmography details to columns 5 and 6 (modify as per your needs)
    for i in range(len(film_ids)):
        # Replace the following line with your desired method of adding the filmography details to columns
        print(f"Column 5: {film_ids[i]}, Column 6: {film_names[i]}")

# Example usage
person_id = input("Enter the person ID: ")
add_filmography_details(person_id)
