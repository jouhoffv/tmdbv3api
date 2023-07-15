### sqlite_script.py

Import necessary libraries:

csv: This library is used for reading CSV files, but in this script, it is not utilized.
sqlite3: This library provides functionality to interact with SQLite databases.
Define the insert_cast_details function:

This function is responsible for inserting cast details into an SQLite database.
It takes the movie_id as a parameter, which represents the movie for which the cast details will be inserted.
cast_ids and cast_names are lists that should contain the corresponding cast IDs and full names for the movie. You'll need to populate these lists with the actual values.
Connect to the SQLite database:

The script establishes a connection to the SQLite database file named "movie_database.db" using sqlite3.connect().
It creates a cursor object to execute SQL statements.
Create the table if it doesn't exist:

The script executes an SQL statement (CREATE TABLE IF NOT EXISTS) to create the "cast_details" table in the SQLite database.
This table has three columns: movie_id (INTEGER), cast_id (INTEGER), and full_name (TEXT).
Insert cast details into the table:

The script iterates over the cast_ids and cast_names lists.
For each cast member, it constructs a tuple values containing movie_id, cast_id, and cast_name.
The SQL statement INSERT INTO cast_details VALUES (?, ?, ?) is executed with the values tuple to insert the cast details into the "cast_details" table.
Commit changes and close the connection:

After inserting all the cast details, the script calls conn.commit() to commit the changes made to the SQLite database.
It then closes the connection to the database using conn.close().
Print a confirmation message:

Finally, the script prints a message to indicate that the cast details have been successfully inserted into the database.