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
        bkts = buckets.Buckets(2, [(5, 1),
                                   (4, 1)])
        self.failUnless(bkts is not None)

        pp = pprint.PrettyPrinter(indent=1)
        pp.pprint(bkts.buckets)

    def test_buckets_add(self):
        bkts = buckets.Buckets(2, [(5, 1),
                                   (4, 1)])

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

    def test_buckets_get_element(self):
        bkts = buckets.Buckets(2, [(5, 1),
                                   (4, 1)])

        bkts.buckets_add_element(10)
        bkts.buckets_add_element(20)

        elem = bkts.buckets_get_element()
        self.failUnless(elem == 20)

        bkts.buckets_add_element(30)
        bkts.buckets_add_element(40)
        bkts.buckets_add_element(50)

        elem = bkts.buckets_get_element()
        print "Elem: ", elem

        bkts.buckets_add_element(60)
        bkts.buckets_add_element(70)
        bkts.buckets_add_element(80)

        elem = bkts.buckets_get_element()
        print "Elem: ", elem

    def delete_mybucket(self, data=None):
        print "Data to delete: ", data

    def test_buckets_buckets_destructor(self):
        bkts = buckets.Buckets(2, [(5, 1),
                                   (4, 1)],
                               bucket_destructor=self.delete_mybucket)

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

    def test_buckets_storefreq(self):
        bkts = buckets.Buckets(2, [(5, 1),
                                   (4, 4)],
                               bucket_destructor=self.delete_mybucket)

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
        bkts.buckets_add_element(180)
        bkts.buckets_add_element(190)
        bkts.buckets_add_element(200)
        bkts.buckets_add_element(210)
        bkts.buckets_add_element(220)
        bkts.buckets_add_element(230)
        bkts.buckets_add_element(240)


        pp = pprint.PrettyPrinter(indent=1)
        pp.pprint(bkts.buckets)



