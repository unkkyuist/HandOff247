"""Who is signed in, and the role check used by the routes."""
from functools import wraps

from flask import abort, redirect, session, url_for

import db


def current_user():
    user_id = session.get("user_id")
    return db.get_user(user_id) if user_id else None


def require_role(*roles):
    """Let the request through only when the signed-in user has one of the roles."""
    def decorator(fn):
        @wraps(fn)
        def inner(*args, **kwargs):
            user = current_user()
            if user is None:
                return redirect(url_for("login"))
            if user["role"] not in roles:
                abort(403)
            return fn(*args, **kwargs)
        return inner
    return decorator
