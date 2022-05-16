import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lynne:lynne2022@localhost/blogs'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'lynneblog'
    SENDER_EMAIL = 'linetlucy21@gmail.com'

    

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://egytnmiusukpcj:2a057ec507e78cac94ae8f70b5600db2ff59727a1354da0b437445bfb08db32f@ec2-3-229-11-55.compute-1.amazonaws.com:5432/d59g9e816k8rj2'
    
    


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lynne:lynne2022@localhost/blogs'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}