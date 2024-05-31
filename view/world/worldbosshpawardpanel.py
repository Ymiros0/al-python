local var_0_0 = class("WorldBossHPAwardPanel", import("view.base.BaseSubView"))

def var_0_0.Ctor(arg_1_0, ...):
	var_0_0.super.Ctor(arg_1_0, ...)

	arg_1_0.buffer = FuncBuffer.New()

def var_0_0.getUIName(arg_2_0):
	return "WorldBossHPAwardWindow"

def var_0_0.OnInit(arg_3_0):
	setText(arg_3_0.findTF("window/top/bg/infomation"), i18n("world_expedition_reward_display"))

	arg_3_0.itemList = arg_3_0.findTF("window/panel/viewport/list")

	onButton(arg_3_0, arg_3_0.findTF("window/top/btnBack"), function()
		arg_3_0.Hide(), SFX_CANCEL)
	onButton(arg_3_0, arg_3_0.findTF("bg_dark"), function()
		arg_3_0.Hide())
	arg_3_0.buffer.SetNotifier(arg_3_0)
	arg_3_0.buffer.ExcuteAll()

def var_0_0.Show(arg_6_0):
	var_0_0.super.Show(arg_6_0)
	pg.UIMgr.GetInstance().BlurPanel(arg_6_0._tf)

def var_0_0.Hide(arg_7_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_7_0._tf)
	var_0_0.super.Hide(arg_7_0)

def var_0_0.UpdateView(arg_8_0, arg_8_1):
	arg_8_0.Show()

	local var_8_0 = arg_8_1.GetHP()

	if arg_8_1.IsPeriodEnemy():
		var_8_0 = math.min(var_8_0, nowWorld().GetHistoryLowestHP(arg_8_1.id))

	local var_8_1 = arg_8_1.GetBattleStageId()
	local var_8_2 = pg.world_expedition_data[var_8_1]
	local var_8_3 = var_8_2 and var_8_2.phase_drop_display

	UIItemList.StaticAlign(arg_8_0.itemList, arg_8_0.itemList.GetChild(0), var_8_3 and #var_8_3 or 0, function(arg_9_0, arg_9_1, arg_9_2)
		if arg_9_0 != UIItemList.EventUpdate:
			return

		local var_9_0 = var_8_3[arg_9_1 + 1]
		local var_9_1 = var_8_0 <= var_9_0[1]

		setText(arg_9_2.Find("target"), i18n("world_expedition_reward_display2", math.ceil(var_9_0[1] / 100)))
		setActive(arg_9_2.Find("mask"), var_9_1)
		UIItemList.StaticAlign(arg_9_2.Find("awards"), arg_9_2.Find("awards").GetChild(0), #var_9_0[2], function(arg_10_0, arg_10_1, arg_10_2)
			if arg_10_0 != UIItemList.EventUpdate:
				return

			local var_10_0 = var_9_0[2][arg_10_1 + 1]
			local var_10_1 = {
				type = var_10_0[1],
				id = var_10_0[2],
				count = var_10_0[3]
			}

			updateDrop(arg_10_2.Find("IconTpl"), var_10_1)
			onButton(arg_8_0, arg_10_2.Find("IconTpl"), function()
				arg_8_0.emit(BaseUI.ON_DROP, var_10_1))))

return var_0_0
