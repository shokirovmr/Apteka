from datetime import datetime

import aiomysql
import asyncio
from environs import Env

env = Env()
env.read_env('envs/.env')


class Database:
    def __init__(self):
        self.pool = None

    async def connect(self):
        self.pool = await aiomysql.create_pool(
            host=env.str('DB_HOST'),
            port=env.int('DB_PORT'),
            user=env.str('DB_USER'),
            password=env.str('DB_PASSWORD'),
            db=env.str('DB_NAME'),
            autocommit=True
        )

    async def execute(self, query, args: tuple = (), fetchone=False, fetchall=False):
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(query, args)
                if fetchone:
                    return await cur.fetchone()
                elif fetchall:
                    return await cur.fetchall()
                else:
                    return None

    async def add_type(self, name_uz, name_ru, name_en, id=None, *args):
        query = ("INSERT INTO types (name, name_uz, name_ru, name_en, created_at, updated_at)"
                 "VALUES (%s, %s, %s, %s, %s, %s);")
        await self.execute(query, (name_uz, name_uz, name_ru, name_en, datetime.now(), datetime.now()))

    async def select_types(self):
        query = "SELECT id, name FROM types;"
        return await self.execute(query, fetchall=True)

    async def select_type(self, id):
        query = "SELECT id, name, name_ru, name_en FROM types WHERE id=%s;"
        return await self.execute(query, (id, ), fetchone=True)

    async def delete_type(self, id):
        # Assuming `type_id` can be set to NULL or you have a default type_id
        update_query = "UPDATE pills SET type_id = NULL WHERE type_id = %s;"
        await self.execute(update_query, (id,))

        # Now, attempt to delete the type
        delete_query = "DELETE FROM types WHERE id = %s;"
        await self.execute(delete_query, (id,))

    async def update_type(self, id, name_uz, name_ru, name_en):
        query = "UPDATE types SET name = %s, name_uz = %s, name_ru = %s, name_en = %s WHERE id = %s;"
        await self.execute(query, (name_uz, name_uz, name_ru, name_en, id))
