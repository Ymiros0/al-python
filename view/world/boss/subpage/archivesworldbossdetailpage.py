local var_0_0 = class("ArchivesWorldBossDetailPage", import(".BaseWorldBossDetailPage"))

def var_0_0.getUIName(arg_1_0):
	return "ArchivesWorldBossDetailUI"

def var_0_0.OnAutoBattleResult(arg_2_0, arg_2_1):
	local var_2_0 = arg_2_1.cnt
	local var_2_1 = arg_2_1.damage
	local var_2_2 = arg_2_1.oil

	arg_2_0.autoBattleResultMsg.ExecuteAction("Show", {
		battleCnt = var_2_0,
		damage = var_2_1,
		oil = var_2_2
	})
	arg_2_0.Flush()
	arg_2_0.UpdatePainting(arg_2_0.groupId)

def var_0_0.OnAutoBattleStart(arg_3_0):
	arg_3_0.Flush()
	arg_3_0.UpdatePainting(arg_3_0.groupId)

def var_0_0.GetResSuffix(arg_4_0):
	return "_archives"

def var_0_0.OnLoaded(arg_5_0):
	var_0_0.super.OnLoaded(arg_5_0)

	arg_5_0.currProgressTr = arg_5_0.findTF("progress")
	arg_5_0.currProgressTxt = arg_5_0.findTF("progress/value").GetComponent(typeof(Text))
	arg_5_0.listBtn = arg_5_0.findTF("list_btn")
	arg_5_0.archivesWorldbossBtn = ArchivesWorldbossBtn.New(arg_5_0.findTF("archives_btn"), arg_5_0.event)
	arg_5_0.autoBattleBtn = arg_5_0.findTF("btns/auto_btn")
	arg_5_0.autoBattleTimeTxt = arg_5_0.autoBattleBtn.Find("Text").GetComponent(typeof(Text))
	arg_5_0.battleMask = arg_5_0.findTF("battle_mask")
	arg_5_0.helpWindow = ArchivesWorldBossHelpPage.New(arg_5_0._parentTf.parent, arg_5_0.event)
	arg_5_0.autoBattleTip = ArchivesWorldBossAutoBattleTipPage.New(arg_5_0._parentTf.parent, arg_5_0.event)
	arg_5_0.autoBattleMsg = ArchivesWorldBossAutoBattleMsgbox.New(arg_5_0._parentTf.parent, arg_5_0.event)
	arg_5_0.autoBattleResultMsg = ArchivesWorldBossAutoBattleResultMsg.New(arg_5_0._parentTf.parent, arg_5_0.event)

def var_0_0.OnInit(arg_6_0):
	var_0_0.super.OnInit(arg_6_0)
	onButton(arg_6_0, arg_6_0.listBtn, function()
		arg_6_0.emit(WorldBossScene.ON_SWITCH, WorldBossScene.PAGE_ARCHIVES_CHALLENGE), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.currProgressTr, function()
		local var_8_0 = WorldBossConst.GetAchieveBossItemInfo()

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideNo = True,
			type = MSGBOX_TYPE_DROP_ITEM,
			name = var_8_0.name,
			content = var_8_0.display,
			iconPath = var_8_0.icon,
			frame = var_8_0.rarity
		}), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.findTF("help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.world_archives_boss_help.tip
		}), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.battleMask, function()
		triggerButton(arg_6_0.autoBattleBtn), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.autoBattleBtn, function()
		if pg.TimeMgr.GetInstance().GetServerTime() + WorldBossConst.GetArchivesBossAutoBattleSecond() > arg_6_0.boss.GetExpiredTime():
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_no_time_to_auto_battle"))

			return

		local var_11_0 = WorldBossConst.GetAutoBattleState(arg_6_0.boss)

		if var_11_0 == WorldBossConst.AUTO_BATTLE_STATE_STARTING:
			arg_6_0.autoBattleMsg.ExecuteAction("Show", {
				def onContent:()
					local var_12_0 = WorldBossConst.GetAutoBattleLeftTime()

					if var_12_0 <= 0:
						return None

					return (pg.TimeMgr.GetInstance().DescCDTime(var_12_0)),
				title = i18n("world_boss_archives_stop_auto_battle_title"),
				yesText = i18n("world_boss_archives_continue_auto_battle"),
				noText = i18n("world_boss_archives_stop_auto_battle"),
				def onNo:()
					arg_6_0.emit(WorldBossMediator.ON_ARCHIVES_BOSS_STOP_AUTO_BATTLE, arg_6_0.boss.id)
			})
		elif var_11_0 == WorldBossConst.AUTO_BATTLE_STATE_HIDE:
			pg.TipsMgr.GetInstance().ShowTip(i18n("world_word_expired"))
		elif var_11_0 == WorldBossConst.AUTO_BATTLE_STATE_LOCK:
			pg.TipsMgr.GetInstance().ShowTips(i18n("world_boss_archives_auto_battle_unopen"))
		else
			local var_11_1 = WorldBossConst.GetHighestDamage()
			local var_11_2 = WorldBossConst.GetAutoBattleCnt()
			local var_11_3 = WorldBossConst.GetAutoBattleOilConsume()
			local var_11_4 = WorldBossConst.GetArchivesBossAutoBattleMinute()

			arg_6_0.autoBattleTip.ExecuteAction("Show", {
				highestDamage = var_11_1,
				autoBattleCnt = var_11_2,
				oil = var_11_3,
				time = var_11_4,
				def onYes:()
					arg_6_0.emit(WorldBossMediator.ON_ARCHIVES_BOSS_AUTO_BATTLE, arg_6_0.boss.id)
			}), SFX_PANEL)

def var_0_0.OnStart(arg_15_0):
	if nowWorld().GetBossProxy().InAutoBattle():
		pg.TipsMgr.GetInstance().ShowTips(i18n("world_boss_archives_need_stop_auto_battle"))

		return

	var_0_0.super.OnStart(arg_15_0)

def var_0_0.OnRescue(arg_16_0):
	if arg_16_0.helpWindow:
		arg_16_0.helpWindow.ExecuteAction("Update", arg_16_0.boss)

def var_0_0.OnUpdateRes(arg_17_0):
	if not arg_17_0.currProgressTxt:
		return

	local var_17_0, var_17_1, var_17_2 = WorldBossConst.GetAchieveBossConsume()
	local var_17_3 = WorldBossConst.GetAchieveBossItemProgress()

	arg_17_0.currProgressTxt.text = var_17_3 .. "/" .. var_17_2

def var_0_0.UpdateMainInfo(arg_18_0):
	var_0_0.super.UpdateMainInfo(arg_18_0)

	local var_18_0 = arg_18_0.boss
	local var_18_1 = var_18_0.GetHP()
	local var_18_2 = var_18_0.GetMaxHp()

	arg_18_0.levelTxt.text = var_18_0.GetLevel()
	arg_18_0.hpTxt.text = var_18_1 .. "/<color=#CF4E24>" .. var_18_2 .. "</color>"

def var_0_0.OnPaintingLoad(arg_19_0):
	local var_19_0 = arg_19_0.painting.Find("fitter")

	if var_19_0.childCount > 0:
		local var_19_1 = var_19_0.GetChild(0)
		local var_19_2 = WorldBossConst.GetAutoBattleState(arg_19_0.boss) == WorldBossConst.AUTO_BATTLE_STATE_STARTING
		local var_19_3 = GetOrAddComponent(var_19_1, typeof(Gradient))

		if var_19_3:
			var_19_3.enabled = var_19_2

def var_0_0.Show(arg_20_0):
	var_0_0.super.Show(arg_20_0)
	arg_20_0.Flush()

def var_0_0.OnBossExpired(arg_21_0):
	if WorldBossConst.GetAutoBattleState(arg_21_0.boss) == WorldBossConst.AUTO_BATTLE_STATE_STARTING:
		if WorldBossConst.GetAutoBattleLeftTime() <= 0:
			arg_21_0.emit(WorldBossMediator.ON_ARCHIVES_BOSS_AUTO_BATTLE_TIMEOVER, arg_21_0.boss.id)

		return

	arg_21_0.emit(WorldBossMediator.ON_SELF_BOSS_OVERTIME)

def var_0_0.Flush(arg_22_0):
	arg_22_0.archivesWorldbossBtn.Flush()

	local var_22_0 = WorldBossConst.GetAutoBattleState(arg_22_0.boss)
	local var_22_1 = arg_22_0.autoBattleBtn.GetComponent(typeof(Image))

	arg_22_0.RemoveBattleTimer()
	setActive(arg_22_0.battleMask, False)

	arg_22_0.autoBattleTimeTxt.text = ""

	local var_22_2

	if var_22_0 == WorldBossConst.AUTO_BATTLE_STATE_LOCK:
		var_22_2 = "auto_03"
	elif var_22_0 == WorldBossConst.AUTO_BATTLE_STATE_STARTING:
		var_22_2 = "auto_02"

		arg_22_0.AddBattleTimer()
		setActive(arg_22_0.battleMask, True)
	else
		var_22_2 = "auto_01"

	GetSpriteFromAtlasAsync("ui/WorldBossUI_atlas", var_22_2, function(arg_23_0)
		var_22_1.sprite = arg_23_0)
	setActive(arg_22_0.autoBattleBtn, var_22_0 != WorldBossConst.AUTO_BATTLE_STATE_HIDE)
	setGray(arg_22_0.startBtn, WorldBossConst.AUTO_BATTLE_STATE_STARTING == var_22_0, True)

def var_0_0.AddBattleTimer(arg_24_0):
	if arg_24_0.boss.IsExpired():
		return

	if WorldBossConst.GetAutoBattleLeftTime() <= 0:
		arg_24_0.emit(WorldBossMediator.ON_ARCHIVES_BOSS_AUTO_BATTLE_TIMEOVER, arg_24_0.boss.id)

		return

	arg_24_0.timer = Timer.New(function()
		local var_25_0 = WorldBossConst.GetAutoBattleLeftTime()

		if var_25_0 < 0:
			arg_24_0.RemoveBattleTimer()

			arg_24_0.autoBattleTimeTxt.text = ""

		if var_25_0 < 0 and arg_24_0.boss:
			arg_24_0.emit(WorldBossMediator.ON_ARCHIVES_BOSS_AUTO_BATTLE_TIMEOVER, arg_24_0.boss.id)
		else
			arg_24_0.autoBattleTimeTxt.text = pg.TimeMgr.GetInstance().DescCDTime(var_25_0), 1, -1)

	arg_24_0.timer.func()
	arg_24_0.timer.Start()

def var_0_0.RemoveBattleTimer(arg_26_0):
	if arg_26_0.timer:
		arg_26_0.timer.Stop()

		arg_26_0.timer = None

def var_0_0.Hide(arg_27_0):
	var_0_0.super.Hide(arg_27_0)
	arg_27_0.RemoveBattleTimer()

def var_0_0.OnDestroy(arg_28_0):
	local var_28_0 = arg_28_0.painting.Find("fitter").GetChild(0)

	if var_28_0 and var_28_0.GetComponent(typeof(Gradient)):
		var_28_0.GetComponent(typeof(Gradient)).enabled = False

	var_0_0.super.OnDestroy(arg_28_0)

	if arg_28_0.helpWindow:
		arg_28_0.helpWindow.Destroy()

		arg_28_0.helpWindow = None

	if arg_28_0.autoBattleTip:
		arg_28_0.autoBattleTip.Destroy()

		arg_28_0.autoBattleTip = None

	if arg_28_0.autoBattleMsg:
		arg_28_0.autoBattleMsg.Destroy()

		arg_28_0.autoBattleMsg = None

	if arg_28_0.archivesWorldbossBtn:
		arg_28_0.archivesWorldbossBtn.Dispose()

		arg_28_0.archivesWorldbossBtn = None

	if arg_28_0.autoBattleResultMsg:
		arg_28_0.autoBattleResultMsg.Destroy()

		arg_28_0.autoBattleResultMsg = None

return var_0_0
