import os
from sqlalchemy.orm import Session
from storage.mariadb_connection import SessionLocal
from models.mariadb_models import Author, ScientificArticle as SQLArticle
from models.mongodb_models import AuthorEmbedded, ScientificArticle as MongoArticle
from usecases.pdf_to_markdown import pdf_to_markdown
from storage.mongodb_connection import connect


def fix_path(path: str) -> str:
    """Ensure the file path points to the correct location."""
    if path.startswith("../papers/"):
        path = path.replace("../papers/", "papers/")
    return os.path.normpath(path)


def transfer_data_to_mongodb() -> None:
    """Transfer articles and authors from MariaDB to MongoDB."""
    session: Session = SessionLocal()
    try:
        articles = session.query(SQLArticle).join(Author).all()
        if not articles:
            print("No articles found in MariaDB.")
            return

        for article in articles:
            fixed_path = fix_path(article.file_path)
            markdown_text = pdf_to_markdown(fixed_path)

            author_embedded = AuthorEmbedded(
                full_name=article.author.full_name,
                title=article.author.title,
            )

            mongo_doc = MongoArticle(
                title=article.title,
                summary=article.summary,
                file_path=fixed_path,
                arxiv_id=article.arxiv_id,
                author=author_embedded,
                text=markdown_text,
            )

            mongo_doc.save()
            print(f"Inserted: {article.title}")

        print("Data transfer from MariaDB to MongoDB completed successfully.")
    except Exception as e:
        print("Error during transfer:", e)
    finally:
        session.close()
