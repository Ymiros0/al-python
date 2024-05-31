local var_0_0 = class("RectColliderController")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.collisionInfo = arg_1_1
	arg_1_0.origins = arg_1_2
	arg_1_0.zeroVec = Vector2.zero

def var_0_0.platformMove(arg_2_0, arg_2_1):
	arg_2_0.collisionInfo.standingOnPlatform = True

	arg_2_0.move(arg_2_1)

def var_0_0.move(arg_3_0, arg_3_1):
	arg_3_0.updateCollisionInfo(arg_3_1)

	if arg_3_1.y <= 0:
		RectCollisionVertical.DescendSlope(arg_3_1, arg_3_0.collisionInfo, arg_3_0.origins)

	RectCollisionHorizontal.HorizontalCollisions(arg_3_1, arg_3_0.collisionInfo, arg_3_0.origins)

	if arg_3_1.y != 0:
		RectCollisionVertical.VerticalCollisions(arg_3_1, arg_3_0.collisionInfo, arg_3_0.origins)

	arg_3_0.collisionInfo.moveAmount = arg_3_1

	arg_3_0.afterUpdateCollisionInfo()

def var_0_0.updateCollisionInfo(arg_4_0, arg_4_1):
	arg_4_0.origins.updateRaycastOrigins()
	arg_4_0.collisionInfo.reset()

	arg_4_0.collisionInfo.moveAmountOld = arg_4_1
	arg_4_0.collisionInfo.MoveDir = arg_4_1.x > 0 and 1 or arg_4_0.collisionInfo.MoveDir
	arg_4_0.collisionInfo.MoveDir = arg_4_1.x < 0 and -1 or arg_4_0.collisionInfo.MoveDir

def var_0_0.afterUpdateCollisionInfo(arg_5_0):
	arg_5_0.collisionInfo.below = arg_5_0.collisionInfo.standingOnPlatform or arg_5_0.collisionInfo.below

return var_0_0
