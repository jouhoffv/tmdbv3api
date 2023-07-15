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

# Function to add the film IDs, names, and release years to columns 5, 6, and 7
def add_filmography_details(person_id):
    filmography = get_person_filmography(person_id)
    film_ids = [film['id'] for film in filmography]
    film_names = [film['title'] for film in filmography]
    film_years = [film['release_date'].split('-')[0] if film['release_date'] else 'N/A' for film in filmography]

    # Write the filmography details to a CSV file
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Column 5', 'Column 6', 'Column 7'])  # Write header row
        for i in range(len(film_ids)):
            writer.writerow([film_ids[i], film_names[i], film_years[i]])

    print("Filmography details have been written to output.csv")

# Example usage
person_id = input("Enter the person ID: ")
add_filmography_details(person_id)
