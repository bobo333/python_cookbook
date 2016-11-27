import struct
import itertools

polys = [
    [ (1.0, 2.5), (3.5, 4.0), (2.5, 1.5) ],
    [ (7.0, 1.2), (5.1, 3.0), (0.5, 7.5), (0.8, 9.0) ],
    [ (3.4, 6.3), (1.2, 0.5), (4.6, 9.2) ]
]

# File will be
#
# header:
# byte    type    description
# 0       int     file code (0x1234, little-endian)
# 4       double  Minimum x
# 12      double  Minimum y
# 20      double  Maximum x
# 28      double  Maximum y
# 36      int     number of polygons
#
# polygons:
# byte    type    description
# 0       int     record length including length (N bytes)
# 4-N     Points  Pairs of (x,y) coords as doubles


# write the file:
def write_polys(filename, polys):
    # determine bounding box
    flattened = list(itertools.chain(*polys))
    min_x = min(x for x, y in flattened)
    max_x = max(x for x, y in flattened)
    min_y = min(y for x, y in flattened)
    max_y = max(y for x, y in flattened)

    with open(filename, 'wb') as f:
        f.write(struct.pack('<iddddi',
                            0x1234,
                            min_x, min_y,
                            max_x, max_y,
                            len(polys)))

        for poly in polys:
            size = len(poly) * struct.calcsize('<dd')
            f.write(struct.pack('<i', size+4))
            for pt in poly:
                f.write(struct.pack('<dd', *pt))

# call with our poly data
write_polys('data_files/polys.bin', polys)


# read the data back
def read_polys(filename):
    with open(filename, 'rb') as f:
        # read the header
        header = f.read(40)
        file_code, min_x, min_y, max_x, max_y, num_polys = struct.unpack('<iddddi', header)

        polys = []
        for n in range(num_polys):
            pbytes, = struct.unpack('<i', f.read(4))
            poly = []
            for m in range(pbytes // 16):
                pt = struct.unpack('<dd', f.read(16))
                poly.append(pt)
            polys.append(poly)

    return polys


# another option is to use a class to abstract away the specifics
class StructFieldV1:
    """
    Descriptor representing a simple structure field
    """
    def __init__(self, format, offset):
        self.format = format
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            r = struct.unpack_from(self.format, instance._buffer, self.offset)

            return r[0] if len(r) == 1 else r


class StructureV1:
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)


class PolyHeaderV1(StructureV1):
    file_code = StructFieldV1('<i', 0)
    min_x = StructFieldV1('<d', 4)
    min_y = StructFieldV1('<d', 12)
    max_x = StructFieldV1('<d', 20)
    max_y = StructFieldV1('<d', 28)
    num_polys = StructFieldV1('<i', 36)

f = open('data_files/polys.bin', 'rb')
phead = PolyHeaderV1(f.read(40))
print(phead.file_code == 0x1234)
print(phead.min_x)
print(phead.min_y)
print(phead.max_x)
print(phead.max_y)
print(phead.num_polys)
print()
f.close()


# to avoid having the user do a bunch of offsets themselves and such, consider using a meta-class
class StructureMetaV2(type):
    """
    Metaclass that automatically creates StructField descriptors
    """
    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if format.startswith(('<', '>', '!', '@')):
                byte_order = format[0]
                format = format[1:]
            format = byte_order + format
            setattr(self, fieldname, StructFieldV1(format, offset))
            offset += struct.calcsize(format)
        setattr(self, 'struct_size', offset)


class StructureV2(metaclass=StructureMetaV2):
    def __init__(self, bytedata):
        self._buffer = bytedata

    @classmethod
    def from_file(cls, f):
        return cls(f.read(cls.struct_size))


class PolyHeaderV2(StructureV2):
    _fields_ = [
        ('<i', 'file_code'),
        ('d', 'min_x'),
        ('d', 'min_y'),
        ('d', 'max_x'),
        ('d', 'max_y'),
        ('i', 'num_polys')
    ]


f = open('data_files/polys.bin', 'rb')
phead = PolyHeaderV2.from_file(f)
print(phead.file_code == 0x1234)
print(phead.min_x)
print(phead.min_y)
print(phead.max_x)
print(phead.max_y)
print(phead.num_polys)
print()
f.close()


# can build more intelligence into the metclass, like support of nested binary structures
class NestedStruct:
    """
    Descriptor representing a nested structure
    """
    def __init__(self, name, struct_type, offset):
        self.name = name
        self.struct_type = struct_type
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self

        else:
            data = instance._buffer[self.offset:self.offset + self.struct_type.struct_size]
            result = self.struct_type(data)
            # save resulting structure back on instance to avoid further recomputation of this step
            setattr(instance, self.name, result)
            return result


class StructureMetaV3(type):
    """
    Metaclass that automatically creates StructField descriptors
    """
    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0

        for format, fieldname in fields:
            if isinstance(format, StructureMetaV3):
                setattr(self, fieldname, NestedStruct(fieldname, format, offset))
                offset += format.struct_size
            else:
                if format.startswith(('<', '>', '!', '@')):
                    byte_order = format[0]
                    format = format[1:]
                format = byte_order + format
                setattr(self, fieldname, StructFieldV1(format, offset))
                offset += struct.calcsize(format)

        setattr(self, 'struct_size', offset)


# must redefine this with the new metaclass
class StructureV3(metaclass=StructureMetaV3):
    def __init__(self, bytedata):
        self._buffer = bytedata

    @classmethod
    def from_file(cls, f):
        return cls(f.read(cls.struct_size))


class Point(StructureV3):
    _fields_ = [
        ('<d', 'x'),
        ('d', 'y')
    ]


class PolyHeaderV3(StructureV3):
    _fields_ = [
        ('<i', 'file_code'),
        (Point, 'min'),     # nested struct
        (Point, 'max'),     # nested struct
        ('i', 'num_polys')
    ]


f = open('data_files/polys.bin', 'rb')
phead = PolyHeaderV3.from_file(f)
print(phead.file_code == 0x1234)
print(phead.min)
print(phead.min.x)
print(phead.min.y)
print(phead.max.x)
print(phead.max.y)
print(phead.num_polys)
print()


# these handle fixed-size records, but what about variable-sized?
class SizedRecord:
    def __init__(self, bytedata):
        self._buffer = bytedata

    @classmethod
    def from_file(cls, f, size_fmt, includes_size=True):
        sz_nbytes = struct.calcsize(size_fmt)
        sz_bytes = f.read(sz_nbytes)
        sz, = struct.unpack(size_fmt, sz_bytes)
        buf = f.read(sz - includes_size * sz_nbytes)
        return cls(buf)

    def iter_as(self, code):
        if isinstance(code, str):
            s = struct.Struct(code)
            for off in range(0, len(self._buffer), s.size):
                yield s.unpack_from(self._buffer, off)

        elif isinstance(code, StructureMetaV3):
            size = code.struct_size
            for off in range(0, len(self._buffer), size):
                data = self._buffer[off:off+size]
                yield code(data)


f = open('data_files/polys.bin', 'rb')
phead = PolyHeaderV3.from_file(f)
print(phead.num_polys)
polydata = [SizedRecord.from_file(f, '<i') for n in range(phead.num_polys)]
print(polydata)

for n, poly in enumerate(polydata):
    print('Polygon', n)
    for p in poly.iter_as('<dd'):
        print(p)

for n, poly in enumerate(polydata):
    print('Polygon', n)
    for p in poly.iter_as(Point):
        print(p.x, p.y)


def read_polys_improved(filename):
    polys = []
    with open(filename, 'rb') as f:
        phead = PolyHeaderV3.from_file(f)
        for n in range(phead.num_polys):
            rec = SizedRecord.from_file(f, '<i')
            poly = [(p.x, p.y) for p in rec.iter_as(Point)]
            polys.append(poly)

    return polys


my_polys = read_polys_improved('data_files/polys.bin')
print(my_polys)
