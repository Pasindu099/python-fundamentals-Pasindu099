from mongoengine import (
    Document,
    EmbeddedDocument,
    StringField,
    EmbeddedDocumentField,
)


class AuthorEmbedded(EmbeddedDocument):
    """Embedded author document for MongoDB."""
    full_name = StringField(required=True)
    title = StringField()


class ScientificArticle(Document):
    """Main MongoDB document for scientific articles."""
    title = StringField(required=True)
    summary = StringField(required=True)
    file_path = StringField()
    arxiv_id = StringField()
    author = EmbeddedDocumentField(AuthorEmbedded)
    text = StringField()  # stores extracted Markdown text from the PDF

    meta = {
        "collection": "scientific_articles",
        "indexes": [
            {"fields": ["$text"], "default_language": "english"}  # full-text index
        ],
    }
    