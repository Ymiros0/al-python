local var_0_0 = class("CurrentWorldBossDetailPage", import(".BaseWorldBossDetailPage"))

def var_0_0.getUIName(arg_1_0):
	return "CurrentWorldBossDetailUI"

def var_0_0.OnLoaded(arg_2_0):
	var_0_0.super.OnLoaded(arg_2_0)

	arg_2_0.listBtn = arg_2_0.findTF("list_btn")
	arg_2_0.metaWorldbossBtn = MetaWorldbossBtn.New(arg_2_0.findTF("archives_btn"), arg_2_0.event)
	arg_2_0.helpWindow = WorldBossHelpPage.New(arg_2_0._tf, arg_2_0.event)
	arg_2_0.currProgressTr = arg_2_0.findTF("progress")
	arg_2_0.currProgressTxt = arg_2_0.findTF("progress/value").GetComponent(typeof(Text))
	arg_2_0.ptBtn = WorldbossPtBtn.New(arg_2_0.findTF("point"))

def var_0_0.OnInit(arg_3_0):
	var_0_0.super.OnInit(arg_3_0)
	onButton(arg_3_0, arg_3_0.listBtn, function()
		arg_3_0.emit(WorldBossScene.ON_SWITCH, WorldBossScene.PAGE_CHALLENGE), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.currProgressTr, function()
		local var_5_0 = WorldBossConst.GetCurrBossItemInfo()

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			hideNo = True,
			type = MSGBOX_TYPE_DROP_ITEM,
			name = var_5_0.name,
			content = var_5_0.display,
			iconPath = var_5_0.icon,
			frame = var_5_0.rarity
		}), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.findTF("point/help"), function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.world_boss_help_meta.tip
		}), SFX_PANEL)

def var_0_0.OnUpdateRes(arg_7_0):
	local var_7_0, var_7_1, var_7_2 = WorldBossConst.GetCurrBossConsume()
	local var_7_3 = WorldBossConst.GetCurrBossItemProgress()

	arg_7_0.currProgressTxt.text = var_7_3 .. "/" .. var_7_2

def var_0_0.OnUpdatePt(arg_8_0):
	if arg_8_0.ptBtn:
		arg_8_0.ptBtn.Update()

def var_0_0.OnRescue(arg_9_0):
	if arg_9_0.helpWindow:
		arg_9_0.helpWindow.ExecuteAction("Update", arg_9_0.boss)

def var_0_0.Show(arg_10_0):
	var_0_0.super.Show(arg_10_0)
	arg_10_0.TryPlayGuide()

def var_0_0.TryPlayGuide(arg_11_0):
	if pg.NewStoryMgr.GetInstance().IsPlayed("WorldG191"):
		WorldGuider.GetInstance().PlayGuide("WorldG191_1")

	if pg.NewStoryMgr.GetInstance().IsPlayed("WorldG191_1") and not CurrentWorldBossDetailPage.formDock:
		WorldGuider.GetInstance().PlayGuide("WorldG192")

	CurrentWorldBossDetailPage.formDock = False

def var_0_0.OnDestroy(arg_12_0):
	var_0_0.super.OnDestroy(arg_12_0)

	if arg_12_0.helpWindow:
		arg_12_0.helpWindow.Destroy()

		arg_12_0.helpWindow = None

	if arg_12_0.metaWorldbossBtn:
		arg_12_0.metaWorldbossBtn.Dispose()

		arg_12_0.metaWorldbossBtn = None

	if arg_12_0.ptBtn:
		arg_12_0.ptBtn.Dispose()

		arg_12_0.ptBtn = None

return var_0_0
