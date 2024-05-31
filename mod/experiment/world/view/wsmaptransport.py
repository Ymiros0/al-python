local var_0_0 = class("WSMapTransport", import("...BaseEntity"))

var_0_0.Fields = {
	map = "table",
	wsMapPath = "table",
	rtForbid = "userdata",
	transform = "userdata",
	dir = "number",
	column = "number",
	updateTimer = "table",
	row = "number",
	rtClick = "userdata",
	rtBottom = "userdata",
	rtDanger = "userdata"
}
var_0_0.Listeners = {
	onStartTrip = "OnStartTrip",
	onArrived = "OnArrived"
}

def var_0_0.GetResName():
	return "world_cell_transport"

def var_0_0.GetName(arg_2_0, arg_2_1, arg_2_2):
	return "transport_" .. arg_2_0 .. "_" .. arg_2_1 .. "_" .. arg_2_2

def var_0_0.Setup(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4):
	arg_3_0.row = arg_3_1
	arg_3_0.column = arg_3_2
	arg_3_0.dir = arg_3_3
	arg_3_0.map = arg_3_4

	arg_3_0.wsMapPath.AddListener(WSMapPath.EventStartTrip, arg_3_0.onStartTrip)
	arg_3_0.wsMapPath.AddListener(WSMapPath.EventArrived, arg_3_0.onArrived)
	arg_3_0.Init()

def var_0_0.Dispose(arg_4_0):
	arg_4_0.wsMapPath.RemoveListener(WSMapPath.EventStartTrip, arg_4_0.onStartTrip)
	arg_4_0.wsMapPath.RemoveListener(WSMapPath.EventArrived, arg_4_0.onArrived)
	arg_4_0.DisposeUpdateTimer()
	arg_4_0.UpdateAlpha(1)
	arg_4_0.Clear()

def var_0_0.Init(arg_5_0):
	local var_5_0 = arg_5_0.transform

	arg_5_0.rtClick = var_5_0.Find("click")
	arg_5_0.rtBottom = var_5_0.Find("bottom")
	arg_5_0.rtDanger = var_5_0.Find("danger")
	arg_5_0.rtForbid = var_5_0.Find("forbid")

	local var_5_1 = arg_5_0.row
	local var_5_2 = arg_5_0.column
	local var_5_3 = arg_5_0.dir

	var_5_0.name = var_0_0.GetName(var_5_1, var_5_2, var_5_3)

	local var_5_4 = 0

	if var_5_3 == WorldConst.DirDown:
		var_5_1 = var_5_1 + 1
		var_5_4 = -90
	elif var_5_3 == WorldConst.DirLeft:
		var_5_2 = var_5_2 - 1
		var_5_4 = 180
	elif var_5_3 == WorldConst.DirUp:
		var_5_1 = var_5_1 - 1
		var_5_4 = 90
	elif var_5_3 == WorldConst.DirRight:
		var_5_2 = var_5_2 + 1
		var_5_4 = 0

	var_5_0.localEulerAngles = Vector3(0, 0, var_5_4)
	var_5_0.anchoredPosition = arg_5_0.map.theme.GetLinePosition(var_5_1, var_5_2)

	local var_5_5 = arg_5_0.map.theme.cellSize

	var_5_0.localScale = Vector3(var_5_5.x / var_5_0.sizeDelta.x, var_5_5.y / var_5_0.sizeDelta.y, 1)

	if arg_5_0.wsMapPath.IsMoving():
		arg_5_0.OnStartTrip()

def var_0_0.UpdateAlpha(arg_6_0, arg_6_1):
	setImageAlpha(arg_6_0.rtBottom, arg_6_1)
	setImageAlpha(arg_6_0.rtDanger, arg_6_1)
	setImageAlpha(arg_6_0.rtForbid, arg_6_1)

def var_0_0.OnStartTrip(arg_7_0):
	arg_7_0.StartUpdateTimer()

def var_0_0.OnArrived(arg_8_0):
	arg_8_0.DisposeUpdateTimer()

def var_0_0.StartUpdateTimer(arg_9_0):
	local var_9_0 = arg_9_0.wsMapPath.wsObject

	if var_9_0.class == WSMapFleet:
		arg_9_0.DisposeUpdateTimer()

		local var_9_1 = arg_9_0.map.theme
		local var_9_2 = var_9_1.GetLinePosition(arg_9_0.row, arg_9_0.column)
		local var_9_3 = math.min(var_9_1.cellSize.x + var_9_1.cellSpace.x, var_9_1.cellSize.y + var_9_1.cellSpace.y)
		local var_9_4 = var_9_0.fleet
		local var_9_5 = arg_9_0.map.GetNormalFleets()
		local var_9_6 = _.map(var_9_5, function(arg_10_0)
			local var_10_0 = var_9_1.GetLinePosition(arg_10_0.row, arg_10_0.column)

			return Vector3.Distance(var_10_0, var_9_2))

		arg_9_0.updateTimer = Timer.New(function()
			var_9_6[var_9_4.index] = Vector3.Distance(var_9_0.transform.anchoredPosition3D, var_9_2)

			local var_11_0 = math.max(1 - _.min(var_9_6) / var_9_3, 0)

			arg_9_0.UpdateAlpha(var_11_0), 0.033, -1)

		arg_9_0.updateTimer.Start()
		arg_9_0.updateTimer.func()

def var_0_0.DisposeUpdateTimer(arg_12_0):
	if arg_12_0.updateTimer:
		arg_12_0.updateTimer.Stop()

		arg_12_0.updateTimer = None

return var_0_0
