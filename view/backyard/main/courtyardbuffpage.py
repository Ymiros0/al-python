local var_0_0 = class("CourtYardBuffPage", import("...base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "CourtYardBuffListPanel"

def var_0_0.OnLoaded(arg_2_0):
	arg_2_0.closeBtn = arg_2_0.findTF("frame/close")
	arg_2_0.uiItemList = UIItemList.New(arg_2_0.findTF("frame/list/content"), arg_2_0.findTF("frame/list/content/tpl"))
	arg_2_0.totalExp = arg_2_0.findTF("frame/subtitle/Text").GetComponent(typeof(Text))

	setText(arg_2_0.findTF("frame/title"), i18n("courtyard_label_exp_addition"))
	setText(arg_2_0.findTF("frame/subtitle"), i18n("courtyard_label_total_exp_addition"))

	arg_2_0.timers = {}

def var_0_0.OnInit(arg_3_0):
	onButton(arg_3_0, arg_3_0._tf, function()
		arg_3_0.Hide(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.closeBtn, function()
		arg_3_0.Hide(), SFX_PANEL)

def var_0_0.Show(arg_6_0, arg_6_1):
	var_0_0.super.Show(arg_6_0)
	arg_6_0.Flush(arg_6_1)

	arg_6_0.list = arg_6_1

def var_0_0.Flush(arg_7_0, arg_7_1):
	local var_7_0 = 0
	local var_7_1 = {}

	for iter_7_0, iter_7_1 in ipairs(arg_7_1):
		if iter_7_1.getLeftTime() > 0:
			table.insert(var_7_1, iter_7_1)

	arg_7_0.uiItemList.make(function(arg_8_0, arg_8_1, arg_8_2)
		if arg_8_0 == UIItemList.EventUpdate:
			local var_8_0 = var_7_1[arg_8_1 + 1]
			local var_8_1 = {
				count = 0,
				type = DROP_TYPE_BUFF,
				id = var_8_0.id
			}

			updateDrop(arg_8_2.Find("award"), var_8_1)
			setText(arg_8_2.Find("Text"), var_8_0.getConfig("desc"))
			arg_7_0.AddTimer(arg_8_2.Find("time"), var_8_0)

			local var_8_2 = var_8_0.getConfig("benefit_effect")

			var_7_0 = var_7_0 + tonumber(var_8_2))
	arg_7_0.uiItemList.align(#var_7_1)

	arg_7_0.totalExp.text = var_7_0 .. "%"

def var_0_0.AddTimer(arg_9_0, arg_9_1, arg_9_2):
	arg_9_0.RemoveTimer(arg_9_2.id)

	local var_9_0 = Timer.New(function()
		local var_10_0 = arg_9_2.getLeftTime()

		if var_10_0 > 0:
			local var_10_1 = pg.TimeMgr.GetInstance().DescCDTime(var_10_0)
			local var_10_2 = var_10_0 <= 600 and setColorStr(var_10_1, COLOR_RED) or setColorStr(var_10_1, "#72bc42")

			setText(arg_9_1, var_10_2)
		else
			arg_9_0.RemoveTimer(arg_9_2.id)
			arg_9_0.Flush(arg_9_0.list), 1, -1)

	var_9_0.func()
	var_9_0.Start()

	arg_9_0.timers[arg_9_2.id] = var_9_0

def var_0_0.RemoveTimer(arg_11_0, arg_11_1):
	if arg_11_0.timers[arg_11_1]:
		arg_11_0.timers[arg_11_1].Stop()

		arg_11_0.timers[arg_11_1] = None

def var_0_0.RemoveAllTimer(arg_12_0):
	for iter_12_0, iter_12_1 in pairs(arg_12_0.timers or {}):
		iter_12_1.Stop()

	arg_12_0.timers = {}

def var_0_0.OnDestroy(arg_13_0):
	arg_13_0.RemoveAllTimer()

return var_0_0
