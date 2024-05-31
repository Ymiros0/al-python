local var_0_0 = class("LinerTime", import("model.vo.BaseVO"))

var_0_0.TYPE = {
	TARGET = 1,
	EXPLORE = 2,
	STORY = 4,
	EVENT = 3
}
var_0_0.EVENT_SUB_TYPE = {
	STORY = 2,
	CLUE = 1
}
var_0_0.BG_TYPE = {
	DAY = "day",
	DUSK = "dusk",
	AURORA = "aurora",
	NIGTH = "night"
}

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.id = arg_1_1
	arg_1_0.configId = arg_1_0.id

def var_0_0.bindConfigTable(arg_2_0):
	return pg.activity_liner_time

def var_0_0.GetTime(arg_3_0):
	return arg_3_0.getConfig("time")

def var_0_0.GetStartTimeDesc(arg_4_0):
	local var_4_0 = arg_4_0.GetTime()[1]
	local var_4_1 = var_4_0 < 12 and "AM" or "PM"

	if var_4_0 > 12:
		var_4_0 = var_4_0 - 12

	return var_4_0 .. ".00 " .. var_4_1

def var_0_0.GetEndTimeDesc(arg_5_0):
	local var_5_0 = arg_5_0.GetTime()[2]
	local var_5_1 = var_5_0 < 12 and "AM" or "PM"

	if var_5_0 > 12:
		var_5_0 = var_5_0 - 12

	return var_5_0 .. ".00 " .. var_5_1

def var_0_0.GetLogDesc(arg_6_0):
	local var_6_0 = arg_6_0.GetTime()[1]
	local var_6_1 = arg_6_0.GetTime()[2] - 1
	local var_6_2 = var_6_0 < 12 and "AM" or "PM"
	local var_6_3 = var_6_1 < 12 and "AM" or "PM"
	local var_6_4

	var_6_4, var_6_1 = var_6_0 > 12 and var_6_0 - 12 or var_6_0, var_6_1 > 12 and var_6_1 - 12 or var_6_1

	return string.format("%d.00 %s~%d.59 %s", var_6_4, var_6_2, var_6_1, var_6_3)

def var_0_0.GetType(arg_7_0):
	return arg_7_0.getConfig("type")

def var_0_0.GetEventSubType(arg_8_0, arg_8_1):
	assert(arg_8_0.GetType() == var_0_0.TYPE.EVENT, "error type")

	local var_8_0 = underscore.detect(arg_8_0.GetParamInfo(), function(arg_9_0)
		return arg_9_0[1] == arg_8_1)

	assert(var_8_0, "error roomId")

	return var_8_0[2]

def var_0_0.GetParamInfo(arg_10_0):
	return arg_10_0.getConfig("param")

def var_0_0.GetTargetRoomIds(arg_11_0):
	local var_11_0 = {}

	switch(arg_11_0.GetType(), {
		[var_0_0.TYPE.TARGET] = function()
			table.insert(var_11_0, tonumber(arg_11_0.GetParamInfo()[1])),
		[var_0_0.TYPE.EXPLORE] = function()
			return,
		[var_0_0.TYPE.EVENT] = function()
			for iter_14_0, iter_14_1 in ipairs(arg_11_0.GetParamInfo()):
				table.insert(var_11_0, iter_14_1[1]),
		[var_0_0.TYPE.STORY] = function()
			table.insert(var_11_0, tonumber(arg_11_0.GetParamInfo()[1]))
	})

	return var_11_0

def var_0_0.GetExploreCnt(arg_16_0):
	if arg_16_0.GetType() != var_0_0.TYPE.EXPLORE:
		return 0

	return tonumber(arg_16_0.GetParamInfo())

def var_0_0.GetEventIds(arg_17_0):
	if arg_17_0.GetType() != var_0_0.TYPE.EVENT:
		return {}

	local var_17_0 = {}

	for iter_17_0, iter_17_1 in ipairs(arg_17_0.GetParamInfo()):
		var_17_0 = table.mergeArray(var_17_0, iter_17_1[4], True)

	return var_17_0

def var_0_0.GetStory(arg_18_0, arg_18_1):
	local var_18_0 = ""

	switch(arg_18_0.GetType(), {
		[var_0_0.TYPE.TARGET] = function()
			var_18_0 = arg_18_0.GetParamInfo()[2],
		[var_0_0.TYPE.EXPLORE] = function()
			return,
		[var_0_0.TYPE.EVENT] = function()
			local var_21_0 = underscore.detect(arg_18_0.GetParamInfo(), function(arg_22_0)
				return arg_22_0[1] == arg_18_1)

			if var_21_0 and var_21_0[2] == var_0_0.EVENT_SUB_TYPE.STORY:
				var_18_0 = var_21_0[3],
		[var_0_0.TYPE.STORY] = function()
			var_18_0 = arg_18_0.GetParamInfo()[2]
	})

	return var_18_0

def var_0_0.GetBeforDesc(arg_24_0, arg_24_1):
	local var_24_0 = arg_24_0.getConfig("desc_before")

	if type(var_24_0) == "table":
		return HXSet.hxLan(var_24_0[arg_24_1][1])
	else
		return HXSet.hxLan(var_24_0)

def var_0_0.GetAfterDesc(arg_25_0, arg_25_1):
	local var_25_0 = arg_25_0.getConfig("desc_after")

	if type(var_25_0) == "table":
		return HXSet.hxLan(var_25_0[arg_25_1][1])
	else
		return HXSet.hxLan(var_25_0)

def var_0_0.GetBgType(arg_26_0):
	return arg_26_0.getConfig("bg_name")

def var_0_0.GetBgm(arg_27_0, arg_27_1):
	local var_27_0 = arg_27_1 or arg_27_0.GetBgType()
	local var_27_1 = "story-niceship-soft"

	switch(var_27_0, {
		[var_0_0.BG_TYPE.DAY] = function()
			var_27_1 = "story-niceship-soft",
		[var_0_0.BG_TYPE.DUSK] = function()
			var_27_1 = "story-richang-5",
		[var_0_0.BG_TYPE.NIGTH] = function()
			var_27_1 = "story-richang-10",
		[var_0_0.BG_TYPE.AURORA] = function()
			var_27_1 = "story-richang-quiet"
	})

	return var_27_1

return var_0_0
