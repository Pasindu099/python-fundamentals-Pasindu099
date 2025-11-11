from storage.mongodb_connection import connect  # ensures MongoDB connection
from models.mongodb_models import ScientificArticle


def search_articles(keyword: str):
    """Search for articles containing a given keyword using MongoDB text index."""
    try:
        results = ScientificArticle.objects.search_text(keyword).order_by("$text_score")

        if not results:
            print(f"No results found for '{keyword}'.")
            return

        print(f"Search results for '{keyword}':")
        for article in results:
            print(f"- {article.title} (Author: {article.author.full_name})")
    except Exception as e:
        print("Error while searching MongoDB:", e)
