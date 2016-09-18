import logging
from urllib.parse import urljoin

import requests
import parsel

log = logging.getLogger('downloader')


class Theme:

    def __init__(self, url, name):
        self.url = url
        self.name = name
        self.image = self.find_image(self.url)

    @staticmethod
    def find_image(url):
        """finds screenshot in README.md"""
        # stupid badges getting in the way of finding the screenshots -.-
        image_blacklist = ['.svg', 'travis-ci', '//badges.', 'shields.io']
        response = requests.get(url)
        sel = parsel.Selector(text=response.text)
        image_urls = sel.xpath("//div[@id='readme']//img/@data-canonical-src").extract()
        image_urls = [i for i in image_urls
                      if not any(b in i for b in image_blacklist)]
        if not image_urls:
            image_urls = sel.xpath("//div[@id='readme']//img[not(@data-canonical-src)]/@src").extract()
        image_url = image_urls[0] if image_urls else None
        if image_url:
            image_url = urljoin(response.url, image_url)
        else:
            log.debug('no images: {}'.format(url))
        return image_url

    def __repr__(self):
        return '{} @ {}'.format(self.name, self.url)


def find_themes(url, allow_no_images=True):
    log.info('Finding themes for {}'.format(url))
    log.debug('Generate themes without images: {}'.format(allow_no_images))
    response = requests.get(url)
    sel = parsel.Selector(text=response.text)
    items = sel.xpath("//tr[re:test(td/svg/@class,'submodule|directory')]"
                      "//td[@class='content']//a")
    for i, item in enumerate(items):
        url = item.xpath('@href').extract_first()
        url = urljoin(response.url, url)
        name = item.xpath('text()').extract_first('').split('@')[0].strip()
        log.info('({}/{}) Downloading: {}'.format(i+1, len(items), name))
        t = Theme(url, name)
        if not allow_no_images and not t.image:
            log.debug('no image, drop theme {}'.format(t))
            continue
        yield t
