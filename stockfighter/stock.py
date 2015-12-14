#!/usr/bin/env python3

import requests


VENUES_API = "https://api.stockfighter.io/ob/api/venues"


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
