local var_0_0 = class("SelectTechnologyLayer", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "SelectTechnologyUI"

def var_0_0.ResUISettings(arg_2_0):
	return True

def var_0_0.setPlayer(arg_3_0, arg_3_1):
	arg_3_0.playerVO = arg_3_1

def var_0_0.init(arg_4_0):
	pg.UIMgr.GetInstance().OverlayPanel(arg_4_0._tf, {
		weight = LayerWeightConst.LOWER_LAYER
	})

	arg_4_0.bg = arg_4_0.findTF("frame/bg")
	arg_4_0.bluePrintBtn = arg_4_0.findTF("blueprint_btn", arg_4_0.bg)
	arg_4_0.bluePrintBtnTip = arg_4_0.bluePrintBtn.Find("tip")
	arg_4_0.technologyBtn = arg_4_0.findTF("technology_btn", arg_4_0.bg)
	arg_4_0.technologyBtnTip = arg_4_0.technologyBtn.Find("tip")
	arg_4_0.fleetBtn = arg_4_0.findTF("fleet_btn", arg_4_0.bg)
	arg_4_0.fleetBtnTip = arg_4_0.fleetBtn.Find("tip")
	arg_4_0.transformBtn = arg_4_0.findTF("transform_btn", arg_4_0.bg)
	arg_4_0.transformBtnTip = arg_4_0.transformBtn.Find("tip")

	setActive(arg_4_0.transformBtn, not LOCK_EQUIPMENT_TRANSFORM)

	arg_4_0.metaBtn = arg_4_0.findTF("meta_btn", arg_4_0.bg)
	arg_4_0.metaBtnTip = arg_4_0.metaBtn.Find("tip")

	setActive(arg_4_0.metaBtn, True)

	arg_4_0.helpBtn = arg_4_0.findTF("help_btn")
	arg_4_0.lockedTpl = arg_4_0.findTF("lockedTpl")
	arg_4_0.backBtn = arg_4_0.findTF("blur_panel/adapt/top/back")

	if not OPEN_TEC_TREE_SYSTEM:
		setActive(arg_4_0.fleetBtn, False)

def var_0_0.didEnter(arg_5_0):
	arg_5_0.checkSystemOpen("ShipBluePrintMediator", arg_5_0.bluePrintBtn)
	arg_5_0.checkSystemOpen("TechnologyMediator", arg_5_0.technologyBtn)
	arg_5_0.checkSystemOpen("EquipmentTransformTreeMediator", arg_5_0.transformBtn)
	arg_5_0.checkSystemOpen("MetaCharacterMediator", arg_5_0.metaBtn)
	onButton(arg_5_0, arg_5_0.fleetBtn, function()
		arg_5_0.emit(TechnologyConst.OPEN_TECHNOLOGY_TREE_SCENE), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.bluePrintBtn, function()
		arg_5_0.emit(SelectTechnologyMediator.ON_BLUEPRINT), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.technologyBtn, function()
		arg_5_0.emit(SelectTechnologyMediator.ON_TECHNOLOGY), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.transformBtn, function()
		arg_5_0.emit(SelectTechnologyMediator.ON_TRANSFORM_EQUIPMENT), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.metaBtn, function()
		if isActive(arg_5_0.findTF("word", arg_5_0.metaBtn)):
			arg_5_0.emit(SelectTechnologyMediator.ON_META)
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("meta_sys_lock_tip")), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.backBtn, function()
		arg_5_0.emit(var_0_0.ON_BACK), SFX_CANCEL)
	onButton(arg_5_0, arg_5_0.helpBtn, function()
		local var_12_0 = pg.SystemOpenMgr.GetInstance().isOpenSystem(arg_5_0.playerVO.level, "ShipBluePrintMediator") and "help_technolog" or "help_technolog0"

		if pg.gametip[var_12_0]:
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				type = MSGBOX_TYPE_HELP,
				helps = pg.gametip[var_12_0].tip,
				weight = LayerWeightConst.SECOND_LAYER
			}), SFX_PANEL)

def var_0_0.checkSystemOpen(arg_13_0, arg_13_1, arg_13_2):
	if arg_13_1 == "MetaCharacterMediator":
		local var_13_0 = True

		setActive(arg_13_0.findTF("word", arg_13_2), var_13_0)
		setGray(arg_13_2, not var_13_0)

		arg_13_2.GetComponent(typeof(Image)).color = Color.New(1, 1, 1, var_13_0 and 1 or 0.7)

		local var_13_1 = arg_13_0.findTF("locked", arg_13_2)

		if var_13_1:
			setActive(var_13_1, False)

		if not var_13_0:
			if IsNil(var_13_1):
				var_13_1 = cloneTplTo(arg_13_0.lockedTpl, arg_13_2)
				var_13_1.localPosition = Vector3.zero

			setActive(var_13_1, True)

		return

	local var_13_2 = pg.SystemOpenMgr.GetInstance().isOpenSystem(arg_13_0.playerVO.level, arg_13_1)

	setActive(arg_13_0.findTF("word", arg_13_2), var_13_2)
	setGray(arg_13_2, not var_13_2)

	arg_13_2.GetComponent(typeof(Image)).color = Color.New(1, 1, 1, var_13_2 and 1 or 0.7)

	local var_13_3 = arg_13_0.findTF("locked", arg_13_2)

	if var_13_3:
		setActive(var_13_3, False)

	if not var_13_2:
		if IsNil(var_13_3):
			var_13_3 = cloneTplTo(arg_13_0.lockedTpl, arg_13_2)
			var_13_3.localPosition = Vector3.zero

		setActive(var_13_3, True)

def var_0_0.notifyTechnology(arg_14_0, arg_14_1):
	setActive(arg_14_0.technologyBtnTip, arg_14_1)

def var_0_0.notifyBlueprint(arg_15_0, arg_15_1):
	setActive(arg_15_0.bluePrintBtnTip, arg_15_1)

def var_0_0.notifyFleet(arg_16_0, arg_16_1):
	setActive(arg_16_0.fleetBtnTip, arg_16_1)

def var_0_0.notifyTransform(arg_17_0, arg_17_1):
	setActive(arg_17_0.transformBtnTip, arg_17_1)

def var_0_0.notifyMeta(arg_18_0, arg_18_1):
	setActive(arg_18_0.metaBtnTip, arg_18_1)

def var_0_0.willExit(arg_19_0):
	return

return var_0_0
