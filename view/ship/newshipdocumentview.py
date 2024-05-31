local var_0_0 = class("NewShipDocumentView", import("..base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "NewShipDocumentView"

def var_0_0.OnInit(arg_2_0):
	arg_2_0.InitUI()
	arg_2_0.AddListener()
	setActive(arg_2_0._tf, True)
	LeanTween.move(rtf(arg_2_0._tf), Vector3(-30, 0, 0), 0.3)

def var_0_0.OnDestroy(arg_3_0):
	arg_3_0._shipVO = None
	arg_3_0.confirmFunc = None

def var_0_0.InitUI(arg_4_0):
	arg_4_0.skillContainer = arg_4_0.findTF("bg/skill_panel/frame/skill_list/viewport")
	arg_4_0.skillTpl = arg_4_0.getTpl("bg/skill_panel/frame/skilltpl", arg_4_0._tf)
	arg_4_0.emptyTpl = arg_4_0.getTpl("bg/skill_panel/frame/emptytpl", arg_4_0._tf)
	arg_4_0.addTpl = arg_4_0.getTpl("bg/skill_panel/frame/addtpl", arg_4_0._tf)

def var_0_0.AddListener(arg_5_0):
	onButton(arg_5_0, arg_5_0.findTF("qr_btn"), function()
		arg_5_0.confirmFunc(), SFX_CONFIRM)

def var_0_0.initSkills(arg_7_0):
	local var_7_0 = arg_7_0._shipVO.getMaxConfigId()
	local var_7_1 = pg.ship_data_template[var_7_0]
	local var_7_2 = 1

	for iter_7_0, iter_7_1 in ipairs(var_7_1.buff_list_display):
		local var_7_3 = getSkillConfig(iter_7_1)
		local var_7_4 = arg_7_0._shipVO.skills
		local var_7_5

		if var_7_4[iter_7_1]:
			var_7_5 = cloneTplTo(arg_7_0.skillTpl, arg_7_0.skillContainer)

			onButton(arg_7_0, var_7_5, function()
				arg_7_0.emit(NewShipMediator.ON_SKILLINFO, var_7_3.id, var_7_4[iter_7_1]), SFX_PANEL)
		else
			var_7_5 = cloneTplTo(arg_7_0.emptyTpl, arg_7_0.skillContainer)

			setActive(arg_7_0.findTF("mask", var_7_5), True)
			onButton(arg_7_0, var_7_5, function()
				arg_7_0.emit(NewShipMediator.ON_SKILLINFO, var_7_3.id), SFX_PANEL)

		var_7_2 = var_7_2 + 1

		LoadImageSpriteAsync("skillicon/" .. var_7_3.icon, findTF(var_7_5, "icon"))

	for iter_7_2 = var_7_2, 3:
		cloneTplTo(arg_7_0.addTpl, arg_7_0.skillContainer)

def var_0_0.UpdatePropertyPanel(arg_10_0):
	arg_10_0.propertyPanel = PropertyPanel.New(arg_10_0.findTF("bg/property_panel/frame"))

	arg_10_0.propertyPanel.initProperty(arg_10_0._shipVO.configId)

def var_0_0.getTpl(arg_11_0, arg_11_1, arg_11_2):
	local var_11_0 = arg_11_0.findTF(arg_11_1, arg_11_2)

	var_11_0.SetParent(arg_11_0._tf, False)
	SetActive(var_11_0, False)

	return var_11_0

def var_0_0.SetParams(arg_12_0, arg_12_1, arg_12_2):
	arg_12_0._shipVO = arg_12_1
	arg_12_0.confirmFunc = arg_12_2

def var_0_0.RefreshUI(arg_13_0):
	arg_13_0.initSkills()
	arg_13_0.UpdatePropertyPanel()

return var_0_0
