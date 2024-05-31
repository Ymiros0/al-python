local var_0_0 = class("Ore")

var_0_0.TYPE_SMALL = 1
var_0_0.TYPE_LA = 2
var_0_0.FallTime = 1

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4, arg_1_5):
	arg_1_0.binder = arg_1_1
	arg_1_0._tf = arg_1_2
	arg_1_0.collisionMgr = arg_1_3
	arg_1_0.id = arg_1_4
	arg_1_0.config = OreGameConfig.ORE_CONFIG[arg_1_0.id]
	arg_1_0.startPoint = arg_1_5

	arg_1_0.Init()

def var_0_0.AddListener(arg_2_0):
	arg_2_0.binder.bind(OreGameConfig.EVENT_UPDATE_ORE_TARGET, function(arg_3_0, arg_3_1)
		if not arg_2_0.isDestroy:
			setActive(findTF(arg_2_0.effectTF, "Frame"), arg_2_0.index == arg_3_1.index)

		arg_2_0.isTarget = arg_2_0.index == arg_3_1.index)
	arg_2_0.binder.bind(OreGameConfig.EVENT_CHECK_CARRY, function(arg_4_0, arg_4_1)
		if not arg_2_0.isDestroy and arg_2_0.isTarget:
			if arg_4_1.weight + arg_2_0.config.weight > OreGameConfig.MAX_WEIGHT:
				setActive(findTF(arg_2_0.effectTF, "Limit"), True)
				setActive(findTF(arg_2_0.effectTF, "Full"), True)
			else
				arg_2_0.binder.emit(OreGameConfig.EVENT_DO_CARRY, {
					weight = arg_2_0.config.weight,
					point = arg_2_0.config.score,
					type = arg_2_0.config.type
				})
				arg_2_0.animator.Play("Vanish")
				arg_2_0.collisionMgr.RemoveOreObject(arg_2_0.index, arg_2_0))

def var_0_0.AddDftAniEvent(arg_5_0):
	findTF(arg_5_0._tf, "main").GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
		arg_5_0.Destroy())
	findTF(arg_5_0._tf, "main/Image").GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
		arg_5_0.Destroy())
	findTF(arg_5_0.effectTF, "Limit").GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
		setActive(findTF(arg_5_0.effectTF, "Limit"), False))
	findTF(arg_5_0.effectTF, "Full").GetComponent(typeof(DftAniEvent)).SetEndEvent(function()
		setActive(findTF(arg_5_0.effectTF, "Full"), False))

def var_0_0.Init(arg_10_0):
	setAnchoredPosition(arg_10_0._tf, arg_10_0.startPoint)

	arg_10_0.effectTF = findTF(arg_10_0._tf, "effect")
	arg_10_0.animator = findTF(arg_10_0._tf, "main/Image").GetComponent(typeof(Animator))
	arg_10_0.index = arg_10_0._tf.name
	arg_10_0.endPoint = findTF(arg_10_0._tf.parent.parent, "pos/" .. arg_10_0._tf.name).anchoredPosition

	local var_10_0 = math.random() > 0.5 and -10 or 10

	arg_10_0.centerPoint = Vector2(arg_10_0.startPoint.x + var_10_0, arg_10_0.startPoint.y + 80)
	arg_10_0.time = 0
	arg_10_0.isFallEnd = False
	arg_10_0.isTarget = False

	arg_10_0.AddListener()
	arg_10_0.AddDftAniEvent()
	arg_10_0._tf.Find("main").GetComponent(typeof(Animator)).Play("Initial")
	arg_10_0._tf.Find("main/Image").GetComponent(typeof(Animator)).Play("Fall")
	eachChild(arg_10_0.effectTF, function(arg_11_0)
		setActive(arg_11_0, False))

def var_0_0.FallEnd(arg_12_0):
	arg_12_0.animator.Play("Spawn")

	arg_12_0.isFallEnd = True

	arg_12_0.collisionMgr.AddOreObject(arg_12_0.index, arg_12_0)

def var_0_0.PlayBlink(arg_13_0):
	findTF(arg_13_0._tf, "main").GetComponent(typeof(Animator)).Play("Blink")

def var_0_0.Destroy(arg_14_0):
	if arg_14_0.isDestroy:
		return

	arg_14_0.binder.emit(OreGameConfig.EVENT_ORE_DESTROY, {
		index = arg_14_0.index,
		id = arg_14_0.id
	})
	arg_14_0.collisionMgr.RemoveOreObject(arg_14_0.index, arg_14_0)

	arg_14_0.isDestroy = True

def var_0_0.Dispose(arg_15_0):
	arg_15_0.isDestroy = True

def var_0_0.OnTimer(arg_16_0, arg_16_1):
	if arg_16_0.time < var_0_0.FallTime:
		arg_16_0.time = arg_16_0.time + arg_16_1

		local var_16_0 = OreGameHelper.GetBeziersPoints(arg_16_0.startPoint, arg_16_0.endPoint, arg_16_0.centerPoint, arg_16_0.time)

		setAnchoredPosition(arg_16_0._tf, var_16_0)
	elif not arg_16_0.isFallEnd:
		arg_16_0.FallEnd()

	if arg_16_0.isFallEnd:
		arg_16_0.time = arg_16_0.time + arg_16_1

		if arg_16_0.time > var_0_0.FallTime + arg_16_0.config.duration:
			arg_16_0.PlayBlink()

def var_0_0.GetAABB(arg_17_0):
	if arg_17_0.config.size == var_0_0.TYPE_SMALL:
		return {
			{
				-7,
				7
			},
			{
				7,
				-7
			}
		}
	else
		return {
			{
				-11,
				11
			},
			{
				13,
				-13
			}
		}

def var_0_0.GetCollisionInfo(arg_18_0):
	return {
		pos = arg_18_0._tf.anchoredPosition,
		aabb = arg_18_0.GetAABB()
	}

return var_0_0
