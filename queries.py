from database import execute_select


def get_all_users():
    return execute_select("select name, password from users;")
