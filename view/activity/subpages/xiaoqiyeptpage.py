local var_0_0 = class("XiaoQiYePtPage", import(".TemplatePage.PtTemplatePage"))

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.hearts = UIItemList.New(arg_1_0.findTF("AD/heart"), arg_1_0.findTF("AD/heart/mark"))
	arg_1_0.helpBtn = arg_1_0.findTF("AD/help_btn")

	onButton(arg_1_0, arg_1_0.helpBtn, function()
		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			type = MSGBOX_TYPE_HELP,
			helps = pg.gametip.gametip_xiaoqiye.tip
		}), SFX_PANEL)

def var_0_0.OnFirstFlush(arg_3_0):
	var_0_0.super.OnFirstFlush(arg_3_0)
	onButton(arg_3_0, arg_3_0.battleBtn, function()
		arg_3_0.emit(ActivityMediator.SPECIAL_BATTLE_OPERA), SFX_PANEL)

def var_0_0.OnUpdateFlush(arg_5_0):
	var_0_0.super.OnUpdateFlush(arg_5_0)

	local var_5_0, var_5_1, var_5_2 = arg_5_0.ptData.GetLevelProgress()

	arg_5_0.hearts.make(function(arg_6_0, arg_6_1, arg_6_2)
		if arg_6_0 == UIItemList.EventUpdate:
			setActive(arg_6_2, arg_6_1 < arg_5_0.ptData.level))
	arg_5_0.hearts.align(var_5_1)

return var_0_0
