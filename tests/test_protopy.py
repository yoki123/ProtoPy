# -*- coding: utf-8 -*-

import unittest

from test_pb import *


class TestProtoPy(unittest.TestCase):
    def test_encode_dict(self):
        raw_dict = {'a': 123456, 'b': [1, 2, 3, 4], 'd': False, 'e': 'tiny pure python protobuf implementation'}
        test_obj = TestProto()
        test_obj.__dict__.update(raw_dict)
        buf1 = test_obj.encode()
        buf2 = encode_raw_dict(TestProto, raw_dict)
        self.assertEqual(buf1, buf2)
