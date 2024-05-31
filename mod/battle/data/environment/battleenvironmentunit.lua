ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = var_0_0.Battle.BattleConfig
local var_0_3 = var_0_0.Battle.BattleDataFunction
local var_0_4 = class("BattleEnvironmentUnit")

var_0_0.Battle.BattleEnvironmentUnit = var_0_4
var_0_4.__name = "BattleEnvironmentUnit"

function var_0_4.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_0.EventDispatcher.AttachEventDispatcher(arg_1_0)

	arg_1_0._uid = arg_1_1
end

function var_0_4.ConfigCallback(arg_2_0, arg_2_1)
	arg_2_0._callback = arg_2_1
end

function var_0_4.GetUniqueID(arg_3_0)
	return arg_3_0._uid
end

function var_0_4.SetTemplate(arg_4_0, arg_4_1)
	arg_4_0._template = arg_4_1

	arg_4_0:initBehaviours()
end

function var_0_4.SetAOEData(arg_5_0, arg_5_1)
	arg_5_0._expireTimeStamp = pg.TimeMgr.GetInstance():GetCombatTime() + arg_5_0._template.life_time
	arg_5_0._aoeData = arg_5_1
end

function var_0_4.GetAOEData(arg_6_0)
	return arg_6_0._aoeData
end

function var_0_4.GetBehaviours(arg_7_0)
	return arg_7_0._behaviours
end

function var_0_4.GetTemplate(arg_8_0)
	return arg_8_0._template
end

function var_0_4.UpdateFrequentlyCollide(arg_9_0, arg_9_1)
	for iter_9_0, iter_9_1 in ipairs(arg_9_0._behaviours) do
		iter_9_1:UpdateCollideUnitList(arg_9_1)
	end
end

function var_0_4.Update(arg_10_0)
	for iter_10_0, iter_10_1 in ipairs(arg_10_0._behaviours) do
		iter_10_1:OnUpdate()
	end
end

function var_0_4.IsExpire(arg_11_0, arg_11_1)
	return arg_11_1 > arg_11_0._expireTimeStamp
end

function var_0_4.Dispose(arg_12_0)
	if arg_12_0._callback then
		arg_12_0._callback()
	end

	for iter_12_0, iter_12_1 in ipairs(arg_12_0._behaviours) do
		iter_12_1:Dispose()
	end
end

function var_0_4.initBehaviours(arg_13_0)
	arg_13_0._behaviours = {}

	local var_13_0 = var_0_3.GetEnvironmentBehaviour(arg_13_0._template.behaviours).behaviour_list

	for iter_13_0, iter_13_1 in ipairs(var_13_0) do
		local var_13_1 = var_0_0.Battle.BattleEnvironmentBehaviour.CreateBehaviour(iter_13_1)

		var_13_1:SetUnitRef(arg_13_0)
		var_13_1:SetTemplate(iter_13_1)
		table.insert(arg_13_0._behaviours, var_13_1)
	end
end
