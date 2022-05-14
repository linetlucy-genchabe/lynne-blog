import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lynne:lynne2022@localhost/lynneblog'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'lynneblog'
    SENDER_EMAIL = 'linetlucy21@gmail.com'

    

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lynne:lynne2022@localhost/lynneblog'
    pass
    


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lynne:lynne2022@localhost/lynneblog'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}