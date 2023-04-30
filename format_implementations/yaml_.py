import yaml


def serialize(data):
    return yaml.dump(data)


def deserialize(data):
    return yaml.load(data, Loader=yaml.FullLoader)
