from utils.env import DATABASE_CONFIG
import psycopg2
import boto3
import sys
import os

def connect_to_rds():
    try:
        connection = psycopg2.connect(
            host=DATABASE_CONFIG['DATABASE_ENDPOINT'],
            port=DATABASE_CONFIG['PORT'],
            database=DATABASE_CONFIG['DATABASE_NAME'],
            user=DATABASE_CONFIG['DATABASE_USER'],
            password=DATABASE_CONFIG['DATABASE_PASSWORD']
        )
        print("Connection to RDS successful")
        return connection
    except Exception as e:
        print(f"Error connecting to RDS: {e}")
        sys.exit(1)

def execute_query(query, params=None, fetch=False):
    conn = connect_to_rds()
    try:
        cursor = conn.cursor()
        print(f"Executing query: {query}")
        print(f"With parameters: {params}")
        cursor.execute(query, params)
        if fetch:
            result = cursor.fetchall()
            print(f"Query result: {result}")
        else:
            conn.commit()
            result = None
            print("Transaction committed")
        cursor.close()
        return result
    except Exception as e:
        print(f"Database error: {e}")
        return None
    finally:
        conn.close()
        print("Connection closed")