from database import execute_select


def get_all_users():
    return execute_select("select name, password from users;")


def get_user_by_id(id): # <- id = valoarea
    #   %(cheia)%
    #
    # { "cheia": valoarea }
    return execute_select(
        "select name, password from users where id = %(id)s;", {"id": id}
        # "select name, password from users where id = '7 or 1 = 1; drop table users';"
    )
