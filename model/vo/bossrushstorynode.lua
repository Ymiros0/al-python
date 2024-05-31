local var_0_0 = class("BossRushStoryNode", import("model.vo.BaseVO"))

var_0_0.TRIGGER_TYPE = {
	PT_GOT = 1,
	STORY_READED = 3,
	SERIES_PASSED = 2
}
var_0_0.NODE_TYPE = {
	EVENT = 2,
	NORMAL = 1,
	BATTLE = 3
}

function var_0_0.bindConfigTable(arg_1_0)
	return pg.activity_series_enemy_story
end

function var_0_0.Ctor(arg_2_0, arg_2_1, ...)
	var_0_0.super.Ctor(arg_2_0, arg_2_1, ...)

	arg_2_0.configId = arg_2_0.id
end

function var_0_0.GetTriggers(arg_3_0)
	local function var_3_0(arg_4_0)
		if type(arg_4_0) ~= "table" then
			return {}
		end

		return arg_4_0
	end

	local var_3_1 = var_3_0(arg_3_0:getConfig("trigger_type"))
	local var_3_2 = var_3_0(arg_3_0:getConfig("trigger_value"))
	local var_3_3 = {}

	table.Foreach(var_3_1, function(arg_5_0, arg_5_1)
		var_3_3[arg_5_0] = {
			type = var_3_1[arg_5_0],
			value = var_3_2[arg_5_0]
		}
	end)

	return var_3_3
end

function var_0_0.GetType(arg_6_0)
	return arg_6_0:getConfig("type")
end

function var_0_0.GetName(arg_7_0)
	return arg_7_0:getConfig("name")
end

function var_0_0.GetIconName(arg_8_0)
	return arg_8_0:getConfig("icon")
end

function var_0_0.GetStory(arg_9_0)
	return arg_9_0:getConfig("story")
end

function var_0_0.GetActiveLink(arg_10_0)
	return arg_10_0:getConfig("line")
end

return var_0_0
