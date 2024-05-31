local var_0_0 = class("NewCommanderScene", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "GetCommanderUI"

def var_0_0.init(arg_2_0):
	arg_2_0.bgTF = arg_2_0.findTF("main/bg")
	arg_2_0.clickTF = arg_2_0.findTF("click")
	arg_2_0.paintTF = arg_2_0.findTF("main/paint")
	arg_2_0.paintTFCG = arg_2_0.paintTF.GetComponent(typeof(CanvasGroup))
	arg_2_0.infoTF = arg_2_0.findTF("main/info")
	arg_2_0.leftPanel = arg_2_0.findTF("left_panel")
	arg_2_0.lockBtn = arg_2_0.findTF("left_panel/btns/lock")
	arg_2_0.unlockBtn = arg_2_0.findTF("left_panel/btns/unlock")
	arg_2_0.shareBtn = arg_2_0.findTF("left_panel/btns/share")
	arg_2_0.nameTF = arg_2_0.findTF("content/name/value", arg_2_0.infoTF).GetComponent(typeof(Text))
	arg_2_0.nationTF = arg_2_0.findTF("content/nation/value", arg_2_0.infoTF).GetComponent(typeof(Text))
	arg_2_0.rarityTF = arg_2_0.findTF("content/rarity/value", arg_2_0.infoTF).GetComponent(typeof(Image))
	arg_2_0.skillTF = arg_2_0.findTF("content/skill/value", arg_2_0.infoTF).GetComponent(typeof(Text))
	arg_2_0.abilitysTF = arg_2_0.findTF("content/abilitys/attrs", arg_2_0.infoTF)
	arg_2_0.talentsTF = arg_2_0.findTF("content/talents", arg_2_0.infoTF)
	arg_2_0.talentsList = UIItemList.New(arg_2_0.talentsTF, arg_2_0.talentsTF.Find("talent"))
	arg_2_0.dateTF = arg_2_0.findTF("content/copyright/Text", arg_2_0.infoTF)
	arg_2_0.treePanel = CommanderTreePage.New(arg_2_0._tf, arg_2_0.event)
	arg_2_0.msgbox = CommanderMsgBoxPage.New(arg_2_0._tf, arg_2_0.event)
	arg_2_0.antor = arg_2_0._tf.GetComponent(typeof(Animator))
	arg_2_0.skipBtn = arg_2_0._tf.Find("skip")
	arg_2_0.getEffect = arg_2_0.findTF("main/effect")
	arg_2_0.skipAnim = True

	if pg.NewGuideMgr.GetInstance().IsBusy():
		arg_2_0.skipAnim = False

	pg.UIMgr.GetInstance().BlurPanel(arg_2_0._tf, False, {
		weight = LayerWeightConst.SECOND_LAYER + 1
	})
	setText(arg_2_0.findTF("main/info/content/abilitys/attrs/command/name/Text"), i18n("commander_command_ability"))
	setText(arg_2_0.findTF("main/info/content/abilitys/attrs/tactic/name/Text"), i18n("commander_tactical_ability"))
	setText(arg_2_0.findTF("main/info/content/abilitys/attrs/support/name/Text"), i18n("commander_logistics_ability"))
	setText(arg_2_0.findTF("main/info/content/copyright/title"), i18n("commander_get_commander_coptyright"))

def var_0_0.openTreePanel(arg_3_0, arg_3_1):
	local function var_3_0()
		arg_3_0.treePanel.ActionInvoke("Show", arg_3_1, LayerWeightConst.SECOND_LAYER + 2)

	if arg_3_0.treePanel.GetLoaded():
		var_3_0()
	else
		arg_3_0.treePanel.Load()
		arg_3_0.treePanel.CallbackInvoke(var_3_0)

def var_0_0.closeTreePanel(arg_5_0):
	arg_5_0.treePanel.ActionInvoke("closeTreePanel")

def var_0_0.onUIAnimEnd(arg_6_0, arg_6_1):
	arg_6_0.antor.SetBool("play", True)

	arg_6_0.isAnim = True

	setActive(arg_6_0.clickTF, arg_6_0.skipAnim)

	local var_6_0 = arg_6_0._tf.GetComponent(typeof(DftAniEvent))

	var_6_0.SetTriggerEvent(function(arg_7_0)
		if arg_6_0.contextData.commander.isSSR():
			arg_6_0.playerEffect()

		var_6_0.SetTriggerEvent(None))
	var_6_0.SetEndEvent(function()
		arg_6_0.isAnim = False

		setActive(arg_6_0.clickTF, True)
		var_6_0.SetEndEvent(None)
		arg_6_1())

def var_0_0.playerEffect(arg_9_0):
	PoolMgr.GetInstance().GetUI("AL_zhihuimiao_zhipian", True, function(arg_10_0)
		arg_9_0.effect = arg_10_0

		SetParent(arg_10_0, arg_9_0._tf)
		setActive(arg_10_0, True))

def var_0_0.openMsgBox(arg_11_0, arg_11_1):
	arg_11_0.isShowMsgBox = True

	local function var_11_0()
		arg_11_0.msgbox.ActionInvoke("Show", arg_11_1)

	if arg_11_0.msgbox.GetLoaded():
		var_11_0()
	else
		arg_11_0.msgbox.Load()
		arg_11_0.msgbox.CallbackInvoke(var_11_0)

def var_0_0.closeMsgBox(arg_13_0):
	arg_13_0.isShowMsgBox = None

	arg_13_0.msgbox.ActionInvoke("Hide")

def var_0_0.didEnter(arg_14_0):
	arg_14_0.updateInfo()
	onButton(arg_14_0, arg_14_0.shareBtn, function()
		pg.ShareMgr.GetInstance().Share(pg.ShareMgr.TypeCommander, pg.ShareMgr.PANEL_TYPE_PINK, {
			weight = LayerWeightConst.TOP_LAYER
		}), SFX_PANEL)
	onButton(arg_14_0, arg_14_0.skipBtn, function(arg_16_0)
		if arg_14_0.isAnim:
			return

		getProxy(CommanderProxy).hasSkipFlag = True

		arg_14_0.DoExit(), SFX_CANCEL)
	onButton(arg_14_0, arg_14_0.lockBtn, function()
		local var_17_0 = getProxy(CommanderProxy).getCommanderById(arg_14_0.contextData.commander.id).getLock()

		arg_14_0.emit(NewCommanderMediator.ON_LOCK, arg_14_0.contextData.commander.id, 1 - var_17_0), SFX_PANEL)
	onButton(arg_14_0, arg_14_0.unlockBtn, function()
		local var_18_0 = getProxy(CommanderProxy).getCommanderById(arg_14_0.contextData.commander.id).getLock()

		arg_14_0.emit(NewCommanderMediator.ON_LOCK, arg_14_0.contextData.commander.id, 1 - var_18_0), SFX_PANEL)
	onButton(arg_14_0, arg_14_0.clickTF, function()
		if arg_14_0.isAnim:
			arg_14_0.antor.SetBool("play", False)

			if arg_14_0.contextData.commander.isSSR() and not arg_14_0.effect:
				arg_14_0.playerEffect()

			arg_14_0.isAnim = None
		else
			arg_14_0.DoExit(), SFX_CANCEL)

def var_0_0.DoExit(arg_20_0):
	if arg_20_0.contextData.commander.ShouldTipLock():
		arg_20_0.openMsgBox({
			content = i18n("commander_lock_tip"),
			def onYes:()
				arg_20_0.emit(NewCommanderMediator.ON_LOCK, arg_20_0.contextData.commander.id, 1)
				arg_20_0.emit(var_0_0.ON_CLOSE),
			layer = LayerWeightConst.SECOND_LAYER + 2,
			def onNo:()
				arg_20_0.emit(var_0_0.ON_CLOSE)
		})
	else
		arg_20_0.emit(var_0_0.ON_CLOSE)

def var_0_0.updateLockState(arg_23_0):
	local var_23_0 = getProxy(CommanderProxy).getCommanderById(arg_23_0.contextData.commander.id).getLock()

	setActive(arg_23_0.lockBtn, var_23_0 != 0)
	setActive(arg_23_0.unlockBtn, var_23_0 == 0)

def var_0_0.updateInfo(arg_24_0, arg_24_1):
	local var_24_0 = arg_24_0.contextData.commander

	arg_24_0.updateLockState(var_24_0.getLock())

	arg_24_0.nameTF.text = var_24_0.getName()
	arg_24_0.nationTF.text = Nation.Nation2Name(var_24_0.getConfig("nationality"))

	local var_24_1 = var_24_0.getSkills()[1]

	arg_24_0.skillTF.text = var_24_1.getConfig("name")

	local var_24_2 = Commander.rarity2Print(var_24_0.getRarity())

	LoadImageSpriteAsync("CommanderRarity/" .. var_24_2, arg_24_0.rarityTF, True)
	setCommanderPaintingPrefab(arg_24_0.paintTF, var_24_0.getPainting(), "get")

	arg_24_0.painting = var_24_0

	arg_24_0.updateAbilitys()
	arg_24_0.updateTalents()
	setText(arg_24_0.dateTF, pg.TimeMgr.GetInstance().CurrentSTimeDesc("%y%m%d"))

	if arg_24_1:
		arg_24_1()

def var_0_0.updateAbilitys(arg_25_0):
	local var_25_0 = arg_25_0.contextData.commander.getAbilitys()

	eachChild(arg_25_0.abilitysTF, function(arg_26_0)
		local var_26_0 = go(arg_26_0).name
		local var_26_1 = var_25_0[var_26_0]

		setText(arg_26_0.Find("slider/point"), var_26_1.value)

		arg_26_0.Find("slider").GetComponent(typeof(Slider)).value = var_26_1.value / CommanderConst.MAX_ABILITY)

def var_0_0.updateTalents(arg_27_0):
	local var_27_0 = arg_27_0.contextData.commander.getTalents()

	arg_27_0.talentsList.make(function(arg_28_0, arg_28_1, arg_28_2)
		if arg_28_0 == UIItemList.EventUpdate:
			local var_28_0 = var_27_0[arg_28_1 + 1]

			setActive(arg_28_2.Find("empty"), not var_28_0)
			setActive(arg_28_2.Find("icon"), var_28_0)

			if var_28_0:
				GetImageSpriteFromAtlasAsync("CommanderTalentIcon/" .. var_28_0.getConfig("icon"), "", arg_28_2.Find("icon"))

			onButton(arg_27_0, arg_28_2, function()
				arg_27_0.openTreePanel(var_28_0), SFX_PANEL))
	arg_27_0.talentsList.align(3)

def var_0_0.onBackPressed(arg_30_0):
	if arg_30_0.isShowMsgBox:
		arg_30_0.closeMsgBox()

		return

def var_0_0.willExit(arg_31_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_31_0._tf, pg.UIMgr.GetInstance().UIMain)
	arg_31_0.treePanel.Destroy()
	arg_31_0.msgbox.Destroy()
	retCommanderPaintingPrefab(arg_31_0.paintTF, arg_31_0.painting.getPainting())

	if arg_31_0.effect:
		PoolMgr.GetInstance().ReturnUI("AL_zhihuimiao_zhipian", arg_31_0.effect)

	if arg_31_0.contextData.onExit:
		arg_31_0.contextData.onExit()

return var_0_0
