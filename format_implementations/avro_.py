import io
import avro.schema
from avro.io import DatumReader, DatumWriter, BinaryEncoder, BinaryDecoder

schema = avro.schema.parse('''
    {
        "type": "record",
        "name": "Data",
        "fields": [
            {"name": "string", "type": "string"},
            {"name": "list", "type": {"type": "array", "items": "int"}},
            {"name": "dict", "type": {"type": "map", "values": "string"}},
            {"name": "int", "type": "int"},
            {"name": "float", "type": "float"}
        ]
    }
''')


def serialize(data):
    writer = io.BytesIO()
    datum_writer = DatumWriter(schema)
    encoder = BinaryEncoder(writer)
    datum_writer.write(data, encoder)
    return writer.getvalue()


def deserialize(data):
    reader = io.BytesIO(data)
    datum_reader = DatumReader(schema)
    decoder = BinaryDecoder(reader)
    return datum_reader.read(decoder)
