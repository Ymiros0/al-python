local var_0_0 = class("SailBoatItem")
local var_0_1

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	var_0_1 = SailBoatGameVo
	arg_1_0._tf = arg_1_1
	arg_1_0._event = arg_1_2
	arg_1_0._collider = GetComponent(findTF(arg_1_0._tf, "bound"), typeof(BoxCollider2D))

def var_0_0.setData(arg_2_0, arg_2_1):
	arg_2_0._itemData = arg_2_1

def var_0_0.start(arg_3_0):
	arg_3_0._removeFlag = False
	arg_3_0._sceneWidth, arg_3_0._sceneHeight = var_0_1.scene_width, var_0_1.scene_height
	arg_3_0._maxRemoveHeight = -arg_3_0._sceneHeight * 2
	arg_3_0._maxRemoveWidth = arg_3_0._sceneWidth * 2
	arg_3_0._speed = arg_3_0.getConfig("speed")

	arg_3_0.setVisible(True)

def var_0_0.step(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_0._tf.anchoredPosition
	local var_4_1 = var_0_1.GetSceneSpeed()

	arg_4_0._speed.x = arg_4_0._speed.x * arg_4_1 + var_4_1.x
	arg_4_0._speed.y = arg_4_0._speed.y * arg_4_1 + var_4_1.y
	var_4_0.x = var_4_0.x + arg_4_0._speed.x
	var_4_0.y = var_4_0.y + arg_4_0._speed.y
	arg_4_0._tf.anchoredPosition = var_4_0

	if not arg_4_0._removeFlag:
		if var_4_0.y < arg_4_0._maxRemoveHeight:
			arg_4_0._removeFlag = True
		elif math.abs(var_4_0.x) > arg_4_0._maxRemoveWidth:
			arg_4_0._removeFlag = True

def var_0_0.getSpeed(arg_5_0):
	return arg_5_0._speed

def var_0_0.setContent(arg_6_0, arg_6_1):
	arg_6_0._content = arg_6_1

	SetParent(arg_6_0._tf, arg_6_1)

def var_0_0.getId(arg_7_0):
	return arg_7_0._itemData.id

def var_0_0.setVisible(arg_8_0, arg_8_1):
	setActive(arg_8_0._tf, arg_8_1)

def var_0_0.setPosition(arg_9_0, arg_9_1):
	arg_9_0._tf.anchoredPosition = arg_9_1

def var_0_0.clear(arg_10_0):
	arg_10_0.setVisible(False)

def var_0_0.setRemoveFlag(arg_11_0, arg_11_1):
	arg_11_0._removeFlag = arg_11_1

def var_0_0.getRemoveFlag(arg_12_0):
	return arg_12_0._removeFlag

def var_0_0.dispose(arg_13_0):
	var_0_1 = None

def var_0_0.getColliderData(arg_14_0):
	local var_14_0 = arg_14_0._content.InverseTransformPoint(arg_14_0._collider.bounds.min)

	if not arg_14_0._boundData:
		local var_14_1 = arg_14_0._content.InverseTransformPoint(arg_14_0._collider.bounds.max)

		arg_14_0._boundData = {
			width = math.floor(var_14_1.x - var_14_0.x),
			height = math.floor(var_14_1.y - var_14_0.y)
		}

	return var_14_0, arg_14_0._boundData

def var_0_0.getWorldColliderData(arg_15_0):
	local var_15_0 = arg_15_0._collider.bounds.min

	if not arg_15_0._worldBoundData:
		local var_15_1 = arg_15_0._collider.bounds.max

		arg_15_0._worldBoundData = {
			width = var_15_1.x - var_15_0.x,
			height = var_15_1.y - var_15_0.y
		}

	return var_15_0, arg_15_0._worldBoundData

def var_0_0.getTf(arg_16_0):
	return arg_16_0._tf

def var_0_0.getUseData(arg_17_0):
	return {
		score = arg_17_0.getConfig("score"),
		hp = arg_17_0.getConfig("hp"),
		skill = arg_17_0.getConfig("skill")
	}

def var_0_0.checkPositionInRange(arg_18_0, arg_18_1):
	local var_18_0 = arg_18_0._tf.anchoredPosition
	local var_18_1 = math.abs(var_18_0.x - arg_18_1.x)
	local var_18_2 = math.abs(var_18_0.y - arg_18_1.y)
	local var_18_3 = arg_18_0.getConfig("range")

	if var_18_1 < var_18_3.x and var_18_2 < var_18_3.y:
		return True

	return False

def var_0_0.getPosition(arg_19_0):
	return arg_19_0._tf.anchoredPosition

def var_0_0.getConfig(arg_20_0, arg_20_1):
	return arg_20_0._itemData[arg_20_1]

return var_0_0
