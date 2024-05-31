local var_0_0 = class("GuideShowSignStep", import(".GuideStep"))

var_0_0.SIGN_TYPE_2 = 2
var_0_0.SIGN_TYPE_3 = 3

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	local var_1_0 = arg_1_1.showSign

	arg_1_0.sType = var_1_0.type
	arg_1_0.duration = var_1_0.duration
	arg_1_0.clickUI = arg_1_0.GenClickData(var_1_0.clickUI)
	arg_1_0.clickArea = var_1_0.clickArea
	arg_1_0.longPress = var_1_0.longPress
	arg_1_0.signIndexList = {}

	for iter_1_0, iter_1_1 in ipairs(var_1_0.signList):
		local var_1_1 = iter_1_1.signType
		local var_1_2 = iter_1_1.pos
		local var_1_3 = iter_1_1.cachedIndex

		if type(var_1_2) == "string":
			if var_1_2 == "useCachePos":
				var_1_2 = WorldGuider.GetInstance().GetTempGridPos(var_1_3)
		elif type(var_1_2) == "table":
			var_1_2 = Vector3.New(var_1_2[1], var_1_2[2], var_1_2[3])

		table.insert(arg_1_0.signIndexList, {
			pos = var_1_2 or Vector3(0, 0, 0),
			signName = arg_1_0.GetSignResName(var_1_1),
			atlasName = iter_1_1.atlasName,
			fileName = iter_1_1.fileName
		})

def var_0_0.GenClickData(arg_2_0, arg_2_1):
	if not arg_2_1:
		return None

	local var_2_0 = arg_2_0.GenSearchData(arg_2_1)
	local var_2_1 = arg_2_1.sizeDeltaPlus or {
		0,
		0
	}

	var_2_0.sizeDeltaPlus = Vector2(var_2_1[1], var_2_1[2])

	return var_2_0

def var_0_0.GetType(arg_3_0):
	return GuideStep.TYPE_SHOWSIGN

def var_0_0.GetSignType(arg_4_0):
	return arg_4_0.sType

def var_0_0.GetFirstSign(arg_5_0):
	return arg_5_0.signIndexList[1]

def var_0_0.GetSignList(arg_6_0):
	return arg_6_0.signIndexList

def var_0_0.GetSignResName(arg_7_0, arg_7_1):
	local var_7_0 = ""

	if arg_7_1 == 1 or arg_7_1 == 6:
		var_7_0 = "wTask"
	elif arg_7_1 == 2:
		var_7_0 = "wDanger"
	elif arg_7_1 == 3:
		var_7_0 = "wForbidden"
	elif arg_7_1 == 4:
		var_7_0 = "wClickArea"
	elif arg_7_1 == 5:
		var_7_0 = "wShowArea"

	return var_7_0

def var_0_0.ShouldClick(arg_8_0):
	return arg_8_0.clickUI != None

def var_0_0.GetClickData(arg_9_0):
	return arg_9_0.clickUI

def var_0_0.ExistClickArea(arg_10_0):
	return arg_10_0.clickArea != None

def var_0_0.GetClickArea(arg_11_0):
	local var_11_0 = arg_11_0.clickArea or {
		0,
		0
	}

	return Vector2(var_11_0[1], var_11_0[2])

def var_0_0.GetTriggerType(arg_12_0):
	return arg_12_0.longPress

def var_0_0.GetExitDelay(arg_13_0):
	return arg_13_0.duration or 0

def var_0_0.ExistTrigger(arg_14_0):
	return arg_14_0.GetSignType() != var_0_0.SIGN_TYPE_3

return var_0_0
