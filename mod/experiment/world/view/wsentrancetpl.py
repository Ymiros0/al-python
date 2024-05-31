local var_0_0 = class("WSEntranceTpl", import("...BaseEntity"))

var_0_0.Fields = {
	markSigns = "table",
	portCamp = "number",
	world = "table",
	transform = "userdata",
	tfMap = "userdata",
	entrance = "table",
	markTFs = "table",
	tfArea = "userdata"
}
var_0_0.Listeners = {
	onUpdateDisplayMarks = "OnUpdateDisplayMarks"
}
var_0_0.DisplayOrder = {
	"step",
	"task_main",
	"task_collecktion",
	"task",
	"sairen",
	"treasure_sairen",
	"treasure",
	"task_following_main",
	"task_following_boss",
	"task_following"
}
var_0_0.prefabName = {
	task_main = "DSJ_BX05_3D",
	buff_a = "buff_a",
	port_gray_2 = "mark_port_gray_2",
	buff_h = "buff_h",
	port_mark_new = "mark_port_tip_new",
	port_2 = "mark_port_2",
	buff_d = "buff_d",
	task_following_main = "DSJ_BX05_3D",
	step = "DSJ_BX05_3D",
	task = "DSJ_BX03_3D",
	treasure_sairen = "DSJ_BX06_3D",
	task_following_boss = "DSJ_BX07_3D",
	buff_d2 = "buff_d2",
	currency = "currency",
	port_gray_1 = "mark_port_gray_1",
	port_1 = "mark_port_1",
	mate = "mate",
	buff_a2 = "buff_a2",
	task_collecktion = "DSJ_BX08_3D",
	task_following = "DSJ_BX03_3D",
	treasure = "DSJ_BX01_3D",
	sairen = "guangzhu",
	core = "core",
	buff_h2 = "buff_h2",
	port_mark = "mark_port_tip"
}
var_0_0.offsetField = {
	task_main = "offset_pos",
	task = "offset_pos",
	treasure_sairen = "offset_pos",
	step = "offset_pos",
	task_collecktion = "offset_pos",
	task_following = "offset_pos",
	treasure = "offset_pos",
	task_following_main = "offset_pos",
	task_following_boss = "offset_pos"
}

def var_0_0.Build(arg_1_0):
	arg_1_0.transform = tf(GameObject.New())

def var_0_0.Setup(arg_2_0):
	pg.DelegateInfo.New(arg_2_0)
	arg_2_0.Init()

def var_0_0.Dispose(arg_3_0):
	pg.DelegateInfo.Dispose(arg_3_0)
	arg_3_0.RemoveEntranceListener()

	local var_3_0 = PoolMgr.GetInstance()

	for iter_3_0, iter_3_1 in pairs(arg_3_0.markTFs):
		iter_3_1.localPosition = Vector3.zero

		var_3_0.ReturnPrefab("world/mark/" .. var_0_0.prefabName[iter_3_0], var_0_0.prefabName[iter_3_0], go(iter_3_1), True)

	Destroy(arg_3_0.transform)
	arg_3_0.Clear()

def var_0_0.Init(arg_4_0):
	arg_4_0.markTFs = {}

def var_0_0.UpdateEntrance(arg_5_0, arg_5_1, arg_5_2):
	if arg_5_2 or arg_5_0.entrance != arg_5_1:
		arg_5_0.RemoveEntranceListener()
		_.each(arg_5_0.markTFs, function(arg_6_0)
			setActive(arg_6_0, False))

		arg_5_0.entrance = arg_5_1
		arg_5_0.portCamp = arg_5_0.entrance.HasPort() and pg.world_port_data[arg_5_0.entrance.config.port_map_icon].port_camp or None

		arg_5_0.AddEntranceListener()
		arg_5_0.InitMarksValue()

		arg_5_0.transform.name = arg_5_0.portCamp and "port_" .. arg_5_1.id or arg_5_1.GetColormaskUniqueID()

		arg_5_0.DoUpdateMark(arg_5_0.GetShowMark(), True)

def var_0_0.InitMarksValue(arg_7_0):
	arg_7_0.markSigns = {}

	local var_7_0 = arg_7_0.entrance.GetDisplayMarks()

	for iter_7_0, iter_7_1 in pairs(var_7_0):
		arg_7_0.markSigns[iter_7_0] = iter_7_1 > 0

def var_0_0.AddEntranceListener(arg_8_0):
	if arg_8_0.entrance:
		arg_8_0.entrance.AddListener(WorldEntrance.EventUpdateDisplayMarks, arg_8_0.onUpdateDisplayMarks)

def var_0_0.RemoveEntranceListener(arg_9_0):
	if arg_9_0.entrance:
		arg_9_0.entrance.RemoveListener(WorldEntrance.EventUpdateDisplayMarks, arg_9_0.onUpdateDisplayMarks)

def var_0_0.LoadPrefab(arg_10_0, arg_10_1, arg_10_2):
	local var_10_0 = PoolMgr.GetInstance()

	var_10_0.GetPrefab("world/mark/" .. var_0_0.prefabName[arg_10_1], var_0_0.prefabName[arg_10_1], True, function(arg_11_0)
		if arg_10_0.markTFs and not arg_10_0.markTFs[arg_10_1]:
			arg_10_0.markTFs[arg_10_1] = tf(arg_11_0)

			SetParent(arg_10_0.markTFs[arg_10_1], arg_10_0.transform, False)

			arg_10_0.markTFs[arg_10_1].localPosition = arg_10_0.GetPrefabOffset(arg_10_1)

			if arg_10_2:
				SetParent(arg_10_0.markTFs[arg_10_1], arg_10_2, True)

			setActive(arg_10_0.markTFs[arg_10_1], True)
		else
			var_10_0.ReturnPrefab("world/mark/" .. var_0_0.prefabName[arg_10_1], var_0_0.prefabName[arg_10_1], arg_11_0, True))

def var_0_0.GetPrefabOffset(arg_12_0, arg_12_1):
	local var_12_0 = var_0_0.offsetField[arg_12_1] and arg_12_0.entrance.config[var_0_0.offsetField[arg_12_1]] or {
		0,
		0
	}

	return Vector3(var_12_0[1] / PIXEL_PER_UNIT, 0, var_12_0[2] / PIXEL_PER_UNIT)

def var_0_0.UpdateMark(arg_13_0, arg_13_1, arg_13_2):
	arg_13_0.DoUpdateMark(arg_13_0.GetShowMark(), False)

	arg_13_0.markSigns[arg_13_1] = arg_13_2

	arg_13_0.DoUpdateMark(arg_13_0.GetShowMark(), True)

def var_0_0.OnUpdateDisplayMarks(arg_14_0, arg_14_1, arg_14_2, arg_14_3, arg_14_4):
	arg_14_0.UpdateMark(arg_14_3, arg_14_4)

def var_0_0.DoUpdateMark(arg_15_0, arg_15_1, arg_15_2, arg_15_3):
	if arg_15_1:
		if arg_15_0.markTFs[arg_15_1]:
			setActive(arg_15_0.markTFs[arg_15_1], arg_15_2)
		elif arg_15_2:
			arg_15_0.LoadPrefab(arg_15_1, arg_15_3)

def var_0_0.GetShowMark(arg_16_0):
	for iter_16_0, iter_16_1 in ipairs(var_0_0.DisplayOrder):
		if arg_16_0.markSigns[iter_16_1]:
			return iter_16_1

def var_0_0.UpdatePort(arg_17_0, arg_17_1, arg_17_2, arg_17_3):
	arg_17_0.DoUpdateMark("port_" .. arg_17_0.portCamp, arg_17_1)
	arg_17_0.DoUpdateMark("port_gray_" .. arg_17_0.portCamp, not arg_17_1)
	arg_17_0.DoUpdateMark("port_mark", arg_17_2)
	arg_17_0.DoUpdateMark("port_mark_new", arg_17_3)

def var_0_0.UpdatePressingAward(arg_18_0):
	local var_18_0 = nowWorld().GetPressingAward(arg_18_0.entrance.id)

	if var_18_0:
		local var_18_1 = pg.world_event_complete[var_18_0.id]

		arg_18_0.DoUpdateMark(var_18_1.map_icon, var_18_0.flag, arg_18_0.tfMap)

return var_0_0
