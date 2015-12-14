#!/usr/bin/env python3

import unittest

from stockfighter.venue import Venue


class TestExistingVenue(unittest.TestCase):

    def setUp(self):
        self.venue_name = "TESTEX"
        self.venue = Venue(self.venue_name)

    def test_venue_name(self):
        self.assertEqual(self.venue.name, self.venue_name)

    def test_http_ok(self):
        self.assertEqual(self.venue.heartbeat.status_code, 200)


class TestFakeVenue(unittest.TestCase):

    def setUp(self):
        self.venue_name = "FAKEX"
        self.venue = Venue(self.venue_name)

    def test_http_error(self):
        self.assertEqual(self.venue.heartbeat.status_code, 404)
