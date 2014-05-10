# -*- coding: utf-8 -*-
"""Scrape the Steam Community market"""
from urllib.request import urlopen

__all__ = ['get_url', 'get_content']

STEAM_MARKET_LISTINGS_URL = 'http://steamcommunity.com/market/listings/'


# I'm sure this exists somewhere in urllib
def sanitize_name_for_web(item_name):
    return item_name.replace(' ', '%20')


def get_url(game, item, filter_criteria=None):
    """Get the url for a Steam Community Market query"""
    url = STEAM_MARKET_LISTINGS_URL + str(game) + '/' + sanitize_name_for_web(item)

    if filter_criteria is not None:
        url += '?filter=%s' % sanitize_name_for_web(filter_criteria)

    return url


def get_content(url):
    """Read the html from a url"""
    with urlopen(url) as f:
        content = f.read()

    return content