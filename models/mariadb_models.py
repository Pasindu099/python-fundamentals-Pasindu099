from __future__ import annotations
from typing import List
from sqlalchemy import String, Integer, ForeignKey, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    """Base class for ORM models."""
    pass


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[str] = mapped_column(String(50), nullable=True)

    # Relationship
    articles: Mapped[List["ScientificArticle"]] = relationship(
        "ScientificArticle", back_populates="author", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Author(id={self.id}, full_name='{self.full_name}', title='{self.title}')>"


class ScientificArticle(Base):
    __tablename__ = "scientific_articles"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    file_path: Mapped[str] = mapped_column(String(255))
    arxiv_id: Mapped[str] = mapped_column(String(50))
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))

    # Relationship
    author: Mapped["Author"] = relationship("Author", back_populates="articles")

    def __repr__(self) -> str:
        return f"<ScientificArticle(id={self.id}, title='{self.title}')>"
