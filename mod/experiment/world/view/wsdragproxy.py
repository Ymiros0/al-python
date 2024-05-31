local var_0_0 = class("WSDragProxy", import("...BaseEntity"))

var_0_0.Fields = {
	map = "table",
	transform = "userdata",
	leftExtend = "number",
	gid = "number",
	longPressTrigger = "userdata",
	topExtend = "number",
	twFocusId = "number",
	dragTrigger = "userdata",
	wsTimer = "table",
	onDragFunction = "function",
	isDraging = "boolean",
	rightExtend = "number",
	callInfo = "table",
	bottomExtend = "number"
}

def var_0_0.Setup(arg_1_0, arg_1_1):
	arg_1_0.callInfo = arg_1_1
	arg_1_0.dragTrigger = GetOrAddComponent(arg_1_0.transform, typeof(EventTriggerListener))

	arg_1_0.dragTrigger.AddBeginDragFunc(function()
		arg_1_0.isDraging = True)
	arg_1_0.dragTrigger.AddDragEndFunc(function()
		arg_1_0.isDraging = False)
	arg_1_0.dragTrigger.AddPointClickFunc(function(arg_4_0, arg_4_1)
		if not arg_1_0.isDraging:
			arg_1_0.callInfo.clickCall(arg_4_0, arg_4_1))

	arg_1_0.dragTrigger.enabled = True
	arg_1_0.longPressTrigger = GetOrAddComponent(arg_1_0.transform, typeof(UILongPressTrigger))

	local var_1_0 = arg_1_0.callInfo.longPressCall

	function arg_1_0.callInfo.longPressCall(...)
		if arg_1_0.isDraging:
			return

		var_1_0(...)

	arg_1_0.longPressTrigger.onLongPressed.AddListener(arg_1_0.callInfo.longPressCall)

	arg_1_0.longPressTrigger.enabled = True

def var_0_0.Dispose(arg_6_0):
	arg_6_0.transform.localPosition = Vector3.zero

	if arg_6_0.map:
		arg_6_0.dragTrigger.RemoveDragFunc()

	arg_6_0.dragTrigger.RemoveBeginDragFunc()
	arg_6_0.dragTrigger.RemoveDragEndFunc()
	arg_6_0.dragTrigger.RemovePointClickFunc()

	arg_6_0.dragTrigger.enabled = True

	arg_6_0.longPressTrigger.onLongPressed.RemoveListener(arg_6_0.callInfo.longPressCall)

	arg_6_0.longPressTrigger.enabled = True

	arg_6_0.Clear()

def var_0_0.Focus(arg_7_0, arg_7_1, arg_7_2, arg_7_3, arg_7_4):
	local var_7_0 = arg_7_0.map.theme
	local var_7_1 = arg_7_0.transform.Find("plane")

	assert(var_7_1, "plane not exist.")

	local var_7_2 = arg_7_0.transform.parent.InverseTransformVector(arg_7_1 - var_7_1.position)

	var_7_2.x = var_7_2.x + var_7_1.localPosition.x
	var_7_2.y = var_7_2.y + var_7_1.localPosition.y - var_7_1.localPosition.z * math.tan(math.pi / 180 * var_7_0.angle)
	var_7_2.x = math.clamp(-var_7_2.x, -arg_7_0.rightExtend, arg_7_0.leftExtend)
	var_7_2.y = math.clamp(-var_7_2.y, -arg_7_0.topExtend, arg_7_0.bottomExtend)
	var_7_2.z = 0

	if arg_7_0.twFocusId:
		arg_7_0.wsTimer.RemoveInMapTween(arg_7_0.twFocusId)

	local var_7_3 = {}

	if arg_7_3:
		table.insert(var_7_3, function(arg_8_0)
			if arg_7_0.isDraging:
				arg_7_0.isDraging = False

			arg_7_0.dragTrigger.enabled = False
			arg_7_0.longPressTrigger.enabled = False

			if not arg_7_2:
				local var_8_0 = (arg_7_0.transform.localPosition - var_7_2).magnitude

				arg_7_2 = var_8_0 > 0 and var_8_0 / (40 * math.sqrt(var_8_0)) or 0

			arg_7_0.twFocusId = LeanTween.moveLocal(arg_7_0.transform.gameObject, var_7_2, arg_7_2).setEase(arg_7_3).setOnComplete(System.Action(arg_8_0)).uniqueId

			arg_7_0.wsTimer.AddInMapTween(arg_7_0.twFocusId))
	else
		arg_7_0.transform.localPosition = var_7_2

	seriesAsync(var_7_3, function()
		arg_7_0.dragTrigger.enabled = True
		arg_7_0.longPressTrigger.enabled = True

		if arg_7_4:
			arg_7_4())

def var_0_0.UpdateMap(arg_10_0, arg_10_1):
	if arg_10_0.map != arg_10_1 or arg_10_0.gid != arg_10_1.gid:
		arg_10_0.map = arg_10_1
		arg_10_0.gid = arg_10_1.gid

		arg_10_0.UpdateDrag()

def var_0_0.UpdateDrag(arg_11_0):
	local var_11_0, var_11_1, var_11_2 = getSizeRate()
	local var_11_3 = arg_11_0.map.theme
	local var_11_4 = var_11_2 * 0.5 / math.tan(math.deg2Rad * var_11_3.fov * 0.5)
	local var_11_5 = math.deg2Rad * var_11_3.angle
	local var_11_6 = Vector3(0, -math.sin(var_11_5), -math.cos(var_11_5))
	local var_11_7 = Vector3(var_11_3.offsetx, var_11_3.offsety, var_11_3.offsetz) + WorldConst.DefaultMapOffset
	local var_11_8 = Vector3.Dot(var_11_6, var_11_7)
	local var_11_9 = var_11_0 * math.clamp((var_11_4 - var_11_8) / var_11_4, 0, 1)

	arg_11_0.leftExtend, arg_11_0.rightExtend, arg_11_0.topExtend, arg_11_0.bottomExtend = arg_11_0.GetDragExtend(var_11_1, var_11_2)
	arg_11_0.transform.sizeDelta = Vector2(var_11_1 + math.max(arg_11_0.leftExtend, arg_11_0.rightExtend) * 2, var_11_2 + math.max(arg_11_0.topExtend, arg_11_0.bottomExtend) * 2)

	arg_11_0.dragTrigger.RemoveDragFunc()
	arg_11_0.dragTrigger.AddDragFunc(function(arg_12_0, arg_12_1)
		if arg_11_0.onDragFunction:
			arg_11_0.onDragFunction()

		local var_12_0 = arg_11_0.transform.localPosition

		var_12_0.x = math.clamp(var_12_0.x + arg_12_1.delta.x * var_11_9.x, -arg_11_0.rightExtend, arg_11_0.leftExtend)
		var_12_0.y = math.clamp(var_12_0.y + arg_12_1.delta.y * var_11_9.y / math.cos(var_11_5), -arg_11_0.topExtend, arg_11_0.bottomExtend)
		arg_11_0.transform.localPosition = var_12_0)

def var_0_0.GetDragExtend(arg_13_0, arg_13_1, arg_13_2):
	local var_13_0 = arg_13_0.map
	local var_13_1 = var_13_0.theme
	local var_13_2 = arg_13_0.transform.Find("plane")

	assert(var_13_2, "plane not exist.")

	local var_13_3 = var_13_2.localPosition.x
	local var_13_4 = var_13_2.localPosition.y - var_13_2.localPosition.z * math.tan(math.pi / 180 * var_13_1.angle)
	local var_13_5 = 99999999
	local var_13_6 = 0
	local var_13_7 = 0

	for iter_13_0, iter_13_1 in pairs(var_13_0.cells):
		if var_13_5 > iter_13_1.row:
			var_13_5 = iter_13_1.row

		if var_13_6 < iter_13_1.row:
			var_13_6 = iter_13_1.row

		if var_13_7 < iter_13_1.column:
			var_13_7 = iter_13_1.column

	local var_13_8 = var_13_0.theme.cellSize + var_13_0.theme.cellSpace
	local var_13_9 = math.max(var_13_7 * var_13_8.x - arg_13_1 * 0.5, 0)
	local var_13_10 = math.max((WorldConst.MaxRow * 0.5 - var_13_5) * var_13_8.y, 0)
	local var_13_11 = math.max((var_13_6 - WorldConst.MaxRow * 0.5) * var_13_8.y, 0)

	return 1000 - var_13_3, var_13_9 + var_13_3, var_13_10 + var_13_4, var_13_11 - var_13_4

def var_0_0.ShakePlane(arg_14_0, arg_14_1, arg_14_2, arg_14_3, arg_14_4, arg_14_5):
	arg_14_2 = math.clamp(arg_14_2, 0, 90)
	arg_14_3 = math.max(arg_14_3, 1)
	arg_14_4 = math.max(arg_14_4, 1)

	local var_14_0 = math.pi / 180 * arg_14_2
	local var_14_1 = Vector3(math.cos(var_14_0), math.sin(var_14_0), 0) * arg_14_1
	local var_14_2 = arg_14_0.transform.anchoredPosition3D
	local var_14_3 = var_14_2 + var_14_1
	local var_14_4 = var_14_2 - var_14_1
	local var_14_5 = 0.0333
	local var_14_6 = var_14_5 * arg_14_3 * 0.5
	local var_14_7 = var_14_5 * arg_14_3
	local var_14_8 = var_14_5 * arg_14_3 * 0.5

	arg_14_0.dragTrigger.enabled = False
	arg_14_0.longPressTrigger.enabled = False

	local var_14_9 = LeanTween.moveLocal(arg_14_0.transform.gameObject, var_14_3, var_14_6)
	local var_14_10 = LeanTween.moveLocal(arg_14_0.transform.gameObject, var_14_4, var_14_7).setDelay(var_14_6).setLoopPingPong(arg_14_4)
	local var_14_11 = LeanTween.moveLocal(arg_14_0.transform.gameObject, var_14_2, var_14_8).setDelay(var_14_6 + var_14_7 * arg_14_4 * 2).setOnComplete(System.Action(function()
		arg_14_0.dragTrigger.enabled = True
		arg_14_0.longPressTrigger.enabled = True

		arg_14_5()))

	arg_14_0.wsTimer.AddInMapTween(var_14_9.uniqueId)
	arg_14_0.wsTimer.AddInMapTween(var_14_10.uniqueId)
	arg_14_0.wsTimer.AddInMapTween(var_14_11.uniqueId)

return var_0_0
