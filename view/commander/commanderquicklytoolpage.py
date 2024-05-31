local var_0_0 = class("CommanderQuicklyToolPage", import("..base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "CommanderQuicklyToolPage"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.closeBtn = arg_2_0.findTF("frame/close_btn")
	arg_2_0.cancelBtn = arg_2_0.findTF("frame/cancel_btn")
	arg_2_0.confirmBtn = arg_2_0.findTF("frame/confirm_btn")
	arg_2_0.addBtn = arg_2_0.findTF("frame/content/count/add")
	arg_2_0.reduceBtn = arg_2_0.findTF("frame/content/count/reduce")
	arg_2_0.valueTxt = arg_2_0.findTF("frame/content/count/Text").GetComponent(typeof(Text))
	arg_2_0.time1Txt = arg_2_0.findTF("frame/content/time/Text").GetComponent(typeof(Text))
	arg_2_0.maxTxt = arg_2_0.findTF("frame/total/Text").GetComponent(typeof(Text))

	setText(arg_2_0.findTF("frame/content/label1"), i18n("commander_box_quickly_tool_tip_1"))
	setText(arg_2_0.findTF("frame/content/label2"), i18n("commander_box_quickly_tool_tip_2"))
	setText(arg_2_0.findTF("frame/content/time/label"), i18n("commander_box_quickly_tool_tip_3"))

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.closeBtn, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.cancelBtn, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.addBtn, function()
		if arg_3_0.maxCnt == 0:
			return

		arg_3_0.UpdateValue(math.min(arg_3_0.value + 1, arg_3_0.maxCnt)), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.reduceBtn, function()
		if arg_3_0.value <= 1:
			return

		arg_3_0.UpdateValue(math.max(1, arg_3_0.value - 1)), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.confirmBtn, function()
		if arg_3_0.value <= 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("cat_accelfrate_notenough"))

			return

		if arg_3_0.value > arg_3_0.maxCnt:
			return

		local var_9_0 = arg_3_0.CalcMaxUsageCnt()

		if var_9_0 <= 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("commander_box_was_finished"))

			return

		if var_9_0 < arg_3_0.value:
			arg_3_0.UpdateValue(var_9_0)
			pg.TipsMgr.GetInstance().ShowTips(i18n("comander_tool_cnt_is_reclac"))

			return

		arg_3_0.emit(CommanderCatMediator.USE_QUICKLY_TOOL, arg_3_0.itemId, arg_3_0.value, arg_3_0.boxId)
		arg_3_0.Hide(), SFX_PANEL)

def var_0_0.Show(arg_10_0, arg_10_1, arg_10_2):
	setParent(arg_10_0._tf, pg.UIMgr.GetInstance().OverlayMain)
	var_0_0.super.Show(arg_10_0)

	arg_10_0.itemId = arg_10_2
	arg_10_0.boxId = arg_10_1
	arg_10_0.cost = Item.getConfigData(arg_10_0.itemId).usage_arg[1]
	arg_10_0.costM = arg_10_0.cost / 60

	local var_10_0 = getProxy(BagProxy).getItemCountById(arg_10_2)
	local var_10_1 = arg_10_0.CalcMaxUsageCnt()

	arg_10_0.maxCnt = math.min(var_10_1, var_10_0)
	arg_10_0.maxTxt.text = var_10_0

	arg_10_0.UpdateValue(arg_10_0.maxCnt)

def var_0_0.Hide(arg_11_0):
	var_0_0.super.Hide(arg_11_0)
	setParent(arg_11_0._tf, arg_11_0._parentTf)

def var_0_0.UpdateValue(arg_12_0, arg_12_1):
	arg_12_0.value = arg_12_1
	arg_12_0.valueTxt.text = arg_12_1

	local var_12_0 = arg_12_0.costM * arg_12_1 * 60
	local var_12_1 = getProxy(CommanderProxy).getBoxById(arg_12_0.boxId).getFinishTime() - var_12_0

	arg_12_0.AddTimer(var_12_1)

def var_0_0.CalcMaxUsageCnt(arg_13_0):
	local var_13_0 = getProxy(CommanderProxy).getBoxById(arg_13_0.boxId).getFinishTime() - pg.TimeMgr.GetInstance().GetServerTime()

	if var_13_0 > 0:
		return (math.ceil(var_13_0 / arg_13_0.cost))
	else
		return 0

def var_0_0.AddTimer(arg_14_0, arg_14_1):
	arg_14_0.RemoveTimer()

	arg_14_0.timer = Timer.New(function()
		local var_15_0 = pg.TimeMgr.GetInstance().GetServerTime()
		local var_15_1 = arg_14_1 - var_15_0

		if var_15_1 <= 0:
			arg_14_0.RemoveTimer()

			arg_14_0.time1Txt.text = "00.00.00"
		else
			local var_15_2 = pg.TimeMgr.GetInstance().DescCDTime(var_15_1)

			arg_14_0.time1Txt.text = var_15_2, 1, -1)

	arg_14_0.timer.Start()
	arg_14_0.timer.func()

def var_0_0.RemoveTimer(arg_16_0):
	if arg_16_0.timer:
		arg_16_0.timer.Stop()

		arg_16_0.timer = None

def var_0_0.Hide(arg_17_0):
	var_0_0.super.Hide(arg_17_0)
	arg_17_0.RemoveTimer()

def var_0_0.OnDestroy(arg_18_0):
	arg_18_0.RemoveTimer()

return var_0_0
