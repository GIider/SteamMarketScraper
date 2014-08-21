# -*- coding: utf-8 -*-
import sys
import bs4
import unittest
import os

import steam_market

TEST_FILE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'html', 'test_normal_listing.html')


class TestScraper(unittest.TestCase):
    """Test the scraper module"""

    def test_url_with_non_ascii_characters(self):
        """Test that we correctly convert non ascii characters"""
        game = 440
        item = 'Killstreak Claidheamh Mòr Kit'

        url = steam_market.get_url(game=game, item=item)
        self.assertEqual('http://steamcommunity.com/market/listings/440/Killstreak%20Claidheamh%20M%C3%B2r%20Kit', url)

    def test_enum_as_game(self):
        """Test that we can pass values from the Games enum to the get_url function"""
        game = steam_market.Games.TF2
        item = ''

        url = steam_market.get_url(game=game, item=item)
        self.assertEqual('http://steamcommunity.com/market/listings/440/', url)

    def test_filter(self):
        """Test that we correctly add filters"""
        game = 440
        item = 'Professional Killstreak Phlogistinator Kit'
        filter_criteria = 'Deadly Daffodil'

        url = steam_market.get_url(game=game, item=item, filter_criteria=filter_criteria)
        self.assertEqual('http://steamcommunity.com/market/listings/440/Professional%20Killstreak%20Phlogistinator%20Kit?filter=Deadly%20Daffodil', url)

    def test_get_soup(self):
        """Test that we get a soup from a url"""
        if sys.platform == 'win32':
            url = r'file:\\'
        else:
            url = 'file://'

        url += TEST_FILE_PATH
        soup = steam_market.get_soup(url=url)

        self.assertIsInstance(soup, bs4.BeautifulSoup)