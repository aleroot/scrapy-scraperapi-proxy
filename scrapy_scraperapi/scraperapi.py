# Copyright (C) 2018 by Alessio Pollero <alessio.pollero@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import urllib
import logging

log = logging.getLogger('scrapy.scraperapi')

class ScraperApiProxy(object):
    def __init__(self, settings):
        self.scraperapi_ena = settings.get('SCRAPERAPI_ENABLED', True)
        self.scraperapi_url = settings.get('SCRAPERAPI_URL', 'api.scraperapi.com')
        self.scraperapi_key = settings.get('SCRAPERAPI_KEY')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_request(self, request, spider):
        if not self.scraperapi_ena:
            log.warning("Skipping Scraper API CALL(disabled)!")
            return
        #Override request url
        if self.scraperapi_url not in request.url: 
            k_name = 'token' if ('proxycrawl' in self.scraperapi_url) else 'key'
            new_url = 'https://%s/?%s=%s&url=%s' % (self.scraperapi_url, k_name, self.scraperapi_key, urllib.quote(request.url))
            log.debug('Using Scraper API, overridden URL is: %s' % (new_url))
            return request.replace(url=new_url)
        
