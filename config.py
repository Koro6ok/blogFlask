import os


class Config:
    WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
    WEATHER_API_URL = os.environ.get("WEATHER_API_URL")
    WEATHER_API_HOST = os.environ.get("WEATHER_API_HOST")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    UPLOAD_PATH = 'static/uploads/'
    BLOG_TITLE = {
        "name": "Blog Cursor",
        "description": "Школа програмування. Ефективна та неформальна IT освiта"
    }
    MENU_ITEMS = [
        {
            'name': "Articles",
            'link': '/articles',
        },
        {
            'name': "Categories",
            'link': '/categories',
        },
    ]

    FOOTER_LINKS = {
        "link1": "https://www.youtube.com/watch?v=xyqmicwcaY8&t=6s",
        "name_link1": "CURSOR.Education",

        "link2": "/contact-us",
        "name_link2":"Contact form"
    }

    FOOTER_INFO = {
        "address": "ОНЛАЙН ОФІС",
        "mob-tel": "+38 (067) 527 30 54",
        "email": "cursor.education@gmail.com"
    }




def articles():
    return [
        {
            "title": "Test Article",
            "img": "https://rozetked.me/images/uploads/dwoilp3BVjlE.jpg",
            "short_description": "bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla blabla bla bla bla bla bla bla",
            "slug": 'test-article'
        },
        {
            "title": "Test Article2",
            "img": "https://rozetked.me/images/uploads/dwoilp3BVjlE.jpg",
            "short_description": "bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla blabla bla bla bla bla bla bla",
            "slug": 'test-article2'
        },
    ]