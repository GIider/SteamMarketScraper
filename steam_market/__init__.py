# -*- coding: utf-8 -*-
"""Steam Community Market Scraper"""
import enum

from .parser import *
from .scraper import *

__all__ = ['get_amount_of_market_listings']


class Games(enum.IntEnum):
    TF2 = 440


def get_amount_of_market_listings(game, item, filter_criteria=None):
    url = get_url(game=game, item=item, filter_criteria=filter_criteria)
    content = get_content(url=url)

    soup = parse_content(content=content)

    return get_total_amount_of_results(soup=soup)