local var_0_0 = class("OreContainerControl")

var_0_0.BREAK_MOVE_TIME = 0.5

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.binder = arg_1_1
	arg_1_0._tf = arg_1_2

	arg_1_0.Init()

def var_0_0.Init(arg_2_0):
	arg_2_0.AddListener()

	arg_2_0.deliverSpeed = 50
	arg_2_0.mainTF = arg_2_0._tf.Find("Container_1/break")

def var_0_0.AddListener(arg_3_0):
	arg_3_0.binder.bind(OreGameConfig.EVENT_DELIVER, function(arg_4_0, arg_4_1)
		arg_3_0.PlayDeliverAnim(arg_4_1.status, arg_4_1.pos, arg_4_1.oreTF))
	arg_3_0.binder.bind(OreGameConfig.EVENT_PLAY_CONTAINER_HIT, function(arg_5_0, arg_5_1)
		arg_3_0.PlayHitAnim(arg_5_1.status, arg_5_1.pos, arg_5_1.hitPos, arg_5_1.oreTF))

var_0_0.DeliveOffsetY = {
	-7,
	-7,
	-16
}

def var_0_0.PlayDeliverAnim(arg_6_0, arg_6_1, arg_6_2, arg_6_3):
	arg_6_0.mainTF = arg_6_0._tf.Find("Container_" .. arg_6_1 .. "/deliver")

	setAnchoredPosition(arg_6_0.mainTF, {
		x = arg_6_2.x,
		y = arg_6_2.y + var_0_0.DeliveOffsetY[arg_6_1]
	})
	setActive(arg_6_0.mainTF, True)

	local var_6_0 = arg_6_0.mainTF.Find("ore/pos")

	removeAllChildren(var_6_0)
	cloneTplTo(arg_6_3, var_6_0)
	arg_6_0.mainTF.Find("BK/Image").GetComponent(typeof(Animator)).Play("Deliver_2_Lift_BK")
	arg_6_0.mainTF.Find("FR/Image").GetComponent(typeof(Animator)).Play("Deliver_2_Lift_FR")

	arg_6_0.deliverTime = 0

var_0_0.moveRata = {
	1,
	1.2,
	1.5
}

def var_0_0.PlayHitAnim(arg_7_0, arg_7_1, arg_7_2, arg_7_3, arg_7_4):
	if arg_7_1 == OreAkashiControl.STATUS_NULL:
		return

	arg_7_0.mainTF = arg_7_0._tf.Find("Container_" .. arg_7_1 .. "/break")

	setAnchoredPosition(arg_7_0.mainTF, arg_7_2)
	setActive(arg_7_0.mainTF, True)

	local var_7_0 = arg_7_0.mainTF.parent.Find("ore/pos")

	removeAllChildren(var_7_0)

	arg_7_0.orePosList = {}
	arg_7_0.oreTFs = cloneTplTo(arg_7_4, var_7_0).Find("oreTF")
	arg_7_0.hitPos = {
		x = -arg_7_3.x * var_0_0.moveRata[arg_7_1],
		y = -arg_7_3.y * var_0_0.moveRata[arg_7_1]
	}

	setAnchoredPosition(var_7_0, Vector2(arg_7_2.x + arg_7_0.hitPos.x, arg_7_2.y + arg_7_0.hitPos.y))
	arg_7_0.mainTF.Find("main/Image").GetComponent(typeof(Animator)).Play("Break")

	arg_7_0.breakTime = 0

	eachChild(arg_7_0.oreTFs, function(arg_8_0)
		arg_7_0.orePosList[arg_8_0.name] = {
			x = math.random(50) - 25,
			y = math.random(50) - 25
		})

def var_0_0.Reset(arg_9_0):
	arg_9_0.deliverTime = None
	arg_9_0.breakTime = None
	arg_9_0.oreTFs = None

	setActive(arg_9_0.mainTF, False)
	setActive(arg_9_0.mainTF.parent.Find("ore/pos"), False)
	removeAllChildren(arg_9_0.mainTF.parent.Find("ore/pos"))
	setAnchoredPosition(arg_9_0.mainTF, Vector2(0, 0))

def var_0_0.OnTimer(arg_10_0, arg_10_1):
	if arg_10_0.deliverTime:
		local var_10_0 = arg_10_1 * arg_10_0.deliverSpeed

		setAnchoredPosition(arg_10_0.mainTF, {
			x = arg_10_0.mainTF.anchoredPosition.x,
			y = arg_10_0.mainTF.anchoredPosition.y - var_10_0
		})

		arg_10_0.deliverTime = arg_10_0.deliverTime + arg_10_1

		if arg_10_0.mainTF.anchoredPosition.y < -230:
			removeAllChildren(arg_10_0.mainTF.Find("ore/pos"))
			arg_10_0.Reset()

	if arg_10_0.breakTime:
		local var_10_1 = {
			x = arg_10_0.mainTF.anchoredPosition.x + arg_10_0.hitPos.x * arg_10_1 / var_0_0.BREAK_MOVE_TIME,
			y = arg_10_0.mainTF.anchoredPosition.y + arg_10_0.hitPos.y * arg_10_1 / var_0_0.BREAK_MOVE_TIME
		}

		setAnchoredPosition(arg_10_0.mainTF, var_10_1)

		arg_10_0.breakTime = arg_10_0.breakTime + arg_10_1

		if arg_10_0.breakTime >= var_0_0.BREAK_MOVE_TIME / 3:
			if not isActive(arg_10_0.mainTF.parent.Find("ore/pos")):
				setActive(arg_10_0.mainTF.parent.Find("ore/pos"), True)

			eachChild(arg_10_0.oreTFs, function(arg_11_0)
				local var_11_0 = arg_10_0.orePosList[arg_11_0.name]
				local var_11_1 = {
					x = arg_11_0.anchoredPosition.x + var_11_0.x * arg_10_1 / (var_0_0.BREAK_MOVE_TIME * 2 / 3),
					y = arg_11_0.anchoredPosition.y + var_11_0.y * arg_10_1 / (var_0_0.BREAK_MOVE_TIME * 2 / 3)
				}

				setAnchoredPosition(arg_11_0, var_11_1))

		if arg_10_0.breakTime >= var_0_0.BREAK_MOVE_TIME:
			arg_10_0.Reset()

return var_0_0
