local var_0_0 = class("DOAPtPage", import(".TemplatePage.PtTemplatePage"))

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.buffModule = arg_1_0.findTF("buff_module", arg_1_0.bg)
	arg_1_0.buffPanel = arg_1_0.findTF("skill", arg_1_0.buffModule)
	arg_1_0.buffLvs = {}

	eachChild(arg_1_0.buffPanel, function(arg_2_0)
		table.insert(arg_1_0.buffLvs, arg_2_0))

	arg_1_0.getGreyBtn = arg_1_0.findTF("get_grey_btn", arg_1_0.bg)
	arg_1_0.helpBtn = arg_1_0.findTF("help_btn", arg_1_0.bg)
	arg_1_0.levelPanel = arg_1_0.findTF("level", arg_1_0.buffModule)
	arg_1_0.f2aPanel = arg_1_0.findTF("f_to_a", arg_1_0.levelPanel)
	arg_1_0.sPanel = arg_1_0.findTF("s_ss", arg_1_0.levelPanel)
	arg_1_0.sssPanel = arg_1_0.findTF("sss", arg_1_0.levelPanel)
	arg_1_0.lvBarImages = arg_1_0.findTF("lv_bars", arg_1_0.bg)
	arg_1_0.lvTagImages = arg_1_0.findTF("lv_tags", arg_1_0.bg)
	arg_1_0.shieldEffect = arg_1_0.findTF("level/shield_effect", arg_1_0.buffModule)
	arg_1_0.starEffect = arg_1_0.findTF("level/star_effect", arg_1_0.buffModule)
	arg_1_0.mask = arg_1_0.findTF("mask", arg_1_0.bg)
	arg_1_0.trainWindow = arg_1_0.findTF("TrainWindow")
	arg_1_0.trainBtn = arg_1_0.findTF("panel/train_btn", arg_1_0.trainWindow)
	arg_1_0.trainSkills = arg_1_0.findTF("panel/skills", arg_1_0.trainWindow)
	arg_1_0.trainSkillBtns = {}

	eachChild(arg_1_0.trainSkills, function(arg_3_0)
		table.insert(arg_1_0.trainSkillBtns, arg_3_0))

	arg_1_0.curInfoPanel = arg_1_0.findTF("panel/info_bg", arg_1_0.trainWindow)
	arg_1_0.curInfo = arg_1_0.findTF("panel/info_bg/cur", arg_1_0.trainWindow)
	arg_1_0.nextInfo = arg_1_0.findTF("panel/info_bg/next", arg_1_0.trainWindow)
	arg_1_0.msgBox = arg_1_0.findTF("MsgBox")
	arg_1_0.msgContent = arg_1_0.findTF("panel/content", arg_1_0.msgBox)
	arg_1_0.msgBoxMask = arg_1_0.findTF("mengban", arg_1_0.msgBox)
	arg_1_0.cancelBtn = arg_1_0.findTF("panel/cancel_btn", arg_1_0.msgBox)
	arg_1_0.confirmBtn = arg_1_0.findTF("panel/confirm_btn", arg_1_0.msgBox)
	arg_1_0.tipPanel = arg_1_0.findTF("Tip")
	arg_1_0.buffBox = arg_1_0.findTF("BuffBox")
	arg_1_0.buffMask = arg_1_0.findTF("mask", arg_1_0.buffBox)
	arg_1_0.buffIconParent = arg_1_0.findTF("window/panel/icon", arg_1_0.buffBox)
	arg_1_0.buffDescContent = arg_1_0.findTF("window/panel/intro_view/Viewport/Content", arg_1_0.buffBox)
	arg_1_0.buffDescTpl = arg_1_0.findTF("window/panel/intro_view/buff_desc_tpl", arg_1_0.buffBox)
	arg_1_0.singleBuffBox = arg_1_0.findTF("SingleBuffBox")
	arg_1_0.singleBuffMask = arg_1_0.findTF("bg", arg_1_0.singleBuffBox)
	arg_1_0.singleSureBtn = arg_1_0.findTF("window/top/btnBack", arg_1_0.singleBuffBox)
	arg_1_0.singleCloseBtn = arg_1_0.findTF("window/sure_btn", arg_1_0.singleBuffBox)
	arg_1_0.singleIconParent = arg_1_0.findTF("window/panel/icon", arg_1_0.singleBuffBox)
	arg_1_0.singleDescContent = arg_1_0.findTF("window/panel/intro_view/Viewport/Content", arg_1_0.singleBuffBox)
	arg_1_0.singleDescTpl = arg_1_0.findTF("window/panel/intro_view/buff_desc_tpl", arg_1_0.singleBuffBox)

	setText(arg_1_0.findTF("window/top/bg/infomation/title", arg_1_0.singleBuffBox), i18n("words_information"))
	setText(arg_1_0.findTF("window/sure_btn/pic", arg_1_0.singleBuffBox), i18n("text_confirm"))

def var_0_0.OnFirstFlush(arg_4_0):
	var_0_0.super.OnFirstFlush(arg_4_0)
	setActive(arg_4_0.bg, True)
	removeOnButton(arg_4_0.getBtn)
	onButton(arg_4_0, arg_4_0.getBtn, function()
		local var_5_0 = {}
		local var_5_1 = arg_4_0.ptData.GetAward()
		local var_5_2 = getProxy(PlayerProxy).getData()

		if var_5_1.type == DROP_TYPE_RESOURCE and var_5_1.id == PlayerConst.ResGold and var_5_2.GoldMax(var_5_1.count):
			table.insert(var_5_0, function(arg_6_0)
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					content = i18n("gold_max_tip_title") .. i18n("award_max_warning"),
					onYes = arg_6_0
				}))

		seriesAsync(var_5_0, function()
			arg_4_0.isShowEffect = True

			local var_7_0 = arg_4_0.ptData.CanTrain() and arg_4_0.ptData.isInBuffTime()

			local function var_7_1()
				if var_7_0:
					arg_4_0.showUpEffect()
				else
					arg_4_0.updateLevelPanel()

			local var_7_2, var_7_3 = arg_4_0.ptData.GetResProgress()

			arg_4_0.emit(ActivityMediator.EVENT_PT_OPERATION, {
				cmd = 1,
				activity_id = arg_4_0.ptData.GetId(),
				arg1 = var_7_3,
				callback = var_7_1
			})), SFX_PANEL)
	removeOnButton(arg_4_0.battleBtn)
	onButton(arg_4_0, arg_4_0.battleBtn, function()
		local var_9_0
		local var_9_1

		if arg_4_0.activity.getConfig("config_client") != "":
			var_9_0 = arg_4_0.activity.getConfig("config_client").linkActID

			if var_9_0:
				var_9_1 = getProxy(ActivityProxy).getActivityById(var_9_0)

		if not var_9_0:
			arg_4_0.emit(ActivityMediator.BATTLE_OPERA)
		elif var_9_1 and not var_9_1.isEnd():
			arg_4_0.emit(ActivityMediator.BATTLE_OPERA)
		else
			arg_4_0.showTip(i18n("common_activity_end")), SFX_PANEL)
	onButton(arg_4_0, arg_4_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = i18n("doa_pt_help")
		}), SFX_PANEL)
	onButton(arg_4_0, arg_4_0.buffModule, function()
		arg_4_0.showBuffBox(), SFX_PANEL)

	if arg_4_0.contextData.singleActivity:
		setActive(arg_4_0.bg, False)
		arg_4_0.showSingleBuffBox()

	arg_4_0.starEffect.GetComponent("DftAniEvent").SetEndEvent(function()
		arg_4_0.updateLevelPanel()
		arg_4_0.managedTween(LeanTween.delayedCall, function()
			arg_4_0.showTrianPanel()
			setActive(arg_4_0.starEffect, False)
			setActive(arg_4_0.mask, False)
			pg.UIMgr.GetInstance().UnOverlayPanel(arg_4_0.mask, arg_4_0.bg), 0.2, None))
	arg_4_0.shieldEffect.GetComponent("DftAniEvent").SetEndEvent(function()
		arg_4_0.updateLevelPanel()
		arg_4_0.managedTween(LeanTween.delayedCall, function()
			arg_4_0.showTrianPanel()
			setActive(arg_4_0.starEffect, False)
			setActive(arg_4_0.mask, False)
			pg.UIMgr.GetInstance().UnOverlayPanel(arg_4_0.mask, arg_4_0.bg), 0.2, None))

	arg_4_0.isShowEffect = False

def var_0_0.showUpEffect(arg_16_0, arg_16_1):
	setSlider(arg_16_0.curPanel, 0, 1, 1)

	local var_16_0 = arg_16_0.ptData.GetBuffLevelProgress()

	if var_16_0 == 8 or var_16_0 == 9:
		setActive(arg_16_0.starEffect, True)
		arg_16_0.starEffect.GetComponent("Animator").Play("saoguang_anim", -1, 0)
	else
		setActive(arg_16_0.shieldEffect, True)
		arg_16_0.shieldEffect.GetComponent("Animator").Play("saoguang_anim", -1, 0)

	setActive(arg_16_0.mask, True)
	pg.UIMgr.GetInstance().OverlayPanel(arg_16_0.mask)

def var_0_0.updateLevelPanel(arg_17_0):
	local var_17_0, var_17_1 = arg_17_0.ptData.GetBuffLevelProgress()

	setActive(arg_17_0.f2aPanel, False)
	setActive(arg_17_0.sPanel, False)
	setActive(arg_17_0.sssPanel, False)

	arg_17_0.curPanel = None

	if var_17_0 == 9:
		arg_17_0.curPanel = arg_17_0.sssPanel
	elif var_17_0 > 6:
		arg_17_0.curPanel = arg_17_0.sPanel
	else
		arg_17_0.curPanel = arg_17_0.f2aPanel

	setActive(arg_17_0.curPanel, True)
	setImageSprite(arg_17_0.findTF("bar", arg_17_0.curPanel), arg_17_0.lvBarImages.Find(var_17_0).GetComponent(typeof(Image)).sprite)
	setImageSprite(arg_17_0.findTF("lv_tag", arg_17_0.curPanel), arg_17_0.lvTagImages.Find(var_17_0).GetComponent(typeof(Image)).sprite, True)
	setSlider(arg_17_0.curPanel, 0, 1, var_17_1)

	return arg_17_0.curPanel

def var_0_0.OnUpdateFlush(arg_18_0):
	setActive(arg_18_0.starEffect, False)
	setActive(arg_18_0.shieldEffect, False)

	local var_18_0 = arg_18_0.ptData.CanTrain()

	if var_18_0 and var_18_0 <= arg_18_0.ptData.level and arg_18_0.ptData.isInBuffTime() and not arg_18_0.contextData.singleActivity and not arg_18_0.isShowEffect:
		arg_18_0.showTrianPanel()

	local var_18_1, var_18_2, var_18_3 = arg_18_0.ptData.GetLevelProgress()
	local var_18_4, var_18_5, var_18_6 = arg_18_0.ptData.GetResProgress()

	setText(arg_18_0.step, var_18_1 .. "/" .. var_18_2)
	setText(arg_18_0.progress, (var_18_6 >= 1 and setColorStr(var_18_4, COLOR_GREEN) or var_18_4) .. "/" .. var_18_5)
	setSlider(arg_18_0.slider, 0, 1, var_18_6)

	if not arg_18_0.isShowEffect:
		arg_18_0.updateLevelPanel()

	local var_18_7 = arg_18_0.ptData.CanGetAward()
	local var_18_8 = arg_18_0.ptData.CanGetNextAward()
	local var_18_9 = arg_18_0.ptData.CanGetMorePt()
	local var_18_10 = arg_18_0.ptData.CanTrain()

	setActive(arg_18_0.battleBtn, var_18_9 and not var_18_7 and var_18_8)
	setActive(arg_18_0.getBtn, var_18_7)
	setActive(arg_18_0.getGreyBtn, not var_18_7)
	setActive(arg_18_0.gotBtn, not var_18_8 and not var_18_10)
	setActive(arg_18_0.buffModule, arg_18_0.ptData.isInBuffTime())

	local var_18_11 = arg_18_0.ptData.GetAward()

	updateDrop(arg_18_0.awardTF, var_18_11)
	onButton(arg_18_0, arg_18_0.awardTF, function()
		arg_18_0.emit(BaseUI.ON_DROP, var_18_11), SFX_PANEL)

	for iter_18_0, iter_18_1 in ipairs(arg_18_0.ptData.GetCurBuffInfos()):
		setText(arg_18_0.buffLvs[iter_18_1.group], iter_18_1.next and "LV." .. iter_18_1.lv or "MAX")

def var_0_0.showTrianPanel(arg_20_0):
	setActive(arg_20_0.trainWindow, True)

	local var_20_0 = arg_20_0.ptData.GetCurBuffInfos()

	arg_20_0.selectIndex = None
	arg_20_0.selectBuffId = None
	arg_20_0.selectBuffLv = None
	arg_20_0.selectNewBuffId = None

	for iter_20_0, iter_20_1 in ipairs(arg_20_0.trainSkillBtns):
		onButton(arg_20_0, iter_20_1, function()
			for iter_21_0, iter_21_1 in ipairs(var_20_0):
				if iter_20_0 == iter_21_1.group:
					if iter_21_1.next:
						arg_20_0.selectIndex = iter_20_0
						arg_20_0.selectBuffId = iter_21_1.id
						arg_20_0.selectNewBuffId = iter_21_1.next
						arg_20_0.selectBuffLv = iter_21_1.lv
					else
						arg_20_0.selectIndex = None
						arg_20_0.selectBuffId = None
						arg_20_0.selectNewBuffId = None
						arg_20_0.selectBuffLv = None

			arg_20_0.flushTrainPanel(), SFX_PANEL)

	onButton(arg_20_0, arg_20_0.trainBtn, function()
		arg_20_0.showMsgBox(), SFX_PANEL)
	;(function()
		for iter_23_0, iter_23_1 in ipairs(var_20_0):
			if iter_23_1.next:
				arg_20_0.selectIndex = iter_23_1.group
				arg_20_0.selectBuffId = iter_23_1.id
				arg_20_0.selectNewBuffId = iter_23_1.next
				arg_20_0.selectBuffLv = iter_23_1.lv

				return)()
	arg_20_0.flushTrainPanel()

def var_0_0.hideTrianPanel(arg_24_0):
	setActive(arg_24_0.trainWindow, False)

def var_0_0.flushTrainPanel(arg_25_0):
	local var_25_0 = arg_25_0.ptData.GetCurBuffInfos()

	if var_25_0:
		for iter_25_0, iter_25_1 in ipairs(var_25_0):
			setText(arg_25_0.findTF("lv_bg/lv", arg_25_0.trainSkillBtns[iter_25_1.group]), iter_25_1.next and "LV." .. iter_25_1.lv or "MAX")

	for iter_25_2, iter_25_3 in ipairs(arg_25_0.trainSkillBtns):
		if iter_25_2 == arg_25_0.selectIndex:
			setActive(arg_25_0.findTF("selected", iter_25_3), True)
		else
			setActive(arg_25_0.findTF("selected", iter_25_3), False)

	if arg_25_0.selectIndex:
		setActive(arg_25_0.curInfoPanel, True)
		setActive(arg_25_0.trainBtn, True)
		setText(arg_25_0.curInfo, pg.benefit_buff_template[arg_25_0.selectBuffId].desc)
		setText(arg_25_0.nextInfo, pg.benefit_buff_template[arg_25_0.selectNewBuffId].desc)
	else
		setActive(arg_25_0.curInfoPanel, False)
		setActive(arg_25_0.trainBtn, False)

def var_0_0.getBuffNameIndex(arg_26_0, arg_26_1):
	if arg_26_1 == 35 or arg_26_1 == 36 or arg_26_1 == 37:
		return 1
	elif arg_26_1 == 38 or arg_26_1 == 39 or arg_26_1 == 40:
		return 2
	elif arg_26_1 == 41 or arg_26_1 == 42 or arg_26_1 == 43:
		return 3
	elif arg_26_1 == 44 or arg_26_1 == 45 or arg_26_1 == 46:
		return 4

	return 1

def var_0_0.getTip(arg_27_0, arg_27_1):
	if arg_27_1 == 35 or arg_27_1 == 36 or arg_27_1 == 37:
		return i18n("doa_liliang")
	elif arg_27_1 == 38 or arg_27_1 == 39 or arg_27_1 == 40:
		return i18n("doa_jiqiao")
	elif arg_27_1 == 41 or arg_27_1 == 42 or arg_27_1 == 43:
		return i18n("doa_tili")
	elif arg_27_1 == 44 or arg_27_1 == 45 or arg_27_1 == 46:
		return i18n("doa_meili")

	return ""

def var_0_0.showMsgBox(arg_28_0):
	if arg_28_0.selectBuffId:
		setActive(arg_28_0.msgBox, True)
		setText(arg_28_0.msgContent, i18n("doa_pt_up", arg_28_0.getTip(pg.benefit_buff_template[arg_28_0.selectBuffId].id)))
		onButton(arg_28_0, arg_28_0.msgBoxMask, function()
			arg_28_0.hideMsgBox(), SFX_PANEL)
		onButton(arg_28_0, arg_28_0.cancelBtn, function()
			arg_28_0.hideMsgBox(), SFX_PANEL)
		onButton(arg_28_0, arg_28_0.confirmBtn, function()
			arg_28_0.hideMsgBox()
			arg_28_0.emit(ActivityMediator.EVENT_PT_OPERATION, {
				cmd = 3,
				activity_id = arg_28_0.ptData.GetId(),
				arg1 = arg_28_0.ptData.CanTrain(),
				arg2 = arg_28_0.selectNewBuffId,
				oldBuffId = arg_28_0.selectBuffId
			})
			arg_28_0.hideTrianPanel()
			arg_28_0.showTip(i18n("doa_pt_complete")), SFX_PANEL)

def var_0_0.hideMsgBox(arg_32_0):
	setActive(arg_32_0.msgBox, False)

def var_0_0.showTip(arg_33_0, arg_33_1):
	local var_33_0 = cloneTplTo(arg_33_0.tipPanel, arg_33_0._tf)

	setActive(var_33_0, True)
	setText(arg_33_0.findTF("Text", var_33_0), arg_33_1)

	var_33_0.transform.localScale = Vector3(0, 0.1, 1)

	LeanTween.scale(var_33_0, Vector3(1.8, 0.1, 1), 0.1).setUseEstimatedTime(True)
	LeanTween.scale(var_33_0, Vector3(1.1, 1.1, 1), 0.1).setDelay(0.1).setUseEstimatedTime(True)

	local var_33_1 = GetOrAddComponent(var_33_0, "CanvasGroup")

	Timer.New(function()
		if IsNil(var_33_0):
			return

		LeanTween.scale(var_33_0, Vector3(0.1, 1.5, 1), 0.1).setUseEstimatedTime(True).setOnComplete(System.Action(function()
			LeanTween.scale(var_33_0, Vector3.zero, 0.1).setUseEstimatedTime(True).setOnComplete(System.Action(function()
				Destroy(var_33_0))))), 3).Start()

def var_0_0.showBuffBox(arg_37_0):
	setActive(arg_37_0.buffBox, True)
	removeAllChildren(arg_37_0.buffIconParent)

	local var_37_0 = cloneTplTo(arg_37_0.updateLevelPanel(), arg_37_0.buffIconParent)

	setLocalPosition(var_37_0, Vector3(0, 0, 0))
	setLocalScale(var_37_0, Vector3(1.3, 1.3, 1))

	local var_37_1 = arg_37_0.ptData.GetCurBuffInfos()

	if var_37_1:
		for iter_37_0, iter_37_1 in ipairs(var_37_1):
			local var_37_2

			if iter_37_0 <= arg_37_0.buffDescContent.childCount:
				var_37_2 = arg_37_0.buffDescContent.GetChild(iter_37_0 - 1)
			else
				var_37_2 = cloneTplTo(arg_37_0.buffDescTpl, arg_37_0.buffDescContent)

			setText(var_37_2, pg.benefit_buff_template[iter_37_1.id].name .. pg.benefit_buff_template[iter_37_1.id].desc)

	onButton(arg_37_0, arg_37_0.buffMask, function()
		setActive(arg_37_0.buffBox, False), SFX_PANEL)

def var_0_0.showSingleBuffBox(arg_39_0):
	setActive(arg_39_0.singleBuffBox, True)
	pg.UIMgr.GetInstance().BlurPanel(arg_39_0.singleBuffBox, False, {
		overlayType = LayerWeightConst.OVERLAY_UI_TOP
	})
	removeAllChildren(arg_39_0.singleIconParent)

	local var_39_0 = cloneTplTo(arg_39_0.updateLevelPanel(), arg_39_0.singleIconParent)

	setLocalPosition(var_39_0, Vector3(0, 0, 0))
	setLocalScale(var_39_0, Vector3(1.3, 1.3, 1))

	local var_39_1 = arg_39_0.ptData.GetCurBuffInfos()

	if var_39_1:
		for iter_39_0, iter_39_1 in ipairs(var_39_1):
			local var_39_2

			if iter_39_0 <= arg_39_0.singleDescContent.childCount:
				var_39_2 = arg_39_0.singleDescContent.GetChild(iter_39_0 - 1)
			else
				var_39_2 = cloneTplTo(arg_39_0.singleDescTpl, arg_39_0.singleDescContent)

			setText(var_39_2, pg.benefit_buff_template[iter_39_1.id].name .. pg.benefit_buff_template[iter_39_1.id].desc)

	local function var_39_3()
		setActive(arg_39_0.singleBuffBox, False)
		arg_39_0.emit(ActivitySingleScene.EXIT)
		arg_39_0.emit(ActivitySingleScene.ON_CLOSE)
		pg.UIMgr.GetInstance().UnblurPanel(arg_39_0.singleBuffBox, arg_39_0._tf)

	onButton(arg_39_0, arg_39_0.singleBuffMask, function()
		var_39_3(), SFX_PANEL)
	onButton(arg_39_0, arg_39_0.singleCloseBtn, function()
		var_39_3(), SFX_PANEL)
	onButton(arg_39_0, arg_39_0.singleSureBtn, function()
		var_39_3(), SFX_PANEL)

def var_0_0.onBackPressed(arg_44_0):
	if arg_44_0.contextData.singleActivity:
		pg.UIMgr.GetInstance().UnblurPanel(arg_44_0.singleBuffBox, arg_44_0._tf)

def var_0_0.willExit(arg_45_0):
	if arg_45_0.contextData.singleActivity:
		pg.UIMgr.GetInstance().UnblurPanel(arg_45_0.singleBuffBox, arg_45_0._tf)

return var_0_0
