from csv import DictReader
import os
from django.core.management import BaseCommand

from reviews.models import (
    User, Titles, Categories, GenreTitle, Reviews, Comments
)


ALREDY_LOADED_ERROR_MESSAGE = '''
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables'''
DATA_DIR = 'static/data'
DATA_PATCH = {
    'users': os.path.join(DATA_DIR, 'users.csv'),
    'category': os.path.join(DATA_DIR, 'category.csv'),
    'titles': os.path.join(DATA_DIR, 'titles.csv'),
    'genre_title': os.path.join(DATA_DIR, 'genre_title.csv'),
    'review': os.path.join(DATA_DIR, 'review.csv'),
    'comments': os.path.join(DATA_DIR, 'comments.csv'),
}


class Command(BaseCommand):
    # Show this when the user types help
    help = 'Loads data from api_yamdb/static/data/*.csv'

    def handle(self, *args, **options):

        # Show this if the data already exist in the database
        # if User.objects.exists():
        #     print('child data already loaded...exiting.')
        #     print(ALREDY_LOADED_ERROR_MESSAGE)
        #     return

        # Show this before loading the data into the database
        print('Loading data')

        # Code to load the data into database
        for row in DictReader(open(DATA_PATCH['users'])):
            user = User(
                id=row['id'],
                username=row['username'],
                email=row['email'],
                role=row['role'],
                bio=row['bio'],
                first_name=row['first_name'],
                last_name=row['last_name'],
            )
            user.save()

        print('Loading data user')

        for row in DictReader(open(DATA_PATCH['category'])):
            category = Categories(
                id=row['id'],
                name=row['name'],
                slug=row['slug'],
            )
            category.save()

        print('Loading data category')

        for row in DictReader(open(DATA_PATCH['titles'])):
            title = Titles(
                id=row['id'],
                name=row['name'],
                year=row['year'],
                category_id=row['category'],
            )
            title.save()

        print('Loading data title')

        # for row in DictReader(open(DATA_PATCH['genre_title'])):
        #     genre_title=GenreTitle(
        #         id=row['id'],
        #         title_id=row['title_id'],
        #         genre_id=row['genre_id'],
        #     )
        #     genre_title.save()

        # print('Loading data genre_title')

        for row in DictReader(open(DATA_PATCH['review'])):
            review = Reviews(
                id=row['id'],
                title_id=row['title_id'],
                text=row['text'],
                author_id=row['author'],
                score=row['score'],
                pub_date=row['pub_date'],
            )
            review.save()

        print('Loading data review')

        for row in DictReader(open(DATA_PATCH['comments'])):
            comments = Comments(
                id=row['id'],
                review_id=row['review_id'],
                text=row['text'],
                author_id=row['author'],
                pub_date=row['pub_date'],
            )
            comments.save()

        print('Loading data comments')
