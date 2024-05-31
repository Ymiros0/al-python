local var_0_0 = require("pb")

module("wire_format")

WIRETYPE_VARINT = 0
WIRETYPE_FIXED64 = 1
WIRETYPE_LENGTH_DELIMITED = 2
WIRETYPE_START_GROUP = 3
WIRETYPE_END_GROUP = 4
WIRETYPE_FIXED32 = 5
_WIRETYPE_MAX = 5

local function var_0_1(arg_1_0)
	if arg_1_0 <= 127:
		return 1

	if arg_1_0 <= 16383:
		return 2

	if arg_1_0 <= 2097151:
		return 3

	if arg_1_0 <= 268435455:
		return 4

	return 5

def PackTag(arg_2_0, arg_2_1):
	return arg_2_0 * 8 + arg_2_1

def UnpackTag(arg_3_0):
	local var_3_0 = arg_3_0 % 8

	return (arg_3_0 - var_3_0) / 8, var_3_0

ZigZagEncode32 = var_0_0.zig_zag_encode32
ZigZagDecode32 = var_0_0.zig_zag_decode32
ZigZagEncode64 = var_0_0.zig_zag_encode64
ZigZagDecode64 = var_0_0.zig_zag_decode64

def Int32ByteSize(arg_4_0, arg_4_1):
	return Int64ByteSize(arg_4_0, arg_4_1)

def Int32ByteSizeNoTag(arg_5_0):
	return var_0_1(arg_5_0)

def Int64ByteSize(arg_6_0, arg_6_1):
	return UInt64ByteSize(arg_6_0, arg_6_1)

def UInt32ByteSize(arg_7_0, arg_7_1):
	return UInt64ByteSize(arg_7_0, arg_7_1)

def UInt64ByteSize(arg_8_0, arg_8_1):
	return TagByteSize(arg_8_0) + var_0_1(arg_8_1)

def SInt32ByteSize(arg_9_0, arg_9_1):
	return UInt32ByteSize(arg_9_0, ZigZagEncode(arg_9_1))

def SInt64ByteSize(arg_10_0, arg_10_1):
	return UInt64ByteSize(arg_10_0, ZigZagEncode(arg_10_1))

def Fixed32ByteSize(arg_11_0, arg_11_1):
	return TagByteSize(arg_11_0) + 4

def Fixed64ByteSize(arg_12_0, arg_12_1):
	return TagByteSize(arg_12_0) + 8

def SFixed32ByteSize(arg_13_0, arg_13_1):
	return TagByteSize(arg_13_0) + 4

def SFixed64ByteSize(arg_14_0, arg_14_1):
	return TagByteSize(arg_14_0) + 8

def FloatByteSize(arg_15_0, arg_15_1):
	return TagByteSize(arg_15_0) + 4

def DoubleByteSize(arg_16_0, arg_16_1):
	return TagByteSize(arg_16_0) + 8

def BoolByteSize(arg_17_0, arg_17_1):
	return TagByteSize(arg_17_0) + 1

def EnumByteSize(arg_18_0, arg_18_1):
	return UInt32ByteSize(arg_18_0, arg_18_1)

def StringByteSize(arg_19_0, arg_19_1):
	return BytesByteSize(arg_19_0, arg_19_1)

def BytesByteSize(arg_20_0, arg_20_1):
	return TagByteSize(arg_20_0) + var_0_1(#arg_20_1) + #arg_20_1

def MessageByteSize(arg_21_0, arg_21_1):
	return TagByteSize(arg_21_0) + var_0_1(arg_21_1.ByteSize()) + arg_21_1.ByteSize()

def MessageSetItemByteSize(arg_22_0, arg_22_1):
	local var_22_0 = 2 * TagByteSize(1) + TagByteSize(2) + TagByteSize(3) + var_0_1(arg_22_0)
	local var_22_1 = arg_22_1.ByteSize()

	return var_22_0 + var_0_1(var_22_1) + var_22_1

def TagByteSize(arg_23_0):
	return var_0_1(PackTag(arg_23_0, 0))
