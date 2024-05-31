ys = ys or {}

local var_0_0 = ys

var_0_0.Battle.BattleGuideWave = class("BattleGuideWave", var_0_0.Battle.BattleWaveInfo)
var_0_0.Battle.BattleGuideWave.__name = "BattleGuideWave"

local var_0_1 = var_0_0.Battle.BattleGuideWave

function var_0_1.Ctor(arg_1_0)
	var_0_1.super.Ctor(arg_1_0)
end

function var_0_1.SetWaveData(arg_2_0, arg_2_1)
	var_0_1.super.SetWaveData(arg_2_0, arg_2_1)

	arg_2_0._guideType = arg_2_0._param.type or 0
	arg_2_0._guideStep = arg_2_0._param.id
	arg_2_0._event = arg_2_0._param.event
end

function var_0_1.DoWave(arg_3_0)
	var_0_1.super.DoWave(arg_3_0)

	if not pg.NewGuideMgr.ENABLE_GUIDE then
		arg_3_0:doPass()
	elseif arg_3_0._guideType == 1 and pg.SeriesGuideMgr.GetInstance():isEnd() then
		arg_3_0:doFail()
	else
		pg.NewGuideMgr.GetInstance():Play(arg_3_0._guideStep, {
			arg_3_0._event
		}, function()
			arg_3_0:doPass()
		end)
	end
end
