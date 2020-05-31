import os
import mysql.connector

class Database:
    def connect():
        return mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            passwd=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
