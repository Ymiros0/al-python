local var_0_0 = class("WSMapFleet", import(".WSMapTransform"))

var_0_0.Fields = {
	rtShadow = "userdata",
	rtSub = "userdata",
	rtArrow = "userdata",
	spineRole = "table",
	selected = "boolean",
	rtRetreat = "userdata",
	theme = "table",
	moveTurnCount = "number",
	fleet = "table",
	rtFx = "userdata",
	timerHealth = "table",
	rtDamage = "userdata",
	rtHealth = "userdata",
	attaches = "table",
	rtMoveTurn = "userdata",
	active = "boolean",
	submarineSupport = "boolean"
}
var_0_0.Listeners = {
	onUpdate = "Update"
}
var_0_0.EventUpdateSelected = "WSMapFleet.EventUpdateSelected"

def var_0_0.GetResName(arg_1_0):
	return "ship_tpl"

def var_0_0.Setup(arg_2_0, arg_2_1, arg_2_2):
	arg_2_0.fleet = arg_2_1

	arg_2_0.fleet.AddListener(WorldMapFleet.EventUpdateLocation, arg_2_0.onUpdate)
	arg_2_0.fleet.AddListener(WorldMapFleet.EventUpdateShipOrder, arg_2_0.onUpdate)
	arg_2_0.fleet.AddListener(WorldMapFleet.EventUpdateBuff, arg_2_0.onUpdate)
	arg_2_0.fleet.AddListener(WorldMapFleet.EventUpdateDamageLevel, arg_2_0.onUpdate)

	arg_2_0.theme = arg_2_2
	arg_2_0.attaches = {}

	arg_2_0.Init()

def var_0_0.Dispose(arg_3_0):
	arg_3_0.fleet.RemoveListener(WorldMapFleet.EventUpdateLocation, arg_3_0.onUpdate)
	arg_3_0.fleet.RemoveListener(WorldMapFleet.EventUpdateShipOrder, arg_3_0.onUpdate)
	arg_3_0.fleet.RemoveListener(WorldMapFleet.EventUpdateBuff, arg_3_0.onUpdate)
	arg_3_0.fleet.RemoveListener(WorldMapFleet.EventUpdateDamageLevel, arg_3_0.onUpdate)
	arg_3_0.ClearAttaches()
	arg_3_0.ClearHealthTimer()
	var_0_0.super.Dispose(arg_3_0)

def var_0_0.Init(arg_4_0):
	arg_4_0.rtRetreat = arg_4_0.transform.Find("retreat")
	arg_4_0.rtArrow = arg_4_0.transform.Find("arrow")
	arg_4_0.rtFx = arg_4_0.transform.Find("fx")
	arg_4_0.rtShadow = arg_4_0.transform.Find("shadow")
	arg_4_0.rtSub = arg_4_0.transform.Find("marks/sub")
	arg_4_0.rtDamage = arg_4_0.transform.Find("marks/damage")
	arg_4_0.rtMoveTurn = arg_4_0.transform.Find("marks/move_turn")
	arg_4_0.rtHealth = arg_4_0.transform.Find("Health")

	setActive(arg_4_0.rtRetreat, False)
	setActive(arg_4_0.rtArrow, False)
	setActive(arg_4_0.rtSub, False)
	setActive(arg_4_0.rtDamage, False)
	setActive(arg_4_0.rtMoveTurn, False)
	setActive(arg_4_0.rtHealth, False)

	arg_4_0.transform.name = "fleet_" .. arg_4_0.fleet.id
	arg_4_0.transform.localEulerAngles = Vector3(-arg_4_0.theme.angle, 0, 0)
	arg_4_0.rtShadow.localPosition = Vector3.zero

	arg_4_0.Update()
	arg_4_0.UpdateActive(arg_4_0.active or True)
	arg_4_0.UpdateSelected(arg_4_0.selected or False)
	arg_4_0.UpdateSubmarineSupport()
	arg_4_0.UpdateModelScale(Vector3(0.4, 0.4, 1))
	arg_4_0.UpdateModelAngles(Vector3.zero)

	arg_4_0.moveTurnCount = 0

def var_0_0.LoadSpine(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_0.modelResAsync
	local var_5_1 = arg_5_0.fleet.GetFlagShipVO()
	local var_5_2 = SpineRole.New(var_5_1)

	var_5_2.Load(function()
		if arg_5_0.modelType != WorldConst.ModelSpine:
			var_5_2.Dispose()

			return

		local var_6_0 = var_5_2.modelRoot.transform

		var_5_2.model.GetComponent("SkeletonGraphic").raycastTarget = False
		var_6_0.anchoredPosition3D = Vector3.zero
		var_6_0.localScale = Vector3.one

		pg.ViewUtils.SetLayer(var_6_0, Layer.UI)
		var_5_2.SetParent(arg_5_0.model)

		arg_5_0.modelComps = {
			var_5_2.model.GetComponent("SpineAnimUI")
		}
		arg_5_0.spineRole = var_5_2

		arg_5_1(), var_5_0, var_5_2.ORBIT_KEY_SLG)

def var_0_0.UnloadSpine(arg_7_0):
	if arg_7_0.spineRole:
		arg_7_0.spineRole.Dispose()

		arg_7_0.spineRole = None

def var_0_0.Update(arg_8_0, arg_8_1):
	local var_8_0 = arg_8_0.fleet

	if arg_8_1 == None or arg_8_1 == WorldMapFleet.EventUpdateLocation and not arg_8_0.isMoving:
		arg_8_0.transform.anchoredPosition3D = arg_8_0.theme.GetLinePosition(var_8_0.row, var_8_0.column)

	if arg_8_1 == None or arg_8_1 == WorldMapFleet.EventUpdateLocation:
		arg_8_0.SetModelOrder(WorldConst.LOFleet, var_8_0.row)
		underscore.each(arg_8_0.attaches, function(arg_9_0)
			arg_9_0.modelOrder = arg_8_0.modelOrder)

	if arg_8_1 == None or arg_8_1 == WorldMapFleet.EventUpdateShipOrder:
		arg_8_0.LoadModel(WorldConst.ModelSpine, var_8_0.GetPrefab(), None, True, function()
			arg_8_0.model.SetParent(arg_8_0.transform.Find("ship"), False))

	if arg_8_1 == None or arg_8_1 == WorldMapFleet.EventUpdateBuff:
		arg_8_0.UpdateAttaches()

	if arg_8_1 == None or arg_8_1 == WorldMapFleet.EventUpdateDamageLevel:
		arg_8_0.UpdateDamageLevel()

def var_0_0.UpdateActive(arg_11_0, arg_11_1):
	if arg_11_0.active != arg_11_1:
		arg_11_0.active = arg_11_1

		setActive(arg_11_0.transform, arg_11_0.active)

def var_0_0.UpdateSelected(arg_12_0, arg_12_1):
	if arg_12_0.selected != arg_12_1:
		arg_12_0.selected = arg_12_1

		setActive(arg_12_0.rtArrow, arg_12_0.selected)
		arg_12_0.DispatchEvent(var_0_0.EventUpdateSelected)

def var_0_0.UpdateSubmarineSupport(arg_13_0):
	local var_13_0 = nowWorld()
	local var_13_1 = var_13_0.IsSubmarineSupporting()

	setActive(arg_13_0.rtSub, var_13_1)

	if var_13_1:
		setGray(arg_13_0.rtSub, not var_13_0.GetSubAidFlag(), False)

def var_0_0.UpdateAttaches(arg_14_0):
	local var_14_0 = arg_14_0.fleet.GetBuffFxList()

	for iter_14_0 = #var_14_0 + 1, #arg_14_0.attaches:
		arg_14_0.attaches[iter_14_0].Unload()

	for iter_14_1 = #arg_14_0.attaches + 1, #var_14_0:
		local var_14_1 = WPool.Get(WSMapEffect)

		var_14_1.transform = createNewGameObject("mapEffect")

		var_14_1.transform.SetParent(arg_14_0.rtFx, False)

		var_14_1.modelOrder = arg_14_0.modelOrder

		table.insert(arg_14_0.attaches, var_14_1)

	for iter_14_2 = 1, #var_14_0:
		local var_14_2 = arg_14_0.attaches[iter_14_2]

		var_14_2.Setup(WorldConst.GetBuffEffect(var_14_0[iter_14_2]))
		var_14_2.Load()

def var_0_0.ClearAttaches(arg_15_0):
	local var_15_0 = _.map(arg_15_0.attaches, function(arg_16_0)
		return arg_16_0.transform)

	WPool.ReturnArray(arg_15_0.attaches)

	for iter_15_0, iter_15_1 in ipairs(var_15_0):
		Destroy(iter_15_1)

	arg_15_0.attaches = {}

def var_0_0.UpdateDamageLevel(arg_17_0):
	local var_17_0 = arg_17_0.fleet.damageLevel

	setActive(arg_17_0.rtDamage, var_17_0 > 0)

	for iter_17_0 = 1, #WorldConst.DamageBuffList:
		setActive(arg_17_0.rtDamage.Find(iter_17_0), var_17_0 == iter_17_0)

def var_0_0.PlusMoveTurn(arg_18_0):
	arg_18_0.moveTurnCount = arg_18_0.moveTurnCount + 1

	setText(arg_18_0.rtMoveTurn.Find("Text"), arg_18_0.moveTurnCount)
	setActive(arg_18_0.rtMoveTurn, arg_18_0.moveTurnCount > 0)

def var_0_0.ClearMoveTurn(arg_19_0):
	arg_19_0.moveTurnCount = 0

	setActive(arg_19_0.rtMoveTurn, False)

def var_0_0.DisplayHealth(arg_20_0):
	arg_20_0.ClearHealthTimer()
	setActive(arg_20_0.rtHealth, True)

	arg_20_0.timerHealth = Timer.New(function()
		setActive(arg_20_0.rtHealth, False)

		arg_20_0.timerHealth = None, 2)

	arg_20_0.timerHealth.Start()

def var_0_0.ClearHealthTimer(arg_22_0):
	if arg_22_0.timerHealth:
		arg_22_0.timerHealth.Stop()

		arg_22_0.timerHealth = None

		setActive(arg_22_0.rtHealth, False)

return var_0_0
