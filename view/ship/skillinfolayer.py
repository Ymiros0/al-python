local var_0_0 = class("SkillInfoLayer", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "SkillInfoUI"

def var_0_0.init(arg_2_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_2_0._tf, False, {
		weight = arg_2_0.getWeightFromData()
	})

	arg_2_0.backBtn = arg_2_0.findTF("panel/top/btnBack")
	arg_2_0.skillInfoName = arg_2_0.findTF("panel/bg/skill_name")
	arg_2_0.skillInfoLv = arg_2_0.findTF("panel/bg/skill_lv")
	arg_2_0.skillInfoIntro = arg_2_0.findTF("panel/bg/help_panel/skill_intro")
	arg_2_0.skillInfoIcon = arg_2_0.findTF("panel/bg/skill_icon")
	arg_2_0.btnTypeNormal = arg_2_0.findTF("panel/bg/btn_type_normal")
	arg_2_0.btnTypeWorld = arg_2_0.findTF("panel/bg/btn_type_world")
	arg_2_0.buttonList = arg_2_0.findTF("panel/buttonList")
	arg_2_0.upgradeBtn = arg_2_0.findTF("panel/buttonList/level_button")
	arg_2_0.metaBtn = arg_2_0.findTF("panel/buttonList/meta_button")

	setText(arg_2_0.findTF("Image", arg_2_0.metaBtn), i18n("meta_skillbtn_tactics"))

def var_0_0.didEnter(arg_3_0):
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.emit(var_0_0.ON_CLOSE), SFX_CANCEL)
	onButton(arg_3_0, arg_3_0.backBtn, function()
		arg_3_0.emit(var_0_0.ON_CLOSE), SFX_CANCEL)
	onButton(arg_3_0, arg_3_0.findTF("panel/buttonList/ok_button"), function()
		arg_3_0.emit(var_0_0.ON_CLOSE), SFX_CONFIRM)
	onButton(arg_3_0, arg_3_0.upgradeBtn, function()
		arg_3_0.emit(SkillInfoMediator.WARP_TO_TACTIC), SFX_UI_CLICK)
	onButton(arg_3_0, arg_3_0.metaBtn, function()
		local var_8_0 = arg_3_0.contextData.shipId
		local var_8_1
		local var_8_2

		if var_8_0:
			var_8_2 = getProxy(BayProxy).getShipById(arg_3_0.contextData.shipId)
			var_8_1 = var_8_2.isMetaShip()

		if var_8_1:
			arg_3_0.emit(SkillInfoMediator.WARP_TO_META_TACTICS, var_8_2.configId), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.btnTypeNormal, function()
		arg_3_0.showInfo(False)
		arg_3_0.flushTypeBtn(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.btnTypeWorld, function()
		arg_3_0.showInfo(True)
		arg_3_0.flushTypeBtn(), SFX_PANEL)

	if tobool(pg.skill_world_display[arg_3_0.contextData.skillId]):
		arg_3_0.flushTypeBtn()
	else
		setActive(arg_3_0.btnTypeNormal, False)
		setActive(arg_3_0.btnTypeWorld, False)

	arg_3_0.showBase()
	arg_3_0.showInfo(False)

def var_0_0.flushTypeBtn(arg_11_0):
	setActive(arg_11_0.btnTypeNormal, arg_11_0.isWorld)
	setActive(arg_11_0.btnTypeWorld, not arg_11_0.isWorld)

def var_0_0.showBase(arg_12_0):
	local var_12_0 = arg_12_0.contextData.skillId
	local var_12_1 = arg_12_0.contextData.skillOnShip

	setText(arg_12_0.skillInfoName, getSkillName(var_12_0))

	local var_12_2 = getSkillConfig(var_12_0)

	LoadImageSpriteAsync("skillicon/" .. var_12_2.icon, arg_12_0.skillInfoIcon)

	local var_12_3 = not arg_12_0.contextData.fromNewShip and var_12_1 and var_12_1.level < #var_12_2 and var_12_1.id != 22262 and var_12_1.id != 22261

	setActive(arg_12_0.upgradeBtn, var_12_3)

	local var_12_4 = arg_12_0.contextData.shipId
	local var_12_5
	local var_12_6

	if var_12_4:
		var_12_5 = getProxy(BayProxy).getShipById(arg_12_0.contextData.shipId).isMetaShip()

	local var_12_7 = MetaCharacterConst.isMetaTaskSkillID(var_12_0)

	setActive(arg_12_0.metaBtn, var_12_5 and var_12_7)

	if var_12_5:
		setActive(arg_12_0.upgradeBtn, False)

def var_0_0.showInfo(arg_13_0, arg_13_1):
	arg_13_0.isWorld = arg_13_1

	local var_13_0 = arg_13_0.contextData.skillId
	local var_13_1 = arg_13_0.contextData.skillOnShip
	local var_13_2 = var_13_1 and var_13_1.level or 1

	setText(arg_13_0.skillInfoLv, "Lv." .. var_13_2)

	if arg_13_0.contextData.fromNewShip:
		setText(arg_13_0.skillInfoIntro, getSkillDescGet(var_13_0, arg_13_1))
	else
		setText(arg_13_0.skillInfoIntro, getSkillDesc(var_13_0, var_13_2, arg_13_1))

def var_0_0.close(arg_14_0):
	arg_14_0.emit(var_0_0.ON_CLOSE)

def var_0_0.willExit(arg_15_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_15_0._tf)

	if arg_15_0.contextData.onExit:
		arg_15_0.contextData.onExit()

return var_0_0
