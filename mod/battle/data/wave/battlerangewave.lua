ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleRangeWave = class("BattleRangeWave", var_0_0.Battle.BattleWaveInfo)
var_0_0.Battle.BattleRangeWave.__name = "BattleRangeWave"

local var_0_1 = var_0_0.Battle.BattleRangeWave

function var_0_1.Ctor(arg_1_0)
	var_0_1.super.Ctor(arg_1_0)
end

function var_0_1.SetWaveData(arg_2_0, arg_2_1)
	var_0_1.super.SetWaveData(arg_2_0, arg_2_1)

	arg_2_0._pos = Vector3(arg_2_0._param.rect[1], 0, arg_2_0._param.rect[2])
	arg_2_0._width = arg_2_0._param.rect[3]
	arg_2_0._height = arg_2_0._param.rect[4]
	arg_2_0._lifeTime = 99999
end

function var_0_1.DoWave(arg_3_0)
	var_0_1.super.DoWave(arg_3_0)
	arg_3_0._spawnFunc(arg_3_0._pos, arg_3_0._width, arg_3_0._height, arg_3_0._lifeTime, function(arg_4_0, arg_4_1)
		for iter_4_0, iter_4_1 in ipairs(arg_4_0) do
			if iter_4_1.IFF ~= arg_4_1:GetCldData().IFF then
				arg_4_1:SetActiveFlag(false)
				arg_3_0:doPass()

				break
			end
		end
	end)
end
