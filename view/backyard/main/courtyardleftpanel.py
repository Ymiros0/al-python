local var_0_0 = class("CourtYardLeftPanel", import(".CourtYardBasePanel"))

def var_0_0.GetUIName(arg_1_0):
	return "main/leftPanel"

def var_0_0.init(arg_2_0):
	arg_2_0.viewBtn = arg_2_0.findTF("eye_btn")

def var_0_0.OnRegister(arg_3_0):
	onToggle(arg_3_0, arg_3_0.viewBtn, function(arg_4_0)
		arg_3_0.emit(CourtYardMediator.FOLD, arg_4_0), SFX_PANEL)

def var_0_0.OnEnterEditMode(arg_5_0):
	var_0_0.super.OnEnterEditMode(arg_5_0)
	setActive(arg_5_0.viewBtn, False)

def var_0_0.OnExitEditMode(arg_6_0):
	var_0_0.super.OnExitEditMode(arg_6_0)
	setActive(arg_6_0.viewBtn, True)

def var_0_0.UpdateFloor(arg_7_0):
	return

def var_0_0.OnVisitRegister(arg_8_0):
	onToggle(arg_8_0, arg_8_0.viewBtn, function(arg_9_0)
		arg_8_0.emit(CourtYardMediator.FOLD, arg_9_0), SFX_PANEL)

def var_0_0.GetMoveX(arg_10_0):
	return {}

def var_0_0.OnFlush(arg_11_0, arg_11_1):
	return

return var_0_0
