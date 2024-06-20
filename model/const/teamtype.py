from luatable import table, pairs, ipairs
import ShipType
Vanguard = "vanguard"
Main = "main"
Submarine = "submarine"
Support = "support"
TeamTypeIndex = table(
	Vanguard,
	Main,
	Submarine
)
VanguardShipType = table(
	ShipType.QuZhu,
	ShipType.QingXun,
	ShipType.ZhongXun,
	ShipType.HangXun,
	ShipType.LeiXun,
	ShipType.ChaoXun,
	ShipType.Yunshu,
	ShipType.DaoQuV,
	ShipType.FengFanV
)
MainShipType = table(
	ShipType.ZhanXun,
	ShipType.ZhanLie,
	ShipType.QingHang,
	ShipType.ZhengHang,
	ShipType.HangZhan,
	ShipType.WeiXiu,
	ShipType.ZhongPao,
	ShipType.DaoQuM,
	ShipType.FengFanM
)
SubShipType = table(
	ShipType.QianTing,
	ShipType.QianMu,
	ShipType.FengFanS
)
VanguardMax = 3
MainMax = 3
SubmarineMax = 3

def GetTeamShipMax(arg_1_0):
	if arg_1_0 == Vanguard:
		return VanguardMax
	elif arg_1_0 == Main:
		return MainMax
	elif arg_1_0 == Submarine:
		return SubmarineMax

TeamPos = table()
TeamPos.FLAG_SHIP = "FlagShip"
TeamPos.LEADER = "Leader"
TeamPos.CENTER = "Center"
TeamPos.REAR = "Rear"
TeamPos.CONSORT = "Consort"
TeamPos.SUB_LEADER = "SubLeader"
TeamPos.SUB_CONSORT = "SubConsort"
TeamPos.UPPER_CONSORT = "UpperConsort"
TeamPos.LOWER_CONSORT = "LowerConsort"

var_0_1 = table({
	Vanguard: VanguardShipType,
	Main: MainShipType,
	Submarine: SubShipType
})

def GetShipTypeListFromTeam(arg_2_0):
	return var_0_1[arg_2_0]

var_0_2 = table()

for iter_0_0, iter_0_1 in pairs(var_0_1):
	for iter_0_2, iter_0_3 in ipairs(iter_0_1):
		var_0_2[iter_0_3] = iter_0_0

def GetTeamFromShipType(arg_3_0):
	return var_0_2[arg_3_0]