import struct
import binascii

values = (1, 'abc', 2.7)
s = struct.Struct('I3sf')
packed_data = s.pack(*values)
unpacked_data = s.unpack(packed_data)

print 'Original values:', values
print 'Format string :', s.format
print 'Uses :', s.size, 'bytes'
print 'Packed Value :', binascii.hexlify(packed_data)
print 'Unpacked Type :', type(unpacked_data), ' Value:', unpacked_data


# import struct
# import binascii
# import ctypes
#
# values = (1, 'abc', 2.7)
# s = struct.Struct('I3sf')
# prebuffer = ctypes.create_string_buffer(s.size)
# print 'Before :', binascii.hexlify(prebuffer)
# s.pack_into(prebuffer, 0, *values)
# print 'After pack:', binascii.hexlify(prebuffer)
# unpacked = s.unpack_from(prebuffer, 0)
# print 'After unpack:', unpacked


#http://www.cnblogs.com/coser/archive/2011/12/17/2291160.html
# import struct
# import binascii
#
# values = (1, 'abc', 2.7)
# s = struct.Struct('I3sf')
# packed_data = s.pack(*values)
# unpacked_data = s.unpack(packed_data)
#
# print 'Original values:', values
# print 'Format string :', s.format
# print 'Uses :', s.size, 'bytes'
# print 'Packed Value :', binascii.hexlify(packed_data)
# print 'Unpacked Type :', type(unpacked_data), ' Value:', unpacked_data
