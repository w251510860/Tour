import functools

from flask import session, g


def user_login_data(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        user_id = session.get('user_id')
        user = None
        if user_id:
            from project.modules.models import User
            user = User.query.get(user_id)
        g.user = user
        return f(*args, **kwargs)

    return wrapper
