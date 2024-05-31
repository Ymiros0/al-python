local var_0_0 = class("BaseWorldBossDetailPage", import("....base.BaseSubView"))
local var_0_1 = {
	[970701] = {
		-36.45481,
		717.0379
	},
	[970702] = {
		-36.45481,
		629.5
	},
	[970201] = {
		-36.45481,
		610.5,
		0.95,
		0.95
	},
	[970703] = {
		818,
		1268.1,
		1.7,
		1.7
	},
	[970401] = {
		-58.2,
		634.2
	},
	[970402] = {
		-58.2,
		634.2
	},
	[970403] = {
		-28.2,
		609.2,
		0.95,
		0.95
	}
}

def var_0_0.Setup(arg_1_0, arg_1_1):
	local var_1_0 = {
		onBossUpdated = "OnBossUpdated",
		onRankListUpdated = "OnRankListUpdated",
		onPtUpdated = "OnPtUpdated",
		onBossProgressUpdate = "OnBossProgressUpdate"
	}

	for iter_1_0, iter_1_1 in pairs(var_1_0):
		arg_1_0[iter_1_0] = function(...)
			var_0_0[iter_1_1](arg_1_0, ...)

	arg_1_0.proxy = arg_1_1

	arg_1_0.AddListeners(arg_1_0.proxy)

def var_0_0.OnLoaded(arg_3_0):
	arg_3_0.supportBtn = arg_3_0.findTF("btns/help_btn")
	arg_3_0.startBtn = arg_3_0.findTF("btns/start_btn")
	arg_3_0.awardBtn = arg_3_0.findTF("btns/award_btn")
	arg_3_0.timeTF = arg_3_0.findTF("btns/time")
	arg_3_0.leftTime = arg_3_0.findTF("btns/time/label/Text").GetComponent(typeof(Text))
	arg_3_0.awardList = UIItemList.New(arg_3_0.findTF("award_panel/list"), arg_3_0.findTF("award_panel/list/tpl"))
	arg_3_0.levelTxt = arg_3_0.findTF("hp/level/Text").GetComponent(typeof(Text))
	arg_3_0.hpTxt = arg_3_0.findTF("hp/Text").GetComponent(typeof(Text))
	arg_3_0.hpSlider = arg_3_0.findTF("hp/slider").GetComponent(typeof(Slider))
	arg_3_0.painting = arg_3_0.findTF("paint")
	arg_3_0.infoAndRankPanel = WorldBossInfoAndRankPanel.New(arg_3_0._tf, arg_3_0.event)

	arg_3_0.infoAndRankPanel.SetCallback(function(arg_4_0)
		setGray(arg_3_0.awardBtn, arg_4_0, True), function(arg_5_0, arg_5_1)
		setGray(arg_3_0.supportBtn, arg_5_1 <= arg_5_0, True)
		onButton(arg_3_0, arg_3_0.supportBtn, function()
			if arg_5_0 >= arg_5_1:
				pg.TipsMgr.GetInstance().ShowTips(i18n("world_joint_max_challenge_people_cnt"))

				return

			if arg_3_0.boss.isDeath():
				pg.TipsMgr.GetInstance().ShowTips(i18n("world_joint_boss_is_death"))
			else
				arg_3_0.OnRescue(), SFX_PANEL))
	setText(arg_3_0.findTF("btns/time/label"), i18n("time_remaining_tip"))

def var_0_0.OnInit(arg_7_0):
	onButton(arg_7_0, arg_7_0.startBtn, function()
		arg_7_0.OnStart(), SFX_PANEL)
	onButton(arg_7_0, arg_7_0.awardBtn, function()
		if arg_7_0.boss.GetLeftTime() <= 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_joint_boss_award_expired"))
		else
			if arg_7_0.boss.ShouldWaitForResult():
				return

			arg_7_0.emit(WorldBossMediator.ON_SUBMIT_AWARD, arg_7_0.boss.id), SFX_PANEL)

def var_0_0.OnStart(arg_10_0):
	if arg_10_0.boss.isDeath():
		pg.TipsMgr.GetInstance().ShowTips(i18n("world_joint_boss_is_death"))
	elif arg_10_0.boss.GetLeftTime() <= 0:
		pg.TipsMgr.GetInstance().ShowTips(i18n("world_joint_boss_is_death"))
	else
		arg_10_0.emit(WorldBossMediator.ON_BATTLE, arg_10_0.boss.id)

def var_0_0.AddListeners(arg_11_0, arg_11_1):
	arg_11_1.AddListener(WorldBossProxy.EventPtUpdated, arg_11_0.onPtUpdated)
	arg_11_1.AddListener(WorldBossProxy.EventBossUpdated, arg_11_0.onBossUpdated)
	arg_11_1.AddListener(WorldBossProxy.EventRankListUpdated, arg_11_0.onRankListUpdated)
	arg_11_1.AddListener(WorldBossProxy.EventUnlockProgressUpdated, arg_11_0.onBossProgressUpdate)

def var_0_0.RemoveListeners(arg_12_0, arg_12_1):
	arg_12_1.RemoveListener(WorldBossProxy.EventPtUpdated, arg_12_0.onPtUpdated)
	arg_12_1.RemoveListener(WorldBossProxy.EventBossUpdated, arg_12_0.onBossUpdated)
	arg_12_1.RemoveListener(WorldBossProxy.EventRankListUpdated, arg_12_0.onRankListUpdated)
	arg_12_1.RemoveListener(WorldBossProxy.EventUnlockProgressUpdated, arg_12_0.onBossProgressUpdate)

def var_0_0.OnBossUpdated(arg_13_0):
	if arg_13_0.isShowing():
		arg_13_0.UpdateBoss()

def var_0_0.OnRankListUpdated(arg_14_0, arg_14_1, arg_14_2, arg_14_3):
	if arg_14_0.isShowing() and arg_14_0.boss and arg_14_0.boss.id == arg_14_3 and arg_14_0.infoAndRankPanel and arg_14_0.infoAndRankPanel.GetLoaded():
		arg_14_0.infoAndRankPanel.FlushRank()

def var_0_0.OnBossProgressUpdate(arg_15_0):
	if arg_15_0.isShowing():
		arg_15_0.OnUpdateRes()

def var_0_0.OnPtUpdated(arg_16_0):
	if arg_16_0.isShowing():
		arg_16_0.OnUpdatePt()

def var_0_0.UpdatePainting(arg_17_0, arg_17_1):
	if not arg_17_1:
		return

	if arg_17_0.groupId != arg_17_1:
		arg_17_0.groupId = arg_17_1

		local var_17_0 = arg_17_0.findTF("label").GetComponent(typeof(Image))

		var_17_0.sprite = GetSpriteFromAtlas("MetaWorldboss/" .. arg_17_0.groupId, "title" .. arg_17_0.GetResSuffix())

		var_17_0.SetNativeSize()
		setMetaPaintingPrefabAsync(arg_17_0.painting, arg_17_0.groupId, "lihuisha", function()
			arg_17_0.OnPaintingLoad())

		local var_17_1
		local var_17_2 = WorldBossConst.MetaId2BossId(arg_17_1)

		if var_17_2:
			var_17_1 = pg.world_joint_boss_template[var_17_2].p_offset or var_0_1[arg_17_1]
		else
			var_17_1 = var_0_1[arg_17_1]

		if var_17_1:
			setAnchoredPosition(arg_17_0.painting, {
				x = var_17_1[1],
				y = var_17_1[2]
			})

			local var_17_3 = var_17_1[3] or 1
			local var_17_4 = var_17_1[4] or 1

			arg_17_0.painting.localScale = Vector3(var_17_3, var_17_4, 1)
	else
		arg_17_0.OnPaintingLoad()

def var_0_0.UpdateBoss(arg_19_0):
	arg_19_0.boss = arg_19_0.proxy.GetBoss()

	if arg_19_0.boss:
		arg_19_0.UpdateMainInfo()
		arg_19_0.RemoveChallengeTimer()
		arg_19_0.AddChanllengTimer()
		arg_19_0.RemoveGetAwardTimer()
		arg_19_0.AddGetAwaradTimer()

def var_0_0.Update(arg_20_0):
	arg_20_0.UpdateBoss()
	arg_20_0.Show()

	if arg_20_0.boss:
		arg_20_0.infoAndRankPanel.ExecuteAction("Flush", arg_20_0.boss, arg_20_0.proxy)
		arg_20_0.UpdateAward()
		arg_20_0.OnUpdateRes()
		arg_20_0.OnUpdatePt()

def var_0_0.UpdateAward(arg_21_0):
	local var_21_0 = arg_21_0.boss.GetAwards()

	arg_21_0.awardList.make(function(arg_22_0, arg_22_1, arg_22_2)
		if arg_22_0 == UIItemList.EventUpdate:
			local var_22_0 = var_21_0[arg_22_1 + 1]
			local var_22_1 = {
				count = 0,
				type = var_22_0[1],
				id = var_22_0[2]
			}

			updateDrop(arg_22_2.Find("equipment/bg"), var_22_1)

			local var_22_2 = arg_22_2.Find("mask/name").GetComponent("ScrollText")
			local var_22_3 = var_22_1.getConfig("name")

			var_22_2.SetText(var_22_3)
			onButton(arg_21_0, arg_22_2, function()
				arg_21_0.emit(BaseUI.ON_DROP, var_22_1), SFX_PANEL))
	arg_21_0.awardList.align(math.min(#var_21_0, 3))

def var_0_0.UpdateMainInfo(arg_24_0):
	local var_24_0 = arg_24_0.boss
	local var_24_1 = arg_24_0.proxy
	local var_24_2 = var_24_0.GetHP()
	local var_24_3 = var_24_0.GetMaxHp()

	arg_24_0.levelTxt.text = var_24_0.GetLevel()
	arg_24_0.hpTxt.text = var_24_2 .. "/<color=#E31D15>" .. var_24_3 .. "</color>"
	arg_24_0.hpSlider.value = var_24_2 / var_24_3

	local var_24_4 = var_24_0.isDeath()
	local var_24_5 = var_24_0.IsExpired()
	local var_24_6 = var_24_1.canGetSelfAward()

	setActive(arg_24_0.supportBtn, not var_24_4 and not var_24_5)
	setActive(tf(arg_24_0.leftTime).parent, True)
	setActive(arg_24_0.awardBtn, var_24_4 and var_24_6)
	setActive(arg_24_0.startBtn, not var_24_4 and not var_24_5)
	arg_24_0.UpdatePainting(var_24_0.config.meta_id)

def var_0_0.AddChanllengTimer(arg_25_0):
	local var_25_0 = arg_25_0.boss

	if var_25_0.isDeath():
		return

	local var_25_1 = pg.TimeMgr.GetInstance().GetServerTime()
	local var_25_2 = var_25_0.GetExpiredTime()

	local function var_25_3()
		arg_25_0.leftTime.text = i18n("world_word_expired")

		onNextTick(function()
			arg_25_0.OnBossExpired())

	if var_25_2 < var_25_1:
		var_25_3()
	else
		arg_25_0.bossTimer = Timer.New(function()
			local var_28_0 = var_25_2 - pg.TimeMgr.GetInstance().GetServerTime()

			if var_28_0 > 0:
				arg_25_0.leftTime.text = pg.TimeMgr.GetInstance().DescCDTime(var_28_0)
			else
				var_25_3()
				arg_25_0.RemoveChallengeTimer(), 1, -1)

		arg_25_0.bossTimer.Start()
		arg_25_0.bossTimer.func()

def var_0_0.RemoveChallengeTimer(arg_29_0):
	if arg_29_0.bossTimer:
		arg_29_0.bossTimer.Stop()

		arg_29_0.bossTimer = None

def var_0_0.AddGetAwaradTimer(arg_30_0):
	local var_30_0 = arg_30_0.boss

	if not var_30_0.isDeath():
		return

	local var_30_1 = pg.TimeMgr.GetInstance().GetServerTime()
	local var_30_2 = var_30_0.GetExpiredTime()

	local function var_30_3()
		arg_30_0.leftTime.text = i18n("world_word_expired")

		onNextTick(function()
			arg_30_0.OnBossExpired())

	if var_30_2 < var_30_1:
		var_30_3()
	else
		arg_30_0.awardTimer = Timer.New(function()
			local var_33_0 = var_30_2 - pg.TimeMgr.GetInstance().GetServerTime()

			if var_33_0 > 0:
				arg_30_0.leftTime.text = pg.TimeMgr.GetInstance().DescCDTime(var_33_0)
			else
				var_30_3()
				arg_30_0.RemoveGetAwardTimer(), 1, -1)

		arg_30_0.awardTimer.Start()
		arg_30_0.awardTimer.func()

def var_0_0.OnBossExpired(arg_34_0):
	arg_34_0.emit(WorldBossMediator.ON_SELF_BOSS_OVERTIME)

def var_0_0.RemoveGetAwardTimer(arg_35_0):
	if arg_35_0.awardTimer:
		arg_35_0.awardTimer.Stop()

		arg_35_0.awardTimer = None

def var_0_0.OnDestroy(arg_36_0):
	if arg_36_0.groupId:
		arg_36_0.OnRetPaintingPrefab()
		retMetaPaintingPrefab(arg_36_0.painting, arg_36_0.groupId)

	arg_36_0.RemoveGetAwardTimer()
	arg_36_0.RemoveListeners(arg_36_0.proxy)
	arg_36_0.RemoveChallengeTimer()

	if arg_36_0.infoAndRankPanel:
		arg_36_0.infoAndRankPanel.Destroy()

		arg_36_0.infoAndRankPanel = None

	if arg_36_0.isShowing():
		arg_36_0.Hide()

def var_0_0.OnRetPaintingPrefab(arg_37_0):
	return

def var_0_0.GetResSuffix(arg_38_0):
	return ""

def var_0_0.OnPaintingLoad(arg_39_0):
	return

def var_0_0.OnUpdateRes(arg_40_0):
	return

def var_0_0.OnUpdatePt(arg_41_0):
	return

def var_0_0.OnRescue(arg_42_0):
	return

return var_0_0
