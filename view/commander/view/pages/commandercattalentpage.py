local var_0_0 = class("CommanderCatTalentPage", import("view.base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "CommanderCatTalentui"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.resetFrame = arg_2_0.findTF("frame/point/reset_frame")
	arg_2_0.resetTimeTF = arg_2_0.findTF("frame/point/reset_frame/reset_time")
	arg_2_0.resetTimeTxt = arg_2_0.findTF("frame/point/reset_frame/reset_time/Text").GetComponent(typeof(Text))
	arg_2_0.resetTimeBtn = arg_2_0.findTF("frame/point/reset_frame/reset_btn")
	arg_2_0.pointTxt = arg_2_0.findTF("frame/point/usage_frame/point/Text").GetComponent(typeof(Text))
	arg_2_0.useBtn = arg_2_0.findTF("frame/point/usage_frame/use_btn")
	arg_2_0.uilist = UIItemList.New(arg_2_0.findTF("frame/talents/content"), arg_2_0.findTF("frame/talents/content/talent_tpl"))
	arg_2_0.resetPanel = CommanderResetTalentPage.New(arg_2_0._parentTf, arg_2_0.event, arg_2_0.contextData)
	arg_2_0.usagePanel = CommanderUsageTalentPage.New(arg_2_0._parentTf, arg_2_0.event, arg_2_0.contextData)

	setText(arg_2_0.findTF("frame/point/Text"), i18n("commander_level_up_tip"))

def var_0_0.OnInit(arg_3_0):
	arg_3_0.RegisterEvent()
	onButton(arg_3_0, arg_3_0.resetTimeBtn, function()
		if arg_3_0.commanderVO.IsSameTalent():
			pg.TipsMgr.GetInstance().ShowTips(i18n("commander_reset_talent_is_not_need"))

			return

		if arg_3_0.inChapter:
			pg.TipsMgr.GetInstance().ShowTips(i18n("commander_is_in_battle"))

			return

		if arg_3_0.commanderVO.CanReset():
			arg_3_0.resetPanel.ExecuteAction("Show", arg_3_0.commanderVO)
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("commander_reset_talent_time_no_rearch")), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.useBtn, function()
		if arg_3_0.inChapter:
			pg.TipsMgr.GetInstance().ShowTips(i18n("commander_is_in_battle"))

			return

		if arg_3_0.commanderVO.getTalentPoint() > 0:
			arg_3_0.usagePanel.ExecuteAction("Show", arg_3_0.commanderVO)
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("commander_skill_point_noengough")), SFX_PANEL)

def var_0_0.RegisterEvent(arg_6_0):
	arg_6_0.bind(CommanderCatScene.EVENT_FOLD, function(arg_7_0, arg_7_1)
		if arg_7_1:
			LeanTween.moveX(rtf(arg_6_0._tf), 1000, 0.5)
		else
			LeanTween.moveX(rtf(arg_6_0._tf), -410, 0.5))
	arg_6_0.bind(CommanderCatScene.EVENT_SELECTED, function(arg_8_0, arg_8_1)
		arg_6_0.Flush(arg_8_1))

def var_0_0.Show(arg_9_0, arg_9_1):
	var_0_0.super.Show(arg_9_0)
	arg_9_0.Flush(arg_9_1)

def var_0_0.Flush(arg_10_0, arg_10_1):
	arg_10_0.commanderVO = arg_10_1
	arg_10_0.inChapter = CommanderCatUtil.CommanderInChapter(arg_10_0.commanderVO)

	arg_10_0.RemoveTimer()
	arg_10_0.UpdatePoint()
	arg_10_0.UpdateStyle()
	arg_10_0.UpdateTimer()
	arg_10_0.UpdateTalents()

def var_0_0.UpdateTalents(arg_11_0):
	local var_11_0 = arg_11_0.commanderVO
	local var_11_1 = var_11_0.GetDisplayTalents()

	arg_11_0.uilist.make(function(arg_12_0, arg_12_1, arg_12_2)
		if arg_12_0 == UIItemList.EventUpdate:
			local var_12_0 = var_11_1[arg_12_1 + 1]

			arg_11_0.UpdateTalentCard(arg_12_2, var_12_0)

			if var_12_0:
				setActive(arg_12_2.Find("unlock/lock"), not var_11_0.IsLearnedTalent(var_12_0.id)))
	arg_11_0.uilist.align(CommanderConst.MAX_TELENT_COUNT)

def var_0_0.UpdateTalentCard(arg_13_0, arg_13_1, arg_13_2):
	local var_13_0 = arg_13_1.Find("unlock")
	local var_13_1 = arg_13_1.Find("lock")

	if arg_13_2:
		GetImageSpriteFromAtlasAsync("CommanderTalentIcon/" .. arg_13_2.getConfig("icon"), "", var_13_0.Find("icon"))

		local var_13_2 = var_13_0.Find("tree_btn")

		if var_13_2:
			onButton(arg_13_0, var_13_2, function()
				arg_13_0.contextData.treePanel.ExecuteAction("Show", arg_13_2), SFX_PANEL)

		setText(var_13_0.Find("name_bg/Text"), arg_13_2.getConfig("name"))
		setScrollText(var_13_0.Find("desc/Text"), arg_13_2.getConfig("desc"))

	setActive(var_13_0, arg_13_2)

	if var_13_1:
		setActive(var_13_1, not arg_13_2)

def var_0_0.UpdateTimer(arg_15_0):
	local var_15_0 = arg_15_0.commanderVO
	local var_15_1 = var_15_0.GetNextResetAbilityTime()
	local var_15_2 = pg.TimeMgr.GetInstance().GetServerTime()
	local var_15_3 = var_15_0.getPt() > 0 or var_15_2 < var_15_1

	setActive(arg_15_0.resetTimeBtn, var_15_3)
	setActive(arg_15_0.resetTimeTF, var_15_3)
	arg_15_0.AddTimer()

def var_0_0.AddTimer(arg_16_0):
	local var_16_0 = arg_16_0.commanderVO.GetNextResetAbilityTime()
	local var_16_1 = pg.TimeMgr.GetInstance().GetServerTime()

	if var_16_0 <= var_16_1:
		arg_16_0.resetTimeTxt.text = i18n("commander_reset_talent")

		setActive(arg_16_0.resetTimeTF, False)

		return

	arg_16_0.timer = Timer.New(function()
		var_16_1 = pg.TimeMgr.GetInstance().GetServerTime()

		local var_17_0 = var_16_0 - var_16_1

		if var_17_0 > 0:
			arg_16_0.resetTimeTxt.text = pg.TimeMgr.GetInstance().DescCDTime(var_17_0)
		else
			arg_16_0.resetTimeTxt.text = i18n("commander_reset_talent")

			setActive(arg_16_0.resetTimeTF, False), 1, -1)

	arg_16_0.timer.Start()
	arg_16_0.timer.func()

def var_0_0.UpdatePoint(arg_18_0):
	local var_18_0 = arg_18_0.commanderVO

	arg_18_0.pointTxt.text = var_18_0.getTalentPoint()

def var_0_0.UpdateStyle(arg_19_0):
	local var_19_0 = arg_19_0.commanderVO

	setActive(arg_19_0.resetFrame, not var_19_0.IsRegularTalent())

def var_0_0.RemoveTimer(arg_20_0):
	if arg_20_0.timer:
		arg_20_0.timer.Stop()

		arg_20_0.timer = None

def var_0_0.CanBack(arg_21_0):
	if arg_21_0.usagePanel and arg_21_0.usagePanel.GetLoaded() and arg_21_0.usagePanel.CanBack and not arg_21_0.usagePanel.CanBack():
		return False

	if arg_21_0.usagePanel and arg_21_0.usagePanel.GetLoaded() and arg_21_0.usagePanel.isShowing():
		arg_21_0.usagePanel.Hide()

		return False

	if arg_21_0.resetPanel and arg_21_0.resetPanel.GetLoaded() and arg_21_0.resetPanel.isShowing():
		arg_21_0.resetPanel.Hide()

		return False

	return True

def var_0_0.OnDestroy(arg_22_0):
	arg_22_0.RemoveTimer()

	if arg_22_0.usagePanel:
		arg_22_0.usagePanel.Destroy()

		arg_22_0.usagePanel = None

	if arg_22_0.resetPanel:
		arg_22_0.resetPanel.Destroy()

		arg_22_0.resetPanel = None

return var_0_0
