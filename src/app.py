from fastapi_offline import FastAPIOffline
import scraper
import app_db
app = FastAPIOffline()


@app.get('/home')
def home():

    return {
        'message': 'Welcome To Divar API'
    }


@app.get('/ads')
def get_all_ads():

    data = scraper.get_ads()

    return {
        'ads': data
    }
    
@app.get('/save')
def save():

    app_db.delete_all_ads()

    ads = scraper.get_ads()

    ads = scraper.get_ads()

    if len(ads) == 0:

        return {
        'message':'No Data'
    }
    
    for item in ads:

        app_db.insert_ad(
            item['title'],
            item['price'],
            item['link']
        )

    return {'message': 'Saved Successfully'}

@app.get('/stats')
def stats():

    ads = app_db.get_all_ads()

    return {
        'count': len(ads)
    }

@app.get('/database')
def database():

    return app_db.get_all_ads()

@app.get('/search/{keyword}')
def search(keyword):

    return app_db.search_ads(keyword)


@app.get('/item/{item_id}')
def item(item_id:int):

    ads = app_db.get_all_ads()

    for ad in ads:

        if ad['id'] == item_id:

            return ad

    return {
        'message':'Not Found'
    }