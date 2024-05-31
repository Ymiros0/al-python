﻿local var_0_0 = require("protobuf")

module("guild_pb")

local var_0_1 = {}

CAPITAL_LOG = var_0_0.Descriptor()
var_0_1.CAPITAL_LOG_MEMBER_ID_FIELD = var_0_0.FieldDescriptor()
var_0_1.CAPITAL_LOG_NAME_FIELD = var_0_0.FieldDescriptor()
var_0_1.CAPITAL_LOG_EVENT_TYPE_FIELD = var_0_0.FieldDescriptor()
var_0_1.CAPITAL_LOG_EVENT_TARGET_FIELD = var_0_0.FieldDescriptor()
var_0_1.CAPITAL_LOG_TIME_FIELD = var_0_0.FieldDescriptor()
WEEKLY_TASK = var_0_0.Descriptor()
var_0_1.WEEKLY_TASK_ID_FIELD = var_0_0.FieldDescriptor()
var_0_1.WEEKLY_TASK_PROGRESS_FIELD = var_0_0.FieldDescriptor()
var_0_1.WEEKLY_TASK_MONDAY_0CLOCK_FIELD = var_0_0.FieldDescriptor()
GUILD_TECHNOLOGY = var_0_0.Descriptor()
var_0_1.GUILD_TECHNOLOGY_ID_FIELD = var_0_0.FieldDescriptor()
var_0_1.GUILD_TECHNOLOGY_STATE_FIELD = var_0_0.FieldDescriptor()
var_0_1.GUILD_TECHNOLOGY_PROGRESS_FIELD = var_0_0.FieldDescriptor()
FLEET_INFO = var_0_0.Descriptor()
var_0_1.FLEET_INFO_ID_FIELD = var_0_0.FieldDescriptor()
var_0_1.FLEET_INFO_SHIP_LIST_FIELD = var_0_0.FieldDescriptor()
var_0_1.CAPITAL_LOG_MEMBER_ID_FIELD.name = "member_id"
var_0_1.CAPITAL_LOG_MEMBER_ID_FIELD.full_name = "guild.capital_log.member_id"
var_0_1.CAPITAL_LOG_MEMBER_ID_FIELD.number = 1
var_0_1.CAPITAL_LOG_MEMBER_ID_FIELD.index = 0
var_0_1.CAPITAL_LOG_MEMBER_ID_FIELD.label = 2
var_0_1.CAPITAL_LOG_MEMBER_ID_FIELD.has_default_value = false
var_0_1.CAPITAL_LOG_MEMBER_ID_FIELD.default_value = 0
var_0_1.CAPITAL_LOG_MEMBER_ID_FIELD.type = 13
var_0_1.CAPITAL_LOG_MEMBER_ID_FIELD.cpp_type = 3
var_0_1.CAPITAL_LOG_NAME_FIELD.name = "name"
var_0_1.CAPITAL_LOG_NAME_FIELD.full_name = "guild.capital_log.name"
var_0_1.CAPITAL_LOG_NAME_FIELD.number = 2
var_0_1.CAPITAL_LOG_NAME_FIELD.index = 1
var_0_1.CAPITAL_LOG_NAME_FIELD.label = 2
var_0_1.CAPITAL_LOG_NAME_FIELD.has_default_value = false
var_0_1.CAPITAL_LOG_NAME_FIELD.default_value = ""
var_0_1.CAPITAL_LOG_NAME_FIELD.type = 9
var_0_1.CAPITAL_LOG_NAME_FIELD.cpp_type = 9
var_0_1.CAPITAL_LOG_EVENT_TYPE_FIELD.name = "event_type"
var_0_1.CAPITAL_LOG_EVENT_TYPE_FIELD.full_name = "guild.capital_log.event_type"
var_0_1.CAPITAL_LOG_EVENT_TYPE_FIELD.number = 3
var_0_1.CAPITAL_LOG_EVENT_TYPE_FIELD.index = 2
var_0_1.CAPITAL_LOG_EVENT_TYPE_FIELD.label = 2
var_0_1.CAPITAL_LOG_EVENT_TYPE_FIELD.has_default_value = false
var_0_1.CAPITAL_LOG_EVENT_TYPE_FIELD.default_value = 0
var_0_1.CAPITAL_LOG_EVENT_TYPE_FIELD.type = 13
var_0_1.CAPITAL_LOG_EVENT_TYPE_FIELD.cpp_type = 3
var_0_1.CAPITAL_LOG_EVENT_TARGET_FIELD.name = "event_target"
var_0_1.CAPITAL_LOG_EVENT_TARGET_FIELD.full_name = "guild.capital_log.event_target"
var_0_1.CAPITAL_LOG_EVENT_TARGET_FIELD.number = 4
var_0_1.CAPITAL_LOG_EVENT_TARGET_FIELD.index = 3
var_0_1.CAPITAL_LOG_EVENT_TARGET_FIELD.label = 3
var_0_1.CAPITAL_LOG_EVENT_TARGET_FIELD.has_default_value = false
var_0_1.CAPITAL_LOG_EVENT_TARGET_FIELD.default_value = {}
var_0_1.CAPITAL_LOG_EVENT_TARGET_FIELD.type = 13
var_0_1.CAPITAL_LOG_EVENT_TARGET_FIELD.cpp_type = 3
var_0_1.CAPITAL_LOG_TIME_FIELD.name = "time"
var_0_1.CAPITAL_LOG_TIME_FIELD.full_name = "guild.capital_log.time"
var_0_1.CAPITAL_LOG_TIME_FIELD.number = 5
var_0_1.CAPITAL_LOG_TIME_FIELD.index = 4
var_0_1.CAPITAL_LOG_TIME_FIELD.label = 2
var_0_1.CAPITAL_LOG_TIME_FIELD.has_default_value = false
var_0_1.CAPITAL_LOG_TIME_FIELD.default_value = 0
var_0_1.CAPITAL_LOG_TIME_FIELD.type = 13
var_0_1.CAPITAL_LOG_TIME_FIELD.cpp_type = 3
CAPITAL_LOG.name = "capital_log"
CAPITAL_LOG.full_name = "guild.capital_log"
CAPITAL_LOG.nested_types = {}
CAPITAL_LOG.enum_types = {}
CAPITAL_LOG.fields = {
	var_0_1.CAPITAL_LOG_MEMBER_ID_FIELD,
	var_0_1.CAPITAL_LOG_NAME_FIELD,
	var_0_1.CAPITAL_LOG_EVENT_TYPE_FIELD,
	var_0_1.CAPITAL_LOG_EVENT_TARGET_FIELD,
	var_0_1.CAPITAL_LOG_TIME_FIELD
}
CAPITAL_LOG.is_extendable = false
CAPITAL_LOG.extensions = {}
var_0_1.WEEKLY_TASK_ID_FIELD.name = "id"
var_0_1.WEEKLY_TASK_ID_FIELD.full_name = "guild.weekly_task.id"
var_0_1.WEEKLY_TASK_ID_FIELD.number = 1
var_0_1.WEEKLY_TASK_ID_FIELD.index = 0
var_0_1.WEEKLY_TASK_ID_FIELD.label = 2
var_0_1.WEEKLY_TASK_ID_FIELD.has_default_value = false
var_0_1.WEEKLY_TASK_ID_FIELD.default_value = 0
var_0_1.WEEKLY_TASK_ID_FIELD.type = 13
var_0_1.WEEKLY_TASK_ID_FIELD.cpp_type = 3
var_0_1.WEEKLY_TASK_PROGRESS_FIELD.name = "progress"
var_0_1.WEEKLY_TASK_PROGRESS_FIELD.full_name = "guild.weekly_task.progress"
var_0_1.WEEKLY_TASK_PROGRESS_FIELD.number = 2
var_0_1.WEEKLY_TASK_PROGRESS_FIELD.index = 1
var_0_1.WEEKLY_TASK_PROGRESS_FIELD.label = 2
var_0_1.WEEKLY_TASK_PROGRESS_FIELD.has_default_value = false
var_0_1.WEEKLY_TASK_PROGRESS_FIELD.default_value = 0
var_0_1.WEEKLY_TASK_PROGRESS_FIELD.type = 13
var_0_1.WEEKLY_TASK_PROGRESS_FIELD.cpp_type = 3
var_0_1.WEEKLY_TASK_MONDAY_0CLOCK_FIELD.name = "monday_0clock"
var_0_1.WEEKLY_TASK_MONDAY_0CLOCK_FIELD.full_name = "guild.weekly_task.monday_0clock"
var_0_1.WEEKLY_TASK_MONDAY_0CLOCK_FIELD.number = 3
var_0_1.WEEKLY_TASK_MONDAY_0CLOCK_FIELD.index = 2
var_0_1.WEEKLY_TASK_MONDAY_0CLOCK_FIELD.label = 2
var_0_1.WEEKLY_TASK_MONDAY_0CLOCK_FIELD.has_default_value = false
var_0_1.WEEKLY_TASK_MONDAY_0CLOCK_FIELD.default_value = 0
var_0_1.WEEKLY_TASK_MONDAY_0CLOCK_FIELD.type = 13
var_0_1.WEEKLY_TASK_MONDAY_0CLOCK_FIELD.cpp_type = 3
WEEKLY_TASK.name = "weekly_task"
WEEKLY_TASK.full_name = "guild.weekly_task"
WEEKLY_TASK.nested_types = {}
WEEKLY_TASK.enum_types = {}
WEEKLY_TASK.fields = {
	var_0_1.WEEKLY_TASK_ID_FIELD,
	var_0_1.WEEKLY_TASK_PROGRESS_FIELD,
	var_0_1.WEEKLY_TASK_MONDAY_0CLOCK_FIELD
}
WEEKLY_TASK.is_extendable = false
WEEKLY_TASK.extensions = {}
var_0_1.GUILD_TECHNOLOGY_ID_FIELD.name = "id"
var_0_1.GUILD_TECHNOLOGY_ID_FIELD.full_name = "guild.guild_technology.id"
var_0_1.GUILD_TECHNOLOGY_ID_FIELD.number = 1
var_0_1.GUILD_TECHNOLOGY_ID_FIELD.index = 0
var_0_1.GUILD_TECHNOLOGY_ID_FIELD.label = 2
var_0_1.GUILD_TECHNOLOGY_ID_FIELD.has_default_value = false
var_0_1.GUILD_TECHNOLOGY_ID_FIELD.default_value = 0
var_0_1.GUILD_TECHNOLOGY_ID_FIELD.type = 13
var_0_1.GUILD_TECHNOLOGY_ID_FIELD.cpp_type = 3
var_0_1.GUILD_TECHNOLOGY_STATE_FIELD.name = "state"
var_0_1.GUILD_TECHNOLOGY_STATE_FIELD.full_name = "guild.guild_technology.state"
var_0_1.GUILD_TECHNOLOGY_STATE_FIELD.number = 2
var_0_1.GUILD_TECHNOLOGY_STATE_FIELD.index = 1
var_0_1.GUILD_TECHNOLOGY_STATE_FIELD.label = 2
var_0_1.GUILD_TECHNOLOGY_STATE_FIELD.has_default_value = false
var_0_1.GUILD_TECHNOLOGY_STATE_FIELD.default_value = 0
var_0_1.GUILD_TECHNOLOGY_STATE_FIELD.type = 13
var_0_1.GUILD_TECHNOLOGY_STATE_FIELD.cpp_type = 3
var_0_1.GUILD_TECHNOLOGY_PROGRESS_FIELD.name = "progress"
var_0_1.GUILD_TECHNOLOGY_PROGRESS_FIELD.full_name = "guild.guild_technology.progress"
var_0_1.GUILD_TECHNOLOGY_PROGRESS_FIELD.number = 3
var_0_1.GUILD_TECHNOLOGY_PROGRESS_FIELD.index = 2
var_0_1.GUILD_TECHNOLOGY_PROGRESS_FIELD.label = 2
var_0_1.GUILD_TECHNOLOGY_PROGRESS_FIELD.has_default_value = false
var_0_1.GUILD_TECHNOLOGY_PROGRESS_FIELD.default_value = 0
var_0_1.GUILD_TECHNOLOGY_PROGRESS_FIELD.type = 13
var_0_1.GUILD_TECHNOLOGY_PROGRESS_FIELD.cpp_type = 3
GUILD_TECHNOLOGY.name = "guild_technology"
GUILD_TECHNOLOGY.full_name = "guild.guild_technology"
GUILD_TECHNOLOGY.nested_types = {}
GUILD_TECHNOLOGY.enum_types = {}
GUILD_TECHNOLOGY.fields = {
	var_0_1.GUILD_TECHNOLOGY_ID_FIELD,
	var_0_1.GUILD_TECHNOLOGY_STATE_FIELD,
	var_0_1.GUILD_TECHNOLOGY_PROGRESS_FIELD
}
GUILD_TECHNOLOGY.is_extendable = false
GUILD_TECHNOLOGY.extensions = {}
var_0_1.FLEET_INFO_ID_FIELD.name = "id"
var_0_1.FLEET_INFO_ID_FIELD.full_name = "guild.fleet_info.id"
var_0_1.FLEET_INFO_ID_FIELD.number = 1
var_0_1.FLEET_INFO_ID_FIELD.index = 0
var_0_1.FLEET_INFO_ID_FIELD.label = 2
var_0_1.FLEET_INFO_ID_FIELD.has_default_value = false
var_0_1.FLEET_INFO_ID_FIELD.default_value = 0
var_0_1.FLEET_INFO_ID_FIELD.type = 13
var_0_1.FLEET_INFO_ID_FIELD.cpp_type = 3
var_0_1.FLEET_INFO_SHIP_LIST_FIELD.name = "ship_list"
var_0_1.FLEET_INFO_SHIP_LIST_FIELD.full_name = "guild.fleet_info.ship_list"
var_0_1.FLEET_INFO_SHIP_LIST_FIELD.number = 2
var_0_1.FLEET_INFO_SHIP_LIST_FIELD.index = 1
var_0_1.FLEET_INFO_SHIP_LIST_FIELD.label = 3
var_0_1.FLEET_INFO_SHIP_LIST_FIELD.has_default_value = false
var_0_1.FLEET_INFO_SHIP_LIST_FIELD.default_value = {}
var_0_1.FLEET_INFO_SHIP_LIST_FIELD.type = 13
var_0_1.FLEET_INFO_SHIP_LIST_FIELD.cpp_type = 3
FLEET_INFO.name = "fleet_info"
FLEET_INFO.full_name = "guild.fleet_info"
FLEET_INFO.nested_types = {}
FLEET_INFO.enum_types = {}
FLEET_INFO.fields = {
	var_0_1.FLEET_INFO_ID_FIELD,
	var_0_1.FLEET_INFO_SHIP_LIST_FIELD
}
FLEET_INFO.is_extendable = false
FLEET_INFO.extensions = {}
capital_log = var_0_0.Message(CAPITAL_LOG)
fleet_info = var_0_0.Message(FLEET_INFO)
guild_technology = var_0_0.Message(GUILD_TECHNOLOGY)
weekly_task = var_0_0.Message(WEEKLY_TASK)
