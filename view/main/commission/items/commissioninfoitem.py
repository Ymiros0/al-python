local var_0_0 = class("CommissionInfoItem")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.view = arg_1_2

	pg.DelegateInfo.New(arg_1_0)

	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_1.transform
	arg_1_0.parentTF = arg_1_0._tf.parent
	arg_1_0.goBtn = arg_1_0._tf.Find("frame/go_btn")
	arg_1_0.finishedBtn = arg_1_0._tf.Find("frame/finish_btn")
	arg_1_0.toggle = arg_1_0._tf.Find("frame")
	arg_1_0.foldFlag = arg_1_0._tf.Find("frame/tip")
	arg_1_0.finishedCounterContainer = arg_1_0._tf.Find("frame/counter/finished")
	arg_1_0.ongoingCounterContainer = arg_1_0._tf.Find("frame/counter/ongoing")
	arg_1_0.leisureCounterContainer = arg_1_0._tf.Find("frame/counter/leisure")
	arg_1_0.finishedCounter = arg_1_0._tf.Find("frame/counter/finished/Text").GetComponent(typeof(Text))
	arg_1_0.ongoingCounter = arg_1_0._tf.Find("frame/counter/ongoing/Text").GetComponent(typeof(Text))
	arg_1_0.leisureCounter = arg_1_0._tf.Find("frame/counter/leisure/Text").GetComponent(typeof(Text))

	local var_1_0 = arg_1_0._tf.Find("list")
	local var_1_1 = var_1_0.GetChild(0)

	arg_1_0.uilist = UIItemList.New(var_1_0, var_1_1)

	setActive(arg_1_0.finishedCounterContainer, False)
	setActive(arg_1_0.ongoingCounterContainer, False)
	setActive(arg_1_0.leisureCounterContainer, False)

	if getProxy(SettingsProxy).IsMellowStyle():
		setText(arg_1_0.goBtn.Find("Image"), i18n("commission_label_go_mellow"))
		setText(arg_1_0.finishedBtn.Find("Image"), i18n("commission_label_finish_mellow"))
		setText(var_1_1.Find("unlock/leisure/go_btn/Image"), i18n("commission_label_go_mellow"))
		setText(var_1_1.Find("unlock/finished/finish_btn/Image"), i18n("commission_label_finish_mellow"))
	else
		setText(arg_1_0.goBtn.Find("Image"), i18n("commission_label_go"))
		setText(arg_1_0.finishedBtn.Find("Image"), i18n("commission_label_finish"))
		setText(var_1_1.Find("unlock/leisure/go_btn/Image"), i18n("commission_label_go"))
		setText(var_1_1.Find("unlock/finished/finish_btn/Image"), i18n("commission_label_finish"))

	arg_1_0.timers = {}

def var_0_0.Init(arg_2_0):
	onToggle(arg_2_0, arg_2_0.toggle, function(arg_3_0)
		arg_2_0.foldFlag.localScale = Vector3(1, arg_3_0 and -1 or 1, 1)

		if not arg_3_0:
			return

		local var_3_0, var_3_1 = arg_2_0.CanOpen()

		if not var_3_0:
			pg.TipsMgr.GetInstance().ShowTips(var_3_1)
			triggerToggle(arg_2_0._tf, False)

			return

		arg_2_0.Adpater()

		if not arg_2_0.isInitList:
			arg_2_0.UpdateList()

			arg_2_0.isInitList = True, SFX_PANEL)
	onButton(arg_2_0, arg_2_0.goBtn, function()
		arg_2_0.OnSkip(), SFX_PANEL)
	onButton(arg_2_0, arg_2_0.finishedBtn, function()
		arg_2_0.OnFinishAll(), SFX_PANEL)
	arg_2_0.uilist.make(function(arg_6_0, arg_6_1, arg_6_2)
		if arg_6_0 == UIItemList.EventUpdate:
			local var_6_0 = arg_2_0.list[arg_6_1 + 1]

			arg_2_0.UpdateListItem(arg_6_1 + 1, var_6_0, arg_6_2))
	arg_2_0.Flush()

def var_0_0.Adpater(arg_7_0):
	local var_7_0 = arg_7_0.parentTF.localPosition.x
	local var_7_1 = Vector3(var_7_0, math.abs(arg_7_0._tf.localPosition.y), 0)

	arg_7_0.parentTF.localPosition = var_7_1

def var_0_0.CanOpen(arg_8_0):
	return True

def var_0_0.Flush(arg_9_0):
	if arg_9_0.CanOpen():
		arg_9_0.OnFlush()

def var_0_0.Update(arg_10_0):
	arg_10_0.Flush()

	if arg_10_0.isInitList:
		arg_10_0.UpdateList()

def var_0_0.RemoveTimers(arg_11_0):
	for iter_11_0, iter_11_1 in pairs(arg_11_0.timers or {}):
		iter_11_1.Stop()

	arg_11_0.timers = {}

def var_0_0.UpdateList(arg_12_0):
	arg_12_0.RemoveTimers()

	local var_12_0, var_12_1 = arg_12_0.GetList()

	arg_12_0.uilist.align(var_12_1 or #var_12_0)

	arg_12_0.list = var_12_0

def var_0_0.OnFlush(arg_13_0):
	return

def var_0_0.UpdateListItem(arg_14_0, arg_14_1, arg_14_2, arg_14_3):
	return

def var_0_0.GetList(arg_15_0):
	assert(False)

def var_0_0.OnSkip(arg_16_0):
	assert(False)

def var_0_0.OnFinishAll(arg_17_0):
	assert(False)

def var_0_0.emit(arg_18_0, ...):
	arg_18_0.view.emit(...)

def var_0_0.Dispose(arg_19_0):
	pg.DelegateInfo.Dispose(arg_19_0)
	arg_19_0.RemoveTimers()

return var_0_0
