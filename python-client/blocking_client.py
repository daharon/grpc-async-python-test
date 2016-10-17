#!/usr/bin/env python3

import grpc
from google.protobuf.empty_pb2 import Empty

from generated.protobuf import random_stream_pb2


def get_random_values(stub):
    for random_value in stub.Read(Empty()):
        print('Read value: 0x{:X}'.format(random_value.value))


if __name__ == '__main__':
    try:
        channel = grpc.insecure_channel('localhost:9000')
        stub = random_stream_pb2.RandomStreamStub(channel)
        get_random_values(stub)
    except (KeyboardInterrupt, SystemExit):
        print("\n")
