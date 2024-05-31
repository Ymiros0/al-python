ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig

var_0_0.Battle.BattleCameraWave = class("BattleCameraWave", var_0_0.Battle.BattleWaveInfo)
var_0_0.Battle.BattleCameraWave.__name = "BattleCameraWave"

local var_0_2 = var_0_0.Battle.BattleCameraWave

function var_0_2.Ctor(arg_1_0)
	var_0_2.super.Ctor(arg_1_0)
end

function var_0_2.SetWaveData(arg_2_0, arg_2_1)
	var_0_2.super.SetWaveData(arg_2_0, arg_2_1)

	arg_2_0._pause = arg_2_0._param.pause
	arg_2_0._cameraType = arg_2_0._param.type or 0
	arg_2_0._modelID = arg_2_0._param.model or 900006
	arg_2_0._duration = arg_2_0._param.duration or 1
	arg_2_0._zoomSize = arg_2_0._param.zoomSize
	arg_2_0._zoomBounce = arg_2_0._param.zoomBounce
end

function var_0_2.DoWave(arg_3_0)
	var_0_2.super.DoWave(arg_3_0)

	local var_3_0 = var_0_0.Battle.BattleCameraUtil.GetInstance()

	if arg_3_0._cameraType == 1 then
		local var_3_1 = var_0_0.Battle.BattleDataProxy.GetInstance():GetUnitList()
		local var_3_2

		for iter_3_0, iter_3_1 in pairs(var_3_1) do
			if iter_3_1:GetTemplateID() == arg_3_0._modelID then
				var_3_2 = iter_3_1

				break
			end
		end

		var_3_0:FocusCharacter(var_3_2, arg_3_0._duration, 0, true, not arg_3_0._zoomBounce)

		if arg_3_0._zoomSize then
			local var_3_3 = arg_3_0._duration * 0.5

			if arg_3_0._zoomBounce then
				var_3_0:ZoomCamara(nil, var_0_1.CAST_CAM_OVERLOOK_SIZE, var_3_3)
				LeanTween.delayedCall(var_3_3, System.Action(function()
					var_3_0:ZoomCamara(var_0_1.CAST_CAM_OVERLOOK_SIZE, arg_3_0._zoomSize, var_3_3)
				end))
			else
				var_3_0:ZoomCamara(nil, arg_3_0._zoomSize, arg_3_0._duration, true)
			end
		end
	elseif arg_3_0._cameraType == 0 then
		var_3_0:FocusCharacter(nil, arg_3_0._duration, 0)
		var_3_0:ZoomCamara(nil, nil, arg_3_0._duration)
	end

	var_3_0:BulletTime(var_0_1.SPEED_FACTOR_FOCUS_CHARACTER, nil)
	arg_3_0:doPass()
end
