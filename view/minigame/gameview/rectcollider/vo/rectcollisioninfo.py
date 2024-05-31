local var_0_0 = class("RectCollisionInfo")

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.above = False
	arg_1_0.below = False
	arg_1_0.left = False
	arg_1_0.right = False
	arg_1_0.fullSliding = False
	arg_1_0.climbingSlope = False
	arg_1_0.descendingSlope = False
	arg_1_0.slidingDownMaxSlope = False
	arg_1_0.slopeAngle = 0
	arg_1_0.slopeAngleOld = 0
	arg_1_0.slopeNormal = Vector3.zero
	arg_1_0.horizontalLeftTfs = {}
	arg_1_0.horizontalRightTfs = {}
	arg_1_0.verticalTopTfs = {}
	arg_1_0.verticalBottomTfs = {}
	arg_1_0.script = None
	arg_1_0.scriptWeight = None
	arg_1_0.scriptTime = None
	arg_1_0.scriptOverrideAble = None
	arg_1_0.frameRate = 0.016666666666666666
	arg_1_0.config = RectCollisionData.New(arg_1_1)
	arg_1_0.layerMask = LayerMask.GetMask("Collider", "Character")
	arg_1_0.ignoreLayerMask = {
		LayerMask.NameToLayer("Character")
	}
	arg_1_0.playerInput = Vector2(0, 0)
	arg_1_0.directionalInput = Vector2.zero
	arg_1_0._velocity = Vector3.zero
	arg_1_0.standingOnPlatform = False
	arg_1_0.velocityXSmoothing = 0
	arg_1_0.moveAmountOld = 0
	arg_1_0.moveAmount = 0
	arg_1_0.fallingThroughPlatform = False
	arg_1_0.MoveDir = 1
	arg_1_0.FaceDir = 1
	arg_1_0.LockFaceDir = False
	arg_1_0.useJumpTimes = 0
	arg_1_0.holdInSlider = False
	arg_1_0.lockHorizontalMove = False
	arg_1_0.lockVerticalMove = False
	arg_1_0.sprint = False
	arg_1_0.damaged = False

	function arg_1_0.wallSliding()
		return (arg_1_0.left and arg_1_0.FaceDir == -1 or arg_1_0.right and arg_1_0.FaceDir == 1) and not arg_1_0.below and arg_1_0.fullSliding

	function arg_1_0.wallSlidingDown()
		return arg_1_0.wallSliding and arg_1_0.moveAmount < 0

	function arg_1_0.wallDirX()
		return arg_1_0.getWallDirX()

def var_0_0.getVelocity(arg_5_0):
	return arg_5_0._velocity

def var_0_0.setVelocity(arg_6_0, arg_6_1):
	arg_6_0._velocity.x = arg_6_1.x
	arg_6_0._velocity.y = arg_6_1.y
	arg_6_0._velocity.z = arg_6_1.z

def var_0_0.changeVelocity(arg_7_0, arg_7_1, arg_7_2, arg_7_3):
	arg_7_0._velocity.x = arg_7_1 or arg_7_0._velocity.x
	arg_7_0._velocity.y = arg_7_2 or arg_7_0._velocity.y
	arg_7_0._velocity.z = arg_7_3 or arg_7_0._velocity.z

def var_0_0.setPos(arg_8_0, arg_8_1):
	arg_8_0._anchoredPosition = arg_8_1

def var_0_0.getPos(arg_9_0):
	return arg_9_0._anchoredPosition or Vector2.zero

def var_0_0.setScript(arg_10_0, arg_10_1, arg_10_2, arg_10_3, arg_10_4):
	arg_10_0.script = arg_10_1
	arg_10_0.scriptWeight = arg_10_2
	arg_10_0.scriptTime = arg_10_3
	arg_10_0.scriptOverrideAble = arg_10_4

def var_0_0.removeScript(arg_11_0):
	if arg_11_0.script:
		arg_11_0.script.active(False)

	arg_11_0.script = None
	arg_11_0.scriptWeight = None
	arg_11_0.scriptTime = None
	arg_11_0.scriptOverrideAble = None

def var_0_0.getWallDirX(arg_12_0):
	if arg_12_0.fullSliding:
		if arg_12_0.left:
			return -1
		elif arg_12_0.right:
			return 1

	return 0

def var_0_0.reset(arg_13_0):
	arg_13_0.above = False
	arg_13_0.below = False
	arg_13_0.left = False
	arg_13_0.right = False
	arg_13_0.climbingSlope = False
	arg_13_0.descendingSlope = False
	arg_13_0.slidingDownMaxSlope = False
	arg_13_0.lockHorizontalMove = False
	arg_13_0.lockVerticalMove = False
	arg_13_0.fullSliding = False
	arg_13_0.slopeNormal = Vector3.zero
	arg_13_0.slopeAngleOld = arg_13_0.slopeAngle
	arg_13_0.slopeAngle = 0
	arg_13_0.standingOnPlatform = False
	arg_13_0.horizontalLeftTfs = {}
	arg_13_0.horizontalRightTfs = {}
	arg_13_0.verticalTopTfs = {}
	arg_13_0.verticalBottomTfs = {}

return var_0_0
