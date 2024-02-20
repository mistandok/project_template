import logging
import os
import sys
import logging
from pathlib import Path

import asyncpg
from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from aiohttp.web_app import Application
from asyncpg import Pool, Record
from pydantic_settings import BaseSettings

BASE_DIR = Path(os.path.dirname(os.path.dirname(__file__)))
ROOT_DIR = BASE_DIR.parent


class Settings(BaseSettings):
    pg_host: str
    pg_port: int
    db_driver: str
    postgres_user: str
    postgres_password: str
    postgres_db: str
    app_host: str
    app_port: int


routes = web.RouteTableDef()
DB_KEY = 'database'
settings = None


@routes.get('/note/{id}')
async def get_example(request: Request) -> Response:
    note_id = int(request.match_info['id'])

    query = """
    SELECT
        id,
        name,
        description
    FROM
        note
    WHERE
        note.id = $1
    """

    connection: Pool = request.app[DB_KEY]
    result: Record = await connection.fetchrow(query, note_id)

    if result is not None:
        return web.json_response(dict(result))

    raise web.HTTPNotFound()


async def create_database_pool(app: Application):
    print("создается пул подключений")
    pool: Pool = await asyncpg.create_pool(
        host=settings.pg_host,
        port=settings.pg_port,
        user=settings.postgres_user,
        password=settings.postgres_password,
        database=settings.postgres_db,
        min_size=6,
        max_size=6,
    )
    app[DB_KEY] = pool


async def destroy_database_pool(app: Application):
    print('уничтожается пул подключений')
    pool: Pool = app[DB_KEY]
    await pool.close()


if __name__ == '__main__':
    _, env_name = sys.argv
    logging.info("try start app")
    print(env_name)
    settings = Settings(_env_file=os.path.join(ROOT_DIR, env_name))
    app = web.Application()
    app.on_startup.append(create_database_pool)
    app.on_cleanup.append(destroy_database_pool)

    app.add_routes(routes)
    web.run_app(app, host=settings.app_host, port=settings.app_port, )
