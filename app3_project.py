from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import psycopg2

app = FastAPI()


db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'password',
    'host': 'localhost',
    'port': '5432',
}

conn = psycopg2.connect(**db_params)
print("Conexión exitosa.")

# tasks_list = []

class Movie(BaseModel):
    tbl_name : str
    author : str
    description : str
    release_date : int

@app.get('/movies')
def get_movies(tbl_name):

    temporal_list = []

    with conn.cursor() as cursor:
        try:
    
            get_data_query = f'''
            SELECT * FROM {tbl_name};
            '''

            print(get_data_query)
            cursor.execute(get_data_query)
            rows = cursor.fetchall()

            # Procesar los resultados
            
            for row in rows:
                print(row)
                temporal_list.append(row)

        except Exception as e:
            print(f"Error: {e}")


    return {"message":temporal_list}

@app.get('/movie/{id}')
def get_movie_id(tbl_name,id):

    with conn.cursor() as cursor:
        try:
    
            get_data_query = f'''
            SELECT * FROM {tbl_name} WHERE id = {id};
            '''

            print(get_data_query)
            cursor.execute(get_data_query)
            rows = cursor.fetchall()
            print(rows)

        except Exception as e:
            print(f"Error: {e}")

    return {"message":rows}

@app.post('/movies')
def create_movies(movie:Movie):

    print(movie.tbl_name)
    print(movie.author)
    print(movie.description)
    print(movie.release_date)

    with conn.cursor() as cursor:
            
        try:

            insert_data_query = f'''
            INSERT INTO {movie.tbl_name} (author, description, release_date) VALUES (%s, %s, %s);
            '''

            data_to_insert = (movie.author, movie.description, movie.release_date)
            print(data_to_insert)
            cursor.execute(insert_data_query, data_to_insert)
            conn.commit()

        except Exception as e:
            print(f"Error: {e}")


    return {"message":"Movie added correctly"}

@app.put('/movies/{id}')
def update_movies(movie:Movie,id):

    print(movie.tbl_name)
    print(movie.author)
    print(movie.description)
    print(movie.release_date)

    with conn.cursor() as cursor:
            
        try:

            insert_data_query = f'''
            UPDATE {movie.tbl_name}
            SET author = '{movie.author}', description= '{movie.description}', release_date = {movie.release_date} 
            WHERE id = {id};
            '''

            data_to_insert = (movie.author, movie.description, movie.release_date)
            print(data_to_insert)
            print(insert_data_query)
            cursor.execute(insert_data_query, data_to_insert)
            conn.commit()

        except Exception as e:
            print(f"Error: {e}")


    return {"message":"Movie updated correctly"}

@app.delete('/movies/{id}')
def remove_movie(tbl_name,id):

    print(tbl_name)

    with conn.cursor() as cursor:
            
        try:

            insert_data_query = f'''
            DELETE FROM {tbl_name}
            WHERE id = {id};
            '''

            print(insert_data_query)
            cursor.execute(insert_data_query)
            conn.commit()

        except Exception as e:
            print(f"Error: {e}")


    return {"message":"Movie updated correctly"}