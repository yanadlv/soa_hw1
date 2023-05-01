import data_pb2


def serialize(data):
    res = data_pb2.Data()
    res.string = data["string"]
    res.list.extend(data["list"])
    for key, value in data["dict"].items():
        res.dict[key] = value
    res.int = data["int"]
    res.float = data["float"]
    return res.SerializeToString()


def deserialize(data):
    res = data_pb2.Data()
    return res.ParseFromString(data)
