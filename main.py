import flask
import backend

app = flask.Flask(__name__)


@app.route('/api/parameters/<user_name>/<name_parameter>/<type_parameter>/<value_parameter>', methods=['POST'])
def set_parameter_one(user_name: str, name_parameter: str, type_parameter: str, value_parameter: str):
    """
    Установить параметр (имя юзера, имя параметра, тип, значение)
    Если параметр отсутствует в БД, то он добавляется, если есть – заменяется.
    Параметры устанавливаются только для существующих юзеров.
    """
    is_ok = backend.set_parameter_to_database(user_name, name_parameter, type_parameter, value_parameter)
    if not is_ok:
        return flask.Response(status=403)
    else:
        return flask.Response(status=201)


@app.route('/api/<user_name>', methods=['POST'])
def set_parameters_json(user_name: str):
    """
    Установить параметры через JSON-API
    """
    parameters = flask.request.json['Query']
    result_data = backend.set_parameters_to_database(user_name, parameters)
    if result_data is None:
        return flask.Response(status=403)
    else:
        return flask.make_response(flask.jsonify({'Result': result_data}), 201)


@app.route('/api/parameters/<user_name>/<name_parameter>/<type_parameter>', methods=['GET'])
def get_parameter_unt(user_name: str, name_parameter: str, type_parameter: str):
    """
    Получить параметр с конкретным типом и именем для пользователя.
    При отсутствии подходящего параметра – пустой список.
    """
    result_data = backend.get_parameters_from_database_unt(user_name, name_parameter, type_parameter)
    if result_data is None:
        return flask.Response(status=403)
    else:
        return flask.make_response(flask.jsonify({'Result': result_data}), 200)


@app.route('/api/parameters/<user_name>/<name_parameter>', methods=['GET'])
def get_parameter_un(user_name: str, name_parameter: str):
    """
    Получить параметры всех типов с данным именем для пользователя.
    При отсутствии подходящего параметра – пустой список.
    """
    result_data = backend.get_parameters_from_database_un(user_name, name_parameter)
    if result_data is None:
        return flask.Response(status=403)
    else:
        return flask.make_response(flask.jsonify({'Result': result_data}), 200)


@app.route('/api/parameters/<user_name>', methods=['GET'])
def get_parameter_u(user_name: str):
    """
    Получить все параметры пользователя.
    При отсутствии подходящего параметра – пустой список.
    """
    result_data = backend.get_parameters_from_database_u(user_name)
    if result_data is None:
        return flask.Response(status=403)
    else:
        return flask.make_response(flask.jsonify({'Result': result_data}), 200)


if __name__ == '__main__':
    app.run(debug=True)
