#!/usr/bin/env python3

import unittest
import pkg_resources
import json

from stockfighter.stock import Stock


class TestExistingStock(unittest.TestCase):

    def setUp(self):
        self.venue = "TESTEX"
        self.name = "Foreign Owned Occluded Bridge Architecture Resources"
        self.symbol = "FOOBAR"

        self.stock = Stock(self.venue, self.name, self.symbol)

    def test_stock_details(self):
        self.assertEquals(self.stock.venue, self.venue)
        self.assertEquals(self.stock.name, self.name)
        self.assertEquals(self.stock.symbol, self.symbol)

    # Example stock orderbook is dynamic
    def test_orderbook(self):
        orderbook = self.stock.orderbook()
        self.assertEqual(orderbook["venue"], self.venue)

    def test_limit_buy(self):
        account = "EXB123456"
        price = 100
        qty = 1
        direction = "buy"
        order_type = "limit"
        order = self.stock.order(account, price, qty, direction, order_type)
        self.assertEqual(order["price"], 100)
        self.assertEqual(order["orderType"], "limit")
        self.assertEqual(order["direction"], "buy")
