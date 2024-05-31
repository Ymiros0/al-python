﻿local var_0_0 = require("protobuf")
local var_0_1 = require("common_pb")

module("p15_pb")

local var_0_2 = {}

SC_15001 = var_0_0.Descriptor()
var_0_2.SC_15001_ITEM_LIST_FIELD = var_0_0.FieldDescriptor()
var_0_2.SC_15001_LIMIT_LIST_FIELD = var_0_0.FieldDescriptor()
var_0_2.SC_15001_ITEM_MISC_LIST_FIELD = var_0_0.FieldDescriptor()
CS_15002 = var_0_0.Descriptor()
var_0_2.CS_15002_ID_FIELD = var_0_0.FieldDescriptor()
var_0_2.CS_15002_COUNT_FIELD = var_0_0.FieldDescriptor()
var_0_2.CS_15002_ARG_FIELD = var_0_0.FieldDescriptor()
SC_15003 = var_0_0.Descriptor()
var_0_2.SC_15003_RESULT_FIELD = var_0_0.FieldDescriptor()
var_0_2.SC_15003_DROP_LIST_FIELD = var_0_0.FieldDescriptor()
CS_15004 = var_0_0.Descriptor()
var_0_2.CS_15004_ID_FIELD = var_0_0.FieldDescriptor()
var_0_2.CS_15004_COUNT_FIELD = var_0_0.FieldDescriptor()
SC_15005 = var_0_0.Descriptor()
var_0_2.SC_15005_RESULT_FIELD = var_0_0.FieldDescriptor()
CS_15006 = var_0_0.Descriptor()
var_0_2.CS_15006_ID_FIELD = var_0_0.FieldDescriptor()
var_0_2.CS_15006_NUM_FIELD = var_0_0.FieldDescriptor()
SC_15007 = var_0_0.Descriptor()
var_0_2.SC_15007_RESULT_FIELD = var_0_0.FieldDescriptor()
CS_15008 = var_0_0.Descriptor()
var_0_2.CS_15008_ITEM_LIST_FIELD = var_0_0.FieldDescriptor()
SC_15009 = var_0_0.Descriptor()
var_0_2.SC_15009_RESULT_FIELD = var_0_0.FieldDescriptor()
CS_15010 = var_0_0.Descriptor()
var_0_2.CS_15010_ID_FIELD = var_0_0.FieldDescriptor()
SC_15011 = var_0_0.Descriptor()
var_0_2.SC_15011_RESULT_FIELD = var_0_0.FieldDescriptor()
CS_15012 = var_0_0.Descriptor()
var_0_2.CS_15012_USE_LIST_FIELD = var_0_0.FieldDescriptor()
SC_15013 = var_0_0.Descriptor()
var_0_2.SC_15013_RET_LIST_FIELD = var_0_0.FieldDescriptor()
ITEMINFO = var_0_0.Descriptor()
var_0_2.ITEMINFO_ID_FIELD = var_0_0.FieldDescriptor()
var_0_2.ITEMINFO_COUNT_FIELD = var_0_0.FieldDescriptor()
ITEMMISC = var_0_0.Descriptor()
var_0_2.ITEMMISC_ID_FIELD = var_0_0.FieldDescriptor()
var_0_2.ITEMMISC_DATA_FIELD = var_0_0.FieldDescriptor()
CS_15300 = var_0_0.Descriptor()
var_0_2.CS_15300_TYPE_FIELD = var_0_0.FieldDescriptor()
var_0_2.CS_15300_VER_STR_FIELD = var_0_0.FieldDescriptor()
var_0_2.SC_15001_ITEM_LIST_FIELD.name = "item_list"
var_0_2.SC_15001_ITEM_LIST_FIELD.full_name = "p15.sc_15001.item_list"
var_0_2.SC_15001_ITEM_LIST_FIELD.number = 1
var_0_2.SC_15001_ITEM_LIST_FIELD.index = 0
var_0_2.SC_15001_ITEM_LIST_FIELD.label = 3
var_0_2.SC_15001_ITEM_LIST_FIELD.has_default_value = false
var_0_2.SC_15001_ITEM_LIST_FIELD.default_value = {}
var_0_2.SC_15001_ITEM_LIST_FIELD.message_type = ITEMINFO
var_0_2.SC_15001_ITEM_LIST_FIELD.type = 11
var_0_2.SC_15001_ITEM_LIST_FIELD.cpp_type = 10
var_0_2.SC_15001_LIMIT_LIST_FIELD.name = "limit_list"
var_0_2.SC_15001_LIMIT_LIST_FIELD.full_name = "p15.sc_15001.limit_list"
var_0_2.SC_15001_LIMIT_LIST_FIELD.number = 2
var_0_2.SC_15001_LIMIT_LIST_FIELD.index = 1
var_0_2.SC_15001_LIMIT_LIST_FIELD.label = 3
var_0_2.SC_15001_LIMIT_LIST_FIELD.has_default_value = false
var_0_2.SC_15001_LIMIT_LIST_FIELD.default_value = {}
var_0_2.SC_15001_LIMIT_LIST_FIELD.message_type = ITEMINFO
var_0_2.SC_15001_LIMIT_LIST_FIELD.type = 11
var_0_2.SC_15001_LIMIT_LIST_FIELD.cpp_type = 10
var_0_2.SC_15001_ITEM_MISC_LIST_FIELD.name = "item_misc_list"
var_0_2.SC_15001_ITEM_MISC_LIST_FIELD.full_name = "p15.sc_15001.item_misc_list"
var_0_2.SC_15001_ITEM_MISC_LIST_FIELD.number = 3
var_0_2.SC_15001_ITEM_MISC_LIST_FIELD.index = 2
var_0_2.SC_15001_ITEM_MISC_LIST_FIELD.label = 3
var_0_2.SC_15001_ITEM_MISC_LIST_FIELD.has_default_value = false
var_0_2.SC_15001_ITEM_MISC_LIST_FIELD.default_value = {}
var_0_2.SC_15001_ITEM_MISC_LIST_FIELD.message_type = ITEMMISC
var_0_2.SC_15001_ITEM_MISC_LIST_FIELD.type = 11
var_0_2.SC_15001_ITEM_MISC_LIST_FIELD.cpp_type = 10
SC_15001.name = "sc_15001"
SC_15001.full_name = "p15.sc_15001"
SC_15001.nested_types = {}
SC_15001.enum_types = {}
SC_15001.fields = {
	var_0_2.SC_15001_ITEM_LIST_FIELD,
	var_0_2.SC_15001_LIMIT_LIST_FIELD,
	var_0_2.SC_15001_ITEM_MISC_LIST_FIELD
}
SC_15001.is_extendable = false
SC_15001.extensions = {}
var_0_2.CS_15002_ID_FIELD.name = "id"
var_0_2.CS_15002_ID_FIELD.full_name = "p15.cs_15002.id"
var_0_2.CS_15002_ID_FIELD.number = 1
var_0_2.CS_15002_ID_FIELD.index = 0
var_0_2.CS_15002_ID_FIELD.label = 2
var_0_2.CS_15002_ID_FIELD.has_default_value = false
var_0_2.CS_15002_ID_FIELD.default_value = 0
var_0_2.CS_15002_ID_FIELD.type = 13
var_0_2.CS_15002_ID_FIELD.cpp_type = 3
var_0_2.CS_15002_COUNT_FIELD.name = "count"
var_0_2.CS_15002_COUNT_FIELD.full_name = "p15.cs_15002.count"
var_0_2.CS_15002_COUNT_FIELD.number = 2
var_0_2.CS_15002_COUNT_FIELD.index = 1
var_0_2.CS_15002_COUNT_FIELD.label = 2
var_0_2.CS_15002_COUNT_FIELD.has_default_value = false
var_0_2.CS_15002_COUNT_FIELD.default_value = 0
var_0_2.CS_15002_COUNT_FIELD.type = 13
var_0_2.CS_15002_COUNT_FIELD.cpp_type = 3
var_0_2.CS_15002_ARG_FIELD.name = "arg"
var_0_2.CS_15002_ARG_FIELD.full_name = "p15.cs_15002.arg"
var_0_2.CS_15002_ARG_FIELD.number = 3
var_0_2.CS_15002_ARG_FIELD.index = 2
var_0_2.CS_15002_ARG_FIELD.label = 3
var_0_2.CS_15002_ARG_FIELD.has_default_value = false
var_0_2.CS_15002_ARG_FIELD.default_value = {}
var_0_2.CS_15002_ARG_FIELD.type = 13
var_0_2.CS_15002_ARG_FIELD.cpp_type = 3
CS_15002.name = "cs_15002"
CS_15002.full_name = "p15.cs_15002"
CS_15002.nested_types = {}
CS_15002.enum_types = {}
CS_15002.fields = {
	var_0_2.CS_15002_ID_FIELD,
	var_0_2.CS_15002_COUNT_FIELD,
	var_0_2.CS_15002_ARG_FIELD
}
CS_15002.is_extendable = false
CS_15002.extensions = {}
var_0_2.SC_15003_RESULT_FIELD.name = "result"
var_0_2.SC_15003_RESULT_FIELD.full_name = "p15.sc_15003.result"
var_0_2.SC_15003_RESULT_FIELD.number = 1
var_0_2.SC_15003_RESULT_FIELD.index = 0
var_0_2.SC_15003_RESULT_FIELD.label = 2
var_0_2.SC_15003_RESULT_FIELD.has_default_value = false
var_0_2.SC_15003_RESULT_FIELD.default_value = 0
var_0_2.SC_15003_RESULT_FIELD.type = 13
var_0_2.SC_15003_RESULT_FIELD.cpp_type = 3
var_0_2.SC_15003_DROP_LIST_FIELD.name = "drop_list"
var_0_2.SC_15003_DROP_LIST_FIELD.full_name = "p15.sc_15003.drop_list"
var_0_2.SC_15003_DROP_LIST_FIELD.number = 2
var_0_2.SC_15003_DROP_LIST_FIELD.index = 1
var_0_2.SC_15003_DROP_LIST_FIELD.label = 3
var_0_2.SC_15003_DROP_LIST_FIELD.has_default_value = false
var_0_2.SC_15003_DROP_LIST_FIELD.default_value = {}
var_0_2.SC_15003_DROP_LIST_FIELD.message_type = var_0_1.DROPINFO
var_0_2.SC_15003_DROP_LIST_FIELD.type = 11
var_0_2.SC_15003_DROP_LIST_FIELD.cpp_type = 10
SC_15003.name = "sc_15003"
SC_15003.full_name = "p15.sc_15003"
SC_15003.nested_types = {}
SC_15003.enum_types = {}
SC_15003.fields = {
	var_0_2.SC_15003_RESULT_FIELD,
	var_0_2.SC_15003_DROP_LIST_FIELD
}
SC_15003.is_extendable = false
SC_15003.extensions = {}
var_0_2.CS_15004_ID_FIELD.name = "id"
var_0_2.CS_15004_ID_FIELD.full_name = "p15.cs_15004.id"
var_0_2.CS_15004_ID_FIELD.number = 1
var_0_2.CS_15004_ID_FIELD.index = 0
var_0_2.CS_15004_ID_FIELD.label = 2
var_0_2.CS_15004_ID_FIELD.has_default_value = false
var_0_2.CS_15004_ID_FIELD.default_value = 0
var_0_2.CS_15004_ID_FIELD.type = 13
var_0_2.CS_15004_ID_FIELD.cpp_type = 3
var_0_2.CS_15004_COUNT_FIELD.name = "count"
var_0_2.CS_15004_COUNT_FIELD.full_name = "p15.cs_15004.count"
var_0_2.CS_15004_COUNT_FIELD.number = 2
var_0_2.CS_15004_COUNT_FIELD.index = 1
var_0_2.CS_15004_COUNT_FIELD.label = 2
var_0_2.CS_15004_COUNT_FIELD.has_default_value = false
var_0_2.CS_15004_COUNT_FIELD.default_value = 0
var_0_2.CS_15004_COUNT_FIELD.type = 13
var_0_2.CS_15004_COUNT_FIELD.cpp_type = 3
CS_15004.name = "cs_15004"
CS_15004.full_name = "p15.cs_15004"
CS_15004.nested_types = {}
CS_15004.enum_types = {}
CS_15004.fields = {
	var_0_2.CS_15004_ID_FIELD,
	var_0_2.CS_15004_COUNT_FIELD
}
CS_15004.is_extendable = false
CS_15004.extensions = {}
var_0_2.SC_15005_RESULT_FIELD.name = "result"
var_0_2.SC_15005_RESULT_FIELD.full_name = "p15.sc_15005.result"
var_0_2.SC_15005_RESULT_FIELD.number = 1
var_0_2.SC_15005_RESULT_FIELD.index = 0
var_0_2.SC_15005_RESULT_FIELD.label = 2
var_0_2.SC_15005_RESULT_FIELD.has_default_value = false
var_0_2.SC_15005_RESULT_FIELD.default_value = 0
var_0_2.SC_15005_RESULT_FIELD.type = 13
var_0_2.SC_15005_RESULT_FIELD.cpp_type = 3
SC_15005.name = "sc_15005"
SC_15005.full_name = "p15.sc_15005"
SC_15005.nested_types = {}
SC_15005.enum_types = {}
SC_15005.fields = {
	var_0_2.SC_15005_RESULT_FIELD
}
SC_15005.is_extendable = false
SC_15005.extensions = {}
var_0_2.CS_15006_ID_FIELD.name = "id"
var_0_2.CS_15006_ID_FIELD.full_name = "p15.cs_15006.id"
var_0_2.CS_15006_ID_FIELD.number = 1
var_0_2.CS_15006_ID_FIELD.index = 0
var_0_2.CS_15006_ID_FIELD.label = 2
var_0_2.CS_15006_ID_FIELD.has_default_value = false
var_0_2.CS_15006_ID_FIELD.default_value = 0
var_0_2.CS_15006_ID_FIELD.type = 13
var_0_2.CS_15006_ID_FIELD.cpp_type = 3
var_0_2.CS_15006_NUM_FIELD.name = "num"
var_0_2.CS_15006_NUM_FIELD.full_name = "p15.cs_15006.num"
var_0_2.CS_15006_NUM_FIELD.number = 2
var_0_2.CS_15006_NUM_FIELD.index = 1
var_0_2.CS_15006_NUM_FIELD.label = 2
var_0_2.CS_15006_NUM_FIELD.has_default_value = false
var_0_2.CS_15006_NUM_FIELD.default_value = 0
var_0_2.CS_15006_NUM_FIELD.type = 13
var_0_2.CS_15006_NUM_FIELD.cpp_type = 3
CS_15006.name = "cs_15006"
CS_15006.full_name = "p15.cs_15006"
CS_15006.nested_types = {}
CS_15006.enum_types = {}
CS_15006.fields = {
	var_0_2.CS_15006_ID_FIELD,
	var_0_2.CS_15006_NUM_FIELD
}
CS_15006.is_extendable = false
CS_15006.extensions = {}
var_0_2.SC_15007_RESULT_FIELD.name = "result"
var_0_2.SC_15007_RESULT_FIELD.full_name = "p15.sc_15007.result"
var_0_2.SC_15007_RESULT_FIELD.number = 1
var_0_2.SC_15007_RESULT_FIELD.index = 0
var_0_2.SC_15007_RESULT_FIELD.label = 2
var_0_2.SC_15007_RESULT_FIELD.has_default_value = false
var_0_2.SC_15007_RESULT_FIELD.default_value = 0
var_0_2.SC_15007_RESULT_FIELD.type = 13
var_0_2.SC_15007_RESULT_FIELD.cpp_type = 3
SC_15007.name = "sc_15007"
SC_15007.full_name = "p15.sc_15007"
SC_15007.nested_types = {}
SC_15007.enum_types = {}
SC_15007.fields = {
	var_0_2.SC_15007_RESULT_FIELD
}
SC_15007.is_extendable = false
SC_15007.extensions = {}
var_0_2.CS_15008_ITEM_LIST_FIELD.name = "item_list"
var_0_2.CS_15008_ITEM_LIST_FIELD.full_name = "p15.cs_15008.item_list"
var_0_2.CS_15008_ITEM_LIST_FIELD.number = 1
var_0_2.CS_15008_ITEM_LIST_FIELD.index = 0
var_0_2.CS_15008_ITEM_LIST_FIELD.label = 3
var_0_2.CS_15008_ITEM_LIST_FIELD.has_default_value = false
var_0_2.CS_15008_ITEM_LIST_FIELD.default_value = {}
var_0_2.CS_15008_ITEM_LIST_FIELD.message_type = ITEMINFO
var_0_2.CS_15008_ITEM_LIST_FIELD.type = 11
var_0_2.CS_15008_ITEM_LIST_FIELD.cpp_type = 10
CS_15008.name = "cs_15008"
CS_15008.full_name = "p15.cs_15008"
CS_15008.nested_types = {}
CS_15008.enum_types = {}
CS_15008.fields = {
	var_0_2.CS_15008_ITEM_LIST_FIELD
}
CS_15008.is_extendable = false
CS_15008.extensions = {}
var_0_2.SC_15009_RESULT_FIELD.name = "result"
var_0_2.SC_15009_RESULT_FIELD.full_name = "p15.sc_15009.result"
var_0_2.SC_15009_RESULT_FIELD.number = 1
var_0_2.SC_15009_RESULT_FIELD.index = 0
var_0_2.SC_15009_RESULT_FIELD.label = 2
var_0_2.SC_15009_RESULT_FIELD.has_default_value = false
var_0_2.SC_15009_RESULT_FIELD.default_value = 0
var_0_2.SC_15009_RESULT_FIELD.type = 13
var_0_2.SC_15009_RESULT_FIELD.cpp_type = 3
SC_15009.name = "sc_15009"
SC_15009.full_name = "p15.sc_15009"
SC_15009.nested_types = {}
SC_15009.enum_types = {}
SC_15009.fields = {
	var_0_2.SC_15009_RESULT_FIELD
}
SC_15009.is_extendable = false
SC_15009.extensions = {}
var_0_2.CS_15010_ID_FIELD.name = "id"
var_0_2.CS_15010_ID_FIELD.full_name = "p15.cs_15010.id"
var_0_2.CS_15010_ID_FIELD.number = 1
var_0_2.CS_15010_ID_FIELD.index = 0
var_0_2.CS_15010_ID_FIELD.label = 2
var_0_2.CS_15010_ID_FIELD.has_default_value = false
var_0_2.CS_15010_ID_FIELD.default_value = 0
var_0_2.CS_15010_ID_FIELD.type = 13
var_0_2.CS_15010_ID_FIELD.cpp_type = 3
CS_15010.name = "cs_15010"
CS_15010.full_name = "p15.cs_15010"
CS_15010.nested_types = {}
CS_15010.enum_types = {}
CS_15010.fields = {
	var_0_2.CS_15010_ID_FIELD
}
CS_15010.is_extendable = false
CS_15010.extensions = {}
var_0_2.SC_15011_RESULT_FIELD.name = "result"
var_0_2.SC_15011_RESULT_FIELD.full_name = "p15.sc_15011.result"
var_0_2.SC_15011_RESULT_FIELD.number = 1
var_0_2.SC_15011_RESULT_FIELD.index = 0
var_0_2.SC_15011_RESULT_FIELD.label = 2
var_0_2.SC_15011_RESULT_FIELD.has_default_value = false
var_0_2.SC_15011_RESULT_FIELD.default_value = 0
var_0_2.SC_15011_RESULT_FIELD.type = 13
var_0_2.SC_15011_RESULT_FIELD.cpp_type = 3
SC_15011.name = "sc_15011"
SC_15011.full_name = "p15.sc_15011"
SC_15011.nested_types = {}
SC_15011.enum_types = {}
SC_15011.fields = {
	var_0_2.SC_15011_RESULT_FIELD
}
SC_15011.is_extendable = false
SC_15011.extensions = {}
var_0_2.CS_15012_USE_LIST_FIELD.name = "use_list"
var_0_2.CS_15012_USE_LIST_FIELD.full_name = "p15.cs_15012.use_list"
var_0_2.CS_15012_USE_LIST_FIELD.number = 1
var_0_2.CS_15012_USE_LIST_FIELD.index = 0
var_0_2.CS_15012_USE_LIST_FIELD.label = 3
var_0_2.CS_15012_USE_LIST_FIELD.has_default_value = false
var_0_2.CS_15012_USE_LIST_FIELD.default_value = {}
var_0_2.CS_15012_USE_LIST_FIELD.message_type = CS_15002
var_0_2.CS_15012_USE_LIST_FIELD.type = 11
var_0_2.CS_15012_USE_LIST_FIELD.cpp_type = 10
CS_15012.name = "cs_15012"
CS_15012.full_name = "p15.cs_15012"
CS_15012.nested_types = {}
CS_15012.enum_types = {}
CS_15012.fields = {
	var_0_2.CS_15012_USE_LIST_FIELD
}
CS_15012.is_extendable = false
CS_15012.extensions = {}
var_0_2.SC_15013_RET_LIST_FIELD.name = "ret_list"
var_0_2.SC_15013_RET_LIST_FIELD.full_name = "p15.sc_15013.ret_list"
var_0_2.SC_15013_RET_LIST_FIELD.number = 1
var_0_2.SC_15013_RET_LIST_FIELD.index = 0
var_0_2.SC_15013_RET_LIST_FIELD.label = 3
var_0_2.SC_15013_RET_LIST_FIELD.has_default_value = false
var_0_2.SC_15013_RET_LIST_FIELD.default_value = {}
var_0_2.SC_15013_RET_LIST_FIELD.message_type = SC_15003
var_0_2.SC_15013_RET_LIST_FIELD.type = 11
var_0_2.SC_15013_RET_LIST_FIELD.cpp_type = 10
SC_15013.name = "sc_15013"
SC_15013.full_name = "p15.sc_15013"
SC_15013.nested_types = {}
SC_15013.enum_types = {}
SC_15013.fields = {
	var_0_2.SC_15013_RET_LIST_FIELD
}
SC_15013.is_extendable = false
SC_15013.extensions = {}
var_0_2.ITEMINFO_ID_FIELD.name = "id"
var_0_2.ITEMINFO_ID_FIELD.full_name = "p15.iteminfo.id"
var_0_2.ITEMINFO_ID_FIELD.number = 1
var_0_2.ITEMINFO_ID_FIELD.index = 0
var_0_2.ITEMINFO_ID_FIELD.label = 2
var_0_2.ITEMINFO_ID_FIELD.has_default_value = false
var_0_2.ITEMINFO_ID_FIELD.default_value = 0
var_0_2.ITEMINFO_ID_FIELD.type = 13
var_0_2.ITEMINFO_ID_FIELD.cpp_type = 3
var_0_2.ITEMINFO_COUNT_FIELD.name = "count"
var_0_2.ITEMINFO_COUNT_FIELD.full_name = "p15.iteminfo.count"
var_0_2.ITEMINFO_COUNT_FIELD.number = 2
var_0_2.ITEMINFO_COUNT_FIELD.index = 1
var_0_2.ITEMINFO_COUNT_FIELD.label = 2
var_0_2.ITEMINFO_COUNT_FIELD.has_default_value = false
var_0_2.ITEMINFO_COUNT_FIELD.default_value = 0
var_0_2.ITEMINFO_COUNT_FIELD.type = 13
var_0_2.ITEMINFO_COUNT_FIELD.cpp_type = 3
ITEMINFO.name = "iteminfo"
ITEMINFO.full_name = "p15.iteminfo"
ITEMINFO.nested_types = {}
ITEMINFO.enum_types = {}
ITEMINFO.fields = {
	var_0_2.ITEMINFO_ID_FIELD,
	var_0_2.ITEMINFO_COUNT_FIELD
}
ITEMINFO.is_extendable = false
ITEMINFO.extensions = {}
var_0_2.ITEMMISC_ID_FIELD.name = "id"
var_0_2.ITEMMISC_ID_FIELD.full_name = "p15.itemmisc.id"
var_0_2.ITEMMISC_ID_FIELD.number = 1
var_0_2.ITEMMISC_ID_FIELD.index = 0
var_0_2.ITEMMISC_ID_FIELD.label = 2
var_0_2.ITEMMISC_ID_FIELD.has_default_value = false
var_0_2.ITEMMISC_ID_FIELD.default_value = 0
var_0_2.ITEMMISC_ID_FIELD.type = 13
var_0_2.ITEMMISC_ID_FIELD.cpp_type = 3
var_0_2.ITEMMISC_DATA_FIELD.name = "data"
var_0_2.ITEMMISC_DATA_FIELD.full_name = "p15.itemmisc.data"
var_0_2.ITEMMISC_DATA_FIELD.number = 2
var_0_2.ITEMMISC_DATA_FIELD.index = 1
var_0_2.ITEMMISC_DATA_FIELD.label = 2
var_0_2.ITEMMISC_DATA_FIELD.has_default_value = false
var_0_2.ITEMMISC_DATA_FIELD.default_value = 0
var_0_2.ITEMMISC_DATA_FIELD.type = 13
var_0_2.ITEMMISC_DATA_FIELD.cpp_type = 3
ITEMMISC.name = "itemmisc"
ITEMMISC.full_name = "p15.itemmisc"
ITEMMISC.nested_types = {}
ITEMMISC.enum_types = {}
ITEMMISC.fields = {
	var_0_2.ITEMMISC_ID_FIELD,
	var_0_2.ITEMMISC_DATA_FIELD
}
ITEMMISC.is_extendable = false
ITEMMISC.extensions = {}
var_0_2.CS_15300_TYPE_FIELD.name = "type"
var_0_2.CS_15300_TYPE_FIELD.full_name = "p15.cs_15300.type"
var_0_2.CS_15300_TYPE_FIELD.number = 1
var_0_2.CS_15300_TYPE_FIELD.index = 0
var_0_2.CS_15300_TYPE_FIELD.label = 2
var_0_2.CS_15300_TYPE_FIELD.has_default_value = false
var_0_2.CS_15300_TYPE_FIELD.default_value = 0
var_0_2.CS_15300_TYPE_FIELD.type = 13
var_0_2.CS_15300_TYPE_FIELD.cpp_type = 3
var_0_2.CS_15300_VER_STR_FIELD.name = "ver_str"
var_0_2.CS_15300_VER_STR_FIELD.full_name = "p15.cs_15300.ver_str"
var_0_2.CS_15300_VER_STR_FIELD.number = 2
var_0_2.CS_15300_VER_STR_FIELD.index = 1
var_0_2.CS_15300_VER_STR_FIELD.label = 2
var_0_2.CS_15300_VER_STR_FIELD.has_default_value = false
var_0_2.CS_15300_VER_STR_FIELD.default_value = ""
var_0_2.CS_15300_VER_STR_FIELD.type = 9
var_0_2.CS_15300_VER_STR_FIELD.cpp_type = 9
CS_15300.name = "cs_15300"
CS_15300.full_name = "p15.cs_15300"
CS_15300.nested_types = {}
CS_15300.enum_types = {}
CS_15300.fields = {
	var_0_2.CS_15300_TYPE_FIELD,
	var_0_2.CS_15300_VER_STR_FIELD
}
CS_15300.is_extendable = false
CS_15300.extensions = {}
cs_15002 = var_0_0.Message(CS_15002)
cs_15004 = var_0_0.Message(CS_15004)
cs_15006 = var_0_0.Message(CS_15006)
cs_15008 = var_0_0.Message(CS_15008)
cs_15010 = var_0_0.Message(CS_15010)
cs_15012 = var_0_0.Message(CS_15012)
cs_15300 = var_0_0.Message(CS_15300)
iteminfo = var_0_0.Message(ITEMINFO)
itemmisc = var_0_0.Message(ITEMMISC)
sc_15001 = var_0_0.Message(SC_15001)
sc_15003 = var_0_0.Message(SC_15003)
sc_15005 = var_0_0.Message(SC_15005)
sc_15007 = var_0_0.Message(SC_15007)
sc_15009 = var_0_0.Message(SC_15009)
sc_15011 = var_0_0.Message(SC_15011)
sc_15013 = var_0_0.Message(SC_15013)
