import settings
import os
import mysql.connector

connection = mysql.connector.connect(
    user = "root",
    password = os.getenv("SQL_PWD"),
    host = 'localhost',
    database = "company_db"
)
