﻿local var_0_0 = class("RectColliderController")

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	arg_1_0.collisionInfo = arg_1_1
	arg_1_0.origins = arg_1_2
	arg_1_0.zeroVec = Vector2.zero
end

function var_0_0.platformMove(arg_2_0, arg_2_1)
	arg_2_0.collisionInfo.standingOnPlatform = true

	arg_2_0:move(arg_2_1)
end

function var_0_0.move(arg_3_0, arg_3_1)
	arg_3_0:updateCollisionInfo(arg_3_1)

	if arg_3_1.y <= 0 then
		RectCollisionVertical.DescendSlope(arg_3_1, arg_3_0.collisionInfo, arg_3_0.origins)
	end

	RectCollisionHorizontal.HorizontalCollisions(arg_3_1, arg_3_0.collisionInfo, arg_3_0.origins)

	if arg_3_1.y ~= 0 then
		RectCollisionVertical.VerticalCollisions(arg_3_1, arg_3_0.collisionInfo, arg_3_0.origins)
	end

	arg_3_0.collisionInfo.moveAmount = arg_3_1

	arg_3_0:afterUpdateCollisionInfo()
end

function var_0_0.updateCollisionInfo(arg_4_0, arg_4_1)
	arg_4_0.origins:updateRaycastOrigins()
	arg_4_0.collisionInfo:reset()

	arg_4_0.collisionInfo.moveAmountOld = arg_4_1
	arg_4_0.collisionInfo.MoveDir = arg_4_1.x > 0 and 1 or arg_4_0.collisionInfo.MoveDir
	arg_4_0.collisionInfo.MoveDir = arg_4_1.x < 0 and -1 or arg_4_0.collisionInfo.MoveDir
end

function var_0_0.afterUpdateCollisionInfo(arg_5_0)
	arg_5_0.collisionInfo.below = arg_5_0.collisionInfo.standingOnPlatform or arg_5_0.collisionInfo.below
end

return var_0_0
