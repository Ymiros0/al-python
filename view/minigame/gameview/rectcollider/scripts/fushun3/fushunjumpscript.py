local var_0_0 = class("FuShunJumpScript", import("..RectBaseScript"))

def var_0_0.onInit(arg_1_0):
	arg_1_0._loop = False
	arg_1_0._active = False
	arg_1_0._weight = 2
	arg_1_0._scriptTime = 0.01
	arg_1_0._lastActive = False
	arg_1_0._name = "FuShunJumpScript"

def var_0_0.onStep(arg_2_0):
	if arg_2_0._active:
		if arg_2_0._collisionInfo.below and arg_2_0._collisionInfo.useJumpTimes == 0:
			local var_2_0 = arg_2_0._collisionInfo.getVelocity()

			var_2_0.x = 0

			arg_2_0._collisionInfo.setVelocity(var_2_0)
	elif arg_2_0._lastActive and arg_2_0.checkScirptApply() and arg_2_0._collisionInfo.below and arg_2_0._collisionInfo.useJumpTimes == 0:
		local var_2_1 = arg_2_0._collisionInfo.getVelocity()

		var_2_1.y = arg_2_0._collisionInfo.config.maxJumpVelocity
		arg_2_0._collisionInfo.useJumpTimes = 1

		if arg_2_0._event:
			arg_2_0._event.emit(Fushun3GameEvent.script_jump_event)

		var_2_1.x = arg_2_0._collisionInfo.config.moveSpeed

		arg_2_0._collisionInfo.setVelocity(var_2_1)

	arg_2_0._lastActive = arg_2_0._active

def var_0_0.onLateStep(arg_3_0):
	if arg_3_0._collisionInfo.below and arg_3_0._collisionInfo.useJumpTimes == 1:
		arg_3_0._collisionInfo.useJumpTimes = 0

def var_0_0.onTrigger(arg_4_0, arg_4_1, arg_4_2):
	if Application.isEditor and arg_4_0._triggerKey == KeyCode.Space:
		if not arg_4_2:
			print()

		if arg_4_0.checkScirptApply():
			arg_4_0._active = True

return var_0_0
