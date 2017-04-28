from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from flask_appbuilder.filemanager import ImageManager
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship
from flask import Markup, url_for

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

class Suit(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    
    def __repr__(self):
        return '%s' % (self.name)

class Card(Model):
    id = Column(Integer, primary_key=True)
    suit_id = Column(Integer, ForeignKey('suit.id'))
    suit = relationship("Suit")
    value = Column(Integer)
    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    def photo_img(self):
        im = ImageManager()
        if self.photo:
            return Markup('<a href="' + url_for('CardModelView.show', pk=str(self.id)) + \
             '" class="thumbnail"><img src="' + im.get_url(self.photo) + \
              '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for('CardModelView.show', pk=str(self.id)) + \
             '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def photo_img_thumbnail(self):
        im = ImageManager()
        if self.photo:
            return Markup('<a href="' + url_for('CardModelView.show', pk=str(self.id)) + \
             '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) + \
              '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for('CardModelView.show', pk=str(self.id)) + \
             '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')
    
    def __repr__(self):
        return '%d of %s' % (self.value, self.suit)

class DeckName(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    
    def __repr__(self):
        return self.name
    
class Deck(Model):
    id = Column(Integer, primary_key=True)
    deck_id = Column(Integer, ForeignKey('deck_name.id'))
    deck = relationship("DeckName")
    card_id = Column(Integer, ForeignKey('card.id'))
    card = relationship("Card")
    
    def __repr__(self):
        return '[%s]: %s' % (self.deck, self.card)
