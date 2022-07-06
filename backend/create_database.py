import sqlite3


PATH_TO_DATABASE = 'backend/database.db'


def _create_connection() -> sqlite3.Connection:
    return sqlite3.connect(PATH_TO_DATABASE)


def _create_cursor(connection: sqlite3.Connection) -> sqlite3.Cursor:
    return connection.cursor()


def create_database() -> None:
    sql_1 = 'CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name_u TEXT UNIQUE)'
    sql_2 = """
    CREATE TABLE parameters (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, name_p TEXT, 
    type_p TEXT, value_p TEXT)
    """
    with _create_connection() as connection:
        cursor = _create_cursor(connection)
        cursor.execute(sql_1)
        connection.commit()
        cursor.execute(sql_2)
        connection.commit()


def create_user(user_name: str) -> None:
    sql = f'INSERT INTO users (name_u) VALUES ("{user_name}")'
    with _create_connection() as connection:
        cursor = _create_cursor(connection)
        cursor.execute(sql)


if __name__ == '__main__':
    create_database()
    create_user('stacy')
