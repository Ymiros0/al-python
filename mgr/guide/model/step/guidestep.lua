﻿local var_0_0 = class("GuideStep")

var_0_0.TYPE_DOFUNC = 0
var_0_0.TYPE_DONOTHING = 1
var_0_0.TYPE_FINDUI = 2
var_0_0.TYPE_HIDEUI = 3
var_0_0.TYPE_SENDNOTIFIES = 4
var_0_0.TYPE_SHOWSIGN = 5
var_0_0.TYPE_STORY = 6
var_0_0.DIALOGUE_BLUE = 1
var_0_0.DIALOGUE_WHITE = 2
var_0_0.HIGH_TYPE_LINE = 1
var_0_0.HIGH_TYPE_GAMEOBJECT = 2

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.delay = arg_1_1.delay
	arg_1_0.waitScene = arg_1_1.waitScene
	arg_1_0.code = arg_1_1.code
	arg_1_0.alpha = arg_1_1.alpha
	arg_1_0.styleData = arg_1_0:GenStyleData(arg_1_1.style)
	arg_1_0.highLightData = arg_1_0:GenHighLightData(arg_1_1.style)
	arg_1_0.baseUI = arg_1_0:GenSearchData(arg_1_1.baseui)
	arg_1_0.spriteUI = arg_1_0:GenSpriteSearchData(arg_1_1.spriteui)
	arg_1_0.sceneName = arg_1_1.style and arg_1_1.style.scene
	arg_1_0.otherTriggerTarget = arg_1_1.style and arg_1_1.style.trigger
	arg_1_0.isWorld = defaultValue(arg_1_1.isWorld, true)
end

function var_0_0.UpdateIsWorld(arg_2_0, arg_2_1)
	arg_2_0.isWorld = arg_2_1
end

function var_0_0.IsMatchWithCode(arg_3_0, arg_3_1)
	local var_3_0 = arg_3_0:GetMatchCode()

	if not var_3_0 then
		return true
	end

	if type(var_3_0) == "number" then
		return table.contains(arg_3_1, var_3_0)
	elseif type(var_3_0) == "table" then
		return _.any(arg_3_1, function(arg_4_0)
			return table.contains(var_3_0, arg_4_0)
		end)
	end

	return false
end

function var_0_0.GetMatchCode(arg_5_0)
	return arg_5_0.code
end

function var_0_0.GetDelay(arg_6_0)
	return arg_6_0.delay or 0
end

function var_0_0.GetAlpha(arg_7_0)
	return arg_7_0.alpha or 0.4
end

function var_0_0.ShouldWaitScene(arg_8_0)
	return arg_8_0.waitScene and arg_8_0.waitScene ~= ""
end

function var_0_0.GetWaitScene(arg_9_0)
	return arg_9_0.waitScene
end

function var_0_0.ShouldShowDialogue(arg_10_0)
	return arg_10_0.styleData ~= nil
end

function var_0_0.GetDialogueType(arg_11_0)
	return arg_11_0.styleData.mode
end

local function var_0_1(arg_12_0, arg_12_1)
	local var_12_0 = "char"

	if arg_12_1.char and arg_12_1.char == 1 then
		var_12_0 = arg_12_0.isWorld and "char_world" or "char_world1"
	elseif arg_12_1.char and arg_12_1.char == "amazon" then
		var_12_0 = "char_amazon"
	end

	return var_12_0
end

local function var_0_2(arg_13_0, arg_13_1)
	if arg_13_1.charPos then
		return Vector2(arg_13_1.charPos[1], arg_13_1.charPos[2])
	elseif arg_13_1.dir == 1 then
		return arg_13_1.mode == var_0_0.DIALOGUE_BLUE and Vector2(-400, -170) or Vector2(-350, 0)
	else
		return arg_13_1.mode == var_0_0.DIALOGUE_BLUE and Vector2(400, -170) or Vector2(350, 0)
	end
end

local function var_0_3(arg_14_0)
	local var_14_0

	if arg_14_0.charScale then
		var_14_0 = Vector2(arg_14_0.charScale[1], arg_14_0.charScale[2])
	else
		var_14_0 = Vector2(1, 1)
	end

	return arg_14_0.dir == 1 and var_14_0 or Vector3(-var_14_0.x, var_14_0.y, 1)
end

function var_0_0.GenStyleData(arg_15_0, arg_15_1)
	if not arg_15_1 then
		return nil
	end

	return {
		mode = arg_15_1.mode,
		text = HXSet.hxLan(arg_15_1.text or ""),
		counsellor = {
			name = var_0_1(arg_15_0, arg_15_1),
			position = var_0_2(arg_15_0, arg_15_1),
			scale = var_0_3(arg_15_1)
		},
		scale = arg_15_1.dir == 1 and Vector3(1, 1, 1) or Vector3(-1, 1, 1),
		position = Vector2(arg_15_1.posX or 0, arg_15_1.posY or 0),
		handPosition = arg_15_1.handPos and Vector3(arg_15_1.handPos.x, arg_15_1.handPos.y, 0) or Vector3(-267, -96, 0),
		handAngle = arg_15_1.handPos and Vector3(0, 0, arg_15_1.handPos.w or 0) or Vector3(0, 0, 0)
	}
end

function var_0_0.GetStyleData(arg_16_0)
	return arg_16_0.styleData
end

function var_0_0.GenHighLightData(arg_17_0, arg_17_1)
	local function var_17_0(arg_18_0)
		local var_18_0 = arg_17_0:GenSearchData(arg_18_0)

		var_18_0.type = arg_18_0.lineMode or var_0_0.HIGH_TYPE_GAMEOBJECT

		return var_18_0
	end

	local var_17_1 = {}

	if arg_17_1 and arg_17_1.ui then
		table.insert(var_17_1, var_17_0(arg_17_1.ui))
	elseif arg_17_1 and arg_17_1.uiset then
		for iter_17_0, iter_17_1 in ipairs(arg_17_1.uiset) do
			table.insert(var_17_1, var_17_0(iter_17_1))
		end
	elseif arg_17_1 and arg_17_1.uiFunc then
		local var_17_2 = arg_17_1.uiFunc()

		for iter_17_2, iter_17_3 in ipairs(var_17_2) do
			table.insert(var_17_1, var_17_0(iter_17_3))
		end
	end

	return var_17_1
end

function var_0_0.ShouldHighLightTarget(arg_19_0)
	return #arg_19_0.highLightData > 0
end

function var_0_0.GetHighLightTarget(arg_20_0)
	return arg_20_0.highLightData
end

function var_0_0.ExistTrigger(arg_21_0)
	local var_21_0 = arg_21_0:GetType()

	return var_21_0 == var_0_0.TYPE_FINDUI or var_21_0 == var_0_0.TYPE_STORY
end

function var_0_0.ShouldGoScene(arg_22_0)
	return arg_22_0.sceneName and arg_22_0.sceneName ~= ""
end

function var_0_0.GetSceneName(arg_23_0)
	return arg_23_0.sceneName
end

function var_0_0.ShouldTriggerOtherTarget(arg_24_0)
	return arg_24_0.otherTriggerTarget ~= nil
end

function var_0_0.GetOtherTriggerTarget(arg_25_0)
	local var_25_0 = arg_25_0.otherTriggerTarget

	return arg_25_0:GenSearchData(var_25_0)
end

function var_0_0.GenSearchData(arg_26_0, arg_26_1)
	if not arg_26_1 then
		return nil
	end

	local var_26_0 = arg_26_1.path

	if arg_26_1.dynamicPath then
		var_26_0 = arg_26_1.dynamicPath()
	end

	return {
		path = var_26_0,
		delay = arg_26_1.delay,
		pathIndex = arg_26_1.pathIndex,
		conditionData = arg_26_1.conditionData
	}
end

function var_0_0.GenSpriteSearchData(arg_27_0, arg_27_1)
	if not arg_27_1 then
		return nil
	end

	local var_27_0 = arg_27_0:GenSearchData(arg_27_1)

	var_27_0.defaultName = arg_27_1.defaultName
	var_27_0.childPath = arg_27_1.childPath

	return var_27_0
end

function var_0_0.ShouldCheckBaseUI(arg_28_0)
	return arg_28_0.baseUI ~= nil
end

function var_0_0.GetBaseUI(arg_29_0)
	return arg_29_0.baseUI
end

function var_0_0.ShouldCheckSpriteUI(arg_30_0)
	return arg_30_0.spriteUI ~= nil
end

function var_0_0.GetSpriteUI(arg_31_0)
	return arg_31_0.spriteUI
end

function var_0_0.GetType(arg_32_0)
	assert(false, "overwrite me!!!")
end

return var_0_0