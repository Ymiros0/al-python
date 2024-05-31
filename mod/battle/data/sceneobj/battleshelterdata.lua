ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConst
local var_0_2 = pg.effect_offset

var_0_0.Battle.BattleShelterData = class("BattleShelterData")
var_0_0.Battle.BattleShelterData.__name = "BattleShelterData"

local var_0_3 = var_0_0.Battle.BattleShelterData

function var_0_3.Ctor(arg_1_0, arg_1_1)
	arg_1_0._id = arg_1_1
end

function var_0_3.SetIFF(arg_2_0, arg_2_1)
	arg_2_0._IFF = arg_2_1
end

function var_0_3.SetArgs(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4, arg_3_5)
	arg_3_0._duration = arg_3_2
	arg_3_0._bulletType = var_0_0.Battle.BattleConst.BulletType.CANNON
	arg_3_0._count = arg_3_1
	arg_3_0._effect = arg_3_5
	arg_3_0._doWhenHit = "intercept"

	local function var_3_0(arg_4_0)
		if arg_4_0:GetType() == arg_3_0._bulletType and arg_3_0:IsWallActive() then
			arg_3_0:DoWhenHit(arg_4_0)
		end

		return arg_3_0._count > 0
	end

	local var_3_1 = {
		0,
		0,
		0
	}

	arg_3_0._wall = var_0_0.Battle.BattleDataProxy.GetInstance():SpawnWall(arg_3_0, var_3_0, arg_3_3, var_3_1)
	arg_3_0._centerPos = arg_3_4
end

function var_0_3.SetStartTimeStamp(arg_5_0, arg_5_1)
	arg_5_0._startTimeStamp = arg_5_1
end

function var_0_3.Update(arg_6_0, arg_6_1)
	if arg_6_1 - arg_6_0._startTimeStamp > arg_6_0._duration then
		arg_6_0._startTimeStamp = nil
	end
end

function var_0_3.DoWhenHit(arg_7_0, arg_7_1)
	if arg_7_0._doWhenHit == "intercept" then
		arg_7_1:Intercepted()
		var_0_0.Battle.BattleDataProxy.GetInstance():RemoveBulletUnit(arg_7_1:GetUniqueID())

		arg_7_0._count = arg_7_0._count - 1
	elseif arg_7_0._doWhenHit == "reflect" and arg_7_0:GetIFF() ~= arg_7_1:GetIFF() then
		arg_7_1:Reflected()

		arg_7_0._count = arg_7_0._count - 1
	end
end

function var_0_3.GetUniqueID(arg_8_0)
	return arg_8_0._id
end

function var_0_3.GetIFF(arg_9_0)
	return arg_9_0._IFF
end

function var_0_3.GetFXID(arg_10_0)
	return arg_10_0._effect
end

function var_0_3.GetPosition(arg_11_0)
	return arg_11_0._centerPos
end

function var_0_3.Deactive(arg_12_0)
	var_0_0.Battle.BattleDataProxy.GetInstance():RemoveWall(arg_12_0._wall:GetUniqueID())
end

function var_0_3.IsWallActive(arg_13_0)
	return arg_13_0._count > 0 and arg_13_0._startTimeStamp
end
