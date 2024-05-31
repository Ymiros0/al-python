local var_0_0 = class("GuildOfficeLogPage", import("....base.BaseSubView"))
local var_0_1 = {
	{
		GuildConst.TYPE_SUPPLY,
		GuildConst.START_BATTLE,
		GuildConst.TECHNOLOGY
	},
	{
		GuildConst.TYPE_DONATE,
		GuildConst.WEEKLY_TASK
	},
	{
		GuildConst.TECHNOLOGY_OVER,
		GuildConst.SWITCH_TOGGLE
	}
}

def var_0_0.Flag2Filter(arg_1_0, arg_1_1):
	local var_1_0 = {}

	for iter_1_0, iter_1_1 in ipairs(var_0_1):
		local var_1_1 = bit.lshift(1, iter_1_0)

		if bit.band(arg_1_1, var_1_1) > 0:
			for iter_1_2, iter_1_3 in ipairs(iter_1_1):
				table.insert(var_1_0, iter_1_3)

	return var_1_0

def var_0_0.getUIName(arg_2_0):
	return "GuildOfficeLogPage"

def var_0_0.OnLoaded(arg_3_0):
	arg_3_0.uilist = UIItemList.New(arg_3_0.findTF("frame/window/sliders/list/content"), arg_3_0.findTF("frame/window/sliders/list/content/tpl"))

	setText(arg_3_0.findTF("frame/window/top/bg/infomation/title"), i18n("guild_log_title"))

	arg_3_0.btnAll = arg_3_0.findTF("frame/window/sliders/filter/1")
	arg_3_0.btns = {
		arg_3_0.findTF("frame/window/sliders/filter/2"),
		arg_3_0.findTF("frame/window/sliders/filter/3"),
		arg_3_0.findTF("frame/window/sliders/filter/4")
	}

def var_0_0.OnInit(arg_4_0):
	onButton(arg_4_0, arg_4_0._tf.Find("frame/window/top/btnBack"), function()
		arg_4_0.Close(), SFX_PANEL)
	onButton(arg_4_0, arg_4_0._tf.Find("frame"), function()
		arg_4_0.Close(), SFX_PANEL)
	onButton(arg_4_0, arg_4_0.btnAll, function()
		arg_4_0.SelectAll(), SFX_PANEL)

	for iter_4_0, iter_4_1 in ipairs(arg_4_0.btns):
		onButton(arg_4_0, iter_4_1, function()
			if arg_4_0.allFlags != arg_4_0.flags and bit.band(arg_4_0.flags, bit.lshift(1, iter_4_0)) > 0:
				arg_4_0.UnSelectFlag(iter_4_0, iter_4_1)
			else
				arg_4_0.SelectFlag(iter_4_0, iter_4_1), SFX_PANEL)

def var_0_0.SelectAll(arg_9_0):
	arg_9_0.flags = 0

	for iter_9_0, iter_9_1 in pairs(arg_9_0.btns):
		setActive(iter_9_1.Find("sel"), False)

		arg_9_0.flags = bit.bor(arg_9_0.flags, bit.lshift(1, iter_9_0))

	setActive(arg_9_0.btnAll.Find("sel"), True)
	arg_9_0.Filter()

def var_0_0.UnSelectFlag(arg_10_0, arg_10_1, arg_10_2):
	setActive(arg_10_2.Find("sel"), False)

	local var_10_0 = bit.bxor(arg_10_0.flags, bit.lshift(1, arg_10_1))

	if var_10_0 == 0:
		arg_10_0.SelectAll()
	else
		arg_10_0.flags = var_10_0

		arg_10_0.Filter()

def var_0_0.SelectFlag(arg_11_0, arg_11_1, arg_11_2):
	local var_11_0 = arg_11_0.flags

	local function var_11_1()
		setActive(arg_11_2.Find("sel"), True)
		setActive(arg_11_0.btnAll.Find("sel"), False)

		arg_11_0.flags = bit.bor(arg_11_0.flags, bit.lshift(1, arg_11_1))

		arg_11_0.Filter()

	if var_11_0 != arg_11_0.allFlags and arg_11_0.allFlags == bit.bor(arg_11_0.flags, bit.lshift(1, arg_11_1)):
		arg_11_0.SelectAll()
	elif var_11_0 == arg_11_0.allFlags:
		arg_11_0.flags = 0

		var_11_1()
	else
		var_11_1()

def var_0_0.Show(arg_13_0, arg_13_1):
	arg_13_0.guild = arg_13_1

	pg.UIMgr.GetInstance().BlurPanel(arg_13_0._tf)
	setActive(arg_13_0._tf, True)
	triggerButton(arg_13_0.btnAll)

	arg_13_0.allFlags = arg_13_0.flags

def var_0_0.Filter(arg_14_0):
	local var_14_0 = arg_14_0.guild.getCapitalLogs()

	arg_14_0.displays = {}

	local var_14_1 = arg_14_0.Flag2Filter(arg_14_0.flags)

	for iter_14_0, iter_14_1 in ipairs(var_14_0):
		if iter_14_1.IsSameType(var_14_1):
			table.insert(arg_14_0.displays, iter_14_1)

	arg_14_0.uilist.make(function(arg_15_0, arg_15_1, arg_15_2)
		if arg_15_0 == UIItemList.EventUpdate:
			local var_15_0 = arg_14_0.displays[arg_15_1 + 1]

			setText(arg_15_2, var_15_0.getText()))
	arg_14_0.uilist.align(#arg_14_0.displays)

def var_0_0.Close(arg_16_0):
	setActive(arg_16_0._tf, False)
	pg.UIMgr.GetInstance().UnblurPanel(arg_16_0._tf, arg_16_0._parentTf)

def var_0_0.OnDestroy(arg_17_0):
	arg_17_0.Close()

return var_0_0
