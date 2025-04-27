import psycopg2

def get_conn():
    return psycopg2.connect(
        database="DA_APR_PROJECT", 
        user="postgres", 
        password="941125",
        host="localhost",
        port="5432"
    )
