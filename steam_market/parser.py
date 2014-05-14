# -*- coding: utf-8 -*-
"""Parse the HTML in the Steam Community market"""

__all__ = ['get_total_amount_of_listings', 'get_lowest_price']


def get_total_amount_of_listings(soup):
    """Get the amount of market listings from a result"""
    spans = soup.find_all('span', id='searchResults_total')

    if len(spans) == 0:
        return 0

    elif len(spans) > 1:
        raise AssertionError('%d searchResults_total <spans> found' % len(spans))

    return int(spans[0].text.replace(',', ''))


def get_lowest_price(soup):
    """Get the lowest price from a result

    Returns a string with the price and currency or None if there is no listing.

    Possible return values:
        * R$ 35,20
        * $16.00
        * 590 pуб.
        * 12,33€
    """
    # I couldn't find a way to convince the page to give me a certain currency, but
    # I'm not alone with this problem, see: http://stackoverflow.com/a/22623700
    spans = soup.find_all('span', attrs={'class': 'market_listing_price market_listing_price_with_fee'})

    if len(spans) == 0:
        return None

    lowest_price = spans[0].text.strip()

    return lowest_price