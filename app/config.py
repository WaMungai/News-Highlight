import os
class Config:
    '''
    General configuration parent class
    '''
    SOURCE_BASE_URL='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLE_BASE_URL='https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
    API_KEY= os.environ.get('API_KEY')
    API_KEY = os.environ.get('API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    class ProdConfig(Config):
        '''
        Production configuration child class
        
        Args:
            Config:The parent configuration class with General congiration settings
        '''
        pass
    
    class DevConfig(onfig):
        '''
        Development configuration child class
        
        Args:
            Config:The parent configuration class with General configuration settings
        '''
        
        DEBUG = True
        
    config_options = {
        'development':DevConfig,
        'production':ProdConfig
    }
        
    