local var_0_0 = class("GuideFindUIStep", import(".GuideStep"))

var_0_0.TRIGGER_TYPE_BUTTON = 1
var_0_0.TRIGGER_TYPE_TOGGLE = 2
var_0_0.EVENT_TYPE_CLICK = 3
var_0_0.EVENT_TYPE_STICK = 4
var_0_0.SHOW_UI = 5
var_0_0.TRIGGER_TYPE_BUTTONEX = 6
var_0_0.SNAP_PAGE = 7
var_0_0.EVENT_TYPE_EVT_CLICK = 8

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.eventUI = arg_1_0.GenEventSearchData(arg_1_1.ui)

def var_0_0.GenEventSearchData(arg_2_0, arg_2_1):
	if not arg_2_1:
		return None

	local var_2_0 = arg_2_0.GenSearchData(arg_2_1)
	local var_2_1 = arg_2_1.scale != None
	local var_2_2 = arg_2_1.scale or 1

	if arg_2_1.dynamicPath:
		local var_2_3, var_2_4 = arg_2_1.dynamicPath()

		if var_2_3:
			var_2_0.path = var_2_3

		if var_2_4:
			var_2_1 = True
			var_2_2 = var_2_4

	var_2_0.settings = {
		pos = arg_2_1.pos,
		scale = var_2_2,
		eulerAngles = arg_2_1.eulerAngles,
		isLevelPoint = arg_2_1.isLevelPoint,
		image = arg_2_1.image,
		customPosition = arg_2_1.pos or var_2_1 or arg_2_1.eulerAngles or arg_2_1.isLevelPoint,
		clearChildEvent = arg_2_1.eventPath != None,
		keepScrollTxt = arg_2_1.keepScrollTxt
	}

	local var_2_5
	local var_2_6

	if arg_2_1.onClick:
		var_2_5 = var_0_0.TRIGGER_TYPE_BUTTONEX
		var_2_6 = arg_2_1.onClick
	else
		var_2_5 = arg_2_1.triggerType and arg_2_1.triggerType[1] or var_0_0.TRIGGER_TYPE_BUTTON
		var_2_6 = arg_2_1.triggerType and arg_2_1.triggerType[2]

	local var_2_7 = arg_2_1.eventPath

	if arg_2_1.dynamicEventPath:
		var_2_7 = arg_2_1.dynamicEventPath()

	var_2_0.triggerData = {
		type = var_2_5,
		arg = var_2_6
	}
	var_2_0.childIndex = arg_2_1.eventIndex
	var_2_0.eventPath = var_2_7
	var_2_0.fingerPos = arg_2_1.fingerPos
	var_2_0.slipAnim = var_2_5 == var_0_0.SNAP_PAGE

	return var_2_0

def var_0_0.GetType(arg_3_0):
	return GuideStep.TYPE_FINDUI

def var_0_0.GetEventUI(arg_4_0):
	return arg_4_0.eventUI

return var_0_0
