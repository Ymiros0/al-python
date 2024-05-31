local var_0_0 = class("TypedFleet", import(".Fleet"))

function var_0_0.Ctor(arg_1_0, arg_1_1)
	assert(arg_1_1.fleetType)

	arg_1_0.fleetType = arg_1_1.fleetType or FleetType.Unknowns

	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.saveLastShipFlag = arg_1_1.saveLastShipFlag
end

function var_0_0.SetFleetType(arg_2_0, arg_2_1)
	arg_2_0.fleetType = arg_2_1 or FleetType.Normal
end

function var_0_0.isSubmarineFleet(arg_3_0)
	return tobool(arg_3_0:getFleetType() == FleetType.Submarine)
end

function var_0_0.SetSaveLastShip(arg_4_0, arg_4_1)
	arg_4_0.saveLastShipFlag = arg_4_1
end

function var_0_0.canRemove(arg_5_0, arg_5_1)
	if not arg_5_0.saveLastShipFlag then
		return true
	end

	local var_5_0, var_5_1 = arg_5_0:getShipPos(arg_5_1)

	if var_5_0 > 0 and #(arg_5_0:getTeamByName(var_5_1) or {}) == 1 then
		return false
	end

	return true
end

function var_0_0.getFleetType(arg_6_0)
	assert(arg_6_0.fleetType and arg_6_0.fleetType ~= FleetType.Unknown, "not set fleet type on init")

	if arg_6_0.fleetType == FleetType.Unknown then
		return FleetType.Normal
	end

	return arg_6_0.fleetType
end

function var_0_0.IsTeamMatch(arg_7_0, arg_7_1)
	local var_7_0 = arg_7_0:getFleetType()

	if var_7_0 == FleetType.Submarine then
		return arg_7_1 == TeamType.Submarine
	elseif var_7_0 == FleetType.Normal then
		return arg_7_1 == TeamType.Vanguard or arg_7_1 == TeamType.Main
	end

	assert(false)

	return true
end

function var_0_0.CanInsertShip(arg_8_0, arg_8_1, arg_8_2)
	if not var_0_0.super.CanInsertShip(arg_8_0, arg_8_1, arg_8_2) then
		return false
	end

	return arg_8_0:IsTeamMatch(arg_8_2)
end

return var_0_0
