local var_0_0 = class("OreAkashiControl")

var_0_0.STATUS_NULL = 0
var_0_0.STATUS_WOOD_BOX = 1
var_0_0.STATUS_IRON_BOX = 2
var_0_0.STATUS_CART = 3
var_0_0.HIT_DELTA = 15
var_0_0.HIT_MOVE_TIME = 0.5

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_0.binder = arg_1_1
	arg_1_0._tf = arg_1_2
	arg_1_0.collisionMgr = arg_1_3

	arg_1_0.Init()

def var_0_0.Init(arg_2_0):
	arg_2_0.uiMgr = pg.UIMgr.GetInstance()

	arg_2_0.collisionMgr.SetAkashiObject(arg_2_0)

	arg_2_0.oreTpl = arg_2_0._tf.Find("oreTpl")

	arg_2_0.AddListener()
	arg_2_0.AddDftAniEvent()
	arg_2_0.Reset()

	arg_2_0.aabbTF = arg_2_0._tf.Find("aabb")

	setActive(arg_2_0.aabbTF, OreGameConfig.SHOW_AABB)

	arg_2_0.aabb = OreGameHelper.GetAABBWithTF(arg_2_0.aabbTF)

def var_0_0.AddListener(arg_3_0):
	arg_3_0.binder.bind(OreGameConfig.EVENT_DO_CARRY, function(arg_4_0, arg_4_1)
		arg_3_0.weight = arg_3_0.weight + arg_4_1.weight
		arg_3_0.point = arg_3_0.point + arg_4_1.point

		arg_3_0.CheckStatus()
		arg_3_0.AddOre(arg_4_1.type))
	arg_3_0.binder.bind(OreGameConfig.EVENT_AKASHI_HIT, function(arg_5_0, arg_5_1)
		if arg_3_0.invincible:
			return

		arg_3_0.PlayHitAnim(arg_5_1.dir, arg_5_1.class, arg_5_1.y))

def var_0_0.AddDftAniEvent(arg_6_0):
	eachChild(arg_6_0._tf.Find("main"), function(arg_7_0)
		arg_7_0.Find("main/Image").GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
			if arg_6_0.isDeliver:
				arg_6_0.ResetData()
			else
				arg_6_0.ResetData()
				arg_6_0.mainTF.Find("main/Image").GetComponent(typeof(Animator)).Play("Idle_S_Sad")

				arg_6_0.mainAnimName = "Idle_S_Sad"))
	eachChild(arg_6_0._tf.Find("effect"), function(arg_9_0)
		arg_9_0.GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
			setActive(arg_9_0, False)))

def var_0_0.Reset(arg_11_0):
	setAnchoredPosition(arg_11_0._tf, Vector2(0, -100))

	arg_11_0.invincible = None

	arg_11_0.ResetData()
	arg_11_0.mainTF.Find("main/Image").GetComponent(typeof(Animator)).Play("Idle_S_0")

def var_0_0.ResetData(arg_12_0):
	arg_12_0.mainAnimName, arg_12_0.toolAnimName, arg_12_0.oreAnimName = "", "", ""

	arg_12_0.SetAnimDir("S")

	arg_12_0.weight = 0
	arg_12_0.point = 0
	arg_12_0.isDeliver = False
	arg_12_0.playHitAnim = None

	arg_12_0.ResetStatus()

def var_0_0.ResetStatus(arg_13_0):
	arg_13_0.SetStatus(var_0_0.STATUS_NULL)

	arg_13_0.oreList = {}

	eachChild(arg_13_0._tf.Find("main"), function(arg_14_0)
		for iter_14_0 = 1, 3:
			local var_14_0 = arg_14_0.Find("ore/Image/" .. iter_14_0 .. "/oreTF")

			removeAllChildren(var_14_0))

local var_0_1 = {
	S = {
		EF_Get = {
			Vector2(0, 0),
			Vector2(-1, 0),
			Vector2(0, -11)
		},
		EF_Upgrade = {
			Vector2(0, -5),
			Vector2(0, -4)
		}
	},
	E = {
		EF_Get = {
			Vector2(13, 3),
			Vector2(14.8, 4.4),
			Vector2(-23, 4)
		},
		EF_Upgrade = {
			Vector2(13, 0),
			Vector2(18, 2.7)
		}
	},
	W = {
		EF_Get = {
			Vector2(-16, 3.5),
			Vector2(-16, 5),
			Vector2(-24, 4)
		},
		EF_Upgrade = {
			Vector2(-18, 2),
			Vector2(-22, 2)
		}
	}
}

def var_0_0.PlayEffect(arg_15_0, arg_15_1):
	local var_15_0 = arg_15_0.animDir

	if var_15_0 == "N":
		return

	local var_15_1 = arg_15_0._tf.Find("effect/" .. arg_15_1)
	local var_15_2 = arg_15_0.status

	if arg_15_1 == "EF_Upgrade":
		var_15_2 = arg_15_0.status == var_0_0.STATUS_IRON_BOX and 2 or 1

	local var_15_3 = var_0_1[var_15_0][arg_15_1][var_15_2]

	setAnchoredPosition(var_15_1, var_15_3)
	setActive(var_15_1, True)

def var_0_0.AddOre(arg_16_0, arg_16_1):
	if arg_16_0.status == var_0_0.STATUS_WOOD_BOX and #arg_16_0.oreList >= 6:
		return

	if (arg_16_0.status == var_0_0.STATUS_IRON_BOX or arg_16_0.status == var_0_0.STATUS_CART) and #arg_16_0.oreList >= 8:
		return

	table.insert(arg_16_0.oreList, arg_16_1)
	eachChild(arg_16_0._tf.Find("main"), function(arg_17_0)
		if arg_17_0.name == "N" and arg_16_0.status != var_0_0.STATUS_CART:
			return

		local var_17_0 = arg_17_0.Find("ore/Image/" .. arg_16_0.status .. "/oreTF")
		local var_17_1 = arg_17_0.Find("ore/Image/" .. arg_16_0.status .. "/pos/" .. "num_" .. #arg_16_0.oreList)

		if var_17_0.childCount < #arg_16_0.oreList - 1:
			for iter_17_0, iter_17_1 in ipairs(arg_16_0.oreList):
				local var_17_2 = arg_16_0.oreTpl.Find(iter_17_1)
				local var_17_3 = cloneTplTo(var_17_2, var_17_0, iter_17_0)
		else
			local var_17_4 = arg_16_0.oreTpl.Find(arg_16_1)
			local var_17_5 = cloneTplTo(var_17_4, var_17_0, #arg_16_0.oreList)

		eachChild(var_17_1, function(arg_18_0)
			setAnchoredPosition(var_17_0.Find(arg_18_0.name), arg_18_0.anchoredPosition)))

def var_0_0.CheckStatus(arg_19_0):
	local var_19_0 = False

	if arg_19_0.status == var_0_0.STATUS_NULL:
		var_19_0 = arg_19_0.weight >= 0
	elif arg_19_0.status == var_0_0.STATUS_WOOD_BOX:
		var_19_0 = arg_19_0.weight >= OreGameConfig.CAPACITY.WOOD_BOX
	elif arg_19_0.status == var_0_0.STATUS_IRON_BOX:
		var_19_0 = arg_19_0.weight >= OreGameConfig.CAPACITY.IRON_BOX

	if var_19_0:
		arg_19_0.PlayEffect("EF_Upgrade")
		arg_19_0.SetStatus(arg_19_0.status + 1)
	else
		arg_19_0.PlayEffect("EF_Get")

def var_0_0.SetStatus(arg_20_0, arg_20_1):
	arg_20_0.status = arg_20_1

	eachChild(arg_20_0._tf.Find("main"), function(arg_21_0)
		setActive(arg_21_0.Find("tool"), arg_20_0.status != var_0_0.STATUS_NULL)
		setActive(arg_21_0.Find("ore"), arg_20_0.status != var_0_0.STATUS_NULL)
		eachChild(arg_21_0.Find("ore/Image"), function(arg_22_0)
			setActive(arg_22_0, arg_20_0.status == tonumber(arg_22_0.name))))

	arg_20_0.speed = OreGameConfig.SPEED[arg_20_0.status]

def var_0_0.SetAnimDir(arg_23_0, arg_23_1):
	arg_23_0.animDir = arg_23_1

	eachChild(arg_23_0._tf.Find("main"), function(arg_24_0)
		if arg_24_0.name == arg_23_0.animDir:
			setActive(arg_24_0, True)

			arg_23_0.mainTF = arg_24_0
		else
			setActive(arg_24_0, False))

def var_0_0.PlayHitAnim(arg_25_0, arg_25_1, arg_25_2, arg_25_3):
	arg_25_0.invincible = 0

	setActive(arg_25_0._tf.Find("effect/EF_Clash_" .. arg_25_1), True)

	local var_25_0 = ""
	local var_25_1 = arg_25_2 < 4 and "Light" or "Heavy"

	arg_25_0.hitPos = {
		x = 0,
		y = 0
	}
	arg_25_0.hitPos.x = arg_25_1 == "W" and -var_0_0.HIT_DELTA or var_0_0.HIT_DELTA

	if arg_25_3 <= arg_25_0._tf.anchoredPosition.y:
		var_25_0 = arg_25_1 == "W" and "CW" or "CCW"
		arg_25_0.hitPos.y = var_0_0.HIT_DELTA
	else
		var_25_0 = arg_25_1 == "W" and "CCW" or "CW"
		arg_25_0.hitPos.y = -var_0_0.HIT_DELTA

	arg_25_0.hitTime = 0
	arg_25_0.hitAnimName = "Stun_" .. var_25_1 .. "_" .. var_25_0

	arg_25_0.mainTF.Find("main/Image").GetComponent(typeof(Animator)).Play("Clash_" .. arg_25_1)
	arg_25_0.binder.emit(OreGameConfig.EVENT_PLAY_CONTAINER_HIT, {
		pos = arg_25_0._tf.anchoredPosition,
		hitPos = arg_25_0.hitPos,
		status = arg_25_0.status,
		oreTF = arg_25_0.mainTF.Find("ore/Image/" .. tostring(arg_25_0.status))
	})
	arg_25_0.ResetStatus()

def var_0_0.PlayDeliver(arg_26_0):
	arg_26_0.isDeliver = True

	setActive(arg_26_0.mainTF.Find("tool"), False)
	setActive(arg_26_0.mainTF.Find("ore"), False)
	arg_26_0.mainTF.Find("main/Image").GetComponent(typeof(Animator)).Play("Deliver")

def var_0_0.CheckDeliver(arg_27_0):
	if arg_27_0._tf.anchoredPosition.y < OreGameConfig.RANGE_Y[1] + 2 and arg_27_0._tf.anchoredPosition.x > -100 and arg_27_0._tf.anchoredPosition.x < 100 and arg_27_0.animDir == "S" and arg_27_0.weight > 0:
		arg_27_0.PlayDeliver()
		arg_27_0.binder.emit(OreGameConfig.EVENT_DELIVER, {
			point = arg_27_0.point,
			status = arg_27_0.status,
			pos = arg_27_0._tf.anchoredPosition,
			oreTF = arg_27_0.mainTF.Find("ore/Image/" .. tostring(arg_27_0.status))
		})

def var_0_0.OnTimer(arg_28_0, arg_28_1):
	if arg_28_0.invincible:
		arg_28_0.invincible = arg_28_0.invincible + arg_28_1

		if arg_28_0.invincible >= OreGameConfig.INVINCIBLE_TIME:
			arg_28_0.invincible = None

	if arg_28_0.hitTime:
		if arg_28_1 * 5 < arg_28_0.hitTime and arg_28_0.hitTime <= arg_28_1 * 6:
			arg_28_0.mainTF.Find("main/Image").GetComponent(typeof(Animator)).Play(arg_28_0.hitAnimName)

			arg_28_0.playHitAnim = True
		elif arg_28_0.hitTime > arg_28_1 * 6:
			local var_28_0 = {
				x = arg_28_0._tf.anchoredPosition.x + arg_28_0.hitPos.x * arg_28_1 / var_0_0.HIT_MOVE_TIME,
				y = arg_28_0._tf.anchoredPosition.y + arg_28_0.hitPos.y * arg_28_1 / var_0_0.HIT_MOVE_TIME
			}

			arg_28_0.SetPosition(var_28_0)

		arg_28_0.hitTime = arg_28_0.hitTime + arg_28_1

		if arg_28_0.hitTime >= var_0_0.HIT_MOVE_TIME:
			arg_28_0.hitTime = None

		return

	if not arg_28_0.isDeliver and not arg_28_0.playHitAnim:
		local var_28_1 = Vector2(arg_28_0.uiMgr.hrz, arg_28_0.uiMgr.vtc)

		arg_28_0.UpdateAnim(var_28_1)
		arg_28_0.UpdatePosition(var_28_1)
		arg_28_0.CheckDeliver()

def var_0_0.UpdateAnim(arg_29_0, arg_29_1):
	local var_29_0 = OreGameHelper.GetFourDirLabel(arg_29_1)
	local var_29_1 = False

	if var_29_0 == "STAND":
		var_29_0 = arg_29_0.animDir
		var_29_1 = True

	arg_29_0.SetAnimDir(var_29_0)

	local var_29_2 = ""
	local var_29_3 = ""
	local var_29_4 = ""

	if var_29_1:
		if arg_29_0.mainAnimName != "Idle_S_Sad":
			var_29_2 = "Idle_" .. var_29_0 .. "_" .. arg_29_0.status

			if arg_29_0.status != var_0_0.STATUS_NULL:
				var_29_3 = var_29_2
				var_29_4 = var_29_2
		else
			var_29_2 = "Idle_S_Sad"
			var_29_3 = "Idle_S_1"
			var_29_4 = "Idle_S_1"
	else
		var_29_2 = "Move_" .. var_29_0 .. "_" .. arg_29_0.status

		if arg_29_0.status != var_0_0.STATUS_NULL:
			var_29_3 = var_29_2
			var_29_4 = var_29_2

	if var_29_2 != "" and arg_29_0.mainAnimName != var_29_2:
		arg_29_0.mainTF.Find("main/Image").GetComponent(typeof(Animator)).Play(var_29_2)

		arg_29_0.mainAnimName = var_29_2

	if arg_29_0.status != var_0_0.STATUS_NULL:
		if var_29_4 != "" and var_29_4 != arg_29_0.toolAnimName:
			if string.find(var_29_4, "N_1") or string.find(var_29_4, "N_2"):
				arg_29_0.mainTF.Find("tool/Image").GetComponent(typeof(Image)).enabled = False
			else
				arg_29_0.mainTF.Find("tool/Image").GetComponent(typeof(Image)).enabled = True

				arg_29_0.mainTF.Find("tool/Image").GetComponent(typeof(Animator)).Play(var_29_4)

			arg_29_0.toolAnimName = var_29_4

		if var_29_3 != "" and var_29_3 != arg_29_0.oreAnimName:
			arg_29_0.mainTF.Find("ore/Image").GetComponent(typeof(Animator)).Play(var_29_3)

			arg_29_0.oreAnimName = var_29_3

			local var_29_5 = arg_29_0.mainTF.Find("ore/Image/" .. arg_29_0.status .. "/oreTF")

			if not var_29_1 and var_0_0.oreAnimOffset[arg_29_0.status][arg_29_0.animDir]:
				setAnchoredPosition(var_29_5, var_0_0.oreAnimOffset[arg_29_0.status][arg_29_0.animDir])
			else
				setAnchoredPosition(var_29_5, Vector2(0, 0))

var_0_0.oreAnimOffset = {
	{
		S = Vector2(0, -2),
		W = Vector2(1, -2)
	},
	{
		S = Vector2(0, -2)
	},
	{
		W = Vector2(5, 0),
		E = Vector2(-3, 0)
	}
}

def var_0_0.UpdatePosition(arg_30_0, arg_30_1):
	local var_30_0 = OreGameHelper.GetEightDirVector(arg_30_1) * OreGameConfig.TIME_INTERVAL * arg_30_0.speed
	local var_30_1 = {
		x = arg_30_0._tf.anchoredPosition.x + var_30_0.x,
		y = arg_30_0._tf.anchoredPosition.y + var_30_0.y
	}

	arg_30_0.SetPosition(var_30_1)

def var_0_0.SetPosition(arg_31_0, arg_31_1):
	if OreGameHelper.CheckRemovable(arg_31_1):
		setAnchoredPosition(arg_31_0._tf, arg_31_1)

		arg_31_0._tf.GetComponent(typeof(Canvas)).sortingOrder = -arg_31_1.y + 320

def var_0_0.IsInvincible(arg_32_0):
	return arg_32_0.invincible

def var_0_0.GetAnimDirLabel(arg_33_0):
	return arg_33_0.animDir

def var_0_0.GetAABB(arg_34_0):
	return arg_34_0.aabb

def var_0_0.GetCarryTriggerOffset(arg_35_0):
	return {
		0,
		10
	}

def var_0_0.GetCollisionInfo(arg_36_0):
	return {
		pos = {
			x = arg_36_0._tf.anchoredPosition.x + arg_36_0.aabbTF.anchoredPosition.x,
			y = arg_36_0._tf.anchoredPosition.y + arg_36_0.aabbTF.anchoredPosition.y
		},
		aabb = arg_36_0.GetAABB(),
		carryOffset = arg_36_0.GetCarryTriggerOffset()
	}

return var_0_0
