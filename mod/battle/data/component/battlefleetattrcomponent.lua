ys = ys or {}
ys.Battle.BattleFleetAttrComponent = class("BattleFleetAttrComponent")
ys.Battle.BattleFleetAttrComponent.__name = "BattleFleetAttrComponent"

local var_0_0 = ys.Battle.BattleFleetAttrComponent
local var_0_1 = ys.Battle.BattleConst
local var_0_2 = ys.Battle.BattleConfig
local var_0_3 = ys.Battle.BattleEvent

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0._client = arg_1_1

	arg_1_0:initFleetAttr()
end

function var_0_0.Dispose(arg_2_0)
	arg_2_0._client = nil
end

function var_0_0.initFleetAttr(arg_3_0)
	arg_3_0._fleetAttrList = {}
end

function var_0_0.GetCurrent(arg_4_0, arg_4_1)
	return arg_4_0._fleetAttrList[arg_4_1] or 0
end

function var_0_0.SetCurrent(arg_5_0, arg_5_1, arg_5_2)
	local var_5_0 = arg_5_0:GetCurrent(arg_5_1)
	local var_5_1 = var_0_2.FLEET_ATTR_CAP[arg_5_1]

	if var_5_1 then
		arg_5_2 = Mathf.Clamp(arg_5_2, 0, var_5_1)
	else
		arg_5_2 = math.max(arg_5_2, 0)
	end

	arg_5_0._fleetAttrList[arg_5_1] = arg_5_2

	if var_5_0 ~= arg_5_2 then
		local var_5_2 = arg_5_2 - var_5_0

		arg_5_0._client:FleetBuffTrigger(var_0_1.BuffEffectType.ON_FLEET_ATTR_UPDATE, {
			attr = arg_5_1,
			value = arg_5_2,
			delta = var_5_2
		})
		arg_5_0._client:DispatchEvent(ys.Event.New(var_0_3.UPDATE_FLEET_ATTR, {
			attr = arg_5_1,
			value = arg_5_2
		}))
	end
end
