﻿local var_0_0 = class("WSMapFleet", import(".WSMapTransform"))

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

function var_0_0.GetResName(arg_1_0)
	return "ship_tpl"
end

function var_0_0.Setup(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0.fleet = arg_2_1

	arg_2_0.fleet:AddListener(WorldMapFleet.EventUpdateLocation, arg_2_0.onUpdate)
	arg_2_0.fleet:AddListener(WorldMapFleet.EventUpdateShipOrder, arg_2_0.onUpdate)
	arg_2_0.fleet:AddListener(WorldMapFleet.EventUpdateBuff, arg_2_0.onUpdate)
	arg_2_0.fleet:AddListener(WorldMapFleet.EventUpdateDamageLevel, arg_2_0.onUpdate)

	arg_2_0.theme = arg_2_2
	arg_2_0.attaches = {}

	arg_2_0:Init()
end

function var_0_0.Dispose(arg_3_0)
	arg_3_0.fleet:RemoveListener(WorldMapFleet.EventUpdateLocation, arg_3_0.onUpdate)
	arg_3_0.fleet:RemoveListener(WorldMapFleet.EventUpdateShipOrder, arg_3_0.onUpdate)
	arg_3_0.fleet:RemoveListener(WorldMapFleet.EventUpdateBuff, arg_3_0.onUpdate)
	arg_3_0.fleet:RemoveListener(WorldMapFleet.EventUpdateDamageLevel, arg_3_0.onUpdate)
	arg_3_0:ClearAttaches()
	arg_3_0:ClearHealthTimer()
	var_0_0.super.Dispose(arg_3_0)
end

function var_0_0.Init(arg_4_0)
	arg_4_0.rtRetreat = arg_4_0.transform:Find("retreat")
	arg_4_0.rtArrow = arg_4_0.transform:Find("arrow")
	arg_4_0.rtFx = arg_4_0.transform:Find("fx")
	arg_4_0.rtShadow = arg_4_0.transform:Find("shadow")
	arg_4_0.rtSub = arg_4_0.transform:Find("marks/sub")
	arg_4_0.rtDamage = arg_4_0.transform:Find("marks/damage")
	arg_4_0.rtMoveTurn = arg_4_0.transform:Find("marks/move_turn")
	arg_4_0.rtHealth = arg_4_0.transform:Find("Health")

	setActive(arg_4_0.rtRetreat, false)
	setActive(arg_4_0.rtArrow, false)
	setActive(arg_4_0.rtSub, false)
	setActive(arg_4_0.rtDamage, false)
	setActive(arg_4_0.rtMoveTurn, false)
	setActive(arg_4_0.rtHealth, false)

	arg_4_0.transform.name = "fleet_" .. arg_4_0.fleet.id
	arg_4_0.transform.localEulerAngles = Vector3(-arg_4_0.theme.angle, 0, 0)
	arg_4_0.rtShadow.localPosition = Vector3.zero

	arg_4_0:Update()
	arg_4_0:UpdateActive(arg_4_0.active or true)
	arg_4_0:UpdateSelected(arg_4_0.selected or false)
	arg_4_0:UpdateSubmarineSupport()
	arg_4_0:UpdateModelScale(Vector3(0.4, 0.4, 1))
	arg_4_0:UpdateModelAngles(Vector3.zero)

	arg_4_0.moveTurnCount = 0
end

function var_0_0.LoadSpine(arg_5_0, arg_5_1)
	local var_5_0 = arg_5_0.modelResAsync
	local var_5_1 = arg_5_0.fleet:GetFlagShipVO()
	local var_5_2 = SpineRole.New(var_5_1)

	var_5_2:Load(function()
		if arg_5_0.modelType ~= WorldConst.ModelSpine then
			var_5_2:Dispose()

			return
		end

		local var_6_0 = var_5_2.modelRoot.transform

		var_5_2.model:GetComponent("SkeletonGraphic").raycastTarget = false
		var_6_0.anchoredPosition3D = Vector3.zero
		var_6_0.localScale = Vector3.one

		pg.ViewUtils.SetLayer(var_6_0, Layer.UI)
		var_5_2:SetParent(arg_5_0.model)

		arg_5_0.modelComps = {
			var_5_2.model:GetComponent("SpineAnimUI")
		}
		arg_5_0.spineRole = var_5_2

		arg_5_1()
	end, var_5_0, var_5_2.ORBIT_KEY_SLG)
end

function var_0_0.UnloadSpine(arg_7_0)
	if arg_7_0.spineRole then
		arg_7_0.spineRole:Dispose()

		arg_7_0.spineRole = nil
	end
end

function var_0_0.Update(arg_8_0, arg_8_1)
	local var_8_0 = arg_8_0.fleet

	if arg_8_1 == nil or arg_8_1 == WorldMapFleet.EventUpdateLocation and not arg_8_0.isMoving then
		arg_8_0.transform.anchoredPosition3D = arg_8_0.theme:GetLinePosition(var_8_0.row, var_8_0.column)
	end

	if arg_8_1 == nil or arg_8_1 == WorldMapFleet.EventUpdateLocation then
		arg_8_0:SetModelOrder(WorldConst.LOFleet, var_8_0.row)
		underscore.each(arg_8_0.attaches, function(arg_9_0)
			arg_9_0.modelOrder = arg_8_0.modelOrder
		end)
	end

	if arg_8_1 == nil or arg_8_1 == WorldMapFleet.EventUpdateShipOrder then
		arg_8_0:LoadModel(WorldConst.ModelSpine, var_8_0:GetPrefab(), nil, true, function()
			arg_8_0.model:SetParent(arg_8_0.transform:Find("ship"), false)
		end)
	end

	if arg_8_1 == nil or arg_8_1 == WorldMapFleet.EventUpdateBuff then
		arg_8_0:UpdateAttaches()
	end

	if arg_8_1 == nil or arg_8_1 == WorldMapFleet.EventUpdateDamageLevel then
		arg_8_0:UpdateDamageLevel()
	end
end

function var_0_0.UpdateActive(arg_11_0, arg_11_1)
	if arg_11_0.active ~= arg_11_1 then
		arg_11_0.active = arg_11_1

		setActive(arg_11_0.transform, arg_11_0.active)
	end
end

function var_0_0.UpdateSelected(arg_12_0, arg_12_1)
	if arg_12_0.selected ~= arg_12_1 then
		arg_12_0.selected = arg_12_1

		setActive(arg_12_0.rtArrow, arg_12_0.selected)
		arg_12_0:DispatchEvent(var_0_0.EventUpdateSelected)
	end
end

function var_0_0.UpdateSubmarineSupport(arg_13_0)
	local var_13_0 = nowWorld()
	local var_13_1 = var_13_0:IsSubmarineSupporting()

	setActive(arg_13_0.rtSub, var_13_1)

	if var_13_1 then
		setGray(arg_13_0.rtSub, not var_13_0:GetSubAidFlag(), false)
	end
end

function var_0_0.UpdateAttaches(arg_14_0)
	local var_14_0 = arg_14_0.fleet:GetBuffFxList()

	for iter_14_0 = #var_14_0 + 1, #arg_14_0.attaches do
		arg_14_0.attaches[iter_14_0]:Unload()
	end

	for iter_14_1 = #arg_14_0.attaches + 1, #var_14_0 do
		local var_14_1 = WPool:Get(WSMapEffect)

		var_14_1.transform = createNewGameObject("mapEffect")

		var_14_1.transform:SetParent(arg_14_0.rtFx, false)

		var_14_1.modelOrder = arg_14_0.modelOrder

		table.insert(arg_14_0.attaches, var_14_1)
	end

	for iter_14_2 = 1, #var_14_0 do
		local var_14_2 = arg_14_0.attaches[iter_14_2]

		var_14_2:Setup(WorldConst.GetBuffEffect(var_14_0[iter_14_2]))
		var_14_2:Load()
	end
end

function var_0_0.ClearAttaches(arg_15_0)
	local var_15_0 = _.map(arg_15_0.attaches, function(arg_16_0)
		return arg_16_0.transform
	end)

	WPool:ReturnArray(arg_15_0.attaches)

	for iter_15_0, iter_15_1 in ipairs(var_15_0) do
		Destroy(iter_15_1)
	end

	arg_15_0.attaches = {}
end

function var_0_0.UpdateDamageLevel(arg_17_0)
	local var_17_0 = arg_17_0.fleet.damageLevel

	setActive(arg_17_0.rtDamage, var_17_0 > 0)

	for iter_17_0 = 1, #WorldConst.DamageBuffList do
		setActive(arg_17_0.rtDamage:Find(iter_17_0), var_17_0 == iter_17_0)
	end
end

function var_0_0.PlusMoveTurn(arg_18_0)
	arg_18_0.moveTurnCount = arg_18_0.moveTurnCount + 1

	setText(arg_18_0.rtMoveTurn:Find("Text"), arg_18_0.moveTurnCount)
	setActive(arg_18_0.rtMoveTurn, arg_18_0.moveTurnCount > 0)
end

function var_0_0.ClearMoveTurn(arg_19_0)
	arg_19_0.moveTurnCount = 0

	setActive(arg_19_0.rtMoveTurn, false)
end

function var_0_0.DisplayHealth(arg_20_0)
	arg_20_0:ClearHealthTimer()
	setActive(arg_20_0.rtHealth, true)

	arg_20_0.timerHealth = Timer.New(function()
		setActive(arg_20_0.rtHealth, false)

		arg_20_0.timerHealth = nil
	end, 2)

	arg_20_0.timerHealth:Start()
end

function var_0_0.ClearHealthTimer(arg_22_0)
	if arg_22_0.timerHealth then
		arg_22_0.timerHealth:Stop()

		arg_22_0.timerHealth = nil

		setActive(arg_22_0.rtHealth, false)
	end
end

return var_0_0
