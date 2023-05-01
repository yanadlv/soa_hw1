import socket
import os
from sys import getsizeof
import timeit


HOST = "0.0.0.0"
DATA = {
    "string": "i love soa",
    "list": [-500, -50, -5, 0, 5, 50, 500],
    "dict": {
        "name": "yana",
        "surname": "dolvatova",
        "category": "soa enjoyer"
    },
    "int": 2023,
    "float": 3.14
}


def calculate():
    requested_format = os.environ.get("FORMAT")
    serializer = None
    deserializer = None
    if requested_format == "native":
        from native_ import serialize, deserialize
        serializer = serialize
        deserializer = deserialize
    if requested_format == "xml":
        from xml_ import serialize, deserialize
        serializer = serialize
        deserializer = deserialize
    if requested_format == "json":
        from json_ import serialize, deserialize
        serializer = serialize
        deserializer = deserialize
    if requested_format == "proto":
        from proto_ import serialize, deserialize
        serializer = serialize
        deserializer = deserialize
    if requested_format == "avro":
        from avro_ import serialize, deserialize
        serializer = serialize
        deserializer = deserialize
    if requested_format == "yaml":
        from yaml_ import serialize, deserialize
        serializer = serialize
        deserializer = deserialize
    if requested_format == "msgpack":
        from msgpack_ import serialize, deserialize
        serializer = serialize
        deserializer = deserialize

    ser_data = serializer(DATA)
    ser_total_time = timeit.timeit(lambda: serializer(DATA), number=1000) * 1000

    des_data = deserializer(ser_data)
    des_total_time = timeit.timeit(lambda: deserializer(ser_data), number=1000) * 1000

    return f"{requested_format.upper()} - {getsizeof(ser_data)} - " \
           f"{ser_total_time:.2f}ms - {des_total_time:.2f}ms\n\n".encode()


def run():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, int(os.environ.get("PORT"))))

        while True:
            request, address = s.recvfrom(2048)
            response = calculate()
            s.sendto(response, address)


if __name__ == "__main__":
    run()
