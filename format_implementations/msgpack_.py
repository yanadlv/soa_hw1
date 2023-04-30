import msgpack


def serialize(data):
    return msgpack.packb(data)


def deserialize(data):
    return msgpack.unpackb(data, raw=False)
