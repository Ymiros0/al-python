local var_0_0 = class("UIStrikeAnim", import(".UIAnim"))

var_0_0.Fields = {
	spineAnim = "userdata",
	prefab = "string",
	aniEvent = "userdata",
	char = "userdata",
	transform = "userdata",
	playing = "boolean",
	onTrigger = "function",
	onStart = "function",
	onEnd = "function",
	skelegraph = "userdata",
	painting = "userdata",
	shipVO = "table"
}
var_0_0.EventLoaded = "UIStrikeAnim.EventLoaded"

def var_0_0.Setup(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.prefab = arg_1_1
	arg_1_0.shipVO = arg_1_2

def var_0_0.LoadBack(arg_2_0):
	if arg_2_0.transform and arg_2_0.painting and arg_2_0.char:
		arg_2_0.Init()
		arg_2_0.DispatchEvent(var_0_0.EventLoaded)

def var_0_0.Load(arg_3_0):
	local var_3_0 = arg_3_0.prefab
	local var_3_1 = PoolMgr.GetInstance()

	var_3_1.GetUI(var_3_0, True, function(arg_4_0)
		if var_3_0 == arg_3_0.prefab:
			arg_3_0.transform = arg_4_0.transform

			arg_3_0.LoadBack()
		else
			var_3_1.ReturnUI(var_3_0, arg_4_0))
	arg_3_0.ReloadShip(arg_3_0.shipVO)

def var_0_0.ReloadShip(arg_5_0, arg_5_1):
	arg_5_0.shipVO = arg_5_1
	arg_5_0.aniEvent = None
	arg_5_0.painting = None
	arg_5_0.char = None

	local var_5_0 = PoolMgr.GetInstance()

	var_5_0.GetInstance().GetPainting(arg_5_1.getPainting(), True, function(arg_6_0)
		arg_5_0.painting = arg_6_0

		ShipExpressionHelper.SetExpression(arg_5_0.painting, arg_5_1.getPainting())
		arg_5_0.LoadBack())
	var_5_0.GetInstance().GetSpineChar(arg_5_1.getPrefab(), True, function(arg_7_0)
		arg_5_0.char = arg_7_0
		arg_5_0.char.transform.localScale = Vector3.one

		arg_5_0.LoadBack())

def var_0_0.UnloadShipVO(arg_8_0):
	local var_8_0 = arg_8_0.shipVO

	retPaintingPrefab(arg_8_0.transform.Find("mask/painting"), var_8_0.getPainting())
	PoolMgr.GetInstance().ReturnSpineChar(var_8_0.getPrefab(), arg_8_0.char)

	arg_8_0.shipVO = None
	arg_8_0.painting = None
	arg_8_0.char = None

def var_0_0.Play(arg_9_0, arg_9_1):
	arg_9_0.playing = True

	function arg_9_0.onStart(arg_10_0)
		arg_9_0.spineAnim.SetAction("attack", 0)

		arg_9_0.skelegraph.freeze = True

	function arg_9_0.onTrigger(arg_11_0)
		arg_9_0.skelegraph.freeze = False

		arg_9_0.spineAnim.SetActionCallBack(function(arg_12_0)
			if arg_12_0 == "action":
				-- block empty
			elif arg_12_0 == "finish":
				arg_9_0.skelegraph.freeze = True)

	arg_9_0.onEnd = arg_9_1

	arg_9_0.Update()

def var_0_0.Stop(arg_13_0):
	arg_13_0.playing = False

	arg_13_0.Update()

	if arg_13_0.skelegraph:
		arg_13_0.skelegraph.freeze = False

	arg_13_0.UnloadShipVO()

def var_0_0.Init(arg_14_0):
	setActive(arg_14_0.transform, False)

	local var_14_0 = arg_14_0.transform.Find("torpedo")
	local var_14_1 = arg_14_0.transform.Find("mask/painting")
	local var_14_2 = arg_14_0.transform.Find("ship")

	setParent(arg_14_0.painting, var_14_1.Find("fitter"), False)
	setParent(arg_14_0.char, var_14_2, False)
	setActive(var_14_2, False)
	setActive(var_14_0, False)

	arg_14_0.spineAnim = arg_14_0.char.GetComponent("SpineAnimUI")
	arg_14_0.skelegraph = arg_14_0.spineAnim.GetComponent("SkeletonGraphic")
	arg_14_0.aniEvent = arg_14_0.transform.GetComponent("DftAniEvent")

	arg_14_0.Update()

return var_0_0
