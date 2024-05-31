ys = ys or {}

local var_0_0 = ys
local var_0_1 = var_0_0.Battle.BattleConfig

var_0_0.Battle.BattleCameraWave = class("BattleCameraWave", var_0_0.Battle.BattleWaveInfo)
var_0_0.Battle.BattleCameraWave.__name = "BattleCameraWave"

local var_0_2 = var_0_0.Battle.BattleCameraWave

def var_0_2.Ctor(arg_1_0):
	var_0_2.super.Ctor(arg_1_0)

def var_0_2.SetWaveData(arg_2_0, arg_2_1):
	var_0_2.super.SetWaveData(arg_2_0, arg_2_1)

	arg_2_0._pause = arg_2_0._param.pause
	arg_2_0._cameraType = arg_2_0._param.type or 0
	arg_2_0._modelID = arg_2_0._param.model or 900006
	arg_2_0._duration = arg_2_0._param.duration or 1
	arg_2_0._zoomSize = arg_2_0._param.zoomSize
	arg_2_0._zoomBounce = arg_2_0._param.zoomBounce

def var_0_2.DoWave(arg_3_0):
	var_0_2.super.DoWave(arg_3_0)

	local var_3_0 = var_0_0.Battle.BattleCameraUtil.GetInstance()

	if arg_3_0._cameraType == 1:
		local var_3_1 = var_0_0.Battle.BattleDataProxy.GetInstance().GetUnitList()
		local var_3_2

		for iter_3_0, iter_3_1 in pairs(var_3_1):
			if iter_3_1.GetTemplateID() == arg_3_0._modelID:
				var_3_2 = iter_3_1

				break

		var_3_0.FocusCharacter(var_3_2, arg_3_0._duration, 0, True, not arg_3_0._zoomBounce)

		if arg_3_0._zoomSize:
			local var_3_3 = arg_3_0._duration * 0.5

			if arg_3_0._zoomBounce:
				var_3_0.ZoomCamara(None, var_0_1.CAST_CAM_OVERLOOK_SIZE, var_3_3)
				LeanTween.delayedCall(var_3_3, System.Action(function()
					var_3_0.ZoomCamara(var_0_1.CAST_CAM_OVERLOOK_SIZE, arg_3_0._zoomSize, var_3_3)))
			else
				var_3_0.ZoomCamara(None, arg_3_0._zoomSize, arg_3_0._duration, True)
	elif arg_3_0._cameraType == 0:
		var_3_0.FocusCharacter(None, arg_3_0._duration, 0)
		var_3_0.ZoomCamara(None, None, arg_3_0._duration)

	var_3_0.BulletTime(var_0_1.SPEED_FACTOR_FOCUS_CHARACTER, None)
	arg_3_0.doPass()
