from protobuf_utils import *

class TestProto(Message):
    a = None
    b = None
    c = None
    d = None
    e = None

    def __init__(self):
        self.__lookup__ = [("optional", type_uint64, "a", 1),
                           ("repeated", type_uint32, "b", 2),
                           ("optional", type_uint32, "c", 3),
                           ("required", type_bool, "d", 4),
                           ("optional", type_bytes, "e", 5)]


