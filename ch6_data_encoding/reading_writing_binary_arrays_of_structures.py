"""
<idd is little-endian, 32-bit integer, two double precision floats, ex: 2, 3.5, 58.8
"""
from collections import namedtuple
import struct
from struct import Struct


def write_records(records, format, f):
    """
    Write a sequence of tuples to a binary file of structures.
    """
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))


def read_records(format, f):
    """
    Unpack in chunks.
    """
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')  # read chunks that are the same size as the struct itself
    return (record_struct.unpack(chunk) for chunk in chunks)


def unpack_records(format, data):
    """
    Unpack all at once.
    """
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset) for offset in range(0, len(data), record_struct.size))


if __name__ == '__main__':
    records = [(1, 2.3, 4.5),
               (6, 7.8, 9.0),
               (12, 13.4, 56.7)]

    with open('data_files/data.b', 'wb') as f:
        write_records(records, '<idd', f)
    print()

    with open('data_files/data.b', 'rb') as f:
        for rec in read_records('<idd', f):
            print(rec)
    print()

    with open('data_files/data.b', 'rb') as f:
        data = f.read()

        for rec in unpack_records('<idd', data):
            print(rec)
    print()

    # structs have various methods on them for manipulating and getting info
    record_struct = Struct('<idd')
    print(record_struct.size)
    packed = record_struct.pack(1, 2.3, 5.7)     # populate the struct with data
    print(packed)
    unpacked = record_struct.unpack(packed)
    print(unpacked)
    print()

    # can also call module-level pack and unpack
    packed = struct.pack('<idd', 1, 2.0, 3.0)
    print(packed)

    unpacked = struct.unpack('<idd', packed)
    print(unpacked)
    print()

    # using a named tuple when unpacking binary data can be useful
    Record = namedtuple('Record', ['kind', 'x', 'y'])
    record = Record(*record_struct.unpack(packed))
    print(record.kind, record.x, record.y)

    # there are also some utilities in numpy for working with binary data in very large data sets
