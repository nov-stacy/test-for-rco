import backend.work_with_sql as work_with_sql
import typing as tp


def get_user_id(user_name: str) -> int:
    user_id = work_with_sql.get_user_from_table(user_name)
    return user_id


def check_type_parameter(type_parameter: str) -> bool:
    return type_parameter in ['str', 'int']


def check_value_parameter(type_parameter: str, value_parameter: str) -> None:
    return type_parameter == 'str' or value_parameter.isdigit()


def set_parameter_to_database(user_name: str, name_parameter: str, type_parameter: str, value_parameter: str) -> bool:
    user_id = get_user_id(user_name)
    if user_id is None:
        return False
    if not(check_type_parameter(type_parameter) and check_value_parameter(type_parameter, value_parameter)):
        return False
    if not len(work_with_sql.get_parameters_from_table_unt(user_id, name_parameter, type_parameter)):
        work_with_sql.set_parameters_to_table(user_id, name_parameter, type_parameter, value_parameter)
    else:
        work_with_sql.update_parameters_in_table(user_id, name_parameter, type_parameter, value_parameter)
    return True


def set_parameters_to_database(user_name: str, parameters: tp.List[tp.Dict[str, str]]) -> tp.List[tp.Dict[str, str]]:
    user_id = get_user_id(user_name)
    if user_id is None:
        return None
    result = []
    for parameter in parameters:
        name_parameter, type_parameter, value_parameter = parameter['Name'], parameter['Type'], str(parameter['Value'])
        if not (check_type_parameter(type_parameter) and check_value_parameter(type_parameter, value_parameter)):
            result.append({
                'Operation': parameter['Operation'],
                'Name': name_parameter,
                'Type': type_parameter,
                'Status': 'ERROR'
            })
        else:
            if not len(work_with_sql.get_parameters_from_table_unt(user_id, name_parameter, type_parameter)):
                work_with_sql.set_parameters_to_table(user_id, name_parameter, type_parameter, value_parameter)
            else:
                work_with_sql.update_parameters_in_table(user_id, name_parameter, type_parameter, value_parameter)
            result.append({
                'Operation': parameter['Operation'],
                'Name': name_parameter,
                'Type': type_parameter,
                'Status': 'OK'
            })
    return result


def get_parameters_from_database_unt(user_name: str, name_parameter: str,
                                     type_parameter: str) -> tp.List[tp.Dict[str, tp.Any]]:
    user_id = get_user_id(user_name)
    if user_id is None:
        return None
    if not check_type_parameter(type_parameter):
        return None
    result_from_table = work_with_sql.get_parameters_from_table_unt(user_id, name_parameter, type_parameter)
    return [
        {
            'name_parameter': name,
            'type_parameter': type_,
            'value_parameter': int(value) if type_ == 'int' else value}
        for name, type_, value in result_from_table
    ]


def get_parameters_from_database_un(user_name: str, name_parameter: str) -> tp.List[tp.Dict[str, tp.Any]]:
    user_id = get_user_id(user_name)
    if user_id is None:
        return None
    result_from_table = work_with_sql.get_parameters_from_table_un(user_id, name_parameter)
    return [
        {
            'name_parameter': name,
            'type_parameter': type_,
            'value_parameter': int(value) if type_ == 'int' else value}
        for name, type_, value in result_from_table
    ]


def get_parameters_from_database_u(user_name: str):
    user_id = get_user_id(user_name)
    if user_id is None:
        return None
    result_from_table = work_with_sql.get_parameters_from_table_u(user_id)
    return [
        {
            'name_parameter': name,
            'type_parameter': type_,
            'value_parameter': int(value) if type_ == 'int' else value}
        for name, type_, value in result_from_table
    ]
