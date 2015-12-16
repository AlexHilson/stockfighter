#!/usr/bin/env python3

import requests

from stockfighter.config import KEY, LEVELS_API, INSTANCES_API


class Level(object):
    def __init__(self,  details):
        self.details = details
        if details["ok"] == True:
            self.details = details
            self.name = details["name"]
            self.instance_id = details["instanceId"]
            self.account = details["account"]
            self.venues = details["venues"]
            self.tickers = details["tickers"]
            self.instance = Instance(self.instance_id)
        else:
            raise RuntimeError(details["error"])

    @staticmethod
    def new_level(level_name):
        authorization = {"X-Starfighter-Authorization": KEY}
        details = requests.post(
            "{}/{}".format(LEVELS_API, level_name),
            headers=authorization).json()
        return Level(details)


class Instance(object):
    def __init__(self, instance_id):
        self.authorization = {"X-Starfighter-Authorization": KEY}
        self.instance_id = instance_id

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
