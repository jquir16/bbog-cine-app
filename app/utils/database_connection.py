from utils.env import DATABASE_CONFIG
import psycopg2
import boto3
import sys
import os

def connect_to_rds():
    print('Connecting to RDS...', DATABASE_CONFIG)
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
        cursor.execute(query, params)
        if fetch:
            result = cursor.fetchall()
        else:
            conn.commit()
            result = None
        cursor.close()
        return result
    except Exception as e:
        print(f"Database error: {e}")
        return None
    finally:
        conn.close()