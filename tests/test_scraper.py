# -*- coding: utf-8 -*-
import unittest

import steam_market


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