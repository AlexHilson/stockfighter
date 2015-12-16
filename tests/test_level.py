#!/usr/bin/env python

# import unittest

# from stockfighter.level import Level


'''
This is not yet enabled, as the GM interface is dynamic and I haven't worked
out a way yet to test it in a reliable + useful way.
'''

# class TestLevelManagement(unittest.TestCase):
#     def setUp(self):
#         name = "first_steps"
#         self.level = Level.new_level(name)
#         self.instance = self.level.instance

#     def test_status(self):
#         status = self.level.status
#         print(self.level.account)
#         print(self.level.venues)
#         print(self.level.tickers)
#         print(self.level.instructions)

#    def test_stopping_instance(self):
#        self.instance.stop()
#        self.assertTrue(
#            self.instance.status()["error"],
#            "Level instance not running")
