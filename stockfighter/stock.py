#!/usr/bin/env python3

import json

import requests

from stockfighter.config import VENUES_API, KEY


class Stock(object):

    def __init__(self, venue, name, symbol):
        self.venue = venue
        self.name = name
        self.symbol = symbol

    def orderbook(self):
        return requests.get(
            "{}/{}/stocks/{}"
            .format(VENUES_API, self.venue, self.symbol)
        ).json()

    def order(self, account, price, qty, direction, order_type):

        data = json.dumps({
            "account": account,
            "price": price,
            "qty": qty,
            "direction": direction,
            "orderType": order_type,
            "stock": self.symbol,
            "venue": self.venue
        })
        headers = {
            "X-Starfighter-Authorization": KEY,
            "content-type": "application/json"
        }
        response = requests.post(
            "{}/{}/stocks/{}/orders"
            .format(VENUES_API, self.venue, self.symbol),
            data=data,
            headers=headers
        )
        return response.json()
