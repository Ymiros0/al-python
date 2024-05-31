local var_0_0 = class("FuShunMovementScript", import("..RectBaseScript"))

def var_0_0.onInit(arg_1_0):
	arg_1_0._loop = True
	arg_1_0._active = True
	arg_1_0._weight = 1
	arg_1_0._scriptTime = None
	arg_1_0._name = "FuShunMovementScript"

def var_0_0.onStep(arg_2_0):
	arg_2_0._collisionInfo.playerInput.x = 1

	local var_2_0 = arg_2_0._collisionInfo.playerInput.x * arg_2_0._collisionInfo.config.moveSpeed
	local var_2_1 = arg_2_0._collisionInfo.getVelocity()
	local var_2_2 = arg_2_0._collisionInfo.velocityXSmoothing

	if var_2_1.x == var_2_0:
		var_2_2 = 0

	local var_2_3 = arg_2_0._collisionInfo.below and arg_2_0._collisionInfo.config.accelerationTimeGrounded or arg_2_0._collisionInfo.config.accelerationTimeAirborne
	local var_2_4

	var_2_1.x, var_2_4 = Mathf.SmoothDamp(var_2_1.x, var_2_0, var_2_2, var_2_3)

	if not arg_2_0._collisionInfo.below:
		var_2_1.y = var_2_1.y + arg_2_0._collisionInfo.config.gravity * arg_2_0._collisionInfo.frameRate

	arg_2_0._collisionInfo.setVelocity(var_2_1)

	arg_2_0._collisionInfo.velocityXSmoothing = var_2_4

def var_0_0.onLateStep(arg_3_0):
	return

def var_0_0.onTrigger(arg_4_0):
	if Application.isEditor and arg_4_0._triggerKey == KeyCode.A or arg_4_0._triggerKey == KeyCode.D:
		local var_4_0 = arg_4_0._keyInfo.getKeyCode(KeyCode.A)
		local var_4_1 = arg_4_0._keyInfo.getKeyCode(KeyCode.D)

		if arg_4_0._triggerKey == KeyCode.A:
			arg_4_0._collisionInfo.playerInput.x = arg_4_0._triggerStatus and -1 or var_4_1 and 1 or 0
		elif arg_4_0._triggerKey == KeyCode.D:
			arg_4_0._collisionInfo.playerInput.x = arg_4_0._triggerStatus and 1 or var_4_0 and -1 or 0

		arg_4_0._collisionInfo.directionalInput = arg_4_0._collisionInfo.playerInput

return var_0_0
