from database import execute_select


def get_all_users():
    return execute_select("select name, password from users;")


def get_user_by_id(id): # <- id = valoarea
    #   %(cheia)s
    #
    # { "cheia": valoarea }
    return execute_select(
        "select name, password from users where id = %(id)s;", {"id": id}
        # "select name, password from users where id = '7 or 1 = 1; drop table users';"
    )

def selecting_and_updating(id, name):
    return execute_select("""
        select username where id = %(id)s;
        set name = 'gigi' where name = %(name)s;
        delete from users where id = %(id)s;
    """, {
        "id": id,
        "name": name
    })