# -*- coding: utf-8 -*-
"""Parse the HTML in the Steam Community market"""
from bs4 import BeautifulSoup


__all__ = ['parse_content', 'get_total_amount_of_results']


def parse_content(content):
    """Parses a result from the Steam Community Market"""
    soup = BeautifulSoup(content)

    return soup


def get_total_amount_of_results(soup):
    """Get the amount of market listings from a result"""
    spans = soup.find_all('span', id='searchResults_total')

    if len(spans) == 0:
        return 0

    elif len(spans) > 1:
        raise AssertionError('%d searchResults_total <spans> found' % len(spans))

    return int(spans[0].text.replace(',', ''))