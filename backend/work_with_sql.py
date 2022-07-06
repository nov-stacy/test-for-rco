import sqlite3


PATH_TO_DATABASE = 'backend/database.db'


def _create_connection() -> sqlite3.Connection:
    return sqlite3.connect(PATH_TO_DATABASE)


def _create_cursor(connection: sqlite3.Connection) -> sqlite3.Cursor:
    return connection.cursor()


def get_user_from_table(user_name: str) -> bool:
    sql = f'SELECT id FROM users WHERE name_u = "{user_name}"'
    with _create_connection() as connection:
        cursor = _create_cursor(connection)
        cursor.execute(sql)
        result = cursor.fetchall()
    return result[0][0] if len(result) == 1 else None


def get_parameters_from_table_unt(user_id: int, name_parameter: str, type_parameter: str):
    sql = f'SELECT name_p, type_p, value_p FROM parameters ' \
          f'WHERE user_id = {user_id} AND name_p = "{name_parameter}" ' \
          f'AND type_p = "{type_parameter}"'
    with _create_connection() as connection:
        cursor = _create_cursor(connection)
        cursor.execute(sql)
        result = cursor.fetchall()
    return result


def get_parameters_from_table_un(user_id: int, name_parameter: str):
    sql = f'SELECT name_p, type_p, value_p FROM parameters ' \
          f'WHERE user_id = {user_id} AND name_p = "{name_parameter}"'
    with _create_connection() as connection:
        cursor = _create_cursor(connection)
        cursor.execute(sql)
        result = cursor.fetchall()
    return result


def get_parameters_from_table_u(user_id: int):
    sql = f'SELECT name_p, type_p, value_p FROM parameters ' \
          f'WHERE user_id = {user_id}'
    with _create_connection() as connection:
        cursor = _create_cursor(connection)
        cursor.execute(sql)
        result = cursor.fetchall()
    return result


def set_parameters_to_table(user_id: int, name_parameter: str, type_parameter: str, value_parameter: str) -> None:
    sql = f'INSERT INTO parameters (user_id, name_p, type_p, value_p) VALUES ' \
          f'({user_id}, "{name_parameter}", "{type_parameter}", "{value_parameter}")'
    with _create_connection() as connection:
        cursor = _create_cursor(connection)
        cursor.execute(sql)
        connection.commit()


def update_parameters_in_table(user_id: int, name_parameter: str, type_parameter: str, value_parameter: str) -> None:
    sql = f'UPDATE parameters SET value_p = "{value_parameter}" ' \
          f'WHERE user_id = {user_id} AND name_p = "{name_parameter}" ' \
          f'AND type_p = "{type_parameter}"'
    with _create_connection() as connection:
        cursor = _create_cursor(connection)
        cursor.execute(sql)
        connection.commit()
