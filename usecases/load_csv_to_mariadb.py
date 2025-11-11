import csv
from sqlalchemy.orm import Session
from models.mariadb_models import Author, ScientificArticle
from storage.mariadb_connection import SessionLocal


def load_articles_from_csv(csv_path: str) -> None:
    session: Session = SessionLocal()

    try:
        with open(csv_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Check if author already exists
                author = (
                    session.query(Author)
                    .filter(Author.full_name == row["author_full_name"])
                    .first()
                )

                if not author:
                    author = Author(
                        full_name=row["author_full_name"],
                        title=row["author_title"],
                    )
                    session.add(author)
                    session.flush()  # to get author.id immediately

                article = ScientificArticle(
                    title=row["title"],
                    summary=row["summary"],
                    file_path=row["file_path"],
                    arxiv_id=row["arxiv_id"],
                    author_id=author.id,
                )

                session.add(article)

        session.commit()
        print("Data loaded successfully from CSV into MariaDB.")
    except Exception as e:
        session.rollback()
        print("Error loading CSV:", e)
    finally:
        session.close()
