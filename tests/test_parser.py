# -*- coding: utf-8 -*-
import os
import unittest

from bs4 import BeautifulSoup

import steam_market


TEST_FILE_NORMAL_LISTING = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'html', 'test_normal_listing.html')
TEST_FILE_NO_RESULTS = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'html', 'test_no_results.html')
TEST_FILE_MANY_RESULTS = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'html', 'test_many_listings.html')


def get_soup_from_path(file_path):
    """Get a soup file from a pre-recorded html result"""
    with open(file_path, encoding='utf-8') as f:
        soup = BeautifulSoup(f.read())

    return soup


class TestParser(unittest.TestCase):
    """Test the parser module"""

    def test_amount_of_listings(self):
        """Verify that we correctly count the amount of listings"""
        listings = steam_market.get_total_amount_of_listings(soup=get_soup_from_path(TEST_FILE_NORMAL_LISTING))
        self.assertEqual(10, listings)

    def test_amount_of_listings_no_listings(self):
        """Verify that we correctly count the amount of listings when there are no results"""
        listings = steam_market.get_total_amount_of_listings(soup=get_soup_from_path(TEST_FILE_NO_RESULTS))
        self.assertEqual(0, listings)

    def test_amount_of_listings_many_listings(self):
        """Verify that we correctly count the amount of listings with multi-page results"""
        listings = steam_market.get_total_amount_of_listings(soup=get_soup_from_path(TEST_FILE_MANY_RESULTS))
        self.assertEqual(164720, listings)

    def test_lowest_price(self):
        """Verify that we correctly find the lowest price"""
        listings = steam_market.get_lowest_price(soup=get_soup_from_path(TEST_FILE_NORMAL_LISTING))
        self.assertEqual('11,59€', listings)

    def test_lowest_price_no_listings(self):
        """Verify that we return None when there are no results"""
        listings = steam_market.get_lowest_price(soup=get_soup_from_path(TEST_FILE_NO_RESULTS))
        self.assertIsNone(listings)

    def test_lowest_price_many_listings(self):
        """Verify that we return None when there are no results"""
        listings = steam_market.get_lowest_price(soup=get_soup_from_path(TEST_FILE_MANY_RESULTS))
        self.assertEqual('0,03€', listings)

