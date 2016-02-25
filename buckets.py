#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Buckets(object):
    '''
    Buckets class
    '''
    def __init__(self, bucket_count=2,
                 bucketlist_size=[5, 4]):
        print "Initialize buckets"
        print type(bucketlist_size)

        self.buckets = []
        self.buckets_count = bucket_count
        self.cumulative_count = 0

        for idx in range(0, bucket_count):
            bucketsobject = {}
            bucketsobject['current_idx'] = 0
            bucketsobject['cumulative_count'] = 0
            bucketsobject['size'] = bucketlist_size[idx]
            bucketsobject['list'] = self.__initialize_buckets(
                bucketsobject['size'])
            print "bucket: ", bucketsobject
            self.buckets.append(bucketsobject)

        print self.buckets

    def __initialize_buckets(self, size):
        bucket_list = []
        for idx in range(0, size):
            bucket = {}
            bucket['last_update_ts'] = 0
            bucket['data'] = None
            bucket_list.append(bucket)

        return bucket_list

    def __buckets_add_element_internal(self, data, level):
        '''
        Internal function to add element to the buckets
        '''
        print "LEVEL: ", level
        #for idx in range(level, self.buckets_count):
        idx = level
        if idx in range(level, self.buckets_count):
            bucketsobject = self.buckets[idx]
            curr_idx = bucketsobject['current_idx']
            curr_idx = curr_idx % bucketsobject['size']
            print "curr_idx: ", curr_idx
            if bucketsobject['list'][curr_idx]['data'] is None:
                print "Bucket object is none"
                bucketsobject['list'][curr_idx]['data'] = data
                bucketsobject['current_idx'] += 1
            else:
                print "Bucket object is not None: idx", idx
                olddata = bucketsobject['list'][curr_idx]['data']
                bucketsobject['list'][curr_idx]['data'] = data
                bucketsobject['current_idx'] += 1
                self.__buckets_add_element_internal(olddata,
                                                    idx+1)

    def buckets_add_element(self, data):
        '''
        Main API to add a new element to the buckets.
        Adding a new element to the buckets always happens at the
        topmost bucket list. Old values get pushed to lower bucket lists.
        '''
        self.__buckets_add_element_internal(data, 0)








