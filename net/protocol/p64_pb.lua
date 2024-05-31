﻿local var_0_0 = require("protobuf")
local var_0_1 = require("common_pb")

module("p64_pb")

local var_0_2 = {}

SC_64000 = var_0_0.Descriptor()
var_0_2.SC_64000_TECH_LIST_FIELD = var_0_0.FieldDescriptor()
var_0_2.SC_64000_TECHSET_LIST_FIELD = var_0_0.FieldDescriptor()
CS_64001 = var_0_0.Descriptor()
var_0_2.CS_64001_TECH_GROUP_ID_FIELD = var_0_0.FieldDescriptor()
var_0_2.CS_64001_TECH_ID_FIELD = var_0_0.FieldDescriptor()
SC_64002 = var_0_0.Descriptor()
var_0_2.SC_64002_RESULT_FIELD = var_0_0.FieldDescriptor()
CS_64003 = var_0_0.Descriptor()
var_0_2.CS_64003_TECH_GROUP_ID_FIELD = var_0_0.FieldDescriptor()
SC_64004 = var_0_0.Descriptor()
var_0_2.SC_64004_RESULT_FIELD = var_0_0.FieldDescriptor()
CS_64005 = var_0_0.Descriptor()
var_0_2.CS_64005_GROUP_ID_FIELD = var_0_0.FieldDescriptor()
var_0_2.CS_64005_TECH_ID_FIELD = var_0_0.FieldDescriptor()
SC_64006 = var_0_0.Descriptor()
var_0_2.SC_64006_RESULT_FIELD = var_0_0.FieldDescriptor()
var_0_2.SC_64006_REWARDS_FIELD = var_0_0.FieldDescriptor()
CS_64007 = var_0_0.Descriptor()
var_0_2.CS_64007_TYPE_FIELD = var_0_0.FieldDescriptor()
SC_64008 = var_0_0.Descriptor()
var_0_2.SC_64008_RESULT_FIELD = var_0_0.FieldDescriptor()
var_0_2.SC_64008_REWARDS_FIELD = var_0_0.FieldDescriptor()
CS_64009 = var_0_0.Descriptor()
var_0_2.CS_64009_TECHSET_LIST_FIELD = var_0_0.FieldDescriptor()
SC_64010 = var_0_0.Descriptor()
var_0_2.SC_64010_RESULT_FIELD = var_0_0.FieldDescriptor()
FLEETTECH = var_0_0.Descriptor()
var_0_2.FLEETTECH_GROUP_ID_FIELD = var_0_0.FieldDescriptor()
var_0_2.FLEETTECH_EFFECT_TECH_ID_FIELD = var_0_0.FieldDescriptor()
var_0_2.FLEETTECH_STUDY_TECH_ID_FIELD = var_0_0.FieldDescriptor()
var_0_2.FLEETTECH_STUDY_FINISH_TIME_FIELD = var_0_0.FieldDescriptor()
var_0_2.FLEETTECH_REWARDED_TECH_FIELD = var_0_0.FieldDescriptor()
TECHSET = var_0_0.Descriptor()
var_0_2.TECHSET_SHIP_TYPE_FIELD = var_0_0.FieldDescriptor()
var_0_2.TECHSET_ATTR_TYPE_FIELD = var_0_0.FieldDescriptor()
var_0_2.TECHSET_SET_VALUE_FIELD = var_0_0.FieldDescriptor()
var_0_2.SC_64000_TECH_LIST_FIELD.name = "tech_list"
var_0_2.SC_64000_TECH_LIST_FIELD.full_name = "p64.sc_64000.tech_list"
var_0_2.SC_64000_TECH_LIST_FIELD.number = 1
var_0_2.SC_64000_TECH_LIST_FIELD.index = 0
var_0_2.SC_64000_TECH_LIST_FIELD.label = 3
var_0_2.SC_64000_TECH_LIST_FIELD.has_default_value = false
var_0_2.SC_64000_TECH_LIST_FIELD.default_value = {}
var_0_2.SC_64000_TECH_LIST_FIELD.message_type = FLEETTECH
var_0_2.SC_64000_TECH_LIST_FIELD.type = 11
var_0_2.SC_64000_TECH_LIST_FIELD.cpp_type = 10
var_0_2.SC_64000_TECHSET_LIST_FIELD.name = "techset_list"
var_0_2.SC_64000_TECHSET_LIST_FIELD.full_name = "p64.sc_64000.techset_list"
var_0_2.SC_64000_TECHSET_LIST_FIELD.number = 2
var_0_2.SC_64000_TECHSET_LIST_FIELD.index = 1
var_0_2.SC_64000_TECHSET_LIST_FIELD.label = 3
var_0_2.SC_64000_TECHSET_LIST_FIELD.has_default_value = false
var_0_2.SC_64000_TECHSET_LIST_FIELD.default_value = {}
var_0_2.SC_64000_TECHSET_LIST_FIELD.message_type = TECHSET
var_0_2.SC_64000_TECHSET_LIST_FIELD.type = 11
var_0_2.SC_64000_TECHSET_LIST_FIELD.cpp_type = 10
SC_64000.name = "sc_64000"
SC_64000.full_name = "p64.sc_64000"
SC_64000.nested_types = {}
SC_64000.enum_types = {}
SC_64000.fields = {
	var_0_2.SC_64000_TECH_LIST_FIELD,
	var_0_2.SC_64000_TECHSET_LIST_FIELD
}
SC_64000.is_extendable = false
SC_64000.extensions = {}
var_0_2.CS_64001_TECH_GROUP_ID_FIELD.name = "tech_group_id"
var_0_2.CS_64001_TECH_GROUP_ID_FIELD.full_name = "p64.cs_64001.tech_group_id"
var_0_2.CS_64001_TECH_GROUP_ID_FIELD.number = 1
var_0_2.CS_64001_TECH_GROUP_ID_FIELD.index = 0
var_0_2.CS_64001_TECH_GROUP_ID_FIELD.label = 2
var_0_2.CS_64001_TECH_GROUP_ID_FIELD.has_default_value = false
var_0_2.CS_64001_TECH_GROUP_ID_FIELD.default_value = 0
var_0_2.CS_64001_TECH_GROUP_ID_FIELD.type = 13
var_0_2.CS_64001_TECH_GROUP_ID_FIELD.cpp_type = 3
var_0_2.CS_64001_TECH_ID_FIELD.name = "tech_id"
var_0_2.CS_64001_TECH_ID_FIELD.full_name = "p64.cs_64001.tech_id"
var_0_2.CS_64001_TECH_ID_FIELD.number = 2
var_0_2.CS_64001_TECH_ID_FIELD.index = 1
var_0_2.CS_64001_TECH_ID_FIELD.label = 2
var_0_2.CS_64001_TECH_ID_FIELD.has_default_value = false
var_0_2.CS_64001_TECH_ID_FIELD.default_value = 0
var_0_2.CS_64001_TECH_ID_FIELD.type = 13
var_0_2.CS_64001_TECH_ID_FIELD.cpp_type = 3
CS_64001.name = "cs_64001"
CS_64001.full_name = "p64.cs_64001"
CS_64001.nested_types = {}
CS_64001.enum_types = {}
CS_64001.fields = {
	var_0_2.CS_64001_TECH_GROUP_ID_FIELD,
	var_0_2.CS_64001_TECH_ID_FIELD
}
CS_64001.is_extendable = false
CS_64001.extensions = {}
var_0_2.SC_64002_RESULT_FIELD.name = "result"
var_0_2.SC_64002_RESULT_FIELD.full_name = "p64.sc_64002.result"
var_0_2.SC_64002_RESULT_FIELD.number = 1
var_0_2.SC_64002_RESULT_FIELD.index = 0
var_0_2.SC_64002_RESULT_FIELD.label = 2
var_0_2.SC_64002_RESULT_FIELD.has_default_value = false
var_0_2.SC_64002_RESULT_FIELD.default_value = 0
var_0_2.SC_64002_RESULT_FIELD.type = 13
var_0_2.SC_64002_RESULT_FIELD.cpp_type = 3
SC_64002.name = "sc_64002"
SC_64002.full_name = "p64.sc_64002"
SC_64002.nested_types = {}
SC_64002.enum_types = {}
SC_64002.fields = {
	var_0_2.SC_64002_RESULT_FIELD
}
SC_64002.is_extendable = false
SC_64002.extensions = {}
var_0_2.CS_64003_TECH_GROUP_ID_FIELD.name = "tech_group_id"
var_0_2.CS_64003_TECH_GROUP_ID_FIELD.full_name = "p64.cs_64003.tech_group_id"
var_0_2.CS_64003_TECH_GROUP_ID_FIELD.number = 1
var_0_2.CS_64003_TECH_GROUP_ID_FIELD.index = 0
var_0_2.CS_64003_TECH_GROUP_ID_FIELD.label = 2
var_0_2.CS_64003_TECH_GROUP_ID_FIELD.has_default_value = false
var_0_2.CS_64003_TECH_GROUP_ID_FIELD.default_value = 0
var_0_2.CS_64003_TECH_GROUP_ID_FIELD.type = 13
var_0_2.CS_64003_TECH_GROUP_ID_FIELD.cpp_type = 3
CS_64003.name = "cs_64003"
CS_64003.full_name = "p64.cs_64003"
CS_64003.nested_types = {}
CS_64003.enum_types = {}
CS_64003.fields = {
	var_0_2.CS_64003_TECH_GROUP_ID_FIELD
}
CS_64003.is_extendable = false
CS_64003.extensions = {}
var_0_2.SC_64004_RESULT_FIELD.name = "result"
var_0_2.SC_64004_RESULT_FIELD.full_name = "p64.sc_64004.result"
var_0_2.SC_64004_RESULT_FIELD.number = 1
var_0_2.SC_64004_RESULT_FIELD.index = 0
var_0_2.SC_64004_RESULT_FIELD.label = 2
var_0_2.SC_64004_RESULT_FIELD.has_default_value = false
var_0_2.SC_64004_RESULT_FIELD.default_value = 0
var_0_2.SC_64004_RESULT_FIELD.type = 13
var_0_2.SC_64004_RESULT_FIELD.cpp_type = 3
SC_64004.name = "sc_64004"
SC_64004.full_name = "p64.sc_64004"
SC_64004.nested_types = {}
SC_64004.enum_types = {}
SC_64004.fields = {
	var_0_2.SC_64004_RESULT_FIELD
}
SC_64004.is_extendable = false
SC_64004.extensions = {}
var_0_2.CS_64005_GROUP_ID_FIELD.name = "group_id"
var_0_2.CS_64005_GROUP_ID_FIELD.full_name = "p64.cs_64005.group_id"
var_0_2.CS_64005_GROUP_ID_FIELD.number = 1
var_0_2.CS_64005_GROUP_ID_FIELD.index = 0
var_0_2.CS_64005_GROUP_ID_FIELD.label = 2
var_0_2.CS_64005_GROUP_ID_FIELD.has_default_value = false
var_0_2.CS_64005_GROUP_ID_FIELD.default_value = 0
var_0_2.CS_64005_GROUP_ID_FIELD.type = 13
var_0_2.CS_64005_GROUP_ID_FIELD.cpp_type = 3
var_0_2.CS_64005_TECH_ID_FIELD.name = "tech_id"
var_0_2.CS_64005_TECH_ID_FIELD.full_name = "p64.cs_64005.tech_id"
var_0_2.CS_64005_TECH_ID_FIELD.number = 2
var_0_2.CS_64005_TECH_ID_FIELD.index = 1
var_0_2.CS_64005_TECH_ID_FIELD.label = 2
var_0_2.CS_64005_TECH_ID_FIELD.has_default_value = false
var_0_2.CS_64005_TECH_ID_FIELD.default_value = 0
var_0_2.CS_64005_TECH_ID_FIELD.type = 13
var_0_2.CS_64005_TECH_ID_FIELD.cpp_type = 3
CS_64005.name = "cs_64005"
CS_64005.full_name = "p64.cs_64005"
CS_64005.nested_types = {}
CS_64005.enum_types = {}
CS_64005.fields = {
	var_0_2.CS_64005_GROUP_ID_FIELD,
	var_0_2.CS_64005_TECH_ID_FIELD
}
CS_64005.is_extendable = false
CS_64005.extensions = {}
var_0_2.SC_64006_RESULT_FIELD.name = "result"
var_0_2.SC_64006_RESULT_FIELD.full_name = "p64.sc_64006.result"
var_0_2.SC_64006_RESULT_FIELD.number = 1
var_0_2.SC_64006_RESULT_FIELD.index = 0
var_0_2.SC_64006_RESULT_FIELD.label = 2
var_0_2.SC_64006_RESULT_FIELD.has_default_value = false
var_0_2.SC_64006_RESULT_FIELD.default_value = 0
var_0_2.SC_64006_RESULT_FIELD.type = 13
var_0_2.SC_64006_RESULT_FIELD.cpp_type = 3
var_0_2.SC_64006_REWARDS_FIELD.name = "rewards"
var_0_2.SC_64006_REWARDS_FIELD.full_name = "p64.sc_64006.rewards"
var_0_2.SC_64006_REWARDS_FIELD.number = 2
var_0_2.SC_64006_REWARDS_FIELD.index = 1
var_0_2.SC_64006_REWARDS_FIELD.label = 3
var_0_2.SC_64006_REWARDS_FIELD.has_default_value = false
var_0_2.SC_64006_REWARDS_FIELD.default_value = {}
var_0_2.SC_64006_REWARDS_FIELD.message_type = var_0_1.DROPINFO
var_0_2.SC_64006_REWARDS_FIELD.type = 11
var_0_2.SC_64006_REWARDS_FIELD.cpp_type = 10
SC_64006.name = "sc_64006"
SC_64006.full_name = "p64.sc_64006"
SC_64006.nested_types = {}
SC_64006.enum_types = {}
SC_64006.fields = {
	var_0_2.SC_64006_RESULT_FIELD,
	var_0_2.SC_64006_REWARDS_FIELD
}
SC_64006.is_extendable = false
SC_64006.extensions = {}
var_0_2.CS_64007_TYPE_FIELD.name = "type"
var_0_2.CS_64007_TYPE_FIELD.full_name = "p64.cs_64007.type"
var_0_2.CS_64007_TYPE_FIELD.number = 1
var_0_2.CS_64007_TYPE_FIELD.index = 0
var_0_2.CS_64007_TYPE_FIELD.label = 2
var_0_2.CS_64007_TYPE_FIELD.has_default_value = false
var_0_2.CS_64007_TYPE_FIELD.default_value = 0
var_0_2.CS_64007_TYPE_FIELD.type = 13
var_0_2.CS_64007_TYPE_FIELD.cpp_type = 3
CS_64007.name = "cs_64007"
CS_64007.full_name = "p64.cs_64007"
CS_64007.nested_types = {}
CS_64007.enum_types = {}
CS_64007.fields = {
	var_0_2.CS_64007_TYPE_FIELD
}
CS_64007.is_extendable = false
CS_64007.extensions = {}
var_0_2.SC_64008_RESULT_FIELD.name = "result"
var_0_2.SC_64008_RESULT_FIELD.full_name = "p64.sc_64008.result"
var_0_2.SC_64008_RESULT_FIELD.number = 1
var_0_2.SC_64008_RESULT_FIELD.index = 0
var_0_2.SC_64008_RESULT_FIELD.label = 2
var_0_2.SC_64008_RESULT_FIELD.has_default_value = false
var_0_2.SC_64008_RESULT_FIELD.default_value = 0
var_0_2.SC_64008_RESULT_FIELD.type = 13
var_0_2.SC_64008_RESULT_FIELD.cpp_type = 3
var_0_2.SC_64008_REWARDS_FIELD.name = "rewards"
var_0_2.SC_64008_REWARDS_FIELD.full_name = "p64.sc_64008.rewards"
var_0_2.SC_64008_REWARDS_FIELD.number = 2
var_0_2.SC_64008_REWARDS_FIELD.index = 1
var_0_2.SC_64008_REWARDS_FIELD.label = 3
var_0_2.SC_64008_REWARDS_FIELD.has_default_value = false
var_0_2.SC_64008_REWARDS_FIELD.default_value = {}
var_0_2.SC_64008_REWARDS_FIELD.message_type = var_0_1.DROPINFO
var_0_2.SC_64008_REWARDS_FIELD.type = 11
var_0_2.SC_64008_REWARDS_FIELD.cpp_type = 10
SC_64008.name = "sc_64008"
SC_64008.full_name = "p64.sc_64008"
SC_64008.nested_types = {}
SC_64008.enum_types = {}
SC_64008.fields = {
	var_0_2.SC_64008_RESULT_FIELD,
	var_0_2.SC_64008_REWARDS_FIELD
}
SC_64008.is_extendable = false
SC_64008.extensions = {}
var_0_2.CS_64009_TECHSET_LIST_FIELD.name = "techset_list"
var_0_2.CS_64009_TECHSET_LIST_FIELD.full_name = "p64.cs_64009.techset_list"
var_0_2.CS_64009_TECHSET_LIST_FIELD.number = 1
var_0_2.CS_64009_TECHSET_LIST_FIELD.index = 0
var_0_2.CS_64009_TECHSET_LIST_FIELD.label = 3
var_0_2.CS_64009_TECHSET_LIST_FIELD.has_default_value = false
var_0_2.CS_64009_TECHSET_LIST_FIELD.default_value = {}
var_0_2.CS_64009_TECHSET_LIST_FIELD.message_type = TECHSET
var_0_2.CS_64009_TECHSET_LIST_FIELD.type = 11
var_0_2.CS_64009_TECHSET_LIST_FIELD.cpp_type = 10
CS_64009.name = "cs_64009"
CS_64009.full_name = "p64.cs_64009"
CS_64009.nested_types = {}
CS_64009.enum_types = {}
CS_64009.fields = {
	var_0_2.CS_64009_TECHSET_LIST_FIELD
}
CS_64009.is_extendable = false
CS_64009.extensions = {}
var_0_2.SC_64010_RESULT_FIELD.name = "result"
var_0_2.SC_64010_RESULT_FIELD.full_name = "p64.sc_64010.result"
var_0_2.SC_64010_RESULT_FIELD.number = 1
var_0_2.SC_64010_RESULT_FIELD.index = 0
var_0_2.SC_64010_RESULT_FIELD.label = 2
var_0_2.SC_64010_RESULT_FIELD.has_default_value = false
var_0_2.SC_64010_RESULT_FIELD.default_value = 0
var_0_2.SC_64010_RESULT_FIELD.type = 13
var_0_2.SC_64010_RESULT_FIELD.cpp_type = 3
SC_64010.name = "sc_64010"
SC_64010.full_name = "p64.sc_64010"
SC_64010.nested_types = {}
SC_64010.enum_types = {}
SC_64010.fields = {
	var_0_2.SC_64010_RESULT_FIELD
}
SC_64010.is_extendable = false
SC_64010.extensions = {}
var_0_2.FLEETTECH_GROUP_ID_FIELD.name = "group_id"
var_0_2.FLEETTECH_GROUP_ID_FIELD.full_name = "p64.fleettech.group_id"
var_0_2.FLEETTECH_GROUP_ID_FIELD.number = 1
var_0_2.FLEETTECH_GROUP_ID_FIELD.index = 0
var_0_2.FLEETTECH_GROUP_ID_FIELD.label = 2
var_0_2.FLEETTECH_GROUP_ID_FIELD.has_default_value = false
var_0_2.FLEETTECH_GROUP_ID_FIELD.default_value = 0
var_0_2.FLEETTECH_GROUP_ID_FIELD.type = 13
var_0_2.FLEETTECH_GROUP_ID_FIELD.cpp_type = 3
var_0_2.FLEETTECH_EFFECT_TECH_ID_FIELD.name = "effect_tech_id"
var_0_2.FLEETTECH_EFFECT_TECH_ID_FIELD.full_name = "p64.fleettech.effect_tech_id"
var_0_2.FLEETTECH_EFFECT_TECH_ID_FIELD.number = 2
var_0_2.FLEETTECH_EFFECT_TECH_ID_FIELD.index = 1
var_0_2.FLEETTECH_EFFECT_TECH_ID_FIELD.label = 2
var_0_2.FLEETTECH_EFFECT_TECH_ID_FIELD.has_default_value = false
var_0_2.FLEETTECH_EFFECT_TECH_ID_FIELD.default_value = 0
var_0_2.FLEETTECH_EFFECT_TECH_ID_FIELD.type = 13
var_0_2.FLEETTECH_EFFECT_TECH_ID_FIELD.cpp_type = 3
var_0_2.FLEETTECH_STUDY_TECH_ID_FIELD.name = "study_tech_id"
var_0_2.FLEETTECH_STUDY_TECH_ID_FIELD.full_name = "p64.fleettech.study_tech_id"
var_0_2.FLEETTECH_STUDY_TECH_ID_FIELD.number = 3
var_0_2.FLEETTECH_STUDY_TECH_ID_FIELD.index = 2
var_0_2.FLEETTECH_STUDY_TECH_ID_FIELD.label = 2
var_0_2.FLEETTECH_STUDY_TECH_ID_FIELD.has_default_value = false
var_0_2.FLEETTECH_STUDY_TECH_ID_FIELD.default_value = 0
var_0_2.FLEETTECH_STUDY_TECH_ID_FIELD.type = 13
var_0_2.FLEETTECH_STUDY_TECH_ID_FIELD.cpp_type = 3
var_0_2.FLEETTECH_STUDY_FINISH_TIME_FIELD.name = "study_finish_time"
var_0_2.FLEETTECH_STUDY_FINISH_TIME_FIELD.full_name = "p64.fleettech.study_finish_time"
var_0_2.FLEETTECH_STUDY_FINISH_TIME_FIELD.number = 4
var_0_2.FLEETTECH_STUDY_FINISH_TIME_FIELD.index = 3
var_0_2.FLEETTECH_STUDY_FINISH_TIME_FIELD.label = 2
var_0_2.FLEETTECH_STUDY_FINISH_TIME_FIELD.has_default_value = false
var_0_2.FLEETTECH_STUDY_FINISH_TIME_FIELD.default_value = 0
var_0_2.FLEETTECH_STUDY_FINISH_TIME_FIELD.type = 13
var_0_2.FLEETTECH_STUDY_FINISH_TIME_FIELD.cpp_type = 3
var_0_2.FLEETTECH_REWARDED_TECH_FIELD.name = "rewarded_tech"
var_0_2.FLEETTECH_REWARDED_TECH_FIELD.full_name = "p64.fleettech.rewarded_tech"
var_0_2.FLEETTECH_REWARDED_TECH_FIELD.number = 5
var_0_2.FLEETTECH_REWARDED_TECH_FIELD.index = 4
var_0_2.FLEETTECH_REWARDED_TECH_FIELD.label = 2
var_0_2.FLEETTECH_REWARDED_TECH_FIELD.has_default_value = false
var_0_2.FLEETTECH_REWARDED_TECH_FIELD.default_value = 0
var_0_2.FLEETTECH_REWARDED_TECH_FIELD.type = 13
var_0_2.FLEETTECH_REWARDED_TECH_FIELD.cpp_type = 3
FLEETTECH.name = "fleettech"
FLEETTECH.full_name = "p64.fleettech"
FLEETTECH.nested_types = {}
FLEETTECH.enum_types = {}
FLEETTECH.fields = {
	var_0_2.FLEETTECH_GROUP_ID_FIELD,
	var_0_2.FLEETTECH_EFFECT_TECH_ID_FIELD,
	var_0_2.FLEETTECH_STUDY_TECH_ID_FIELD,
	var_0_2.FLEETTECH_STUDY_FINISH_TIME_FIELD,
	var_0_2.FLEETTECH_REWARDED_TECH_FIELD
}
FLEETTECH.is_extendable = false
FLEETTECH.extensions = {}
var_0_2.TECHSET_SHIP_TYPE_FIELD.name = "ship_type"
var_0_2.TECHSET_SHIP_TYPE_FIELD.full_name = "p64.techset.ship_type"
var_0_2.TECHSET_SHIP_TYPE_FIELD.number = 1
var_0_2.TECHSET_SHIP_TYPE_FIELD.index = 0
var_0_2.TECHSET_SHIP_TYPE_FIELD.label = 2
var_0_2.TECHSET_SHIP_TYPE_FIELD.has_default_value = false
var_0_2.TECHSET_SHIP_TYPE_FIELD.default_value = 0
var_0_2.TECHSET_SHIP_TYPE_FIELD.type = 13
var_0_2.TECHSET_SHIP_TYPE_FIELD.cpp_type = 3
var_0_2.TECHSET_ATTR_TYPE_FIELD.name = "attr_type"
var_0_2.TECHSET_ATTR_TYPE_FIELD.full_name = "p64.techset.attr_type"
var_0_2.TECHSET_ATTR_TYPE_FIELD.number = 2
var_0_2.TECHSET_ATTR_TYPE_FIELD.index = 1
var_0_2.TECHSET_ATTR_TYPE_FIELD.label = 2
var_0_2.TECHSET_ATTR_TYPE_FIELD.has_default_value = false
var_0_2.TECHSET_ATTR_TYPE_FIELD.default_value = 0
var_0_2.TECHSET_ATTR_TYPE_FIELD.type = 13
var_0_2.TECHSET_ATTR_TYPE_FIELD.cpp_type = 3
var_0_2.TECHSET_SET_VALUE_FIELD.name = "set_value"
var_0_2.TECHSET_SET_VALUE_FIELD.full_name = "p64.techset.set_value"
var_0_2.TECHSET_SET_VALUE_FIELD.number = 3
var_0_2.TECHSET_SET_VALUE_FIELD.index = 2
var_0_2.TECHSET_SET_VALUE_FIELD.label = 2
var_0_2.TECHSET_SET_VALUE_FIELD.has_default_value = false
var_0_2.TECHSET_SET_VALUE_FIELD.default_value = 0
var_0_2.TECHSET_SET_VALUE_FIELD.type = 13
var_0_2.TECHSET_SET_VALUE_FIELD.cpp_type = 3
TECHSET.name = "techset"
TECHSET.full_name = "p64.techset"
TECHSET.nested_types = {}
TECHSET.enum_types = {}
TECHSET.fields = {
	var_0_2.TECHSET_SHIP_TYPE_FIELD,
	var_0_2.TECHSET_ATTR_TYPE_FIELD,
	var_0_2.TECHSET_SET_VALUE_FIELD
}
TECHSET.is_extendable = false
TECHSET.extensions = {}
cs_64001 = var_0_0.Message(CS_64001)
cs_64003 = var_0_0.Message(CS_64003)
cs_64005 = var_0_0.Message(CS_64005)
cs_64007 = var_0_0.Message(CS_64007)
cs_64009 = var_0_0.Message(CS_64009)
fleettech = var_0_0.Message(FLEETTECH)
sc_64000 = var_0_0.Message(SC_64000)
sc_64002 = var_0_0.Message(SC_64002)
sc_64004 = var_0_0.Message(SC_64004)
sc_64006 = var_0_0.Message(SC_64006)
sc_64008 = var_0_0.Message(SC_64008)
sc_64010 = var_0_0.Message(SC_64010)
techset = var_0_0.Message(TECHSET)
