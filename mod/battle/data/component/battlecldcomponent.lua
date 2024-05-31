ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = class("BattleCldComponent")

var_0_0.Battle.BattleCldComponent = var_0_2
var_0_2.__name = "BattleCldComponent"

function var_0_2.Ctor(arg_1_0)
	return
end

function var_0_2.SetActive(arg_2_0, arg_2_1)
	arg_2_0._cldData.Active = arg_2_1
end

function var_0_2.SetImmuneCLD(arg_3_0, arg_3_1)
	arg_3_0._cldData.ImmuneCLD = arg_3_1
end

function var_0_2.SetCldData(arg_4_0, arg_4_1)
	arg_4_0._cldData = arg_4_1
	arg_4_0._cldData.distList = {}
	arg_4_0._cldData.Active = false
	arg_4_0._cldData.ImmuneCLD = false
	arg_4_0._cldData.FriendlyCld = false
	arg_4_0._cldData.Surface = var_0_1.OXY_STATE.FLOAT
	arg_4_0._box.data = arg_4_1
end

function var_0_2.ActiveFriendlyCld(arg_5_0)
	arg_5_0._cldData.FriendlyCld = true
end

function var_0_2.GetCldData(arg_6_0)
	return arg_6_0._cldData
end

function var_0_2.GetCldBox(arg_7_0, arg_7_1)
	assert(false, "BattleCldComponent.GetCldBox:重写这个方法啦！")
end

function var_0_2.GetCldBoxSize(arg_8_0)
	assert(false, "BattleCldComponent.GetCldBoxSize:重写这个方法啦！")

	return nil
end

function var_0_2.FixSpeed(arg_9_0, arg_9_1)
	if not arg_9_0._cldData.FriendlyCld then
		return
	end

	if #arg_9_0._cldData.distList == 0 then
		return
	end

	if arg_9_1.x == 0 and arg_9_1.z == 0 then
		arg_9_0:HandleStaticCld(arg_9_1)
	else
		arg_9_0:HandleDynamicCld(arg_9_1)
	end
end

function var_0_2.HandleDynamicCld(arg_10_0, arg_10_1)
	local var_10_0 = false
	local var_10_1 = false

	for iter_10_0, iter_10_1 in ipairs(arg_10_0._cldData.distList) do
		local var_10_2 = iter_10_1.x

		if not var_10_0 and var_10_2 * math.abs(arg_10_1.x) / arg_10_1.x < 0 then
			arg_10_1.x = 0
			var_10_0 = true
		end

		local var_10_3 = iter_10_1.z

		if not var_10_1 and var_10_3 * math.abs(arg_10_1.z) / arg_10_1.z < 0 then
			arg_10_1.z = 0
			var_10_1 = true
		end

		if var_10_0 and var_10_1 then
			return
		end
	end
end

function var_0_2.HandleStaticCld(arg_11_0, arg_11_1)
	local var_11_0 = arg_11_0._cldData.distList[1]
	local var_11_1 = Vector3(var_11_0.x, 0, var_11_0.z).normalized

	arg_11_1.x = var_0_0.Battle.BattleFormulas.ConvertShipSpeed(var_11_1.x)
	arg_11_1.z = var_0_0.Battle.BattleFormulas.ConvertShipSpeed(var_11_1.z)
end
