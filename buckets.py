#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Buckets: A python module to manage data. A bucket is a place holder
for data. And with Buckets you can manage multiple bucket lists.

A bucket list is a fixed size list of buckets. When data exceeds the bucket
list, the oldest data gets moved to a lower priority bucket list if there
exists, else it gets chunked.

'''

import datetime

class Buckets(object):
    '''
    Buckets class
    '''
    def __init__(self,
                 bucketlist_count,
                 bucketlist_size):
        '''
        Initialize Buckets.
        @args:
            - bucket-count: Number of bucket lists to manage.
            - bucketlist_size - Size of each bucket list.
        '''

        self.buckets = []
        self.buckets_count = bucketlist_count
        self.cumulative_count = 0

        for idx in range(0, bucketlist_count):
            bucketsobject = {}
            bucketsobject['current_idx'] = 0
            bucketsobject['size'] = bucketlist_size[idx]
            bucketsobject['list'] = self.__initialize_buckets(
                bucketsobject['size'])
            self.buckets.append(bucketsobject)

    def __initialize_buckets(self, size):
        '''
        Internal API: Initalize buckets to None
        '''
        bucket_list = []
        for _ in range(0, size):
            bucket = {}
            bucket['data'] = None
            bucket['id'] = 0
            bucket['keep'] = False
            bucket['last_updated_ts'] = None
            bucket_list.append(bucket)

        return bucket_list

    def __bucket_create_internal(self,
                                 data,
                                 bucket_id,
                                 keep=False,
                                 oldbucket=None):
        '''
        Create a new bucket or createa copy
        '''
        bucket = {}
        if oldbucket is None:
            bucket['data'] = data
            bucket['id'] = bucket_id
            bucket['last_updated_ts'] = datetime.datetime.now()
            bucket['keep'] = keep
        else:
            bucket['data'] = oldbucket['data']
            bucket['id'] = oldbucket['id']
            bucket['last_updated_ts'] = oldbucket['last_updated_ts']
            bucket['keep'] = oldbucket['keep']

        return bucket

    def __buckets_add_element_internal(self,
                                       data,
                                       level,
                                       keep=False,
                                       oldbucket=None):
        '''
        Internal function to add element to the buckets
        '''
        #for idx in range(level, self.buckets_count):
        self.cumulative_count += 1
        idx = level

        if idx in range(level, self.buckets_count):
            bucketsobject = self.buckets[idx]
            curr_idx = bucketsobject['current_idx']
            curr_idx = curr_idx % bucketsobject['size']
            if bucketsobject['list'][curr_idx]['data'] is None:
                bucketsobject['list'][curr_idx] = \
                    self.__bucket_create_internal(data,
                                                  self.cumulative_count,
                                                  keep=keep,
                                                  oldbucket=oldbucket)

                bucketsobject['current_idx'] += 1
            else:
                olddata = bucketsobject['list'][curr_idx]['data']
                currbucket = bucketsobject['list'][curr_idx]

                bucketsobject['list'][curr_idx] = \
                    self.__bucket_create_internal(data,
                                                  self.cumulative_count,
                                                  keep=keep,
                                                  oldbucket=oldbucket)

                bucketsobject['current_idx'] += 1
                self.__buckets_add_element_internal(olddata,
                                                    idx+1,
                                                    oldbucket=currbucket)

    def buckets_add_element(self, data, keep=False):
        '''
        Main API to add a new element to the buckets.
        Adding a new element to the buckets always happens at the
        topmost bucket list. Old values get pushed to lower bucket lists.
        '''
        self.__buckets_add_element_internal(data, 0, keep=keep)








