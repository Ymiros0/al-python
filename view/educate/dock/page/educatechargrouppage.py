local var_0_0 = class("EducateCharGroupPage", import("view.base.BaseEventLogic"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	pg.DelegateInfo.New(arg_1_0)
	var_0_0.super.Ctor(arg_1_0, arg_1_2)

	arg_1_0.contextData = arg_1_3
	arg_1_0.tf = arg_1_1
	arg_1_0.go = arg_1_1.gameObject
	arg_1_0.confirmBtn = findTF(arg_1_1, "confirm_btn")
	arg_1_0.cancelBtn = findTF(arg_1_1, "cancel_btn")
	arg_1_0.uiItemList = UIItemList.New(findTF(arg_1_1, "main/list"), findTF(arg_1_1, "main/list/tpl"))
	arg_1_0.profileBtn = findTF(arg_1_1, "left/icon")
	arg_1_0.animation = arg_1_1.GetComponent(typeof(Animation))
	arg_1_0.dftAniEvent = arg_1_1.GetComponent(typeof(DftAniEvent))
	arg_1_0.timers = {}

	arg_1_0.RegisterEvent()

def var_0_0.RegisterEvent(arg_2_0):
	onButton(arg_2_0, arg_2_0.profileBtn, function()
		arg_2_0.emit(EducateCharDockMediator.GO_PROFILE), SFX_PANEL)
	arg_2_0.bind(EducateCharDockScene.MSG_CLEAR_TIP, function(arg_4_0, arg_4_1)
		arg_2_0.FlushList(arg_2_0.selectedId))

def var_0_0.Update(arg_5_0):
	arg_5_0.InitList()

def var_0_0.Show(arg_6_0):
	setActive(arg_6_0.tf, True)

def var_0_0.Hide(arg_7_0):
	setActive(arg_7_0.tf, False)
	arg_7_0.RemoveAllTimer()

def var_0_0.GetSelectedId(arg_8_0):
	return getProxy(PlayerProxy).getRawData().GetEducateCharacter()

def var_0_0.InitList(arg_9_0):
	arg_9_0.cards = {}
	arg_9_0.selectedId = arg_9_0.GetSelectedId()

	local var_9_0 = getProxy(EducateProxy).GetEducateGroupList()

	table.sort(var_9_0, function(arg_10_0, arg_10_1)
		return arg_10_0.GetSortWeight() < arg_10_1.GetSortWeight())
	arg_9_0.RemoveAllTimer()
	arg_9_0.uiItemList.make(function(arg_11_0, arg_11_1, arg_11_2)
		if arg_11_0 == UIItemList.EventUpdate:
			local var_11_0 = var_9_0[arg_11_1 + 1]

			arg_9_0.InitCard(arg_11_2, var_11_0, arg_11_1)
			arg_9_0.UpdateCard(arg_11_2, var_11_0)

			arg_9_0.cards[arg_11_2] = var_11_0)
	arg_9_0.uiItemList.align(#var_9_0)

def var_0_0.FlushList(arg_12_0, arg_12_1):
	arg_12_0.selectedId = arg_12_1

	for iter_12_0, iter_12_1 in pairs(arg_12_0.cards):
		arg_12_0.UpdateCard(iter_12_0, iter_12_1)

def var_0_0.InitCard(arg_13_0, arg_13_1, arg_13_2, arg_13_3):
	local var_13_0 = arg_13_1.Find("anim_root")
	local var_13_1 = var_13_0.Find("label/Text").GetComponent(typeof(Image))

	var_13_1.sprite = GetSpriteFromAtlas("ui/EducateDockUI_atlas", arg_13_2.GetSpriteName())

	var_13_1.SetNativeSize()

	local var_13_2 = arg_13_2.GetShowPainting()

	setPaintingPrefab(var_13_0.Find("mask/painting"), var_13_2, "tb2")
	onButton(arg_13_0, var_13_0, function()
		if arg_13_0.doAnim:
			return

		if arg_13_2.IsLock():
			pg.TipsMgr.GetInstance().ShowTips(i18n("secretary_special_lock_tip"))

			return

		arg_13_0.doAnim = True

		arg_13_0.dftAniEvent.SetEndEvent(function(arg_15_0)
			arg_13_0.doAnim = None

			arg_13_0.dftAniEvent.SetEndEvent(None)
			arg_13_0.emit(EducateCharDockScene.ON_SELECT, arg_13_2, arg_13_0.selectedId))
		arg_13_0.animation.Play("anim_educate_chardock_grouppage_out"), SFX_PANEL)
	setActive(var_13_0, False)

	arg_13_0.timers[arg_13_3] = Timer.New(function()
		setActive(var_13_0, True)
		var_13_0.GetComponent(typeof(Animation)).Play("anim_educate_chardock_tpl"), math.max(1e-05, arg_13_3 * 0.066), 1)

	arg_13_0.timers[arg_13_3].Start()

def var_0_0.UpdateCard(arg_17_0, arg_17_1, arg_17_2):
	local var_17_0 = arg_17_1.Find("anim_root")

	setActive(var_17_0.Find("lock"), arg_17_2.IsLock())
	setActive(var_17_0.Find("mark"), arg_17_2.IsSelected(arg_17_0.selectedId))
	setText(var_17_0.Find("lock/desc/Text"), arg_17_2.GetUnlockDesc())
	setActive(var_17_0.Find("tip"), arg_17_2.ShouldTip())

def var_0_0.RemoveAllTimer(arg_18_0):
	for iter_18_0, iter_18_1 in pairs(arg_18_0.timers):
		iter_18_1.Stop()

		iter_18_1 = None

	arg_18_0.timers = {}

def var_0_0.Destroy(arg_19_0):
	for iter_19_0, iter_19_1 in pairs(arg_19_0.cards or {}):
		local var_19_0 = iter_19_0.Find("mask/painting")
		local var_19_1 = iter_19_1.GetShowPainting()

		retPaintingPrefab(var_19_0, var_19_1)

	pg.DelegateInfo.Dispose(arg_19_0)
	arg_19_0.dftAniEvent.SetEndEvent(None)
	arg_19_0.RemoveAllTimer()

return var_0_0
