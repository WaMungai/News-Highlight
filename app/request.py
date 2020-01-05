import urllib.request,json
from .model import Source,Article

api_key=None
base_url=None
article_url=None

def configure_request(app):
    global api_key,base_url,article_url
    
    api_key = app.config['API_KEY']
    
    base_url= app.config['SOURCE_BASE_URL']
    print('********base source url*******')
    print(base_url)

    article_url = app.config['ARTICLE_BASE_URL']
    print('*******base article url*********')
    print(article_url)
    
def process_souce(source_list):
    source_results =[]
    
    for source_item in source_list:
        id = source_item.get('id')
        name =  source_item.get('name')
        language =source_item.get('language')
        country =source_item.get('country')
        
        source_object=Source(id,name,description,url,category,language,country)
        source_results.append(source_object)
    
    return source_results

def get_source(category):
    get_source_url =base_url.format(category,api_key)
    print('********get_source_url***********')
    print(get_source_url)
    
    with urllib.request.urlopen(get_source-url)as url:
        get_source_data = url.read()
        get_source_response=json.loads(get_source_data)
        
    return source_results

def process_articles(article_list):
    article:object=[]
    
    for article_item in article_list : 
        id = article_item.get('id')
        author=article_item.get('author')
        title=article_item.get('title')
        description=article_item.get('description')
        url=article_item.get('url')
        image=article_item.get('urlToImage')      
        date=article_item.get('publishedAt')
        
    if url:
        article_reults=article_list(id,author,title,description,url,image,date)
        article_object.append(article_result)
        
    return article_objects

def get_articles(id):
    '''
    Function that processes the articles and returns a list of articles get_objects
    '''
    get_articles_url = articles_url.format(id,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        articles_results=json.loads(url.read())
        articles_object =None
        if articles_results['articles']:
            articles_object=process_articles(articles_results['articles'])
            return articles_object
    