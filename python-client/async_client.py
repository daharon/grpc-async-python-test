#!/usr/bin/env python3

import sys
import signal
import asyncio
import threading
from concurrent.futures import ThreadPoolExecutor

import grpc
from google.protobuf.empty_pb2 import Empty

from generated.protobuf import random_stream_pb2


GRPC_TARGET = 'localhost:9000'


def print_random_values(listener: int, cancel: threading.Event):
    channel = grpc.insecure_channel(GRPC_TARGET)
    random_stream = random_stream_pb2.RandomStreamStub(channel)

    for random_value in random_stream.Read(Empty()):
        print('Listener {} read value: {:X}'.format(listener, random_value.value))
        if cancel.is_set():
            return


if __name__ == '__main__':
    executor = ThreadPoolExecutor()
    cancel = threading.Event()
    loop = asyncio.get_event_loop()

    for c in range(2):
        loop.run_in_executor(executor, print_random_values, c, cancel)

    try:
        signal.signal(signal.SIGTERM, lambda signum, frame: sys.exit())
        loop.run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        cancel.set()
        executor.shutdown(wait=True)

    loop.stop()


