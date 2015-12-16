#!/usr/bin/env python3

import requests

from stockfighter.stock import Stock
from stockfighter.config import VENUES_API


class Venue(object):
    def __init__(self, name):
        self.name = name
        self.heartbeat = requests.get(
            "{}/{}/heartbeat"
            .format(VENUES_API, self.name))

        if self.heartbeat.status_code == 200:
            # "In general you can cache this for an entire level"
            self.stocks = self._get_stocks()

    def _get_stocks(self):
        stocks = requests.get(
            "{}/{}/stocks"
            .format(VENUES_API, self.name)).json()
        return [
            Stock(self.name, details["name"], details["symbol"])
            for details in stocks["symbols"]]
