local var_0_0 = class("TeamType")

var_0_0.Vanguard = "vanguard"
var_0_0.Main = "main"
var_0_0.Submarine = "submarine"
var_0_0.Support = "support"
var_0_0.TeamTypeIndex = {
	var_0_0.Vanguard,
	var_0_0.Main,
	var_0_0.Submarine
}
var_0_0.VanguardShipType = {
	ShipType.QuZhu,
	ShipType.QingXun,
	ShipType.ZhongXun,
	ShipType.HangXun,
	ShipType.LeiXun,
	ShipType.ChaoXun,
	ShipType.Yunshu,
	ShipType.DaoQuV,
	ShipType.FengFanV
}
var_0_0.MainShipType = {
	ShipType.ZhanXun,
	ShipType.ZhanLie,
	ShipType.QingHang,
	ShipType.ZhengHang,
	ShipType.HangZhan,
	ShipType.WeiXiu,
	ShipType.ZhongPao,
	ShipType.DaoQuM,
	ShipType.FengFanM
}
var_0_0.SubShipType = {
	ShipType.QianTing,
	ShipType.QianMu,
	ShipType.FengFanS
}
var_0_0.VanguardMax = 3
var_0_0.MainMax = 3
var_0_0.SubmarineMax = 3

function var_0_0.GetTeamShipMax(arg_1_0)
	if arg_1_0 == var_0_0.Vanguard then
		return var_0_0.VanguardMax
	elseif arg_1_0 == var_0_0.Main then
		return var_0_0.MainMax
	elseif arg_1_0 == var_0_0.Submarine then
		return var_0_0.SubmarineMax
	end
end

var_0_0.TeamPos = {}
var_0_0.TeamPos.FLAG_SHIP = "FlagShip"
var_0_0.TeamPos.LEADER = "Leader"
var_0_0.TeamPos.CENTER = "Center"
var_0_0.TeamPos.REAR = "Rear"
var_0_0.TeamPos.CONSORT = "Consort"
var_0_0.TeamPos.SUB_LEADER = "SubLeader"
var_0_0.TeamPos.SUB_CONSORT = "SubConsort"
var_0_0.TeamPos.UPPER_CONSORT = "UpperConsort"
var_0_0.TeamPos.LOWER_CONSORT = "LowerConsort"

local var_0_1 = {
	[var_0_0.Vanguard] = var_0_0.VanguardShipType,
	[var_0_0.Main] = var_0_0.MainShipType,
	[var_0_0.Submarine] = var_0_0.SubShipType
}

function var_0_0.GetShipTypeListFromTeam(arg_2_0)
	return var_0_1[arg_2_0]
end

local var_0_2 = {}

for iter_0_0, iter_0_1 in pairs(var_0_1) do
	for iter_0_2, iter_0_3 in ipairs(iter_0_1) do
		var_0_2[iter_0_3] = iter_0_0
	end
end

function var_0_0.GetTeamFromShipType(arg_3_0)
	return var_0_2[arg_3_0]
end

return var_0_0
