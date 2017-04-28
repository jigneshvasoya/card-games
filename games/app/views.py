from flask import render_template
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder import ModelView
from app import appbuilder, db
# import models
from models import Suit, Card, Deck, DeckName

"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""

"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

class CardModelView(ModelView):
    datamodel = SQLAInterface(Card)
    list_columns = ['suit','value', 'photo_img_thumbnail']

class DeckNameModelView(ModelView):
    datamodel = SQLAInterface(DeckName)
    list_columns = ['name']

class DeckModelView(ModelView):
    datamodel = SQLAInterface(Deck)
    list_columns = ['deck','card']

class SuitModelView(ModelView):
    datamodel = SQLAInterface(Suit)
    list_columns = ['name']
    related_views = [CardModelView, DeckModelView]

db.create_all()


