local var_0_0 = class("FuShunAttakeScript", import("..RectBaseScript"))

def var_0_0.onInit(arg_1_0):
	arg_1_0._loop = False
	arg_1_0._active = False
	arg_1_0._weight = 2
	arg_1_0._scriptTime = 0.4
	arg_1_0._overrideAble = True
	arg_1_0._name = "FuShunAttakeScript"

def var_0_0.onStep(arg_2_0):
	if arg_2_0._active and arg_2_0._collisionInfo.below and not arg_2_0._lateActive:
		arg_2_0._event.emit(Fushun3GameEvent.script_attack_event)

def var_0_0.onLateStep(arg_3_0):
	return

def var_0_0.onTrigger(arg_4_0):
	if Application.isEditor and arg_4_0._triggerKey == KeyCode.J and arg_4_0._triggerStatus and arg_4_0.checkScirptApply():
		arg_4_0._active = True

return var_0_0
