#!/usr/bin/env python3

import requests


VENUES_API = "https://api.stockfighter.io/ob/api/venues"


class Venue(object):

    def __init__(self, name):
        self.name = name
        self.heartbeat = requests.get(
            "{}/{}/heartbeat"
            .format(VENUES_API, name))
