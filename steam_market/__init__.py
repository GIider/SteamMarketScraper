# -*- coding: utf-8 -*-
"""Steam Community Market Scraper

Example usage:
    >>> import steam_market
    >>> game = 440
    >>> item = 'Professional Killstreak Phlogistinator Kit'
    >>> filter_criteria = 'Deadly Daffodil'
    >>> page = steam_market.MarketPage(game=game, item=item, filter_criteria=filter_criteria)
    >>> print(page.amount_of_listings)
    5
    >>> print(page.lowest_price)
    R$ 35,20
"""
import enum

from .parser import *
from .scraper import *

__all__ = ['get_amount_of_market_listings']


class Games(enum.IntEnum):
    TF2 = 440


class MarketPage(object):
    def __init__(self, game, item, filter_criteria=None):
        self.game = game
        self.item = item
        self.filter_criteria = filter

        self.url = get_url(game=game, item=item, filter_criteria=filter_criteria)
        self.soup = get_soup(url=self.url)

    @property
    def amount_of_listings(self):
        return get_total_amount_of_listings(soup=self.soup)

    @property
    def lowest_price(self):
        return get_lowest_price(soup=self.soup)