import logging
from flask import Flask
from flask.ext.appbuilder import SQLA, AppBuilder

"""
 Logging configuration
"""

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')
db = SQLA(app)
appbuilder = AppBuilder(app, db.session)


"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""    

from app import views

appbuilder.add_view(views.SuitModelView, "Suits",icon = "fa-folder-open-o",category = "Decks",
                category_icon = "fa-envelope")
appbuilder.add_view(views.CardModelView, "Cards",icon = "fa-folder-open-o",category = "Decks",
                category_icon = "fa-envelope")
appbuilder.add_view(views.DeckNameModelView, "DeckNames",icon = "fa-folder-open-o",category = "Decks",
                category_icon = "fa-envelope")
appbuilder.add_view(views.DeckModelView, "Decks",icon = "fa-folder-open-o",category = "Decks",
                category_icon = "fa-envelope")
