"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7mad269vf5qb91tcg-a.oregon-postgres.render.com",
        database="assignment_4u06",
        user="root",
        password="MLyBywmJIaiJZuaTLHQZq6xVHyRwy38y")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
