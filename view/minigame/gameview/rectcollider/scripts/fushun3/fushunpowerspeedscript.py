local var_0_0 = class("FuShunPowerSpeedScript", import("..RectBaseScript"))
local var_0_1 = {
	400,
	450
}
local var_0_2 = 20

def var_0_0.onInit(arg_1_0):
	arg_1_0._loop = False
	arg_1_0._active = False
	arg_1_0._weight = 4
	arg_1_0._overrideAble = False
	arg_1_0._lastActive = False
	arg_1_0._scriptTime = 10
	arg_1_0._name = "FuShunPowerSpeedScript"

def var_0_0.onStep(arg_2_0):
	if arg_2_0._active:
		local var_2_0 = arg_2_0._collisionInfo.getVelocity()
		local var_2_1 = arg_2_0._collisionInfo.getPos()

		if var_2_1.y >= var_0_1[2]:
			var_2_0.y = -10
		elif var_2_1.y <= var_0_1[1]:
			var_2_0.y = 10
		else
			var_2_0.y = 0
			var_2_0.x = var_0_2

			if not arg_2_0.powerFlag:
				arg_2_0._event.emit(Fushun3GameEvent.script_power_event)

				arg_2_0.powerFlag = True

		arg_2_0._collisionInfo.setVelocity(var_2_0)
	else
		arg_2_0.powerFlag = False

		if arg_2_0._collisionInfo.script == arg_2_0:
			arg_2_0._collisionInfo.removeScript()

	arg_2_0._lastActive = arg_2_0._active

def var_0_0.onLateStep(arg_3_0):
	return

def var_0_0.onTrigger(arg_4_0):
	return

return var_0_0
