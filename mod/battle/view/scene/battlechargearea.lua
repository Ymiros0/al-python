ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleChargeArea = class("BattleChargeArea")
var_0_0.Battle.BattleChargeArea.__name = "BattleChargeArea"

function var_0_0.Battle.BattleChargeArea.Ctor(arg_1_0, arg_1_1)
	arg_1_1.gameObject:SetActive(false)

	arg_1_0._areaTf = arg_1_1.transform
	arg_1_0._areaGO = arg_1_1
end

function var_0_0.Battle.BattleChargeArea.InitArea(arg_2_0)
	local var_2_0 = arg_2_0._areaTf

	arg_2_0._controller = var_2_0:GetComponent("ChargeArea")

	local var_2_1 = arg_2_0._chargeWeapon:GetTemplateData().range
	local var_2_2 = arg_2_0._chargeWeapon:GetTemplateData().angle
	local var_2_3 = var_2_0.localScale

	var_2_3.x = var_2_1 / 5.5
	var_2_3.y = var_2_1 / 5.5
	var_2_0.localScale = var_2_3
	arg_2_0._controller.maxAngle = var_2_2
	arg_2_0._controller.minAngle = arg_2_0._chargeWeapon:GetMinAngle()
	var_2_0:Find("UpperEdge").transform.localScale = Vector3(1, 1 / var_2_3.y, 1)
	var_2_0:Find("LowerEdge").transform.localScale = Vector3(1, 1 / var_2_3.y, 1)
	arg_2_0._controller.rate = 0.5
end

function var_0_0.Battle.BattleChargeArea.Update(arg_3_0, arg_3_1)
	arg_3_0._areaTf.position = arg_3_1
end

function var_0_0.Battle.BattleChargeArea.SetWeapon(arg_4_0, arg_4_1)
	arg_4_0._chargeWeapon = arg_4_1

	arg_4_0:InitArea()
end

function var_0_0.Battle.BattleChargeArea.SetActive(arg_5_0, arg_5_1)
	arg_5_0._areaGO:SetActive(arg_5_1)
end

function var_0_0.Battle.BattleChargeArea.GetActive(arg_6_0)
	return arg_6_0._areaGO:GetActive()
end

function var_0_0.Battle.BattleChargeArea.Reset(arg_7_0)
	arg_7_0._controller.rate = 1
end
