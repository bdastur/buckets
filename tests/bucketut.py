#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import buckets
import pprint



class BucketUT(unittest.TestCase):
    '''
    Bucket library ut.
    '''
    def test_basic_bucket(self):
        print "Test basic bucket"
        bkts = buckets.Buckets(2, [5, 4])
        self.failUnless(bkts is not None)

        pp = pprint.PrettyPrinter(indent=1)
        pp.pprint(bkts.buckets)

        bkts.buckets_add_element(10)
        bkts.buckets_add_element(20)
        bkts.buckets_add_element(30)
        bkts.buckets_add_element(40)
        bkts.buckets_add_element(50)
        bkts.buckets_add_element(60)
        bkts.buckets_add_element(70)
        bkts.buckets_add_element(80)
        bkts.buckets_add_element(90)
        bkts.buckets_add_element(100)
        bkts.buckets_add_element(110)
        bkts.buckets_add_element(120)
        bkts.buckets_add_element(130)
        bkts.buckets_add_element(140)
        bkts.buckets_add_element(150)
        bkts.buckets_add_element(160)
        bkts.buckets_add_element(170)



        pp = pprint.PrettyPrinter(indent=1)
        pp.pprint(bkts.buckets)



