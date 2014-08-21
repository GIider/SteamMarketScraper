# -*- coding: utf-8 -*-
import os
import unittest

from bs4 import BeautifulSoup

import steam_market


TEST_FILE_NORMAL_LISTING = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'html', 'test_normal_listing.html')


def get_constant_soup(url):
    """Get a fixed soup for testing"""
    with open(TEST_FILE_NORMAL_LISTING, encoding='utf-8') as f:
        soup = BeautifulSoup(f.read())

    return soup


class TestMarketPage(unittest.TestCase):
    """Test the MarketPage class"""

    def setUp(self):
        """Replace the get_soup function with our constant one"""
        self.original_get_soup = steam_market.get_soup
        steam_market.get_soup = get_constant_soup

    def tearDown(self):
        """Restore the original get_soup function"""
        steam_market.get_soup = self.original_get_soup

    def test_market_page(self):
        """Test the MarketPage class"""
        game = steam_market.Games.TF2
        item = 'Professional Killstreak Beggar\'s Bazooka Kit'

        page = steam_market.MarketPage(game=game, item=item)

        self.assertEqual(10, page.amount_of_listings)
        self.assertEqual('11,59€', page.lowest_price)