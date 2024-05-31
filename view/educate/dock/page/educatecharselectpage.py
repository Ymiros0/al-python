local var_0_0 = class("EducateCharSelectPage", import("view.base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "EducateCharDockSelectUI"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.titleTxt = arg_2_0.findTF("title/Text").GetComponent(typeof(Text))
	arg_2_0.labelTxt = arg_2_0.findTF("left/label/icon").GetComponent(typeof(Image))
	arg_2_0.paintingTr = arg_2_0.findTF("left/print/painting")
	arg_2_0.scrollrect = arg_2_0.findTF("list")
	arg_2_0.uiItemList = UIItemList.New(arg_2_0.findTF("list/content"), arg_2_0.findTF("list/content/tpl"))
	arg_2_0.dotUIItemList = UIItemList.New(arg_2_0.findTF("list/dots"), arg_2_0.findTF("list/dots/tpl"))
	arg_2_0.confirmBtn = arg_2_0.findTF("confirm_btn")
	arg_2_0.nextArr = arg_2_0.findTF("prints/next")
	arg_2_0.prevArr = arg_2_0.findTF("prints/prev")
	arg_2_0.nextPrint = arg_2_0.findTF("prints/print1")
	arg_2_0.prevPrint = arg_2_0.findTF("prints/print2")
	arg_2_0.animation = arg_2_0._tf.GetComponent(typeof(Animation))
	arg_2_0.dftAniEvent = arg_2_0._tf.GetComponent(typeof(DftAniEvent))

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0.confirmBtn, function()
		if arg_3_0.doAnim:
			return

		if not arg_3_0.selectedId:
			return

		arg_3_0.doAnim = True

		arg_3_0.Back(function()
			arg_3_0.doAnim = None

			arg_3_0.emit(EducateCharDockScene.ON_CONFIRM, arg_3_0.selectedId)), SFX_PANEL)
	arg_3_0.bind(EducateCharDockScene.MSG_CLEAR_TIP, function(arg_6_0, arg_6_1)
		return)

def var_0_0.Back(arg_7_0, arg_7_1):
	arg_7_0.dftAniEvent.SetEndEvent(function(arg_8_0)
		arg_7_0.dftAniEvent.SetEndEvent(None)
		arg_7_1())
	arg_7_0.animation.Play("anim_educate_chardockselect_out")

def var_0_0.Update(arg_9_0, arg_9_1, arg_9_2):
	arg_9_0.group = arg_9_1

	if arg_9_1.IsSelected(arg_9_2):
		arg_9_0.selectedId = arg_9_2

	arg_9_0.timers = {}

	arg_9_0.FlushPainting(arg_9_1.GetShowPainting())
	arg_9_0.InitLabel()
	arg_9_0.UpdateTitle()
	arg_9_0.InitList()
	arg_9_0.UpdateDots()
	arg_9_0.Show()

def var_0_0.UpdateTitle(arg_10_0):
	local var_10_0 = arg_10_0.group

	arg_10_0.titleTxt.text = var_10_0.GetTitle()

def var_0_0.InitLabel(arg_11_0):
	local var_11_0 = arg_11_0.group

	arg_11_0.labelTxt.sprite = GetSpriteFromAtlas("ui/EducateDockUI_atlas", var_11_0.GetSpriteName())

	arg_11_0.labelTxt.SetNativeSize()

def var_0_0.FlushPainting(arg_12_0, arg_12_1):
	arg_12_0.ReturnPainting()
	setPaintingPrefab(arg_12_0.paintingTr, arg_12_1, "tb1")

	arg_12_0.paintingName = arg_12_1

def var_0_0.InitList(arg_13_0):
	local var_13_0 = arg_13_0.group.GetCharIdList()

	arg_13_0.ReturnCardList()

	arg_13_0.cards = {}

	arg_13_0.RemoveAllTimer()
	arg_13_0.uiItemList.make(function(arg_14_0, arg_14_1, arg_14_2)
		if arg_14_0 == UIItemList.EventUpdate:
			local var_14_0 = var_13_0[arg_14_1 + 1]

			arg_13_0.UpdateCard(arg_14_2, var_14_0, arg_14_1)

			arg_13_0.cards[var_14_0] = arg_14_2)
	arg_13_0.uiItemList.align(#var_13_0)

	local var_13_1 = #var_13_0 > 2

	setActive(arg_13_0.nextArr, var_13_1)
	setActive(arg_13_0.prevArr, var_13_1)
	setActive(arg_13_0.nextPrint, not var_13_1)
	setActive(arg_13_0.prevPrint, not var_13_1)
	scrollTo(arg_13_0.scrollrect, 0, 0)

def var_0_0.UpdateDots(arg_15_0):
	local var_15_0 = arg_15_0.group.GetCharIdList()

	arg_15_0.dotUIItemList.make(function(arg_16_0, arg_16_1, arg_16_2)
		if arg_16_0 == UIItemList.EventUpdate:
			local var_16_0 = var_15_0[arg_16_1 + 1]

			setActive(arg_16_2.Find("Image"), var_16_0 == arg_15_0.selectedId))
	arg_15_0.dotUIItemList.align(#var_15_0)

def var_0_0.IsLockCard(arg_17_0, arg_17_1):
	local var_17_0 = getProxy(EducateProxy).GetSecretaryIDs()

	return not table.contains(var_17_0, arg_17_1)

def var_0_0.UpdateCard(arg_18_0, arg_18_1, arg_18_2, arg_18_3):
	local var_18_0 = arg_18_1.Find("anim_root")
	local var_18_1 = pg.secretary_special_ship[arg_18_2]

	setPaintingPrefab(var_18_0.Find("mask/painting"), var_18_1.prefab, "tb")
	setActive(var_18_0.Find("lock"), arg_18_0.IsLockCard(var_18_1.id))
	setText(var_18_0.Find("lock/desc/Text"), var_18_1.unlock_desc)

	local function var_18_2()
		setActive(var_18_0.Find("tip"), getProxy(SettingsProxy)._ShouldEducateCharTip(arg_18_2))

	var_18_2()

	local function var_18_3()
		setActive(var_18_0.Find("mark"), True)

		arg_18_0.selectedId = arg_18_2

		arg_18_0.UpdateDots()
		arg_18_0.FlushPainting(var_18_1.prefab)

		arg_18_0.prevSelected = var_18_0

		arg_18_0.animation.Stop()
		arg_18_0.animation.Play("anim_educate_chardockselect_change")

	onButton(arg_18_0, var_18_0, function()
		if arg_18_0.IsLockCard(arg_18_2):
			pg.TipsMgr.GetInstance().ShowTips(i18n("secretary_special_lock_tip"))

			return

		if getProxy(SettingsProxy).ClearEducateCharTip(arg_18_2):
			var_18_2()

		arg_18_0.ClearPrevSelected()

		if arg_18_0.selectedId == arg_18_2:
			arg_18_0.selectedId = 0

			arg_18_0.UpdateDots()

			return

		var_18_3(), SFX_PANEL)

	if arg_18_0.selectedId == arg_18_2:
		var_18_3()

	setActive(var_18_0, False)

	arg_18_0.timers[arg_18_3] = Timer.New(function()
		setActive(var_18_0, True)
		var_18_0.GetComponent(typeof(Animation)).Play("anim_educate_chardockselect_tpl"), math.max(1e-05, arg_18_3 * 0.066), 1)

	arg_18_0.timers[arg_18_3].Start()

def var_0_0.RemoveAllTimer(arg_23_0):
	for iter_23_0, iter_23_1 in pairs(arg_23_0.timers):
		iter_23_1.Stop()

		iter_23_1 = None

	arg_23_0.timers = {}

def var_0_0.ClearPrevSelected(arg_24_0):
	if arg_24_0.prevSelected:
		setActive(arg_24_0.prevSelected.Find("mark"), False)

		arg_24_0.prevSelected = None

def var_0_0.ReturnPainting(arg_25_0):
	if arg_25_0.paintingName:
		retPaintingPrefab(arg_25_0.paintingTr, arg_25_0.paintingName)

		arg_25_0.paintingName = None

def var_0_0.ReturnCardList(arg_26_0):
	for iter_26_0, iter_26_1 in pairs(arg_26_0.cards or {}):
		local var_26_0 = pg.secretary_special_ship[iter_26_0]

		retPaintingPrefab(iter_26_1.Find("mask/painting"), var_26_0.prefab)

	arg_26_0.cards = {}

def var_0_0.Hide(arg_27_0):
	var_0_0.super.Hide(arg_27_0)
	arg_27_0.ClearPrevSelected()

	arg_27_0.selectedId = None

	arg_27_0.ReturnCardList()
	arg_27_0.RemoveAllTimer()

def var_0_0.OnDestroy(arg_28_0):
	arg_28_0.RemoveAllTimer()
	arg_28_0.ReturnPainting()
	arg_28_0.ReturnCardList()
	arg_28_0.dftAniEvent.SetEndEvent(None)

return var_0_0
