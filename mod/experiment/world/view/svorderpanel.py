local var_0_0 = class("SVOrderPanel", import("view.base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "SVOrderPanel"

def var_0_0.getBGM(arg_2_0):
	return "echo-loop"

def var_0_0.OnLoaded(arg_3_0):
	return

def var_0_0.OnInit(arg_4_0):
	local var_4_0 = arg_4_0._tf
	local var_4_1 = var_4_0.Find("adapt/order_list")

	arg_4_0.btnRedeploy = var_4_1.Find("redeploy")
	arg_4_0.btnExpansion = var_4_1.Find("expansion")
	arg_4_0.btnMaintenance = var_4_1.Find("maintenance")
	arg_4_0.btnFOV = var_4_1.Find("fov")
	arg_4_0.btnSubmarine = var_4_1.Find("submarine")
	arg_4_0.btnHelp = var_4_0.Find("adapt/help")

	onButton(arg_4_0, arg_4_0.btnHelp, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("world_instruction_help_1")
		}), SFX_PANEL)

	arg_4_0.btnBack = var_4_0.Find("adapt/back")

	onButton(arg_4_0, arg_4_0.btnBack, function()
		arg_4_0.Hide(), SFX_CANCEL)

	arg_4_0.rtRing = var_4_0.Find("bg/ring")
	arg_4_0.wsCompass = WSCompass.New()
	arg_4_0.wsCompass.tf = var_4_0.Find("bg/ring/compass")
	arg_4_0.wsCompass.pool = arg_4_0.contextData.wsPool

	arg_4_0.wsCompass.Setup(True)

	arg_4_0.rtMsgbox = var_4_0.Find("Msgbox")

	setText(arg_4_0.rtMsgbox.Find("window/top/bg/infomation/title"), i18n("title_info"))
	setActive(arg_4_0.rtMsgbox, False)
	onButton(arg_4_0, arg_4_0.rtMsgbox.Find("bg"), function()
		arg_4_0.HideMsgbox(), SFX_CANCEL)
	onButton(arg_4_0, arg_4_0.rtMsgbox.Find("window/top/btnBack"), function()
		arg_4_0.HideMsgbox(), SFX_CANCEL)

	arg_4_0.rtMsgStamina = arg_4_0.rtMsgbox.Find("window/top/bg/stamina")

	setText(arg_4_0.rtMsgStamina.Find("name"), i18n("world_ap"))

	arg_4_0.rtMsgBase = arg_4_0.rtMsgbox.Find("window/msg_panel/base")
	arg_4_0.rtMsgExtra = arg_4_0.rtMsgbox.Find("window/msg_panel/extra")
	arg_4_0.rtMsgBtns = arg_4_0.rtMsgbox.Find("window/button_container")

	setText(arg_4_0.rtMsgBtns.Find("btn_setting/pic"), i18n("msgbox_text_save"))
	setText(arg_4_0.rtMsgBtns.Find("btn_confirm/pic"), i18n("text_confirm"))
	setText(arg_4_0.rtMsgBtns.Find("btn_cancel/pic"), i18n("text_cancel"))
	onButton(arg_4_0, arg_4_0.rtMsgBtns.Find("btn_cancel"), function()
		arg_4_0.HideMsgbox(), SFX_CANCEL)

def var_0_0.OnDestroy(arg_10_0):
	arg_10_0.ClearBtnTimers()
	arg_10_0.wsCompass.Dispose()

def var_0_0.Show(arg_11_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_11_0._tf, False)
	var_0_0.super.Show(arg_11_0)

def var_0_0.Hide(arg_12_0):
	if isActive(arg_12_0.rtMsgbox):
		arg_12_0.HideMsgbox()

	pg.UIMgr.GetInstance().UnblurPanel(arg_12_0._tf, arg_12_0._parentTf)
	arg_12_0.ClearComppass()
	arg_12_0.ClearBtnTimers()
	var_0_0.super.Hide(arg_12_0)

def var_0_0.Setup(arg_13_0, arg_13_1, arg_13_2, arg_13_3):
	arg_13_0.Update(arg_13_1, arg_13_2)
	arg_13_0.wsCompass.SetAnchorEulerAngles(arg_13_3)

def var_0_0.Update(arg_14_0, arg_14_1, arg_14_2):
	if arg_14_0.entrance != arg_14_1 or arg_14_0.map != arg_14_2 or arg_14_0.gid != arg_14_2.gid:
		arg_14_0.entrance = arg_14_1
		arg_14_0.map = arg_14_2
		arg_14_0.gid = arg_14_2.gid

	arg_14_0.UpdateCompassMarks()
	arg_14_0.UpdateOrderBtn()

def var_0_0.SetButton(arg_15_0, arg_15_1, arg_15_2):
	local var_15_0 = arg_15_1.Find("type_lock")
	local var_15_1 = arg_15_1.Find("type_unable")
	local var_15_2 = arg_15_1.Find("type_enable")
	local var_15_3 = nowWorld().IsSystemOpen(arg_15_2.system)

	setActive(var_15_0, not var_15_3)
	setActive(var_15_1, not isActive(var_15_0) and (arg_15_2.isLock or arg_15_2.timeStamp and arg_15_2.timeStamp > pg.TimeMgr.GetInstance().GetServerTime()))
	setActive(var_15_2, not isActive(var_15_0) and not isActive(var_15_1))

	if isActive(var_15_0):
		onButton(arg_15_0, var_15_0, function()
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_instruction_all_1")), SFX_CONFIRM)

	if isActive(var_15_1):
		setActive(var_15_1.Find("cost"), arg_15_2.isLock)
		setActive(var_15_1.Find("time"), not arg_15_2.isLock)

		if arg_15_2.isLock:
			setText(var_15_1.Find("cost/Text"), arg_15_2.cost)
			onButton(arg_15_0, var_15_1, arg_15_2.lockFunc, SFX_CONFIRM)
		else
			arg_15_0.timers[var_15_1] = Timer.New(function()
				local var_17_0 = arg_15_2.timeStamp - pg.TimeMgr.GetInstance().GetServerTime()

				if var_17_0 < 0:
					arg_15_0.UpdateOrderBtn()
				else
					setText(var_15_1.Find("time/Text"), string.format("%d.%02d.%02d", math.floor(var_17_0 / 3600), math.floor(var_17_0 % 3600 / 60), var_17_0 % 60)), 1, -1)

			arg_15_0.timers[var_15_1].func()
			arg_15_0.timers[var_15_1].Start()
			onButton(arg_15_0, var_15_1, arg_15_2.timeFunc, SFX_CONFIRM)

	if isActive(var_15_2):
		setText(var_15_2.Find("cost/Text"), arg_15_2.cost)
		onButton(arg_15_0, var_15_2, arg_15_2.enableFunc, SFX_CONFIRM)

def var_0_0.UpdateOrderBtn(arg_18_0):
	arg_18_0.ClearBtnTimers()

	arg_18_0.timers = {}

	local var_18_0 = nowWorld()
	local var_18_1 = arg_18_0.map.GetConfig("instruction_available")
	local var_18_2 = checkExist(arg_18_0.map, {
		"GetPort"
	})
	local var_18_3 = var_18_0.GetRealm()
	local var_18_4 = var_18_0.IsSystemOpen(WorldConst.SystemOrderRedeploy) and var_18_3 == checkExist(var_18_2, {
		"GetRealm"
	}) and checkExist(var_18_2, {
		"IsOpen",
		{
			var_18_3,
			var_18_0.GetProgress()
		}
	}) and var_18_0.BuildFormationIds()
	local var_18_5 = {
		system = WorldConst.SystemOrderRedeploy,
		isLock = not var_18_4,
		def lockFunc:()
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_instruction_redeploy_1")),
		cost = var_18_0.CalcOrderCost(WorldConst.OpReqRedeploy),
		def enableFunc:(arg_20_0, arg_20_1)
			arg_18_0.Hide()
			arg_18_0.emit(WorldScene.SceneOp, "OpRedeploy")
	}

	arg_18_0.SetButton(arg_18_0.btnRedeploy, var_18_5)
	arg_18_0.SetButton(arg_18_0.btnExpansion, var_18_5)
	setActive(arg_18_0.btnRedeploy, var_18_4 != WorldConst.FleetExpansion)
	setActive(arg_18_0.btnExpansion, var_18_4 == WorldConst.FleetExpansion)
	arg_18_0.SetButton(arg_18_0.btnSubmarine, {
		system = WorldConst.SystemOrderSubmarine,
		isLock = var_18_1[1] == 0 or not var_18_0.CanCallSubmarineSupport() or var_18_0.IsSubmarineSupporting() and var_18_0.GetSubAidFlag(),
		def lockFunc:()
			if var_18_1[1] == 0:
				pg.TipsMgr.GetInstance().ShowTips(i18n("world_instruction_submarine_1"))
			elif not var_18_0.CanCallSubmarineSupport():
				pg.TipsMgr.GetInstance().ShowTips(i18n("world_instruction_submarine_4"))
			else
				pg.TipsMgr.GetInstance().ShowTips(i18n("world_instruction_submarine_3")),
		cost = var_18_0.CalcOrderCost(WorldConst.OpReqSub),
		def enableFunc:()
			arg_18_0.ShowMsgbox(WorldConst.OpReqSub)
	})
	arg_18_0.SetButton(arg_18_0.btnFOV, {
		system = WorldConst.SystemOrderFOV,
		isLock = var_18_1[2] == 0 or arg_18_0.map.visionFlag,
		def lockFunc:()
			if var_18_1[2] == 0:
				pg.TipsMgr.GetInstance().ShowTips(i18n("world_instruction_submarine_1"))
			else
				pg.TipsMgr.GetInstance().ShowTips(i18n("world_instruction_detect_2")),
		cost = var_18_0.CalcOrderCost(WorldConst.OpReqVision),
		def enableFunc:()
			arg_18_0.ShowMsgbox(WorldConst.OpReqVision)
	})

	local var_18_6 = pg.TimeMgr.GetInstance()
	local var_18_7 = pg.gameset.world_instruction_maintenance.description[2]
	local var_18_8 = var_18_0.GetReqCDTime(WorldConst.OpReqMaintenance) + var_18_7

	arg_18_0.SetButton(arg_18_0.btnMaintenance, {
		system = WorldConst.SystemOrderMaintenance,
		isLock = var_18_1[3] == 0,
		def lockFunc:()
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_instruction_submarine_1")),
		timeStamp = var_18_8,
		def timeFunc:(arg_26_0)
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_instruction_supply_2", var_18_6.DescCDTime(var_18_8 - pg.TimeMgr.GetInstance().GetServerTime()))),
		cost = var_18_0.CalcOrderCost(WorldConst.OpReqMaintenance),
		def enableFunc:()
			arg_18_0.ShowMsgbox(WorldConst.OpReqMaintenance)
	})

def var_0_0.ClearBtnTimers(arg_28_0):
	if arg_28_0.timers:
		for iter_28_0, iter_28_1 in pairs(arg_28_0.timers):
			iter_28_1.Stop()

	arg_28_0.timers = None

def var_0_0.UpdateCompassMarks(arg_29_0):
	arg_29_0.wsCompass.ClearMarks()
	arg_29_0.wsCompass.Update(arg_29_0.entrance, arg_29_0.map)

def var_0_0.ClearComppass(arg_30_0):
	arg_30_0.wsCompass.map = None

	arg_30_0.wsCompass.RemoveCellsListener()

def var_0_0.ShowMsgbox(arg_31_0, arg_31_1):
	local var_31_0 = nowWorld()
	local var_31_1 = var_31_0.staminaMgr.GetTotalStamina()

	setText(arg_31_0.rtMsgStamina.Find("Text"), var_31_1)

	local var_31_2 = var_31_0.CalcOrderCost(arg_31_1)
	local var_31_3 = ""
	local var_31_4 = ""
	local var_31_5

	if arg_31_1 == WorldConst.OpReqMaintenance:
		var_31_3 = i18n("world_instruction_morale_1", setColorStr(var_31_2, COLOR_GREEN), setColorStr(var_31_1, var_31_2 <= var_31_1 and COLOR_GREEN or COLOR_RED))
		var_31_4 = i18n("world_instruction_morale_4")

		function var_31_5()
			arg_31_0.emit(WorldScene.SceneOp, "OpReqMaintenance", arg_31_0.map.GetFleet().id)
	elif arg_31_1 == WorldConst.OpReqSub:
		var_31_3 = i18n(var_31_0.IsSubmarineSupporting() and "world_instruction_submarine_7" or "world_instruction_submarine_2", setColorStr(var_31_2, COLOR_GREEN), setColorStr(var_31_1, var_31_2 <= var_31_1 and COLOR_GREEN or COLOR_RED))
		var_31_4 = i18n("world_instruction_submarine_8")

		function var_31_5()
			arg_31_0.emit(WorldScene.SceneOp, "OpReqSub")
	elif arg_31_1 == WorldConst.OpReqVision:
		var_31_3 = i18n("world_instruction_detect_1", setColorStr(var_31_2, COLOR_GREEN), setColorStr(var_31_1, var_31_2 <= var_31_1 and COLOR_GREEN or COLOR_RED))
		var_31_4 = i18n("world_instruction_submarine_8")

		function var_31_5()
			arg_31_0.emit(WorldScene.SceneOp, "OpReqVision")
	else
		assert(False, "req error")

	setText(arg_31_0.rtMsgBase.Find("content"), var_31_3)
	setText(arg_31_0.rtMsgBase.Find("other"), var_31_4)
	onButton(arg_31_0, arg_31_0.rtMsgBtns.Find("btn_confirm"), function()
		arg_31_0.Hide()

		if var_31_0.staminaMgr.GetTotalStamina() < var_31_2:
			var_31_0.staminaMgr.Show()
		else
			var_31_5(), SFX_CONFIRM)
	setActive(arg_31_0.rtMsgExtra, arg_31_1 == WorldConst.OpReqSub)

	if arg_31_1 == WorldConst.OpReqSub:
		setText(arg_31_0.rtMsgExtra.Find("content/text_1"), i18n("world_instruction_submarine_9"))

		local var_31_6 = arg_31_0.rtMsgExtra.Find("content/toggle_area/toggle")
		local var_31_7 = PlayerPrefs.GetInt("world_sub_auto_call", 0) == 1

		triggerToggle(var_31_6, var_31_7)
		onToggle(arg_31_0, var_31_6, function(arg_36_0)
			var_31_7 = arg_36_0

			arg_31_0.DisplayAutoSetting(True), SFX_PANEL)

		local var_31_8 = pg.gameset.world_instruction_submarine.description[1]
		local var_31_9 = math.clamp(PlayerPrefs.GetInt("world_sub_call_line", 0), 0, var_31_8)
		local var_31_10 = arg_31_0.rtMsgExtra.Find("content/counter")

		setText(var_31_10.Find("number/Text"), var_31_9)
		pressPersistTrigger(var_31_10.Find("minus"), 0.5, function()
			if var_31_9 == 0:
				return

			var_31_9 = math.clamp(var_31_9 - 1, 0, var_31_8)

			setText(var_31_10.Find("number/Text"), var_31_9)
			arg_31_0.DisplayAutoSetting(True), None, True, True, 0.1, SFX_PANEL)
		pressPersistTrigger(var_31_10.Find("plus"), 0.5, function()
			if var_31_9 == var_31_8:
				return

			var_31_9 = math.clamp(var_31_9 + 1, 0, var_31_8)

			setText(var_31_10.Find("number/Text"), var_31_9)
			arg_31_0.DisplayAutoSetting(True), None, True, True, 0.1, SFX_PANEL)
		onButton(arg_31_0, arg_31_0.rtMsgBtns.Find("btn_setting"), function()
			isSetting = False

			PlayerPrefs.SetInt("world_sub_auto_call", var_31_7 and 1 or 0)
			PlayerPrefs.SetInt("world_sub_call_line", var_31_9)
			arg_31_0.DisplayAutoSetting(False)
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_instruction_submarine_11")), SFX_PANEL)

	arg_31_0.DisplayAutoSetting(False)
	setActive(arg_31_0.rtMsgbox, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_31_0.rtMsgbox)

def var_0_0.HideMsgbox(arg_40_0):
	setActive(arg_40_0.rtMsgbox, False)
	pg.UIMgr.GetInstance().UnblurPanel(arg_40_0.rtMsgbox, arg_40_0._tf)

def var_0_0.DisplayAutoSetting(arg_41_0, arg_41_1):
	setActive(arg_41_0.rtMsgBtns.Find("btn_confirm"), not arg_41_1)
	setActive(arg_41_0.rtMsgBtns.Find("btn_setting"), arg_41_1)

return var_0_0
