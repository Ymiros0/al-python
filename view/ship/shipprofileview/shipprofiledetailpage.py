local var_0_0 = class("ShipProfileDetailPage", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "ShipProfileDetailPage"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.detailRightBlurRect = arg_2_0.findTF("bg")
	arg_2_0.propertyTF = arg_2_0.findTF("bg/property_panel/frame")
	arg_2_0.skillRect = arg_2_0.findTF("bg/skill_panel/frame/skills_rect")
	arg_2_0.skillPanel = arg_2_0.findTF("skills", arg_2_0.skillRect)
	arg_2_0.skillTpl = arg_2_0.findTF("skilltpl", arg_2_0.skillRect)
	arg_2_0.skillArrLeft = arg_2_0.findTF("bg/skill_panel/frame/arrow1")
	arg_2_0.skillArrRight = arg_2_0.findTF("bg/skill_panel/frame/arrow2")

def var_0_0.OnInit(arg_3_0):
	return

def var_0_0.EnterAnim(arg_4_0, arg_4_1, arg_4_2):
	LeanTween.moveX(rtf(arg_4_0._tf), 0, arg_4_1).setEase(LeanTweenType.easeInOutSine).setOnComplete(System.Action(function()
		if arg_4_2:
			arg_4_2()))

def var_0_0.ExistAnim(arg_6_0, arg_6_1, arg_6_2):
	LeanTween.moveX(rtf(arg_6_0._tf), 1000, arg_6_1).setEase(LeanTweenType.easeInOutSine).setOnComplete(System.Action(function()
		if arg_6_2:
			arg_6_2()

		arg_6_0.Hide()))

def var_0_0.Update(arg_8_0, arg_8_1, arg_8_2, arg_8_3):
	arg_8_0.Show()

	arg_8_0.shipGroup = arg_8_1
	arg_8_0.showTrans = arg_8_2

	arg_8_0.InitSkills()
	arg_8_0.InitProperty()

	if arg_8_3:
		arg_8_3()

def var_0_0.InitProperty(arg_9_0):
	arg_9_0.propertyPanel = PropertyPanel.New(arg_9_0.propertyTF)

	arg_9_0.propertyPanel.initProperty(arg_9_0.shipGroup.shipConfig.id)

	if arg_9_0.showTrans and arg_9_0.shipGroup.trans:
		arg_9_0.propertyPanel.initRadar(arg_9_0.shipGroup.groupConfig.trans_radar_chart)

def var_0_0.InitSkills(arg_10_0):
	local var_10_0 = pg.ship_data_template[arg_10_0.shipGroup.getShipConfigId(arg_10_0.showTrans)]
	local var_10_1 = 0
	local var_10_2 = Clone(var_10_0.buff_list_display)

	if not arg_10_0.showTrans:
		_.each(arg_10_0.shipGroup.groupConfig.trans_skill, function(arg_11_0)
			table.removebyvalue(var_10_2, arg_11_0))

	local var_10_3 = arg_10_0.skillPanel.childCount
	local var_10_4 = #var_10_2 < 3 and 3 or #var_10_2

	for iter_10_0 = var_10_3 + 1, var_10_4:
		cloneTplTo(arg_10_0.skillTpl, arg_10_0.skillPanel)

	local var_10_5 = arg_10_0.skillPanel.childCount

	for iter_10_1 = 1, var_10_5:
		local var_10_6 = arg_10_0.skillPanel.GetChild(iter_10_1 - 1)

		if iter_10_1 <= #var_10_2:
			local var_10_7 = var_10_2[iter_10_1]

			arg_10_0.UpdateSkill(var_10_6, var_10_7)
		else
			setActive(arg_10_0.findTF("icon", var_10_6), False)
			setActive(arg_10_0.findTF("add", var_10_6), True)

		setActive(var_10_6, iter_10_1 <= var_10_4)

	setActive(arg_10_0.skillArrLeft, #var_10_2 > 3)
	setActive(arg_10_0.skillArrRight, #var_10_2 > 3)

	if #var_10_2 > 3:
		onScroll(arg_10_0, arg_10_0.skillRect, function(arg_12_0)
			setActive(arg_10_0.skillArrLeft, arg_12_0.x > 0.01)
			setActive(arg_10_0.skillArrRight, arg_12_0.x < 0.99))
	else
		GetComponent(arg_10_0.skillRect, typeof(ScrollRect)).onValueChanged.RemoveAllListeners()

	setAnchoredPosition(arg_10_0.skillPanel, {
		x = 0
	})

def var_0_0.UpdateSkill(arg_13_0, arg_13_1, arg_13_2):
	if arg_13_0.shipGroup.isBluePrintGroup():
		for iter_13_0, iter_13_1 in ipairs(arg_13_0.shipGroup.getBluePrintChangeSkillList()):
			if iter_13_1[1] == arg_13_2:
				arg_13_2 = iter_13_1[2]

				break

	local var_13_0 = findTF(arg_13_1, "icon")
	local var_13_1 = getSkillConfig(arg_13_2)

	LoadImageSpriteAsync("skillicon/" .. var_13_1.icon, var_13_0)
	setActive(arg_13_0.findTF("icon", arg_13_1), True)
	setActive(arg_13_0.findTF("add", arg_13_1), False)
	onButton(arg_13_0, arg_13_1, function()
		arg_13_0.emit(ShipProfileScene.SHOW_SKILL_INFO, var_13_1.id, {
			id = var_13_1.id,
			level = pg.skill_data_template[var_13_1.id].max_level
		}), SFX_PANEL)

def var_0_0.OnDestroy(arg_15_0):
	return

return var_0_0
