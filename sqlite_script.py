import csv
import sqlite3

# Function to insert cast details into SQLite
def insert_cast_details(movie_id):
    cast_ids = [...]  # List of cast IDs
    cast_names = [...]  # List of cast names

    # Connect to SQLite database
    conn = sqlite3.connect('movie_database.db')
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS cast_details
                      (movie_id INTEGER, cast_id INTEGER, full_name TEXT)''')

    # Insert cast details into the table
    for i in range(len(cast_ids)):
        values = (movie_id, cast_ids[i], cast_names[i])
        cursor.execute("INSERT INTO cast_details VALUES (?, ?, ?)", values)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Cast details have been inserted into the database")

# Example usage
movie_id = input("Enter the movie ID: ")
insert_cast_details(movie_id)
