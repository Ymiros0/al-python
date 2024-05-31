local var_0_0 = class("ActivityBossSceneTemplate", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	error("Need Complete")

var_0_0.optionsPath = {
	"adapt/top/option"
}

def var_0_0.init(arg_2_0):
	arg_2_0.mainTF = arg_2_0.findTF("adapt")
	arg_2_0.bg = arg_2_0.findTF("bg")
	arg_2_0.bottom = arg_2_0.findTF("bottom", arg_2_0.mainTF)
	arg_2_0.hpBar = arg_2_0.findTF("progress", arg_2_0.bottom)
	arg_2_0.barList = {}

	for iter_2_0 = 1, 4:
		arg_2_0.barList[iter_2_0] = arg_2_0.findTF(iter_2_0, arg_2_0.hpBar)

	arg_2_0.progressDigit = arg_2_0.findTF("digit", arg_2_0.bottom)
	arg_2_0.digitbig = arg_2_0.progressDigit.Find("big")
	arg_2_0.digitsmall = arg_2_0.progressDigit.Find("small")
	arg_2_0.left = arg_2_0.findTF("left", arg_2_0.mainTF)
	arg_2_0.rankTF = arg_2_0.findTF("rank", arg_2_0.left)
	arg_2_0.rankList = CustomIndexLayer.Clone2Full(arg_2_0.rankTF.Find("layout"), 3)

	for iter_2_1, iter_2_2 in ipairs(arg_2_0.rankList):
		setActive(iter_2_2, False)

	arg_2_0.right = arg_2_0.findTF("right", arg_2_0.mainTF)
	arg_2_0.stageList = {}

	for iter_2_3 = 1, 4:
		arg_2_0.stageList[iter_2_3] = arg_2_0.findTF(iter_2_3, arg_2_0.right)

	arg_2_0.stageSP = arg_2_0.findTF("5", arg_2_0.right)

	if not IsNil(arg_2_0.stageSP):
		setActive(arg_2_0.stageSP, False)

	arg_2_0.awardFlash = arg_2_0.findTF("ptaward/flash", arg_2_0.right)
	arg_2_0.awardBtn = arg_2_0.findTF("ptaward/button", arg_2_0.right)
	arg_2_0.ptScoreTxt = arg_2_0.findTF("ptaward/Text", arg_2_0.right)
	arg_2_0.top = arg_2_0.findTF("top", arg_2_0.mainTF)
	arg_2_0.ticketNum = arg_2_0.findTF("ticket/Text", arg_2_0.top)
	arg_2_0.helpBtn = arg_2_0.findTF("help", arg_2_0.top)

	onButton(arg_2_0, arg_2_0.top.Find("back_btn"), function()
		arg_2_0.emit(var_0_0.ON_BACK), SOUND_BACK)
	setActive(arg_2_0.top, False)
	setAnchoredPosition(arg_2_0.top, {
		y = 1080
	})
	setActive(arg_2_0.left, False)
	setAnchoredPosition(arg_2_0.left, {
		x = -1920
	})
	setActive(arg_2_0.right, False)
	setAnchoredPosition(arg_2_0.right, {
		x = 1920
	})
	setActive(arg_2_0.bottom, False)
	setAnchoredPosition(arg_2_0.bottom, {
		y = -1080
	})
	arg_2_0.buildCommanderPanel()

def var_0_0.GetBonusWindow(arg_4_0):
	if not arg_4_0.bonusWindow:
		arg_4_0.bonusWindow = ActivityBossPtAwardSubPanel.New(arg_4_0)

		arg_4_0.bonusWindow.Load()

	return arg_4_0.bonusWindow

def var_0_0.DestroyBonusWindow(arg_5_0):
	if arg_5_0.bonusWindow:
		arg_5_0.bonusWindow.Destroy()

		arg_5_0.bonusWindow = None

def var_0_0.GetFleetEditPanel(arg_6_0):
	if not arg_6_0.fleetEditPanel:
		arg_6_0.fleetEditPanel = ActivityBossBattleFleetSelectSubPanel.New(arg_6_0)

		arg_6_0.fleetEditPanel.Load()

	return arg_6_0.fleetEditPanel

def var_0_0.DestroyFleetEditPanel(arg_7_0):
	if arg_7_0.fleetEditPanel:
		arg_7_0.fleetEditPanel.Destroy()

		arg_7_0.fleetEditPanel = None

def var_0_0.EnterAnim(arg_8_0):
	setActive(arg_8_0.top, True)
	setActive(arg_8_0.left, True)
	setActive(arg_8_0.right, True)
	setActive(arg_8_0.bottom, True)
	arg_8_0.mainTF.GetComponent("Animation").Play("Enter_Animation")

def var_0_0.didEnter(arg_9_0):
	onButton(arg_9_0, arg_9_0.awardBtn, function()
		arg_9_0.ShowAwards(), SFX_PANEL)
	onButton(arg_9_0, arg_9_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.world_boss_help.tip
		}), SFX_PANEL)
	arg_9_0.UpdateDropItems()

	for iter_9_0 = 1, #arg_9_0.stageList - 1:
		onButton(arg_9_0, arg_9_0.stageList[iter_9_0], function()
			if arg_9_0.contextData.activity.checkBattleTimeInBossAct():
				arg_9_0.ShowNormalFleet(iter_9_0, True)
			else
				pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end")), SFX_PANEL)

	onButton(arg_9_0, arg_9_0.stageList[#arg_9_0.stageList], function()
		if arg_9_0.contextData.activity.checkBattleTimeInBossAct():
			arg_9_0.ShowEXFleet()
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end")), SFX_PANEL)

	if not IsNil(arg_9_0.stageSP):
		setActive(arg_9_0.stageSP, arg_9_0.contextData.spStageID)
		onButton(arg_9_0, arg_9_0.stageSP, function()
			if arg_9_0.contextData.activity.checkBattleTimeInBossAct():
				arg_9_0.emit(ActivityBossMediatorTemplate.ONEN_BUFF_SELECT)
			else
				pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end")), SFX_PANEL)

	if arg_9_0.contextData.editFleet:
		local var_9_0 = arg_9_0.contextData.editFleet

		if var_9_0 <= #arg_9_0.contextData.normalStageIDs:
			arg_9_0.ShowNormalFleet(var_9_0)
		elif arg_9_0.contextData.editFleet == #arg_9_0.contextData.normalStageIDs + 1:
			arg_9_0.ShowEXFleet()
		elif arg_9_0.contextData.editFleet == #arg_9_0.contextData.normalStageIDs + 2:
			arg_9_0.ShowSPFleet()

	arg_9_0.EnterAnim()

	if arg_9_0.contextData.msg:
		local var_9_1 = arg_9_0.contextData.msg.param

		switch(arg_9_0.contextData.msg.type, {
			def lastBonus:()
				pg.MsgboxMgr.GetInstance().ShowMsgBox(var_9_1),
			def oil:()
				if not ItemTipPanel.ShowOilBuyTip(var_9_1):
					pg.TipsMgr.GetInstance().ShowTips(i18n("stage_beginStage_error_noResource")),
			def shipCapacity:()
				BeginStageCommand.DockOverload(),
			def energy:()
				Fleet.EnergyCheck(_.map(_.values(var_9_1.ships), function(arg_19_0)
					return getProxy(BayProxy).getShipById(arg_19_0)), Fleet.DEFAULT_NAME_BOSS_ACT[var_9_1.id], function(arg_20_0)
					if arg_20_0:
						arg_9_0.emit(PreCombatMediator.BEGIN_STAGE_PROXY, {
							curFleetId = var_9_1.id
						}))
		})

		arg_9_0.contextData.msg = None

def var_0_0.UpdateView(arg_21_0):
	arg_21_0.UpdatePage()
	arg_21_0.CheckStory()

def var_0_0.CheckStory(arg_22_0):
	local var_22_0 = pg.NewStoryMgr.GetInstance()
	local var_22_1 = arg_22_0.contextData.activity.getConfig("config_client").story

	table.SerialIpairsAsync(var_22_1, function(arg_23_0, arg_23_1, arg_23_2)
		if arg_22_0.contextData.bossHP < arg_23_1[1] + ((arg_23_0 == 1 or arg_23_1[1] == 0) and 1 or 0) and not pg.NewStoryMgr.GetInstance().IsPlayed(arg_23_1[2]):
			var_22_0.Play(arg_23_1[2], arg_23_2)

			return

		arg_23_2())

def var_0_0.UpdatePage(arg_24_0):
	local var_24_0 = arg_24_0.contextData.bossHP

	setText(arg_24_0.digitbig, math.floor(var_24_0 / 100))
	setText(arg_24_0.digitsmall, string.format("%02d", var_24_0 % 100) .. "%")

	local var_24_1 = pg.TimeMgr.GetInstance()

	for iter_24_0 = 1, 4:
		local var_24_2 = arg_24_0.barList[iter_24_0]

		setSlider(arg_24_0.findTF("Slider", var_24_2), 0, 2500, math.min(math.max(var_24_0 - (iter_24_0 - 1) * 2500, 0), 2500))

		local var_24_3 = arg_24_0.contextData.mileStones[5 - iter_24_0]

		setActive(arg_24_0.findTF("milestone/item", var_24_2), not var_24_3)
		setActive(arg_24_0.findTF("milestone/time", var_24_2), var_24_3)

		if var_24_3:
			local var_24_4 = var_24_1.STimeDescC(arg_24_0.contextData.mileStones[5 - iter_24_0], "%m/%d/%H.%M")

			setText(arg_24_0.findTF("milestone/time/Text", var_24_2), var_24_4)

	for iter_24_1 = 1, #arg_24_0.stageList - 1:
		local var_24_5 = arg_24_0.contextData.normalStageIDs[iter_24_1]
		local var_24_6 = arg_24_0.stageList[iter_24_1]

		for iter_24_2, iter_24_3 in ipairs(arg_24_0.contextData.ticketInitPools):
			for iter_24_4, iter_24_5 in ipairs(iter_24_3[1]):
				if iter_24_5 == var_24_5:
					local var_24_7 = iter_24_3[2]
					local var_24_8 = arg_24_0.contextData.stageTickets[var_24_5] or 0

					setActive(var_24_6.Find("Text"), var_24_8 > 0)
					setText(var_24_6.Find("Text"), string.format("%d/%d", var_24_8, var_24_7))

	setText(arg_24_0.ptScoreTxt, arg_24_0.contextData.ptData.count)
	setActive(arg_24_0.awardFlash, arg_24_0.contextData.ptData.CanGetAward())

	if arg_24_0.bonusWindow and arg_24_0.bonusWindow.IsShowing():
		arg_24_0.bonusWindow.buffer.UpdateView(arg_24_0.contextData.ptData)

	local var_24_9 = arg_24_0.GetEXTicket()

	setText(arg_24_0.ticketNum, var_24_9)

def var_0_0.GetEXTicket(arg_25_0):
	return getProxy(PlayerProxy).getRawData().getResource(arg_25_0.contextData.TicketID)

def var_0_0.ShowNormalFleet(arg_26_0, arg_26_1, arg_26_2):
	if not arg_26_0.contextData.actFleets[arg_26_1]:
		arg_26_0.contextData.actFleets[arg_26_1] = arg_26_0.CreateNewFleet(arg_26_1)

	if not arg_26_0.contextData.actFleets[arg_26_1 + 10]:
		arg_26_0.contextData.actFleets[arg_26_1 + 10] = arg_26_0.CreateNewFleet(arg_26_1 + 10)

	local var_26_0 = arg_26_0.contextData.actFleets[arg_26_1]

	if arg_26_2 and #var_26_0.ships <= 0:
		for iter_26_0 = #arg_26_0.contextData.normalStageIDs, 1, -1:
			local var_26_1 = arg_26_0.contextData.actFleets[iter_26_0]

			if iter_26_0 != arg_26_1 and var_26_1 and var_26_1.isLegalToFight() == True:
				var_26_0.updateShips(var_26_1.ships)

				break

	local var_26_2 = arg_26_0.GetFleetEditPanel()

	var_26_2.buffer.SetSettings(1, 1, False)
	var_26_2.buffer.SetFleets({
		arg_26_0.contextData.actFleets[arg_26_1],
		arg_26_0.contextData.actFleets[arg_26_1 + 10]
	})

	local var_26_3 = arg_26_0.contextData.useOilLimit[arg_26_1]
	local var_26_4 = arg_26_0.contextData.normalStageIDs[arg_26_1]

	if not arg_26_0.contextData.activity.IsOilLimit(var_26_4):
		var_26_3 = {
			0,
			0
		}

	var_26_2.buffer.SetOilLimit(var_26_3)

	arg_26_0.contextData.editFleet = arg_26_1

	var_26_2.buffer.UpdateView()
	var_26_2.buffer.Show()

def var_0_0.ShowEXFleet(arg_27_0):
	local var_27_0 = #arg_27_0.contextData.normalStageIDs + 1

	if not arg_27_0.contextData.actFleets[var_27_0]:
		arg_27_0.contextData.actFleets[var_27_0] = arg_27_0.CreateNewFleet(var_27_0)

	if not arg_27_0.contextData.actFleets[var_27_0 + 10]:
		arg_27_0.contextData.actFleets[var_27_0 + 10] = arg_27_0.CreateNewFleet(var_27_0 + 10)

	local var_27_1 = arg_27_0.GetFleetEditPanel()

	var_27_1.buffer.SetSettings(1, 1, True)
	var_27_1.buffer.SetFleets({
		arg_27_0.contextData.actFleets[var_27_0],
		arg_27_0.contextData.actFleets[var_27_0 + 10]
	})

	local var_27_2 = arg_27_0.contextData.useOilLimit[var_27_0]
	local var_27_3 = arg_27_0.contextData.exStageID

	if not arg_27_0.contextData.activity.IsOilLimit(var_27_3):
		var_27_2 = {
			0,
			0
		}

	var_27_1.buffer.SetOilLimit(var_27_2)

	arg_27_0.contextData.editFleet = var_27_0

	var_27_1.buffer.UpdateView()
	var_27_1.buffer.Show()

def var_0_0.ShowSPFleet(arg_28_0):
	local var_28_0 = #arg_28_0.contextData.normalStageIDs + 2

	if not arg_28_0.contextData.actFleets[var_28_0]:
		arg_28_0.contextData.actFleets[var_28_0] = arg_28_0.CreateNewFleet(var_28_0)

	if not arg_28_0.contextData.actFleets[var_28_0 + 10]:
		arg_28_0.contextData.actFleets[var_28_0 + 10] = arg_28_0.CreateNewFleet(var_28_0 + 10)

	local var_28_1 = arg_28_0.GetFleetEditPanel()

	var_28_1.buffer.SetSettings(1, 1, False)
	var_28_1.buffer.SetFleets({
		arg_28_0.contextData.actFleets[var_28_0],
		arg_28_0.contextData.actFleets[var_28_0 + 10]
	})

	local var_28_2 = {
		0,
		0
	}

	var_28_1.buffer.SetOilLimit(var_28_2)

	arg_28_0.contextData.editFleet = var_28_0

	var_28_1.buffer.UpdateView()
	var_28_1.buffer.Show()

def var_0_0.commitEdit(arg_29_0):
	arg_29_0.emit(arg_29_0.contextData.mediatorClass.ON_COMMIT_FLEET)

def var_0_0.commitCombat(arg_30_0):
	if arg_30_0.contextData.editFleet <= #arg_30_0.contextData.normalStageIDs:
		arg_30_0.emit(arg_30_0.contextData.mediatorClass.ON_PRECOMBAT, arg_30_0.contextData.editFleet)
	elif arg_30_0.contextData.editFleet == #arg_30_0.contextData.normalStageIDs + 1:
		arg_30_0.emit(arg_30_0.contextData.mediatorClass.ON_EX_PRECOMBAT, arg_30_0.contextData.editFleet, False)
	elif arg_30_0.contextData.editFleet <= #arg_30_0.contextData.normalStageIDs + 2:
		arg_30_0.emit(arg_30_0.contextData.mediatorClass.ON_SP_PRECOMBAT, arg_30_0.contextData.editFleet, False)

def var_0_0.commitTrybat(arg_31_0):
	arg_31_0.emit(arg_31_0.contextData.mediatorClass.ON_EX_PRECOMBAT, arg_31_0.contextData.editFleet, True)

def var_0_0.updateEditPanel(arg_32_0):
	if arg_32_0.fleetEditPanel:
		arg_32_0.fleetEditPanel.buffer.UpdateView()

def var_0_0.hideFleetEdit(arg_33_0):
	if arg_33_0.fleetEditPanel:
		arg_33_0.fleetEditPanel.buffer.Hide()

	if arg_33_0.commanderFormationPanel:
		arg_33_0.commanderFormationPanel.buffer.Close()

	arg_33_0.contextData.editFleet = None

def var_0_0.openShipInfo(arg_34_0, arg_34_1, arg_34_2):
	local var_34_0 = arg_34_0.contextData.actFleets[arg_34_2]
	local var_34_1 = {}
	local var_34_2 = getProxy(BayProxy)

	for iter_34_0, iter_34_1 in ipairs(var_34_0 and var_34_0.ships or {}):
		table.insert(var_34_1, var_34_2.getShipById(iter_34_1))

	arg_34_0.emit(arg_34_0.contextData.mediatorClass.ON_FLEET_SHIPINFO, {
		shipId = arg_34_1,
		shipVOs = var_34_1
	})

def var_0_0.setCommanderPrefabs(arg_35_0, arg_35_1):
	arg_35_0.commanderPrefabs = arg_35_1

def var_0_0.openCommanderPanel(arg_36_0, arg_36_1, arg_36_2):
	local var_36_0 = arg_36_0.contextData.activityID

	arg_36_0.levelCMDFormationView.setCallback(function(arg_37_0)
		if arg_37_0.type == LevelUIConst.COMMANDER_OP_SHOW_SKILL:
			arg_36_0.emit(ActivityBossMediatorTemplate.ON_COMMANDER_SKILL, arg_37_0.skill)
		elif arg_37_0.type == LevelUIConst.COMMANDER_OP_ADD:
			arg_36_0.contextData.eliteCommanderSelected = {
				fleetIndex = arg_36_2,
				cmdPos = arg_37_0.pos,
				mode = arg_36_0.curMode
			}

			arg_36_0.emit(ActivityBossMediatorTemplate.ON_SELECT_COMMANDER, arg_36_2, arg_37_0.pos)
		else
			arg_36_0.emit(ActivityBossMediatorTemplate.COMMANDER_FORMATION_OP, {
				FleetType = LevelUIConst.FLEET_TYPE_ACTIVITY,
				data = arg_37_0,
				fleetId = arg_36_1.id,
				actId = var_36_0
			}))
	arg_36_0.levelCMDFormationView.Load()
	arg_36_0.levelCMDFormationView.ActionInvoke("update", arg_36_1, arg_36_0.commanderPrefabs)
	arg_36_0.levelCMDFormationView.ActionInvoke("Show")

def var_0_0.updateCommanderFleet(arg_38_0, arg_38_1):
	if arg_38_0.levelCMDFormationView.isShowing():
		arg_38_0.levelCMDFormationView.ActionInvoke("updateFleet", arg_38_1)

def var_0_0.updateCommanderPrefab(arg_39_0):
	if arg_39_0.levelCMDFormationView.isShowing():
		arg_39_0.levelCMDFormationView.ActionInvoke("updatePrefabs", arg_39_0.commanderPrefabs)

def var_0_0.closeCommanderPanel(arg_40_0):
	if arg_40_0.levelCMDFormationView.isShowing():
		arg_40_0.levelCMDFormationView.ActionInvoke("Hide")

def var_0_0.buildCommanderPanel(arg_41_0):
	arg_41_0.levelCMDFormationView = LevelCMDFormationView.New(arg_41_0._tf, arg_41_0.event, arg_41_0.contextData)

def var_0_0.destroyCommanderPanel(arg_42_0):
	arg_42_0.levelCMDFormationView.Destroy()

	arg_42_0.levelCMDFormationView = None

def var_0_0.ShowAwards(arg_43_0):
	local var_43_0 = arg_43_0.GetBonusWindow()

	var_43_0.buffer.UpdateView(arg_43_0.contextData.ptData)
	var_43_0.buffer.Show()

def var_0_0.CreateNewFleet(arg_44_0, arg_44_1):
	return TypedFleet.New({
		id = arg_44_1,
		ship_list = {},
		commanders = {},
		fleetType = arg_44_1 > 10 and FleetType.Submarine or FleetType.Normal
	})

def var_0_0.UpdateRank(arg_45_0, arg_45_1):
	arg_45_1 = arg_45_1 or {}

	for iter_45_0 = 1, #arg_45_0.rankList:
		local var_45_0 = arg_45_0.rankList[iter_45_0]

		setActive(var_45_0, iter_45_0 <= #arg_45_1)

		if iter_45_0 <= #arg_45_1:
			local var_45_1 = var_45_0.Find("Text")

			setText(var_45_1, tostring(arg_45_1[iter_45_0].name))

def var_0_0.UpdateDropItems(arg_46_0):
	for iter_46_0, iter_46_1 in ipairs(arg_46_0.contextData.DisplayItems or {}):
		local var_46_0 = arg_46_0.findTF("milestone/item", arg_46_0.barList[iter_46_0])
		local var_46_1 = Drop.New({
			type = arg_46_0.contextData.DisplayItems[5 - iter_46_0][1],
			id = arg_46_0.contextData.DisplayItems[5 - iter_46_0][2],
			count = arg_46_0.contextData.DisplayItems[5 - iter_46_0][3]
		})

		onButton(arg_46_0, var_46_0, function()
			arg_46_0.emit(var_0_0.ON_DROP, var_46_1), SFX_PANEL)

def var_0_0.onBackPressed(arg_48_0):
	if arg_48_0.bonusWindow and arg_48_0.bonusWindow.IsShowing():
		arg_48_0.bonusWindow.buffer.Hide()

		return

	var_0_0.super.onBackPressed(arg_48_0)

def var_0_0.willExit(arg_49_0):
	arg_49_0.DestroyBonusWindow()
	arg_49_0.DestroyFleetEditPanel()
	arg_49_0.destroyCommanderPanel()

return var_0_0
