#!/usr/bin/env python

import os

from runtest import TestBase

class TestCase(TestBase):
    def __init__(self):
        TestBase.__init__(self, 'abc', """
# DURATION     TID     FUNCTION
            [ 28141] | __main__.<module>() {
            [ 28141] |   a() {
            [ 28141] |     b() {
            [ 28141] |       c() {
   0.753 us [ 28141] |         posix.getpid();
   1.430 us [ 28141] |       } /* c */
   1.915 us [ 28141] |     } /* b */
   2.405 us [ 28141] |   } /* a */
   3.005 us [ 28141] | } /* __main__.<module> */
""", lang='Python', sort='simple')
