local var_0_0 = class("EducateScheduleResultLayer", import(".base.EducateBaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "EducateScheduleResultUI"

def var_0_0.init(arg_2_0):
	arg_2_0.anim = arg_2_0.findTF("anim_root").GetComponent(typeof(Animation))
	arg_2_0.animEvent = arg_2_0.findTF("anim_root").GetComponent(typeof(DftAniEvent))
	arg_2_0.inAnimPlaying = True

	arg_2_0.animEvent.SetEndEvent(function()
		arg_2_0.inAnimPlaying = False

		arg_2_0.animEvent.SetEndEvent(function()
			arg_2_0.emit(var_0_0.ON_CLOSE)))

	arg_2_0.windowTF = arg_2_0.findTF("anim_root/window")
	arg_2_0.personalTF = arg_2_0.findTF("personal", arg_2_0.windowTF)
	arg_2_0.majorArrTF = arg_2_0.findTF("major", arg_2_0.windowTF)
	arg_2_0.minorArrTF = arg_2_0.findTF("minor", arg_2_0.windowTF)
	arg_2_0.resTF = arg_2_0.findTF("res/content", arg_2_0.windowTF)

	setText(arg_2_0.findTF("tip", arg_2_0.windowTF), i18n("child_close_tip"))
	pg.UIMgr.GetInstance().BlurPanel(arg_2_0._tf, None, {
		groupName = arg_2_0.getGroupNameFromData(),
		weight = arg_2_0.getWeightFromData() + 1
	})

def var_0_0.didEnter(arg_5_0):
	onButton(arg_5_0, arg_5_0._tf, function()
		arg_5_0._close(), SFX_CANCEL)

	local var_5_0 = arg_5_0.contextData.plan_results or {}

	arg_5_0.result = {}
	arg_5_0.resResult = {}
	arg_5_0.drops = {}

	local function var_5_1(arg_7_0)
		for iter_7_0, iter_7_1 in ipairs(arg_7_0):
			table.insert(arg_5_0.drops, iter_7_1)

			if iter_7_1.type == EducateConst.DROP_TYPE_ATTR:
				if not arg_5_0.result[iter_7_1.id]:
					arg_5_0.result[iter_7_1.id] = 0

				arg_5_0.result[iter_7_1.id] = arg_5_0.result[iter_7_1.id] + iter_7_1.number

			if iter_7_1.type == EducateConst.DROP_TYPE_RES:
				if not arg_5_0.resResult[iter_7_1.id]:
					arg_5_0.resResult[iter_7_1.id] = 0

				arg_5_0.resResult[iter_7_1.id] = arg_5_0.resResult[iter_7_1.id] + iter_7_1.number

	for iter_5_0, iter_5_1 in ipairs(var_5_0):
		var_5_1(iter_5_1.plan_drops)
		var_5_1(iter_5_1.event_drops)
		var_5_1(iter_5_1.spec_event_drops)

	arg_5_0.char = getProxy(EducateProxy).GetCharData()
	arg_5_0.natureIds = arg_5_0.char.GetAttrIdsByType(EducateChar.ATTR_TYPE_PERSONALITY)
	arg_5_0.majorIds = arg_5_0.char.GetAttrIdsByType(EducateChar.ATTR_TYPE_MAJOR)
	arg_5_0.minorIds = arg_5_0.char.GetAttrIdsByType(EducateChar.ATTR_TYPE_MINOR)
	arg_5_0.resIds = {
		EducateChar.RES_MOOD_ID,
		EducateChar.RES_MONEY_ID
	}

	arg_5_0.updatePersonalPanel()
	arg_5_0.updateMajorPanel()
	arg_5_0.updateMinorPanel()
	arg_5_0.updateResPanel()

def var_0_0.updatePersonalPanel(arg_8_0):
	local var_8_0 = EducateHelper.IsShowNature()

	setActive(arg_8_0.personalTF, var_8_0)

	if var_8_0:
		local var_8_1 = arg_8_0.findTF("content", arg_8_0.natureTF)

		for iter_8_0, iter_8_1 in ipairs(arg_8_0.natureIds):
			local var_8_2 = arg_8_0.findTF(tostring(iter_8_1), arg_8_0.personalTF)
			local var_8_3 = arg_8_0.char.GetAttrById(iter_8_1)

			setText(arg_8_0.findTF("old", var_8_2), pg.child_attr[iter_8_1].name .. " " .. var_8_3)

			local var_8_4 = arg_8_0.result[iter_8_1] or 0

			setActive(arg_8_0.findTF("new", var_8_2), var_8_4 != 0)

			if var_8_4 != 0:
				local var_8_5 = var_8_4 > 0 and "39BFFF" or "FF6767"
				local var_8_6 = var_8_4 > 0 and "+" or ""

				setText(arg_8_0.findTF("new", var_8_2), var_8_6 .. " " .. var_8_4)
				setTextColor(arg_8_0.findTF("new", var_8_2), Color.NewHex(var_8_5))

def var_0_0.updateMajorPanel(arg_9_0):
	for iter_9_0 = 1, arg_9_0.majorArrTF.childCount:
		local var_9_0 = arg_9_0.majorArrTF.GetChild(iter_9_0 - 1)
		local var_9_1 = arg_9_0.majorIds[iter_9_0]

		GetImageSpriteFromAtlasAsync("ui/educatecommonui_atlas", "attr_" .. var_9_1, arg_9_0.findTF("icon_bg/icon", var_9_0), True)
		setScrollText(arg_9_0.findTF("name_mask/name", var_9_0), pg.child_attr[var_9_1].name)

		local var_9_2 = arg_9_0.char.GetAttrInfo(var_9_1)

		setText(arg_9_0.findTF("grade/Text", var_9_0), var_9_2)

		local var_9_3 = arg_9_0.char.GetAttrById(var_9_1)

		setText(arg_9_0.findTF("value_old", var_9_0), var_9_3)

		local var_9_4 = EducateConst.GRADE_2_COLOR[var_9_2][1]
		local var_9_5 = EducateConst.GRADE_2_COLOR[var_9_2][2]

		setImageColor(arg_9_0.findTF("gradient", var_9_0), Color.NewHex(var_9_4))
		setImageColor(arg_9_0.findTF("grade", var_9_0), Color.NewHex(var_9_5))

		local var_9_6 = arg_9_0.result[var_9_1] or 0
		local var_9_7 = var_9_6 == 0 and "39393C" or "39BFFF"

		setActive(arg_9_0.findTF("VX", var_9_0), var_9_6 != 0)
		setImageColor(arg_9_0.findTF("arrow", var_9_0), Color.NewHex(var_9_7))
		setText(arg_9_0.findTF("value_new", var_9_0), var_9_3 + var_9_6)
		setTextColor(arg_9_0.findTF("value_new", var_9_0), Color.NewHex(var_9_7))

def var_0_0.updateMinorPanel(arg_10_0):
	for iter_10_0 = 1, arg_10_0.minorArrTF.childCount:
		local var_10_0 = arg_10_0.minorArrTF.GetChild(iter_10_0 - 1)
		local var_10_1 = arg_10_0.minorIds[iter_10_0]

		GetImageSpriteFromAtlasAsync("ui/educatecommonui_atlas", "attr_" .. var_10_1, arg_10_0.findTF("icon", var_10_0), True)
		setText(arg_10_0.findTF("name", var_10_0), pg.child_attr[var_10_1].name)

		local var_10_2 = arg_10_0.char.GetAttrById(var_10_1)

		setText(arg_10_0.findTF("value_add/value_old", var_10_0), var_10_2)

		local var_10_3 = arg_10_0.result[var_10_1] or 0

		setActive(arg_10_0.findTF("VX", var_10_0), var_10_3 != 0)
		setText(arg_10_0.findTF("value_add", var_10_0), "")

		if var_10_3 != 0:
			onDelayTick(function()
				setText(arg_10_0.findTF("value_add", var_10_0), "+" .. var_10_3), 0.891)

def var_0_0.updateResPanel(arg_12_0):
	for iter_12_0 = 1, #arg_12_0.resIds:
		local var_12_0 = arg_12_0.resTF.GetChild(iter_12_0 - 1)
		local var_12_1 = arg_12_0.resIds[iter_12_0]

		GetImageSpriteFromAtlasAsync("ui/educatecommonui_atlas", "res_" .. var_12_1, arg_12_0.findTF("icon", var_12_0), True)
		setText(arg_12_0.findTF("name", var_12_0), pg.child_resource[var_12_1].name)

		local var_12_2 = arg_12_0.char.GetResById(var_12_1)

		if var_12_2 < 0:
			var_12_2 = 0

		setText(arg_12_0.findTF("value_add/value_old", var_12_0), var_12_2)

		local var_12_3 = arg_12_0.resResult[var_12_1] or 0
		local var_12_4 = var_12_3 == 0 and "" or "+" .. var_12_3

		setText(arg_12_0.findTF("value_add", var_12_0), var_12_4)

def var_0_0._close(arg_13_0):
	if arg_13_0.inAnimPlaying:
		return

	arg_13_0.anim.Play("anim_educate_result_out")

def var_0_0.onBackPressed(arg_14_0):
	arg_14_0._close()

def var_0_0.willExit(arg_15_0):
	getProxy(EducateProxy).OnNextWeek()
	arg_15_0.animEvent.SetEndEvent(None)

	if arg_15_0.drops:
		EducateHelper.UpdateDropsData(arg_15_0.drops)

	pg.UIMgr.GetInstance().UnblurPanel(arg_15_0._tf)

	if arg_15_0.contextData.onExit:
		arg_15_0.contextData.onExit()

return var_0_0
