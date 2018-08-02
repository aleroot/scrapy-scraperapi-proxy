Scraper API middleware for Scrapy (http://scrapy.org/)
=======================================================

Processes Scrapy requests a man in the middle proxy service like https://www.scraperapi.com or https://proxycrawl.com


Install
--------

Checkout the source and run

    python setup.py install


settings.py
-----------

    # Activate the middleware
    SCRAPERAPI_ENABLED = True
    # Address of the API service
    SCRAPERAPI_URL='api.proxycrawl.com'
    #The API key 
    SCRAPERAPI_KEY='your API key'

    DOWNLOADER_MIDDLEWARES = {
        'scrapy_scraperapi.ScraperApiProxy': 610,
    }


