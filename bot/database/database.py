import datetime
import sqlite3


class Database:
    def __init__(self):
        self.pool = None

    async def connect(self):
        self.pool = sqlite3.connect('../db.sqlite3')

    async def add_type(self, name_uz, name_ru, name_en):
        query = ("INSERT INTO types (name, name_uz, name_ru, name_en, created_at, updated_at)"
                 "VALUES (?, ?, ?, ?, ?, ?);")
        cur = self.pool.cursor()
        cur.execute(query, (name_uz, name_uz, name_ru, name_en, datetime.datetime.now(), datetime.datetime.now()))
        self.pool.commit()
