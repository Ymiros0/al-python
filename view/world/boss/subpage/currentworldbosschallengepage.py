local var_0_0 = class("CurrentWorldBossChallengePage", import(".BaseWorldBossChallengePage"))

var_0_0.Listeners = {
	onPtUpdated = "OnPtUpdated",
	onRankListUpdated = "OnRankListUpdated",
	onCacheBossUpdated = "OnCacheBossUpdated"
}

def var_0_0.getUIName(arg_1_0):
	return "CurrentWorldBossChallengeUI"

def var_0_0.OnFilterBoss(arg_2_0, arg_2_1):
	return WorldBossConst._IsCurrBoss(arg_2_1)

def var_0_0.Setup(arg_3_0, arg_3_1):
	for iter_3_0, iter_3_1 in pairs(var_0_0.Listeners):
		arg_3_0[iter_3_0] = function(...)
			var_0_0[iter_3_1](arg_3_0, ...)

	arg_3_0.proxy = arg_3_1

def var_0_0.AddListeners(arg_5_0, arg_5_1):
	var_0_0.super.AddListeners(arg_5_0, arg_5_1)
	arg_5_1.AddListener(WorldBossProxy.EventPtUpdated, arg_5_0.onPtUpdated)

def var_0_0.RemoveListeners(arg_6_0, arg_6_1):
	var_0_0.super.RemoveListeners(arg_6_0, arg_6_1)
	arg_6_1.RemoveListener(WorldBossProxy.EventPtUpdated, arg_6_0.onPtUpdated)

def var_0_0.OnPtUpdated(arg_7_0, arg_7_1):
	if arg_7_0.ptBtn:
		arg_7_0.ptBtn.Update()

def var_0_0.OnLoaded(arg_8_0):
	var_0_0.super.OnLoaded(arg_8_0)

	arg_8_0.awardPage = WorldBossAwardPage.New(arg_8_0._tf.parent.parent, arg_8_0.event)
	arg_8_0.switchBtn = arg_8_0.findTF("detail_btn")
	arg_8_0.archivesChallengeBtn = arg_8_0.findTF("archives_list_btn")
	arg_8_0.awardBtn = arg_8_0.findTF("main/award_btn")

	setActive(arg_8_0.archivesChallengeBtn, not LOCK_WORLDBOSS_ARCHIVES)

def var_0_0.OnInit(arg_9_0):
	var_0_0.super.OnInit(arg_9_0)
	onButton(arg_9_0, arg_9_0.switchBtn, function()
		local var_10_0 = nowWorld().GetBossProxy().GetSelfBoss()

		if var_10_0 and not WorldBossConst._IsCurrBoss(var_10_0):
			pg.TipsMgr.GetInstance().ShowTips(i18n("archives_boss_was_opened"))
		else
			arg_9_0.emit(WorldBossScene.ON_SWITCH, WorldBossScene.PAGE_CURRENT), SFX_PANEL)
	onButton(arg_9_0, arg_9_0.archivesChallengeBtn, function()
		arg_9_0.emit(WorldBossScene.ON_SWITCH, WorldBossScene.PAGE_ARCHIVES_CHALLENGE), SFX_PANEL)
	onToggle(arg_9_0, arg_9_0.findTF("list_panel/frame/filter/toggles/world"), function(arg_12_0)
		arg_9_0.filterFlags[1] = arg_12_0 and WorldBoss.BOSS_TYPE_WORLD or -1

		arg_9_0.CheckToggle()
		arg_9_0.UpdateNonProcessList(), SFX_PANEL)
	onButton(arg_9_0, arg_9_0.findTF("point/help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.world_boss_help_meta.tip
		}), SFX_PANEL)

	arg_9_0.ptBtn = WorldbossPtBtn.New(arg_9_0.findTF("point"))

def var_0_0.CheckToggle(arg_14_0):
	var_0_0.super.CheckToggle(arg_14_0)

	if _.all(arg_14_0.filterFlags, function(arg_15_0)
		return arg_15_0 == -1):
		triggerToggle(arg_14_0.findTF("list_panel/frame/filter/toggles/world"), True)

def var_0_0.UpdateMainView(arg_16_0, arg_16_1, arg_16_2):
	var_0_0.super.UpdateMainView(arg_16_0, arg_16_1, arg_16_2)

	local var_16_0 = arg_16_1.isDeath()

	setActive(arg_16_0.awardBtn, not var_16_0)
	onButton(arg_16_0, arg_16_0.awardBtn, function()
		arg_16_0.awardPage.ExecuteAction("Update", arg_16_1), SFX_PANEL)

def var_0_0.OnDestroy(arg_18_0):
	var_0_0.super.OnDestroy(arg_18_0)

	if arg_18_0.awardPage:
		arg_18_0.awardPage.Destroy()

		arg_18_0.awardPage = None

	if arg_18_0.ptBtn:
		arg_18_0.ptBtn.Dispose()

		arg_18_0.ptBtn = None

return var_0_0
