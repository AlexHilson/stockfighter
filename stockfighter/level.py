#!/usr/bin/env python3

import requests

from stockfighter.config import KEY, LEVELS_API, INSTANCES_API


class Level(object):
    def __init__(self, name):
        self.name = name
        self.authorization = {"X-Starfighter-Authorization": KEY}
        self.details = requests.post(
            "{}/{}".format(LEVELS_API, self.name),
            headers=self.authorization).json()
        if self.details["ok"] == True:
            self.id = self.details["instanceId"]
            self.account = self.details["account"]
            self.venues = self.details["venues"]
            self.tickers = self.details["tickers"]
        else:
            raise RuntimeError(self.details["error"])

    def status(self):
        return requests.get(
            "{}/{}".format(INSTANCES_API, self.id),
            headers=self.authorization).json()

    def stop(self):
        return requests.post(
            "{}/{}/stop".format(INSTANCES_API, self.id),
            headers=self.authorization).json()

    # This doesn't seem  to  behave in the same way as the 'restart'
    # button on the web gui. The first time it's called it always
    # seems to return 'level locked' error, and causes to level to
    # enter 'stopped' status. Second time it's called Stockfighter creates
    # a new instance of the level with new details.
    def restart(self):
        return requests.post(
            "{}/{}/restart".format(INSTANCES_API, self.id),
            headers=self.authorization).json()
