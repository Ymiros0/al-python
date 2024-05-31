﻿local var_0_0 = require("protobuf")
local var_0_1 = require("common_pb")

module("p16_pb")

local var_0_2 = {}

CS_16001 = var_0_0.Descriptor()
var_0_2.CS_16001_ID_FIELD = var_0_0.FieldDescriptor()
var_0_2.CS_16001_NUMBER_FIELD = var_0_0.FieldDescriptor()
SC_16002 = var_0_0.Descriptor()
var_0_2.SC_16002_RESULT_FIELD = var_0_0.FieldDescriptor()
var_0_2.SC_16002_DROP_LIST_FIELD = var_0_0.FieldDescriptor()
CS_16100 = var_0_0.Descriptor()
var_0_2.CS_16100_CNT_FIELD = var_0_0.FieldDescriptor()
SC_16101 = var_0_0.Descriptor()
var_0_2.SC_16101_RESULT_FIELD = var_0_0.FieldDescriptor()
var_0_2.SC_16101_SHIP_LIST_FIELD = var_0_0.FieldDescriptor()
CS_16104 = var_0_0.Descriptor()
var_0_2.CS_16104_TYPE_FIELD = var_0_0.FieldDescriptor()
SC_16105 = var_0_0.Descriptor()
var_0_2.SC_16105_FIRST_PAY_LIST_FIELD = var_0_0.FieldDescriptor()
var_0_2.SC_16105_PAY_LIST_FIELD = var_0_0.FieldDescriptor()
var_0_2.SC_16105_NORMAL_LIST_FIELD = var_0_0.FieldDescriptor()
var_0_2.SC_16105_NORMAL_GROUP_LIST_FIELD = var_0_0.FieldDescriptor()
CS_16106 = var_0_0.Descriptor()
var_0_2.CS_16106_TYPE_FIELD = var_0_0.FieldDescriptor()
SC_16107 = var_0_0.Descriptor()
var_0_2.SC_16107_RESULT_FIELD = var_0_0.FieldDescriptor()
var_0_2.SC_16107_ITEM_FLASH_TIME_FIELD = var_0_0.FieldDescriptor()
var_0_2.SC_16107_GOOD_LIST_FIELD = var_0_0.FieldDescriptor()
CS_16108 = var_0_0.Descriptor()
var_0_2.CS_16108_FLASH_TIME_FIELD = var_0_0.FieldDescriptor()
var_0_2.CS_16108_SHOPID_FIELD = var_0_0.FieldDescriptor()
var_0_2.CS_16108_SELECTED_FIELD = var_0_0.FieldDescriptor()
SC_16109 = var_0_0.Descriptor()
var_0_2.SC_16109_RESULT_FIELD = var_0_0.FieldDescriptor()
var_0_2.SC_16109_DROP_LIST_FIELD = var_0_0.FieldDescriptor()
SC_16200 = var_0_0.Descriptor()
var_0_2.SC_16200_CORE_SHOP_LIST_FIELD = var_0_0.FieldDescriptor()
var_0_2.SC_16200_BLUE_SHOP_LIST_FIELD = var_0_0.FieldDescriptor()
var_0_2.SC_16200_NORMAL_SHOP_LIST_FIELD = var_0_0.FieldDescriptor()
var_0_2.SC_16200_MONTH_FIELD = var_0_0.FieldDescriptor()
CS_16201 = var_0_0.Descriptor()
var_0_2.CS_16201_TYPE_FIELD = var_0_0.FieldDescriptor()
var_0_2.CS_16201_ID_FIELD = var_0_0.FieldDescriptor()
var_0_2.CS_16201_COUNT_FIELD = var_0_0.FieldDescriptor()
SC_16202 = var_0_0.Descriptor()
var_0_2.SC_16202_RESULT_FIELD = var_0_0.FieldDescriptor()
var_0_2.SC_16202_DROP_LIST_FIELD = var_0_0.FieldDescriptor()
CS_16203 = var_0_0.Descriptor()
var_0_2.CS_16203_FLAG_FIELD = var_0_0.FieldDescriptor()
SC_16204 = var_0_0.Descriptor()
var_0_2.SC_16204_RET_FIELD = var_0_0.FieldDescriptor()
CS_16205 = var_0_0.Descriptor()
var_0_2.CS_16205_ID_FIELD = var_0_0.FieldDescriptor()
var_0_2.CS_16205_COST_TYPE_FIELD = var_0_0.FieldDescriptor()
SC_16206 = var_0_0.Descriptor()
var_0_2.SC_16206_RET_FIELD = var_0_0.FieldDescriptor()
SHOPINFO = var_0_0.Descriptor()
var_0_2.SHOPINFO_SHOP_ID_FIELD = var_0_0.FieldDescriptor()
var_0_2.SHOPINFO_PAY_COUNT_FIELD = var_0_0.FieldDescriptor()
GOODS_INFO = var_0_0.Descriptor()
var_0_2.GOODS_INFO_ID_FIELD = var_0_0.FieldDescriptor()
var_0_2.GOODS_INFO_COUNT_FIELD = var_0_0.FieldDescriptor()
SELECTED_INFO = var_0_0.Descriptor()
var_0_2.SELECTED_INFO_ID_FIELD = var_0_0.FieldDescriptor()
var_0_2.SELECTED_INFO_COUNT_FIELD = var_0_0.FieldDescriptor()
var_0_2.CS_16001_ID_FIELD.name = "id"
var_0_2.CS_16001_ID_FIELD.full_name = "p16.cs_16001.id"
var_0_2.CS_16001_ID_FIELD.number = 1
var_0_2.CS_16001_ID_FIELD.index = 0
var_0_2.CS_16001_ID_FIELD.label = 2
var_0_2.CS_16001_ID_FIELD.has_default_value = false
var_0_2.CS_16001_ID_FIELD.default_value = 0
var_0_2.CS_16001_ID_FIELD.type = 13
var_0_2.CS_16001_ID_FIELD.cpp_type = 3
var_0_2.CS_16001_NUMBER_FIELD.name = "number"
var_0_2.CS_16001_NUMBER_FIELD.full_name = "p16.cs_16001.number"
var_0_2.CS_16001_NUMBER_FIELD.number = 2
var_0_2.CS_16001_NUMBER_FIELD.index = 1
var_0_2.CS_16001_NUMBER_FIELD.label = 2
var_0_2.CS_16001_NUMBER_FIELD.has_default_value = false
var_0_2.CS_16001_NUMBER_FIELD.default_value = 0
var_0_2.CS_16001_NUMBER_FIELD.type = 13
var_0_2.CS_16001_NUMBER_FIELD.cpp_type = 3
CS_16001.name = "cs_16001"
CS_16001.full_name = "p16.cs_16001"
CS_16001.nested_types = {}
CS_16001.enum_types = {}
CS_16001.fields = {
	var_0_2.CS_16001_ID_FIELD,
	var_0_2.CS_16001_NUMBER_FIELD
}
CS_16001.is_extendable = false
CS_16001.extensions = {}
var_0_2.SC_16002_RESULT_FIELD.name = "result"
var_0_2.SC_16002_RESULT_FIELD.full_name = "p16.sc_16002.result"
var_0_2.SC_16002_RESULT_FIELD.number = 1
var_0_2.SC_16002_RESULT_FIELD.index = 0
var_0_2.SC_16002_RESULT_FIELD.label = 2
var_0_2.SC_16002_RESULT_FIELD.has_default_value = false
var_0_2.SC_16002_RESULT_FIELD.default_value = 0
var_0_2.SC_16002_RESULT_FIELD.type = 13
var_0_2.SC_16002_RESULT_FIELD.cpp_type = 3
var_0_2.SC_16002_DROP_LIST_FIELD.name = "drop_list"
var_0_2.SC_16002_DROP_LIST_FIELD.full_name = "p16.sc_16002.drop_list"
var_0_2.SC_16002_DROP_LIST_FIELD.number = 2
var_0_2.SC_16002_DROP_LIST_FIELD.index = 1
var_0_2.SC_16002_DROP_LIST_FIELD.label = 3
var_0_2.SC_16002_DROP_LIST_FIELD.has_default_value = false
var_0_2.SC_16002_DROP_LIST_FIELD.default_value = {}
var_0_2.SC_16002_DROP_LIST_FIELD.message_type = var_0_1.DROPINFO
var_0_2.SC_16002_DROP_LIST_FIELD.type = 11
var_0_2.SC_16002_DROP_LIST_FIELD.cpp_type = 10
SC_16002.name = "sc_16002"
SC_16002.full_name = "p16.sc_16002"
SC_16002.nested_types = {}
SC_16002.enum_types = {}
SC_16002.fields = {
	var_0_2.SC_16002_RESULT_FIELD,
	var_0_2.SC_16002_DROP_LIST_FIELD
}
SC_16002.is_extendable = false
SC_16002.extensions = {}
var_0_2.CS_16100_CNT_FIELD.name = "cnt"
var_0_2.CS_16100_CNT_FIELD.full_name = "p16.cs_16100.cnt"
var_0_2.CS_16100_CNT_FIELD.number = 1
var_0_2.CS_16100_CNT_FIELD.index = 0
var_0_2.CS_16100_CNT_FIELD.label = 2
var_0_2.CS_16100_CNT_FIELD.has_default_value = false
var_0_2.CS_16100_CNT_FIELD.default_value = 0
var_0_2.CS_16100_CNT_FIELD.type = 13
var_0_2.CS_16100_CNT_FIELD.cpp_type = 3
CS_16100.name = "cs_16100"
CS_16100.full_name = "p16.cs_16100"
CS_16100.nested_types = {}
CS_16100.enum_types = {}
CS_16100.fields = {
	var_0_2.CS_16100_CNT_FIELD
}
CS_16100.is_extendable = false
CS_16100.extensions = {}
var_0_2.SC_16101_RESULT_FIELD.name = "result"
var_0_2.SC_16101_RESULT_FIELD.full_name = "p16.sc_16101.result"
var_0_2.SC_16101_RESULT_FIELD.number = 1
var_0_2.SC_16101_RESULT_FIELD.index = 0
var_0_2.SC_16101_RESULT_FIELD.label = 2
var_0_2.SC_16101_RESULT_FIELD.has_default_value = false
var_0_2.SC_16101_RESULT_FIELD.default_value = 0
var_0_2.SC_16101_RESULT_FIELD.type = 13
var_0_2.SC_16101_RESULT_FIELD.cpp_type = 3
var_0_2.SC_16101_SHIP_LIST_FIELD.name = "ship_list"
var_0_2.SC_16101_SHIP_LIST_FIELD.full_name = "p16.sc_16101.ship_list"
var_0_2.SC_16101_SHIP_LIST_FIELD.number = 2
var_0_2.SC_16101_SHIP_LIST_FIELD.index = 1
var_0_2.SC_16101_SHIP_LIST_FIELD.label = 3
var_0_2.SC_16101_SHIP_LIST_FIELD.has_default_value = false
var_0_2.SC_16101_SHIP_LIST_FIELD.default_value = {}
var_0_2.SC_16101_SHIP_LIST_FIELD.message_type = var_0_1.SHIPINFO
var_0_2.SC_16101_SHIP_LIST_FIELD.type = 11
var_0_2.SC_16101_SHIP_LIST_FIELD.cpp_type = 10
SC_16101.name = "sc_16101"
SC_16101.full_name = "p16.sc_16101"
SC_16101.nested_types = {}
SC_16101.enum_types = {}
SC_16101.fields = {
	var_0_2.SC_16101_RESULT_FIELD,
	var_0_2.SC_16101_SHIP_LIST_FIELD
}
SC_16101.is_extendable = false
SC_16101.extensions = {}
var_0_2.CS_16104_TYPE_FIELD.name = "type"
var_0_2.CS_16104_TYPE_FIELD.full_name = "p16.cs_16104.type"
var_0_2.CS_16104_TYPE_FIELD.number = 1
var_0_2.CS_16104_TYPE_FIELD.index = 0
var_0_2.CS_16104_TYPE_FIELD.label = 2
var_0_2.CS_16104_TYPE_FIELD.has_default_value = false
var_0_2.CS_16104_TYPE_FIELD.default_value = 0
var_0_2.CS_16104_TYPE_FIELD.type = 13
var_0_2.CS_16104_TYPE_FIELD.cpp_type = 3
CS_16104.name = "cs_16104"
CS_16104.full_name = "p16.cs_16104"
CS_16104.nested_types = {}
CS_16104.enum_types = {}
CS_16104.fields = {
	var_0_2.CS_16104_TYPE_FIELD
}
CS_16104.is_extendable = false
CS_16104.extensions = {}
var_0_2.SC_16105_FIRST_PAY_LIST_FIELD.name = "first_pay_list"
var_0_2.SC_16105_FIRST_PAY_LIST_FIELD.full_name = "p16.sc_16105.first_pay_list"
var_0_2.SC_16105_FIRST_PAY_LIST_FIELD.number = 1
var_0_2.SC_16105_FIRST_PAY_LIST_FIELD.index = 0
var_0_2.SC_16105_FIRST_PAY_LIST_FIELD.label = 3
var_0_2.SC_16105_FIRST_PAY_LIST_FIELD.has_default_value = false
var_0_2.SC_16105_FIRST_PAY_LIST_FIELD.default_value = {}
var_0_2.SC_16105_FIRST_PAY_LIST_FIELD.type = 13
var_0_2.SC_16105_FIRST_PAY_LIST_FIELD.cpp_type = 3
var_0_2.SC_16105_PAY_LIST_FIELD.name = "pay_list"
var_0_2.SC_16105_PAY_LIST_FIELD.full_name = "p16.sc_16105.pay_list"
var_0_2.SC_16105_PAY_LIST_FIELD.number = 2
var_0_2.SC_16105_PAY_LIST_FIELD.index = 1
var_0_2.SC_16105_PAY_LIST_FIELD.label = 3
var_0_2.SC_16105_PAY_LIST_FIELD.has_default_value = false
var_0_2.SC_16105_PAY_LIST_FIELD.default_value = {}
var_0_2.SC_16105_PAY_LIST_FIELD.message_type = SHOPINFO
var_0_2.SC_16105_PAY_LIST_FIELD.type = 11
var_0_2.SC_16105_PAY_LIST_FIELD.cpp_type = 10
var_0_2.SC_16105_NORMAL_LIST_FIELD.name = "normal_list"
var_0_2.SC_16105_NORMAL_LIST_FIELD.full_name = "p16.sc_16105.normal_list"
var_0_2.SC_16105_NORMAL_LIST_FIELD.number = 3
var_0_2.SC_16105_NORMAL_LIST_FIELD.index = 2
var_0_2.SC_16105_NORMAL_LIST_FIELD.label = 3
var_0_2.SC_16105_NORMAL_LIST_FIELD.has_default_value = false
var_0_2.SC_16105_NORMAL_LIST_FIELD.default_value = {}
var_0_2.SC_16105_NORMAL_LIST_FIELD.message_type = SHOPINFO
var_0_2.SC_16105_NORMAL_LIST_FIELD.type = 11
var_0_2.SC_16105_NORMAL_LIST_FIELD.cpp_type = 10
var_0_2.SC_16105_NORMAL_GROUP_LIST_FIELD.name = "normal_group_list"
var_0_2.SC_16105_NORMAL_GROUP_LIST_FIELD.full_name = "p16.sc_16105.normal_group_list"
var_0_2.SC_16105_NORMAL_GROUP_LIST_FIELD.number = 4
var_0_2.SC_16105_NORMAL_GROUP_LIST_FIELD.index = 3
var_0_2.SC_16105_NORMAL_GROUP_LIST_FIELD.label = 3
var_0_2.SC_16105_NORMAL_GROUP_LIST_FIELD.has_default_value = false
var_0_2.SC_16105_NORMAL_GROUP_LIST_FIELD.default_value = {}
var_0_2.SC_16105_NORMAL_GROUP_LIST_FIELD.message_type = SHOPINFO
var_0_2.SC_16105_NORMAL_GROUP_LIST_FIELD.type = 11
var_0_2.SC_16105_NORMAL_GROUP_LIST_FIELD.cpp_type = 10
SC_16105.name = "sc_16105"
SC_16105.full_name = "p16.sc_16105"
SC_16105.nested_types = {}
SC_16105.enum_types = {}
SC_16105.fields = {
	var_0_2.SC_16105_FIRST_PAY_LIST_FIELD,
	var_0_2.SC_16105_PAY_LIST_FIELD,
	var_0_2.SC_16105_NORMAL_LIST_FIELD,
	var_0_2.SC_16105_NORMAL_GROUP_LIST_FIELD
}
SC_16105.is_extendable = false
SC_16105.extensions = {}
var_0_2.CS_16106_TYPE_FIELD.name = "type"
var_0_2.CS_16106_TYPE_FIELD.full_name = "p16.cs_16106.type"
var_0_2.CS_16106_TYPE_FIELD.number = 1
var_0_2.CS_16106_TYPE_FIELD.index = 0
var_0_2.CS_16106_TYPE_FIELD.label = 2
var_0_2.CS_16106_TYPE_FIELD.has_default_value = false
var_0_2.CS_16106_TYPE_FIELD.default_value = 0
var_0_2.CS_16106_TYPE_FIELD.type = 13
var_0_2.CS_16106_TYPE_FIELD.cpp_type = 3
CS_16106.name = "cs_16106"
CS_16106.full_name = "p16.cs_16106"
CS_16106.nested_types = {}
CS_16106.enum_types = {}
CS_16106.fields = {
	var_0_2.CS_16106_TYPE_FIELD
}
CS_16106.is_extendable = false
CS_16106.extensions = {}
var_0_2.SC_16107_RESULT_FIELD.name = "result"
var_0_2.SC_16107_RESULT_FIELD.full_name = "p16.sc_16107.result"
var_0_2.SC_16107_RESULT_FIELD.number = 1
var_0_2.SC_16107_RESULT_FIELD.index = 0
var_0_2.SC_16107_RESULT_FIELD.label = 2
var_0_2.SC_16107_RESULT_FIELD.has_default_value = false
var_0_2.SC_16107_RESULT_FIELD.default_value = 0
var_0_2.SC_16107_RESULT_FIELD.type = 13
var_0_2.SC_16107_RESULT_FIELD.cpp_type = 3
var_0_2.SC_16107_ITEM_FLASH_TIME_FIELD.name = "item_flash_time"
var_0_2.SC_16107_ITEM_FLASH_TIME_FIELD.full_name = "p16.sc_16107.item_flash_time"
var_0_2.SC_16107_ITEM_FLASH_TIME_FIELD.number = 2
var_0_2.SC_16107_ITEM_FLASH_TIME_FIELD.index = 1
var_0_2.SC_16107_ITEM_FLASH_TIME_FIELD.label = 2
var_0_2.SC_16107_ITEM_FLASH_TIME_FIELD.has_default_value = false
var_0_2.SC_16107_ITEM_FLASH_TIME_FIELD.default_value = 0
var_0_2.SC_16107_ITEM_FLASH_TIME_FIELD.type = 13
var_0_2.SC_16107_ITEM_FLASH_TIME_FIELD.cpp_type = 3
var_0_2.SC_16107_GOOD_LIST_FIELD.name = "good_list"
var_0_2.SC_16107_GOOD_LIST_FIELD.full_name = "p16.sc_16107.good_list"
var_0_2.SC_16107_GOOD_LIST_FIELD.number = 3
var_0_2.SC_16107_GOOD_LIST_FIELD.index = 2
var_0_2.SC_16107_GOOD_LIST_FIELD.label = 3
var_0_2.SC_16107_GOOD_LIST_FIELD.has_default_value = false
var_0_2.SC_16107_GOOD_LIST_FIELD.default_value = {}
var_0_2.SC_16107_GOOD_LIST_FIELD.message_type = GOODS_INFO
var_0_2.SC_16107_GOOD_LIST_FIELD.type = 11
var_0_2.SC_16107_GOOD_LIST_FIELD.cpp_type = 10
SC_16107.name = "sc_16107"
SC_16107.full_name = "p16.sc_16107"
SC_16107.nested_types = {}
SC_16107.enum_types = {}
SC_16107.fields = {
	var_0_2.SC_16107_RESULT_FIELD,
	var_0_2.SC_16107_ITEM_FLASH_TIME_FIELD,
	var_0_2.SC_16107_GOOD_LIST_FIELD
}
SC_16107.is_extendable = false
SC_16107.extensions = {}
var_0_2.CS_16108_FLASH_TIME_FIELD.name = "flash_time"
var_0_2.CS_16108_FLASH_TIME_FIELD.full_name = "p16.cs_16108.flash_time"
var_0_2.CS_16108_FLASH_TIME_FIELD.number = 1
var_0_2.CS_16108_FLASH_TIME_FIELD.index = 0
var_0_2.CS_16108_FLASH_TIME_FIELD.label = 2
var_0_2.CS_16108_FLASH_TIME_FIELD.has_default_value = false
var_0_2.CS_16108_FLASH_TIME_FIELD.default_value = 0
var_0_2.CS_16108_FLASH_TIME_FIELD.type = 13
var_0_2.CS_16108_FLASH_TIME_FIELD.cpp_type = 3
var_0_2.CS_16108_SHOPID_FIELD.name = "shopid"
var_0_2.CS_16108_SHOPID_FIELD.full_name = "p16.cs_16108.shopid"
var_0_2.CS_16108_SHOPID_FIELD.number = 2
var_0_2.CS_16108_SHOPID_FIELD.index = 1
var_0_2.CS_16108_SHOPID_FIELD.label = 2
var_0_2.CS_16108_SHOPID_FIELD.has_default_value = false
var_0_2.CS_16108_SHOPID_FIELD.default_value = 0
var_0_2.CS_16108_SHOPID_FIELD.type = 13
var_0_2.CS_16108_SHOPID_FIELD.cpp_type = 3
var_0_2.CS_16108_SELECTED_FIELD.name = "selected"
var_0_2.CS_16108_SELECTED_FIELD.full_name = "p16.cs_16108.selected"
var_0_2.CS_16108_SELECTED_FIELD.number = 3
var_0_2.CS_16108_SELECTED_FIELD.index = 2
var_0_2.CS_16108_SELECTED_FIELD.label = 3
var_0_2.CS_16108_SELECTED_FIELD.has_default_value = false
var_0_2.CS_16108_SELECTED_FIELD.default_value = {}
var_0_2.CS_16108_SELECTED_FIELD.message_type = SELECTED_INFO
var_0_2.CS_16108_SELECTED_FIELD.type = 11
var_0_2.CS_16108_SELECTED_FIELD.cpp_type = 10
CS_16108.name = "cs_16108"
CS_16108.full_name = "p16.cs_16108"
CS_16108.nested_types = {}
CS_16108.enum_types = {}
CS_16108.fields = {
	var_0_2.CS_16108_FLASH_TIME_FIELD,
	var_0_2.CS_16108_SHOPID_FIELD,
	var_0_2.CS_16108_SELECTED_FIELD
}
CS_16108.is_extendable = false
CS_16108.extensions = {}
var_0_2.SC_16109_RESULT_FIELD.name = "result"
var_0_2.SC_16109_RESULT_FIELD.full_name = "p16.sc_16109.result"
var_0_2.SC_16109_RESULT_FIELD.number = 1
var_0_2.SC_16109_RESULT_FIELD.index = 0
var_0_2.SC_16109_RESULT_FIELD.label = 2
var_0_2.SC_16109_RESULT_FIELD.has_default_value = false
var_0_2.SC_16109_RESULT_FIELD.default_value = 0
var_0_2.SC_16109_RESULT_FIELD.type = 13
var_0_2.SC_16109_RESULT_FIELD.cpp_type = 3
var_0_2.SC_16109_DROP_LIST_FIELD.name = "drop_list"
var_0_2.SC_16109_DROP_LIST_FIELD.full_name = "p16.sc_16109.drop_list"
var_0_2.SC_16109_DROP_LIST_FIELD.number = 2
var_0_2.SC_16109_DROP_LIST_FIELD.index = 1
var_0_2.SC_16109_DROP_LIST_FIELD.label = 3
var_0_2.SC_16109_DROP_LIST_FIELD.has_default_value = false
var_0_2.SC_16109_DROP_LIST_FIELD.default_value = {}
var_0_2.SC_16109_DROP_LIST_FIELD.message_type = var_0_1.DROPINFO
var_0_2.SC_16109_DROP_LIST_FIELD.type = 11
var_0_2.SC_16109_DROP_LIST_FIELD.cpp_type = 10
SC_16109.name = "sc_16109"
SC_16109.full_name = "p16.sc_16109"
SC_16109.nested_types = {}
SC_16109.enum_types = {}
SC_16109.fields = {
	var_0_2.SC_16109_RESULT_FIELD,
	var_0_2.SC_16109_DROP_LIST_FIELD
}
SC_16109.is_extendable = false
SC_16109.extensions = {}
var_0_2.SC_16200_CORE_SHOP_LIST_FIELD.name = "core_shop_list"
var_0_2.SC_16200_CORE_SHOP_LIST_FIELD.full_name = "p16.sc_16200.core_shop_list"
var_0_2.SC_16200_CORE_SHOP_LIST_FIELD.number = 1
var_0_2.SC_16200_CORE_SHOP_LIST_FIELD.index = 0
var_0_2.SC_16200_CORE_SHOP_LIST_FIELD.label = 3
var_0_2.SC_16200_CORE_SHOP_LIST_FIELD.has_default_value = false
var_0_2.SC_16200_CORE_SHOP_LIST_FIELD.default_value = {}
var_0_2.SC_16200_CORE_SHOP_LIST_FIELD.message_type = SHOPINFO
var_0_2.SC_16200_CORE_SHOP_LIST_FIELD.type = 11
var_0_2.SC_16200_CORE_SHOP_LIST_FIELD.cpp_type = 10
var_0_2.SC_16200_BLUE_SHOP_LIST_FIELD.name = "blue_shop_list"
var_0_2.SC_16200_BLUE_SHOP_LIST_FIELD.full_name = "p16.sc_16200.blue_shop_list"
var_0_2.SC_16200_BLUE_SHOP_LIST_FIELD.number = 2
var_0_2.SC_16200_BLUE_SHOP_LIST_FIELD.index = 1
var_0_2.SC_16200_BLUE_SHOP_LIST_FIELD.label = 3
var_0_2.SC_16200_BLUE_SHOP_LIST_FIELD.has_default_value = false
var_0_2.SC_16200_BLUE_SHOP_LIST_FIELD.default_value = {}
var_0_2.SC_16200_BLUE_SHOP_LIST_FIELD.message_type = SHOPINFO
var_0_2.SC_16200_BLUE_SHOP_LIST_FIELD.type = 11
var_0_2.SC_16200_BLUE_SHOP_LIST_FIELD.cpp_type = 10
var_0_2.SC_16200_NORMAL_SHOP_LIST_FIELD.name = "normal_shop_list"
var_0_2.SC_16200_NORMAL_SHOP_LIST_FIELD.full_name = "p16.sc_16200.normal_shop_list"
var_0_2.SC_16200_NORMAL_SHOP_LIST_FIELD.number = 3
var_0_2.SC_16200_NORMAL_SHOP_LIST_FIELD.index = 2
var_0_2.SC_16200_NORMAL_SHOP_LIST_FIELD.label = 3
var_0_2.SC_16200_NORMAL_SHOP_LIST_FIELD.has_default_value = false
var_0_2.SC_16200_NORMAL_SHOP_LIST_FIELD.default_value = {}
var_0_2.SC_16200_NORMAL_SHOP_LIST_FIELD.message_type = SHOPINFO
var_0_2.SC_16200_NORMAL_SHOP_LIST_FIELD.type = 11
var_0_2.SC_16200_NORMAL_SHOP_LIST_FIELD.cpp_type = 10
var_0_2.SC_16200_MONTH_FIELD.name = "month"
var_0_2.SC_16200_MONTH_FIELD.full_name = "p16.sc_16200.month"
var_0_2.SC_16200_MONTH_FIELD.number = 4
var_0_2.SC_16200_MONTH_FIELD.index = 3
var_0_2.SC_16200_MONTH_FIELD.label = 2
var_0_2.SC_16200_MONTH_FIELD.has_default_value = false
var_0_2.SC_16200_MONTH_FIELD.default_value = 0
var_0_2.SC_16200_MONTH_FIELD.type = 13
var_0_2.SC_16200_MONTH_FIELD.cpp_type = 3
SC_16200.name = "sc_16200"
SC_16200.full_name = "p16.sc_16200"
SC_16200.nested_types = {}
SC_16200.enum_types = {}
SC_16200.fields = {
	var_0_2.SC_16200_CORE_SHOP_LIST_FIELD,
	var_0_2.SC_16200_BLUE_SHOP_LIST_FIELD,
	var_0_2.SC_16200_NORMAL_SHOP_LIST_FIELD,
	var_0_2.SC_16200_MONTH_FIELD
}
SC_16200.is_extendable = false
SC_16200.extensions = {}
var_0_2.CS_16201_TYPE_FIELD.name = "type"
var_0_2.CS_16201_TYPE_FIELD.full_name = "p16.cs_16201.type"
var_0_2.CS_16201_TYPE_FIELD.number = 1
var_0_2.CS_16201_TYPE_FIELD.index = 0
var_0_2.CS_16201_TYPE_FIELD.label = 2
var_0_2.CS_16201_TYPE_FIELD.has_default_value = false
var_0_2.CS_16201_TYPE_FIELD.default_value = 0
var_0_2.CS_16201_TYPE_FIELD.type = 13
var_0_2.CS_16201_TYPE_FIELD.cpp_type = 3
var_0_2.CS_16201_ID_FIELD.name = "id"
var_0_2.CS_16201_ID_FIELD.full_name = "p16.cs_16201.id"
var_0_2.CS_16201_ID_FIELD.number = 2
var_0_2.CS_16201_ID_FIELD.index = 1
var_0_2.CS_16201_ID_FIELD.label = 2
var_0_2.CS_16201_ID_FIELD.has_default_value = false
var_0_2.CS_16201_ID_FIELD.default_value = 0
var_0_2.CS_16201_ID_FIELD.type = 13
var_0_2.CS_16201_ID_FIELD.cpp_type = 3
var_0_2.CS_16201_COUNT_FIELD.name = "count"
var_0_2.CS_16201_COUNT_FIELD.full_name = "p16.cs_16201.count"
var_0_2.CS_16201_COUNT_FIELD.number = 3
var_0_2.CS_16201_COUNT_FIELD.index = 2
var_0_2.CS_16201_COUNT_FIELD.label = 2
var_0_2.CS_16201_COUNT_FIELD.has_default_value = false
var_0_2.CS_16201_COUNT_FIELD.default_value = 0
var_0_2.CS_16201_COUNT_FIELD.type = 13
var_0_2.CS_16201_COUNT_FIELD.cpp_type = 3
CS_16201.name = "cs_16201"
CS_16201.full_name = "p16.cs_16201"
CS_16201.nested_types = {}
CS_16201.enum_types = {}
CS_16201.fields = {
	var_0_2.CS_16201_TYPE_FIELD,
	var_0_2.CS_16201_ID_FIELD,
	var_0_2.CS_16201_COUNT_FIELD
}
CS_16201.is_extendable = false
CS_16201.extensions = {}
var_0_2.SC_16202_RESULT_FIELD.name = "result"
var_0_2.SC_16202_RESULT_FIELD.full_name = "p16.sc_16202.result"
var_0_2.SC_16202_RESULT_FIELD.number = 1
var_0_2.SC_16202_RESULT_FIELD.index = 0
var_0_2.SC_16202_RESULT_FIELD.label = 2
var_0_2.SC_16202_RESULT_FIELD.has_default_value = false
var_0_2.SC_16202_RESULT_FIELD.default_value = 0
var_0_2.SC_16202_RESULT_FIELD.type = 13
var_0_2.SC_16202_RESULT_FIELD.cpp_type = 3
var_0_2.SC_16202_DROP_LIST_FIELD.name = "drop_list"
var_0_2.SC_16202_DROP_LIST_FIELD.full_name = "p16.sc_16202.drop_list"
var_0_2.SC_16202_DROP_LIST_FIELD.number = 2
var_0_2.SC_16202_DROP_LIST_FIELD.index = 1
var_0_2.SC_16202_DROP_LIST_FIELD.label = 3
var_0_2.SC_16202_DROP_LIST_FIELD.has_default_value = false
var_0_2.SC_16202_DROP_LIST_FIELD.default_value = {}
var_0_2.SC_16202_DROP_LIST_FIELD.message_type = var_0_1.DROPINFO
var_0_2.SC_16202_DROP_LIST_FIELD.type = 11
var_0_2.SC_16202_DROP_LIST_FIELD.cpp_type = 10
SC_16202.name = "sc_16202"
SC_16202.full_name = "p16.sc_16202"
SC_16202.nested_types = {}
SC_16202.enum_types = {}
SC_16202.fields = {
	var_0_2.SC_16202_RESULT_FIELD,
	var_0_2.SC_16202_DROP_LIST_FIELD
}
SC_16202.is_extendable = false
SC_16202.extensions = {}
var_0_2.CS_16203_FLAG_FIELD.name = "flag"
var_0_2.CS_16203_FLAG_FIELD.full_name = "p16.cs_16203.flag"
var_0_2.CS_16203_FLAG_FIELD.number = 1
var_0_2.CS_16203_FLAG_FIELD.index = 0
var_0_2.CS_16203_FLAG_FIELD.label = 2
var_0_2.CS_16203_FLAG_FIELD.has_default_value = false
var_0_2.CS_16203_FLAG_FIELD.default_value = 0
var_0_2.CS_16203_FLAG_FIELD.type = 13
var_0_2.CS_16203_FLAG_FIELD.cpp_type = 3
CS_16203.name = "cs_16203"
CS_16203.full_name = "p16.cs_16203"
CS_16203.nested_types = {}
CS_16203.enum_types = {}
CS_16203.fields = {
	var_0_2.CS_16203_FLAG_FIELD
}
CS_16203.is_extendable = false
CS_16203.extensions = {}
var_0_2.SC_16204_RET_FIELD.name = "ret"
var_0_2.SC_16204_RET_FIELD.full_name = "p16.sc_16204.ret"
var_0_2.SC_16204_RET_FIELD.number = 1
var_0_2.SC_16204_RET_FIELD.index = 0
var_0_2.SC_16204_RET_FIELD.label = 2
var_0_2.SC_16204_RET_FIELD.has_default_value = false
var_0_2.SC_16204_RET_FIELD.default_value = 0
var_0_2.SC_16204_RET_FIELD.type = 13
var_0_2.SC_16204_RET_FIELD.cpp_type = 3
SC_16204.name = "sc_16204"
SC_16204.full_name = "p16.sc_16204"
SC_16204.nested_types = {}
SC_16204.enum_types = {}
SC_16204.fields = {
	var_0_2.SC_16204_RET_FIELD
}
SC_16204.is_extendable = false
SC_16204.extensions = {}
var_0_2.CS_16205_ID_FIELD.name = "id"
var_0_2.CS_16205_ID_FIELD.full_name = "p16.cs_16205.id"
var_0_2.CS_16205_ID_FIELD.number = 1
var_0_2.CS_16205_ID_FIELD.index = 0
var_0_2.CS_16205_ID_FIELD.label = 2
var_0_2.CS_16205_ID_FIELD.has_default_value = false
var_0_2.CS_16205_ID_FIELD.default_value = 0
var_0_2.CS_16205_ID_FIELD.type = 13
var_0_2.CS_16205_ID_FIELD.cpp_type = 3
var_0_2.CS_16205_COST_TYPE_FIELD.name = "cost_type"
var_0_2.CS_16205_COST_TYPE_FIELD.full_name = "p16.cs_16205.cost_type"
var_0_2.CS_16205_COST_TYPE_FIELD.number = 2
var_0_2.CS_16205_COST_TYPE_FIELD.index = 1
var_0_2.CS_16205_COST_TYPE_FIELD.label = 2
var_0_2.CS_16205_COST_TYPE_FIELD.has_default_value = false
var_0_2.CS_16205_COST_TYPE_FIELD.default_value = 0
var_0_2.CS_16205_COST_TYPE_FIELD.type = 13
var_0_2.CS_16205_COST_TYPE_FIELD.cpp_type = 3
CS_16205.name = "cs_16205"
CS_16205.full_name = "p16.cs_16205"
CS_16205.nested_types = {}
CS_16205.enum_types = {}
CS_16205.fields = {
	var_0_2.CS_16205_ID_FIELD,
	var_0_2.CS_16205_COST_TYPE_FIELD
}
CS_16205.is_extendable = false
CS_16205.extensions = {}
var_0_2.SC_16206_RET_FIELD.name = "ret"
var_0_2.SC_16206_RET_FIELD.full_name = "p16.sc_16206.ret"
var_0_2.SC_16206_RET_FIELD.number = 1
var_0_2.SC_16206_RET_FIELD.index = 0
var_0_2.SC_16206_RET_FIELD.label = 2
var_0_2.SC_16206_RET_FIELD.has_default_value = false
var_0_2.SC_16206_RET_FIELD.default_value = 0
var_0_2.SC_16206_RET_FIELD.type = 13
var_0_2.SC_16206_RET_FIELD.cpp_type = 3
SC_16206.name = "sc_16206"
SC_16206.full_name = "p16.sc_16206"
SC_16206.nested_types = {}
SC_16206.enum_types = {}
SC_16206.fields = {
	var_0_2.SC_16206_RET_FIELD
}
SC_16206.is_extendable = false
SC_16206.extensions = {}
var_0_2.SHOPINFO_SHOP_ID_FIELD.name = "shop_id"
var_0_2.SHOPINFO_SHOP_ID_FIELD.full_name = "p16.shopinfo.shop_id"
var_0_2.SHOPINFO_SHOP_ID_FIELD.number = 1
var_0_2.SHOPINFO_SHOP_ID_FIELD.index = 0
var_0_2.SHOPINFO_SHOP_ID_FIELD.label = 2
var_0_2.SHOPINFO_SHOP_ID_FIELD.has_default_value = false
var_0_2.SHOPINFO_SHOP_ID_FIELD.default_value = 0
var_0_2.SHOPINFO_SHOP_ID_FIELD.type = 13
var_0_2.SHOPINFO_SHOP_ID_FIELD.cpp_type = 3
var_0_2.SHOPINFO_PAY_COUNT_FIELD.name = "pay_count"
var_0_2.SHOPINFO_PAY_COUNT_FIELD.full_name = "p16.shopinfo.pay_count"
var_0_2.SHOPINFO_PAY_COUNT_FIELD.number = 2
var_0_2.SHOPINFO_PAY_COUNT_FIELD.index = 1
var_0_2.SHOPINFO_PAY_COUNT_FIELD.label = 2
var_0_2.SHOPINFO_PAY_COUNT_FIELD.has_default_value = false
var_0_2.SHOPINFO_PAY_COUNT_FIELD.default_value = 0
var_0_2.SHOPINFO_PAY_COUNT_FIELD.type = 13
var_0_2.SHOPINFO_PAY_COUNT_FIELD.cpp_type = 3
SHOPINFO.name = "shopinfo"
SHOPINFO.full_name = "p16.shopinfo"
SHOPINFO.nested_types = {}
SHOPINFO.enum_types = {}
SHOPINFO.fields = {
	var_0_2.SHOPINFO_SHOP_ID_FIELD,
	var_0_2.SHOPINFO_PAY_COUNT_FIELD
}
SHOPINFO.is_extendable = false
SHOPINFO.extensions = {}
var_0_2.GOODS_INFO_ID_FIELD.name = "id"
var_0_2.GOODS_INFO_ID_FIELD.full_name = "p16.goods_info.id"
var_0_2.GOODS_INFO_ID_FIELD.number = 1
var_0_2.GOODS_INFO_ID_FIELD.index = 0
var_0_2.GOODS_INFO_ID_FIELD.label = 2
var_0_2.GOODS_INFO_ID_FIELD.has_default_value = false
var_0_2.GOODS_INFO_ID_FIELD.default_value = 0
var_0_2.GOODS_INFO_ID_FIELD.type = 13
var_0_2.GOODS_INFO_ID_FIELD.cpp_type = 3
var_0_2.GOODS_INFO_COUNT_FIELD.name = "count"
var_0_2.GOODS_INFO_COUNT_FIELD.full_name = "p16.goods_info.count"
var_0_2.GOODS_INFO_COUNT_FIELD.number = 2
var_0_2.GOODS_INFO_COUNT_FIELD.index = 1
var_0_2.GOODS_INFO_COUNT_FIELD.label = 2
var_0_2.GOODS_INFO_COUNT_FIELD.has_default_value = false
var_0_2.GOODS_INFO_COUNT_FIELD.default_value = 0
var_0_2.GOODS_INFO_COUNT_FIELD.type = 13
var_0_2.GOODS_INFO_COUNT_FIELD.cpp_type = 3
GOODS_INFO.name = "goods_info"
GOODS_INFO.full_name = "p16.goods_info"
GOODS_INFO.nested_types = {}
GOODS_INFO.enum_types = {}
GOODS_INFO.fields = {
	var_0_2.GOODS_INFO_ID_FIELD,
	var_0_2.GOODS_INFO_COUNT_FIELD
}
GOODS_INFO.is_extendable = false
GOODS_INFO.extensions = {}
var_0_2.SELECTED_INFO_ID_FIELD.name = "id"
var_0_2.SELECTED_INFO_ID_FIELD.full_name = "p16.selected_info.id"
var_0_2.SELECTED_INFO_ID_FIELD.number = 1
var_0_2.SELECTED_INFO_ID_FIELD.index = 0
var_0_2.SELECTED_INFO_ID_FIELD.label = 2
var_0_2.SELECTED_INFO_ID_FIELD.has_default_value = false
var_0_2.SELECTED_INFO_ID_FIELD.default_value = 0
var_0_2.SELECTED_INFO_ID_FIELD.type = 13
var_0_2.SELECTED_INFO_ID_FIELD.cpp_type = 3
var_0_2.SELECTED_INFO_COUNT_FIELD.name = "count"
var_0_2.SELECTED_INFO_COUNT_FIELD.full_name = "p16.selected_info.count"
var_0_2.SELECTED_INFO_COUNT_FIELD.number = 2
var_0_2.SELECTED_INFO_COUNT_FIELD.index = 1
var_0_2.SELECTED_INFO_COUNT_FIELD.label = 2
var_0_2.SELECTED_INFO_COUNT_FIELD.has_default_value = false
var_0_2.SELECTED_INFO_COUNT_FIELD.default_value = 0
var_0_2.SELECTED_INFO_COUNT_FIELD.type = 13
var_0_2.SELECTED_INFO_COUNT_FIELD.cpp_type = 3
SELECTED_INFO.name = "selected_info"
SELECTED_INFO.full_name = "p16.selected_info"
SELECTED_INFO.nested_types = {}
SELECTED_INFO.enum_types = {}
SELECTED_INFO.fields = {
	var_0_2.SELECTED_INFO_ID_FIELD,
	var_0_2.SELECTED_INFO_COUNT_FIELD
}
SELECTED_INFO.is_extendable = false
SELECTED_INFO.extensions = {}
cs_16001 = var_0_0.Message(CS_16001)
cs_16100 = var_0_0.Message(CS_16100)
cs_16104 = var_0_0.Message(CS_16104)
cs_16106 = var_0_0.Message(CS_16106)
cs_16108 = var_0_0.Message(CS_16108)
cs_16201 = var_0_0.Message(CS_16201)
cs_16203 = var_0_0.Message(CS_16203)
cs_16205 = var_0_0.Message(CS_16205)
goods_info = var_0_0.Message(GOODS_INFO)
sc_16002 = var_0_0.Message(SC_16002)
sc_16101 = var_0_0.Message(SC_16101)
sc_16105 = var_0_0.Message(SC_16105)
sc_16107 = var_0_0.Message(SC_16107)
sc_16109 = var_0_0.Message(SC_16109)
sc_16200 = var_0_0.Message(SC_16200)
sc_16202 = var_0_0.Message(SC_16202)
sc_16204 = var_0_0.Message(SC_16204)
sc_16206 = var_0_0.Message(SC_16206)
selected_info = var_0_0.Message(SELECTED_INFO)
shopinfo = var_0_0.Message(SHOPINFO)
