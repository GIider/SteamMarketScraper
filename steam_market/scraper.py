# -*- coding: utf-8 -*-
"""Scrape the Steam Community market"""
from urllib.request import urlopen
from urllib.parse import quote

__all__ = ['get_url', 'get_content']

STEAM_MARKET_LISTINGS_URL = 'http://steamcommunity.com/market/listings/'


def get_url(game, item, filter_criteria=None):
    """Get the url for a Steam Community Market query"""
    url = STEAM_MARKET_LISTINGS_URL + str(game) + '/' + quote(item)

    if filter_criteria is not None:
        url += '?filter=%s' % quote(filter_criteria)

    return url


def get_content(url):
    """Read the html from a url"""
    with urlopen(url) as f:
        content = f.read()

    return content