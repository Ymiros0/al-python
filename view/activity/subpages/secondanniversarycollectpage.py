local var_0_0 = class("SecondAnniversaryCollectPage", import("...base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.btnContainer = arg_1_0.findTF("BtnList")
	arg_1_0.btn1 = arg_1_0.findTF("1", arg_1_0.btnContainer)
	arg_1_0.btn2 = arg_1_0.findTF("2", arg_1_0.btnContainer)
	arg_1_0.btn3 = arg_1_0.findTF("3", arg_1_0.btnContainer)
	arg_1_0.btn4 = arg_1_0.findTF("4", arg_1_0.btnContainer)
	arg_1_0.btn5 = arg_1_0.findTF("5", arg_1_0.btnContainer)
	arg_1_0.btn6 = arg_1_0.findTF("6", arg_1_0.btnContainer)

def var_0_0.OnFirstFlush(arg_2_0):
	onButton(arg_2_0, arg_2_0.btn1, function()
		arg_2_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.SKINSHOP), SFX_PANEL)
	onButton(arg_2_0, arg_2_0.btn2, function()
		arg_2_0.emit(ActivityMediator.SELECT_ACTIVITY, ActivityConst.ACTIVITY_TYPE_RETURN_AWARD_ID2), SFX_PANEL)
	onButton(arg_2_0, arg_2_0.btn3, function()
		arg_2_0.emit(ActivityMediator.SELECT_ACTIVITY, ActivityConst.YIDALI_MAIN_ID), SFX_PANEL)
	onButton(arg_2_0, arg_2_0.btn4, function()
		arg_2_0.emit(ActivityMediator.SELECT_ACTIVITY, ActivityConst.ANNIVERSARY_LOGIN_ID), SFX_PANEL)
	onButton(arg_2_0, arg_2_0.btn5, function()
		arg_2_0.emit(ActivityMediator.SELECT_ACTIVITY, ActivityConst.CARDPAIR_ZQ), SFX_PANEL)
	onButton(arg_2_0, arg_2_0.btn6, function()
		arg_2_0.emit(ActivityMediator.SELECT_ACTIVITY, ActivityConst.DACHAOLIFU_SKIN), SFX_PANEL)

return var_0_0
