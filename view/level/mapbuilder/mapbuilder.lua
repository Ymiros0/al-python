﻿local var_0_0 = class("MapBuilder", import("view.base.BaseSubView"))

var_0_0.TYPENORMAL = 1
var_0_0.TYPEESCORT = 2
var_0_0.TYPESHINANO = 3
var_0_0.TYPESKIRMISH = 4
var_0_0.TYPEBISMARCK = 5
var_0_0.TYPESSSS = 6
var_0_0.TYPEATELIER = 7
var_0_0.TYPESENRANKAGURA = 8

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2.event, arg_1_2.contextData)

	arg_1_0.sceneParent = arg_1_2
	arg_1_0.map = arg_1_1:Find("maps")
	arg_1_0.float = arg_1_1:Find("float")
	arg_1_0.tweens = {}
	arg_1_0.mapWidth = 1920
	arg_1_0.mapHeight = 1440
	arg_1_0.buffer = setmetatable({}, {
		__index = function(arg_2_0, arg_2_1)
			return function(arg_3_0, ...)
				if arg_2_1 == "UpdateMapItems" and underscore.any(arg_1_0._funcQueue, function(arg_4_0)
					return arg_4_0.funcName == arg_2_1
				end) then
					return
				end

				arg_1_0:ActionInvoke(arg_2_1, ...)
			end
		end,
		__newindex = function()
			errorMsg("Cant write Data in ActionInvoke buffer")
		end
	})
	arg_1_0.isFrozen = nil

	arg_1_0:bind(LevelUIConst.ON_FROZEN, function()
		arg_1_0.isFrozen = true
	end)
	arg_1_0:bind(LevelUIConst.ON_UNFROZEN, function()
		arg_1_0.isFrozen = nil
	end)
end

function var_0_0.Load(arg_8_0)
	if arg_8_0._state ~= var_0_0.STATES.NONE then
		return
	end

	arg_8_0._state = var_0_0.STATES.LOADING

	pg.UIMgr.GetInstance():LoadingOn()

	local var_8_0 = PoolMgr.GetInstance()
	local var_8_1

	parallelAsync({
		function(arg_9_0)
			var_8_0:GetUI(arg_8_0:getUIName(), true, function(arg_10_0)
				if arg_8_0._state == var_0_0.STATES.DESTROY then
					pg.UIMgr.GetInstance():LoadingOff()
					var_8_0:ReturnUI(arg_8_0:getUIName(), arg_10_0)
				else
					var_8_1 = arg_10_0

					arg_9_0()
				end
			end)
		end,
		function(arg_11_0)
			arg_8_0:preload(arg_11_0)
		end
	}, function()
		arg_8_0:Loaded(var_8_1)
		arg_8_0:Init()
	end)
end

function var_0_0.preload(arg_13_0, arg_13_1)
	arg_13_1()
end

function var_0_0.isfrozen(arg_14_0)
	return arg_14_0.isFrozen
end

function var_0_0.DoFunction(arg_15_0, arg_15_1)
	arg_15_1()
end

function var_0_0.InvokeParent(arg_16_0, arg_16_1, ...)
	local var_16_0 = arg_16_0.sceneParent[arg_16_1]

	if var_16_0 then
		return var_16_0(arg_16_0.sceneParent, ...)
	end
end

function var_0_0.GetType(arg_17_0)
	return 0
end

function var_0_0.OnLoaded(arg_18_0)
	arg_18_0._tf:SetParent(arg_18_0.float, false)
end

function var_0_0.Destroy(arg_19_0)
	if arg_19_0._state == var_0_0.STATES.INITED then
		arg_19_0:Hide()
	end

	var_0_0.super.Destroy(arg_19_0)
end

function var_0_0.OnDestroy(arg_20_0)
	arg_20_0.tweens = nil
end

function var_0_0.Show(arg_21_0)
	setActive(arg_21_0._tf, true)
	arg_21_0:OnShow()
end

function var_0_0.Hide(arg_22_0)
	arg_22_0:OnHide()
	setActive(arg_22_0._tf, false)
end

function var_0_0.OnShow(arg_23_0)
	return
end

function var_0_0.OnHide(arg_24_0)
	for iter_24_0, iter_24_1 in pairs(arg_24_0.tweens) do
		LeanTween.cancel(iter_24_1)
	end

	arg_24_0.tweens = {}
end

function var_0_0.ShowButtons(arg_25_0)
	return
end

function var_0_0.HideButtons(arg_26_0)
	return
end

function var_0_0.Update(arg_27_0, arg_27_1)
	arg_27_0.data = arg_27_1
end

function var_0_0.UpdateButtons(arg_28_0)
	return
end

function var_0_0.PostUpdateMap(arg_29_0, arg_29_1)
	return
end

function var_0_0.UpdateMapItems(arg_30_0)
	return
end

function var_0_0.RecordTween(arg_31_0, arg_31_1, arg_31_2)
	arg_31_0.tweens[arg_31_1] = arg_31_2
end

function var_0_0.DeleteTween(arg_32_0, arg_32_1)
	local var_32_0 = arg_32_0.tweens[arg_32_1]

	if var_32_0 then
		LeanTween.cancel(var_32_0)

		arg_32_0.tweens[arg_32_1] = nil
	end
end

function var_0_0.TryOpenChapter(arg_33_0, arg_33_1)
	assert(false)
end

return var_0_0
