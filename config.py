import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kevin:Password2@localhost/blogger'
    SECRET_KEY = 'mykey'
    QUOTES_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kevin:Password2@localhost/blogger'

    

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kevin:Password2@localhost/blogger'
    
    DEBUG = True
    pass
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kevin:Password2@localhost/blog_test'

    
    
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}

