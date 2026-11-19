from models import db
import time


def init_db(app):
    db.init_app(app)

    time.sleep(10)

    with app.app_context():
        db.create_all()
