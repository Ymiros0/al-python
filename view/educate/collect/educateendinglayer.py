local var_0_0 = class("EducateEndingLayer", import(".EducateCollectLayerTemplate"))

def var_0_0.getUIName(arg_1_0):
	return "EducateEndingUI"

def var_0_0.initConfig(arg_2_0):
	arg_2_0.config = pg.child_ending

def var_0_0.didEnter(arg_3_0):
	setText(arg_3_0.findTF("review_btn/Text", arg_3_0.performTF), i18n("child_btn_review"))

	arg_3_0.endings = getProxy(EducateProxy).GetFinishEndings()
	arg_3_0.char = getProxy(EducateProxy).GetCharData()
	arg_3_0.tpl = arg_3_0.findTF("condition_tpl", arg_3_0.windowTF)

	setText(arg_3_0.curCntTF, #arg_3_0.endings)
	setText(arg_3_0.allCntTF, "/" .. #arg_3_0.config.all)
	arg_3_0.updatePage()

def var_0_0.updateItem(arg_4_0, arg_4_1, arg_4_2):
	local var_4_0 = table.contains(arg_4_0.endings, arg_4_1.id)

	if var_4_0:
		LoadImageSpriteAsync("bg/" .. arg_4_1.pic, arg_4_0.findTF("unlock/mask/Image", arg_4_2))
		setText(arg_4_0.findTF("unlock/name", arg_4_2), arg_4_1.name)
		onButton(arg_4_0, arg_4_2, function()
			arg_4_0.showPerformWindow(arg_4_1), SFX_PANEL)
	else
		removeOnButton(arg_4_2)

		local var_4_1 = arg_4_0.findTF("lock/conditions", arg_4_2)
		local var_4_2 = arg_4_1.condition

		arg_4_0.updateConditions(var_4_2, var_4_1)

	setActive(arg_4_0.findTF("unlock", arg_4_2), var_4_0)
	setActive(arg_4_0.findTF("lock", arg_4_2), not var_4_0)

def var_0_0.updateConditions(arg_6_0, arg_6_1, arg_6_2):
	local var_6_0 = 0

	for iter_6_0 = 1, #arg_6_1:
		local var_6_1 = arg_6_1[iter_6_0]

		if var_6_1[1] == EducateConst.DROP_TYPE_ATTR:
			var_6_0 = var_6_0 + 1

			local var_6_2 = iter_6_0 <= arg_6_2.childCount and arg_6_2.GetChild(iter_6_0 - 1) or cloneTplTo(arg_6_0.tpl, arg_6_2)
			local var_6_3 = False
			local var_6_4 = ""

			if var_6_1[3]:
				var_6_3 = arg_6_0.char.GetAttrById(var_6_1[2]) >= var_6_1[3]
				var_6_4 = pg.child_attr[var_6_1[2]].name .. " > " .. var_6_1[3]
			else
				var_6_3 = arg_6_0.char.GetPersonalityId() == var_6_1[2]
				var_6_4 = i18n("child_nature_title") .. pg.child_attr[var_6_1[2]].name

			setActive(arg_6_0.findTF("icon/unlock", var_6_2), var_6_3)

			local var_6_5 = var_6_3 and "F59F48" or "888888"

			setTextColor(arg_6_0.findTF("Text", var_6_2), Color.NewHex(var_6_5))
			setText(arg_6_0.findTF("Text", var_6_2), var_6_4)

	for iter_6_1 = 1, arg_6_2.childCount:
		setActive(arg_6_2.GetChild(iter_6_1 - 1), iter_6_1 <= var_6_0)

def var_0_0.showPerformWindow(arg_7_0, arg_7_1):
	local var_7_0 = arg_7_0.findTF("Image", arg_7_0.performTF)

	LoadImageSpriteAsync("bg/" .. arg_7_1.pic, var_7_0)
	setActive(arg_7_0.performTF, True)
	onButton(arg_7_0, var_7_0, function()
		setActive(arg_7_0.performTF, False), SFX_PANEL)
	onButton(arg_7_0, arg_7_0.findTF("review_btn", arg_7_0.performTF), function()
		pg.PerformMgr.GetInstance().PlayGroup(arg_7_1.performance), SFX_PANEL)

def var_0_0.playAnimChange(arg_10_0):
	arg_10_0.anim.Stop()
	arg_10_0.anim.Play("anim_educate_ending_change")

def var_0_0.playAnimClose(arg_11_0):
	arg_11_0.anim.Play("anim_educate_ending_out")

return var_0_0
