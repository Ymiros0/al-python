local var_0_0 = class("ArchivesWorldBossChallengePage", import(".BaseWorldBossChallengePage"))

def var_0_0.getUIName(arg_1_0):
	return "ArchivesWorldBossChallengeUI"

def var_0_0.OnFilterBoss(arg_2_0, arg_2_1):
	return not WorldBossConst._IsCurrBoss(arg_2_1)

def var_0_0.GetResSuffix(arg_3_0):
	return "_archives"

def var_0_0.OnLoaded(arg_4_0):
	var_0_0.super.OnLoaded(arg_4_0)

	arg_4_0.switchBtn = arg_4_0.findTF("detail_btn")
	arg_4_0.currentChallengeBtn = arg_4_0.findTF("current_list_btn")
	arg_4_0.tipTr = arg_4_0.findTF("tip")

	setText(arg_4_0.tipTr, i18n("world_boss_archives_boss_tip"))

def var_0_0.OnInit(arg_5_0):
	var_0_0.super.OnInit(arg_5_0)
	onButton(arg_5_0, arg_5_0.switchBtn, function()
		local var_6_0 = nowWorld().GetBossProxy().GetSelfBoss()

		if var_6_0 and WorldBossConst._IsCurrBoss(var_6_0):
			pg.TipsMgr.GetInstance().ShowTips(i18n("current_boss_was_opened"))
		else
			arg_5_0.emit(WorldBossScene.ON_SWITCH, WorldBossScene.PAGE_ARCHIVES), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.currentChallengeBtn, function()
		arg_5_0.emit(WorldBossScene.ON_SWITCH, WorldBossScene.PAGE_CHALLENGE), SFX_PANEL)
	onButton(arg_5_0, arg_5_0.findTF("help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.world_archives_boss_help.tip
		}), SFX_PANEL)

def var_0_0.UpdateEmptyCard(arg_9_0):
	local var_9_0 = arg_9_0.findTF("list_panel/mask/tpl").Find("empty").GetComponent(typeof(Image))

	if WorldBossConst.GetAchieveState() == WorldBossConst.ACHIEVE_STATE_STARTING:
		local var_9_1 = WorldBossConst.GetArchivesId()
		local var_9_2 = WorldBossConst.BossId2MetaId(var_9_1)

		var_9_0.sprite = GetSpriteFromAtlas("MetaWorldboss/" .. var_9_2, "item_04")
	else
		var_9_0.sprite = GetSpriteFromAtlas("MetaWorldboss/extra_empty", "")

	var_9_0.SetNativeSize()

return var_0_0
