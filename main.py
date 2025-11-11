from usecases.load_csv_to_mariadb import load_articles_from_csv
from usecases.transfer_to_mongodb import transfer_data_to_mongodb
from usecases.search_mongodb import search_articles
from models.mongodb_models import ScientificArticle


def main():
    print("\n=== STEP 1: Load CSV into MariaDB ===")
    load_articles_from_csv("data/articles.csv")

    print("\n=== STEP 2: Clear old MongoDB data ===")
    ScientificArticle.drop_collection()

    print("\n=== STEP 3: Transfer data to MongoDB ===")
    transfer_data_to_mongodb()

    print("\n=== STEP 4: Full-Text Search in MongoDB ===")
    search_articles("learning")
    search_articles("vision")
    search_articles("tokenization")

    print("\nPipeline completed successfully.")


if __name__ == "__main__":
    main()
