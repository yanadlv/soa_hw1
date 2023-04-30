import socket
import os
from sys import getsizeof
import time


HOST = "127.0.0.1"
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
        from format_implementations import native_
        serializer = native_.serialize
        deserializer = native_.deserialize
    if requested_format == "xml":
        from format_implementations import xml_
        serializer = xml_.serialize
        deserializer = xml_.deserialize
    if requested_format == "json":
        from format_implementations import json_
        serializer = json_.serialize
        deserializer = json_.deserialize
    if requested_format == "proto":
        from format_implementations.proto import proto_
        serializer = proto_.serialize
        deserializer = proto_.deserialize
    if requested_format == "avro":
        from format_implementations import avro_
        serializer = avro_.serialize
        deserializer = avro_.deserialize
    if requested_format == "yaml":
        from format_implementations import yaml_
        serializer = yaml_.serialize
        deserializer = yaml_.deserialize
    if requested_format == "msgpack":
        from format_implementations import msgpack_
        serializer = msgpack_.serialize
        deserializer = msgpack_.deserialize

    ser_begin_time = time.time()
    ser_data = serializer(DATA)
    ser_end_time = time.time()
    ser_total_time = ser_end_time - ser_begin_time

    des_begin_time = time.time()
    des_data = deserializer(ser_data)
    des_end_time = time.time()
    des_total_time = des_begin_time - des_end_time

    return f"{requested_format.upper()} - {getsizeof(ser_data)} - {ser_total_time}ms - {des_total_time}ms".encode()


def run():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, int(os.environ.get("PORT"))))

        while True:
            request, address = s.recvfrom(2048)
            print("process: " + request.decode() + "\n format: " + os.environ.get("FORMAT"))
            response = calculate()
            s.sendto(response, address)


if __name__ == "__main__":
    run()
