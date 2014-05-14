# -*- coding: utf-8 -*-
"""Scrape the Steam Community market"""
from urllib.request import urlopen, Request
from urllib.parse import quote

from bs4 import BeautifulSoup

__all__ = ['get_url', 'get_soup']

STEAM_MARKET_LISTINGS_URL = 'http://steamcommunity.com/market/listings/'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36'


def get_url(game, item, filter_criteria=None):
    """Get the url for a Steam Community Market query"""
    url = STEAM_MARKET_LISTINGS_URL + str(game) + '/' + quote(item)

    if filter_criteria is not None:
        url += '?filter=%s' % quote(filter_criteria)

    return url


def get_soup(url):
    """Read the html from a url and return a soup object"""
    request = Request(url, headers={'User-Agent': USER_AGENT})

    with urlopen(request) as f:
        content = f.read()

    return BeautifulSoup(content)