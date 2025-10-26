import mongoengine as me
from datetime import datetime

# Embedded subdocuments
class Address(me.EmbeddedDocument):
    line1 = me.StringField(required=True)
    city = me.StringField(required=True)
    postal_code = me.StringField(required=True)
    country = me.StringField(required=True)

class Preferences(me.EmbeddedDocument):
    newsletter = me.BooleanField(default=False)
    languages = me.ListField(me.StringField())

class Profile(me.EmbeddedDocument):
    dob = me.DateTimeField(required=True)
    phone = me.StringField()
    address = me.EmbeddedDocumentField(Address)
    preferences = me.EmbeddedDocumentField(Preferences)

# Main document
class User(me.Document):
    email = me.StringField(required=True, unique=True)
    name = me.DictField()
    profile = me.EmbeddedDocumentField(Profile)
    created_at = me.DateTimeField(default=datetime.utcnow)
    updated_at = me.DateTimeField(default=datetime.utcnow)

    meta = {"collection": "users"}
