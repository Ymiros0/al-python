ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleUnitEvent
local var_0_2 = var_0_0.Battle.BattleEvent
local var_0_3 = var_0_0.Battle.BattleCardPuzzleEvent
local var_0_4 = var_0_0.Battle.BattleFormulas
local var_0_5 = var_0_0.Battle.BattleConst
local var_0_6 = var_0_0.Battle.BattleConfig
local var_0_7 = var_0_0.Battle.BattleCardPuzzleConfig
local var_0_8 = var_0_0.Battle.BattleAttr
local var_0_9 = var_0_0.Battle.BattleDataFunction
local var_0_10 = var_0_0.Battle.BattleAttr
local var_0_11 = class("BattleFleetCardPuzzleAttribute")

var_0_0.Battle.BattleFleetCardPuzzleAttribute = var_0_11
var_0_11.__name = "BattleFleetCardPuzzleAttribute"

function var_0_11.Ctor(arg_1_0, arg_1_1)
	arg_1_0:init()

	arg_1_0._client = arg_1_1
end

function var_0_11.init(arg_2_0)
	arg_2_0._buffAttr = {}
	arg_2_0._attrList = {}
	arg_2_0._clampList = {}
end

function var_0_11.AddBaseAttr(arg_3_0, arg_3_1, arg_3_2)
	arg_3_0._attrList[arg_3_1] = math.max(0, arg_3_2 + (arg_3_0._attrList[arg_3_1] or 0))
	arg_3_0._attrList[arg_3_1] = arg_3_0:checkClamp(arg_3_1)

	arg_3_0._client:DispatchUpdateAttr(arg_3_1)
	arg_3_0:specificAttrUpdate(arg_3_1)
end

function var_0_11.SetAttr(arg_4_0, arg_4_1, arg_4_2)
	arg_4_0._attrList[arg_4_1] = arg_4_2
	arg_4_0._attrList[arg_4_1] = arg_4_0:checkClamp(arg_4_1)

	arg_4_0._client:DispatchUpdateAttr(arg_4_1)
	arg_4_0:specificAttrUpdate(arg_4_1)
end

function var_0_11.specificAttrUpdate(arg_5_0, arg_5_1)
	if arg_5_1 == "BaseEnergyBoostRate" or arg_5_1 == "BaseEnergyBoostExtra" then
		arg_5_0._client:FlushHandOverheat()
	end
end

function var_0_11.checkClamp(arg_6_0, arg_6_1)
	if arg_6_0._attrList[arg_6_1] == nil then
		return
	end

	local var_6_0 = arg_6_0._attrList[arg_6_1]
	local var_6_1 = var_0_7.FleetAttrClamp[arg_6_1]

	if var_6_1 then
		local var_6_2 = arg_6_0._attrList[var_6_1.max]
		local var_6_3 = arg_6_0._attrList[var_6_1.min] or 0

		var_6_0 = math.max(var_6_0, var_6_3)
		var_6_0 = var_6_2 and math.min(var_6_0, var_6_2) or var_6_0
	end

	return var_6_0
end

function var_0_11.GetCurrent(arg_7_0, arg_7_1)
	return arg_7_0._attrList[arg_7_1] or 0
end
