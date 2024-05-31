local var_0_0 = class("GuildMissionBossPage", import("....base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "GuildMissionBossPage"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.hp = arg_2_0.findTF("hp/bar")
	arg_2_0.hpProgress = arg_2_0.findTF("hp/bar/Text").GetComponent(typeof(Text))
	arg_2_0.hpL = arg_2_0.hp.rect.width
	arg_2_0.titleTxt = arg_2_0.findTF("title").GetComponent(typeof(Text))
	arg_2_0.assaultBtn = arg_2_0.findTF("btn_a_formation")
	arg_2_0.battleBtn = arg_2_0.findTF("btn_go")
	arg_2_0.reportBtn = arg_2_0.findTF("btn_report")
	arg_2_0.reportTip = arg_2_0.findTF("btn_report/tip")
	arg_2_0.reportTipTxt = arg_2_0.findTF("btn_report/tip/Text").GetComponent(typeof(Text))
	arg_2_0.cntTxt = arg_2_0.findTF("btn_go/cnt/Text").GetComponent(typeof(Text))
	arg_2_0.rankList = UIItemList.New(arg_2_0.findTF("rank/content"), arg_2_0.findTF("rank/content/tpl"))
	arg_2_0.paintingTF = arg_2_0.findTF("painting")
	arg_2_0.prefabTF = arg_2_0.findTF("prefab")
	arg_2_0.viewAllBtn = arg_2_0.findTF("rank/view_all")
	arg_2_0.allRankPage = GuildBossRankPage.New(arg_2_0._parentTf, arg_2_0.event)

	setActive(arg_2_0.viewAllBtn, PLATFORM_CODE != PLATFORM_JP)

	arg_2_0.eventTimerTxt = arg_2_0.findTF("timer/Text").GetComponent(typeof(Text))

	setText(arg_2_0.findTF("timer/label"), i18n("guild_time_remaining_tip"))

	arg_2_0.timeView = GuildEventTimerView.New()

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0.assaultBtn, function()
		arg_3_0.emit(GuildEventLayer.OPEN_BOSS_ASSULT), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.battleBtn, function()
		if not arg_3_0.ExistActiveEvent():
			pg.TipsMgr.GetInstance().ShowTips(i18n("guild_battle_is_end"))

			return

		if arg_3_0.bossMission.IsReachDailyCnt():
			pg.TipsMgr.GetInstance().ShowTips(i18n("guild_boss_cnt_no_enough"))

			return

		if arg_3_0.bossMission.IsDeath():
			pg.TipsMgr.GetInstance().ShowTips(i18n("guild_battle_is_end"))

			return

		arg_3_0.emit(GuildEventLayer.ON_OPEN_BOSS_FORMATION, arg_3_0.bossMission), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.reportBtn, function()
		arg_3_0.emit(GuildEventMediator.ON_OPEN_REPORT), SFX_PANEL)

def var_0_0.UpdateMission(arg_7_0, arg_7_1):
	arg_7_0.bossMission = arg_7_1

def var_0_0.OnReportUpdated(arg_8_0):
	local var_8_0 = getProxy(GuildProxy).GetReports()
	local var_8_1 = _.select(_.values(var_8_0), function(arg_9_0)
		return arg_9_0.CanSubmit())

	setActive(arg_8_0.reportTip, #var_8_1 > 0)

	if #var_8_1 > 0:
		arg_8_0.reportTipTxt.text = #var_8_1

def var_0_0.Show(arg_10_0, arg_10_1):
	arg_10_0.UpdateMission(arg_10_1)
	arg_10_0.InitRanks()
	arg_10_0.UpdateView()
	arg_10_0.UpdatePainting()

	if arg_10_0.contextData.editBossFleet:
		triggerButton(arg_10_0.battleBtn)

	local var_10_0 = arg_10_1.IsReachDailyCnt()

	setActive(arg_10_0.battleBtn.Find("selected"), var_10_0)
	arg_10_0.OnReportUpdated()

	arg_10_0.titleTxt.text = arg_10_1.getConfig("name")

	arg_10_0.CheckFleetShipState()
	arg_10_0.timeView.Flush(arg_10_0.eventTimerTxt, getProxy(GuildProxy).getRawData().GetActiveEvent())

def var_0_0.CheckFleetShipState(arg_11_0):
	local var_11_0 = arg_11_0.bossMission
	local var_11_1 = {
		var_11_0.GetMainFleet(),
		var_11_0.GetSubFleet()
	}
	local var_11_2 = {}

	for iter_11_0, iter_11_1 in ipairs(var_11_1):
		if iter_11_1.ExistInvailShips() or iter_11_1.ExistInvaildCommanders():
			table.insert(var_11_2, iter_11_1)

	if #var_11_2 > 0:
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideNo = True,
			content = i18n("guild_boss_formation_exist_invaild_ship")
		})

		arg_11_0.contextData.editBossFleet = {}

		for iter_11_2, iter_11_3 in ipairs(var_11_2):
			arg_11_0.contextData.editBossFleet[iter_11_3.id] = iter_11_3

		arg_11_0.emit(GuildEventMediator.ON_CLEAR_BOSS_FLEET_INVAILD_SHIP)

def var_0_0.UpdateView(arg_12_0):
	if getProxy(GuildProxy).ShouldRefreshBoss():
		arg_12_0.emit(GuildEventMediator.ON_GET_BOSS_INFO)
	else
		arg_12_0.UpdateBossInfo()
		arg_12_0.AddBossTimer()
		var_0_0.super.Show(arg_12_0)

def var_0_0.UpdatePainting(arg_13_0):
	local var_13_0 = arg_13_0.bossMission
	local var_13_1 = var_13_0.GetPainting()
	local var_13_2 = var_13_1 and var_13_1 != ""

	if var_13_2:
		setGuildPaintingPrefab(arg_13_0.paintingTF, var_13_1, "chuanwu", None)
	else
		local var_13_3 = var_13_0.GetEmenyId()

		LoadSpriteAsync("guildboss/" .. var_13_3, function(arg_14_0)
			if arg_13_0.CheckState(BaseSubView.STATES.DESTROY):
				return

			if arg_14_0:
				local var_14_0 = GetOrAddComponent(arg_13_0.prefabTF.Find("frame/model"), "Image")

				var_14_0.sprite = arg_14_0

				var_14_0.SetNativeSize())

		local var_13_4 = arg_13_0.findTF("name/Image", arg_13_0.prefabTF).GetComponent(typeof(Image))

		var_13_4.sprite = GetSpriteFromAtlas("guildboss/name_" .. var_13_3, "")

		var_13_4.SetNativeSize()

	setActive(arg_13_0.paintingTF, var_13_2)
	setActive(arg_13_0.prefabTF, not var_13_2)

def var_0_0.UpdateBossInfo(arg_15_0):
	local var_15_0 = arg_15_0.bossMission
	local var_15_1 = var_15_0.GetHp()
	local var_15_2 = var_15_0.GetTotalHp()
	local var_15_3 = var_15_1 / math.max(var_15_2, 1)
	local var_15_4 = arg_15_0.hpL * var_15_3
	local var_15_5 = tf(arg_15_0.hp)

	var_15_5.sizeDelta = Vector2(var_15_4, var_15_5.sizeDelta.y)

	local var_15_6 = var_15_3 * 100

	arg_15_0.hpProgress.text = math.max(var_15_6 - var_15_6 % 0.1, 1) .. "%"

	local var_15_7 = var_15_0.GetCanUsageCnt()
	local var_15_8 = var_15_7 > 0 and COLOR_GREEN or COLOR_RED

	arg_15_0.cntTxt.text = "<color=" .. var_15_8 .. ">" .. var_15_7 .. "</color>/" .. GuildConst.MISSION_BOSS_MAX_CNT()

def var_0_0.InitRanks(arg_16_0):
	if getProxy(GuildProxy).ShouldRefreshBossRank():
		arg_16_0.emit(GuildEventMediator.ON_REFRESH_BOSS_RANK)
	else
		arg_16_0.UpdateRank()
		arg_16_0.AddRankTimer()

def var_0_0.UpdateRank(arg_17_0):
	local var_17_0 = getProxy(GuildProxy).GetBossRank()

	table.sort(var_17_0, function(arg_18_0, arg_18_1)
		return arg_18_0.damage > arg_18_1.damage)
	arg_17_0.rankList.make(function(arg_19_0, arg_19_1, arg_19_2)
		if arg_19_0 == UIItemList.EventUpdate:
			local var_19_0 = var_17_0[arg_19_1 + 1]

			setText(arg_19_2.Find("no"), arg_19_1 + 1)
			setText(arg_19_2.Find("name"), var_19_0.name)
			setText(arg_19_2.Find("Text"), var_19_0.damage))
	arg_17_0.rankList.align(math.min(3, #var_17_0))
	onButton(arg_17_0, arg_17_0.viewAllBtn, function()
		arg_17_0.allRankPage.ExecuteAction("Show", var_17_0), SFX_PANEL)

def var_0_0.ExistActiveEvent(arg_21_0):
	local var_21_0 = getProxy(GuildProxy).getRawData().GetActiveEvent()

	return var_21_0 and not var_21_0.IsExpired()

def var_0_0.AddRankTimer(arg_22_0):
	if not arg_22_0.ExistActiveEvent():
		return

	if arg_22_0.rankTimer:
		arg_22_0.rankTimer.Stop()

		arg_22_0.rankTimer = None

	local var_22_0 = arg_22_0.bossMission

	arg_22_0.rankTimer = Timer.New(function()
		arg_22_0.emit(GuildEventMediator.ON_REFRESH_BOSS_RANK), GuildConst.FORCE_REFRESH_MISSION_BOSS_RANK_TIME, 1)

	arg_22_0.rankTimer.Start()

def var_0_0.AddBossTimer(arg_24_0):
	if not arg_24_0.ExistActiveEvent():
		return

	if arg_24_0.bossTimer:
		arg_24_0.bossTimer.Stop()

		arg_24_0.bossTimer = None

	arg_24_0.bossTimer = Timer.New(function()
		arg_24_0.emit(GuildEventMediator.ON_GET_BOSS_INFO), GuildConst.FORCE_REFRESH_BOSS_TIME, 1)

	arg_24_0.bossTimer.Start()

def var_0_0.OnDestroy(arg_26_0):
	if arg_26_0.rankTimer:
		arg_26_0.rankTimer.Stop()

		arg_26_0.rankTimer = None

	if arg_26_0.bossTimer:
		arg_26_0.bossTimer.Stop()

		arg_26_0.bossTimer = None

	arg_26_0.allRankPage.Destroy()
	arg_26_0.timeView.Dispose()

return var_0_0
