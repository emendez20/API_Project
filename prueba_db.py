import psycopg2

db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'password',
    'host': 'localhost',
    'port': '5432',
}

conn = psycopg2.connect(**db_params)
print("Conexión exitosa.")


try:
    # Create a cursor
    cursor = conn.cursor()

    # Define the SQL statement to create a table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS my_movies (
        id SERIAL PRIMARY KEY,
        author VARCHAR(255),
        description VARCHAR(255),
        release_date INT
    );
    '''

    # Execute the SQL statement to create the table
    cursor.execute(create_table_query)

    # Commit changes
    conn.commit()

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and connection
    if conn:
        cursor.close()
        conn.close()
        print("Connection closed.")



# try:
#     # Create a cursor
#     cursor = conn.cursor()

#     # Insert data into the table
#     insert_data_query = '''
#     INSERT INTO your_table (column1, column2) VALUES (%s, %s);
#     '''

#     # Data to be inserted
#     data_to_insert = ('example_value', 42)

#     # Execute the SQL statement to insert data
#     cursor.execute(insert_data_query, data_to_insert)

#     # Commit changes
#     conn.commit()

# except Exception as e:
#     print(f"Error: {e}")

# finally:
#     # Close the cursor and connection
#     if conn:
#         cursor.close()
#         conn.close()
#         print("Connection closed.")