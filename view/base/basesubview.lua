local var_0_0 = class("BaseSubView", import("view.base.BaseEventLogic"))

var_0_0.STATES = {
	DESTROY = 5,
	NONE = 1,
	LOADING = 2,
	INITED = 4,
	LOADED = 3
}

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3)
	var_0_0.super.Ctor(arg_1_0, arg_1_2)

	arg_1_0.contextData = arg_1_3
	arg_1_0._parentTf = arg_1_1
	arg_1_0.event = arg_1_2
	arg_1_0._go = nil
	arg_1_0._tf = nil
	arg_1_0._state = var_0_0.STATES.NONE
	arg_1_0._funcQueue = {}
end

function var_0_0.SetExtra(arg_2_0, arg_2_1)
	arg_2_0.extraGameObject = go(arg_2_1)
	arg_2_0._parentTf = arg_2_1.parent
end

function var_0_0.Load(arg_3_0)
	if arg_3_0._state ~= var_0_0.STATES.NONE then
		return
	end

	arg_3_0._state = var_0_0.STATES.LOADING

	pg.UIMgr.GetInstance():LoadingOn()

	local var_3_0 = PoolMgr.GetInstance()

	seriesAsync({
		function(arg_4_0)
			if arg_3_0.extraGameObject then
				arg_4_0(arg_3_0.extraGameObject)
			else
				var_3_0:GetUI(arg_3_0:getUIName(), true, arg_4_0)
			end
		end
	}, function(arg_5_0)
		if arg_3_0._state == var_0_0.STATES.DESTROY and arg_3_0:getUIName() then
			pg.UIMgr.GetInstance():LoadingOff()
			var_3_0:ReturnUI(arg_3_0:getUIName(), arg_5_0)
		else
			arg_3_0:Loaded(arg_5_0)
			arg_3_0:Init()
		end
	end)
end

function var_0_0.Loaded(arg_6_0, arg_6_1)
	pg.UIMgr.GetInstance():LoadingOff()

	if arg_6_0._state ~= var_0_0.STATES.LOADING then
		return
	end

	arg_6_0._state = var_0_0.STATES.LOADED
	arg_6_0._go = arg_6_1
	arg_6_0._tf = tf(arg_6_1)

	setActiveViaLayer(arg_6_0._tf, true)
	pg.DelegateInfo.New(arg_6_0)
	SetParent(arg_6_0._tf, arg_6_0._parentTf, false)
	arg_6_0:OnLoaded()
end

function var_0_0.Init(arg_7_0)
	if arg_7_0._state ~= var_0_0.STATES.LOADED then
		return
	end

	arg_7_0._state = var_0_0.STATES.INITED

	arg_7_0:OnInit()
	arg_7_0:HandleFuncQueue()
end

function var_0_0.Destroy(arg_8_0)
	if arg_8_0._state == var_0_0.STATES.DESTROY then
		return
	end

	if not arg_8_0:GetLoaded() then
		arg_8_0._state = var_0_0.STATES.DESTROY

		return
	end

	arg_8_0._state = var_0_0.STATES.DESTROY

	pg.DelegateInfo.Dispose(arg_8_0)
	arg_8_0:OnDestroy()
	arg_8_0:disposeEvent()
	arg_8_0:cleanManagedTween()

	arg_8_0._tf = nil

	local var_8_0 = arg_8_0:getUIName()

	if arg_8_0._go ~= nil and var_8_0 then
		PoolMgr.GetInstance():ReturnUI(var_8_0, arg_8_0._go)

		arg_8_0._go = nil
	end
end

function var_0_0.HandleFuncQueue(arg_9_0)
	if arg_9_0._state == var_0_0.STATES.INITED then
		while #arg_9_0._funcQueue > 0 do
			local var_9_0 = table.remove(arg_9_0._funcQueue, 1)

			var_9_0.func(unpack(var_9_0.params, 1, var_9_0.params.len))
		end
	end
end

function var_0_0.Reset(arg_10_0)
	arg_10_0._state = var_0_0.STATES.NONE
end

function var_0_0.ActionInvoke(arg_11_0, arg_11_1, ...)
	assert(arg_11_0[arg_11_1], "func not exist >>>" .. arg_11_1)

	arg_11_0._funcQueue[#arg_11_0._funcQueue + 1] = {
		funcName = arg_11_1,
		func = arg_11_0[arg_11_1],
		params = {
			len = 1 + select("#", ...),
			arg_11_0,
			...
		}
	}

	arg_11_0:HandleFuncQueue()
end

function var_0_0.CallbackInvoke(arg_12_0, arg_12_1, ...)
	arg_12_0._funcQueue[#arg_12_0._funcQueue + 1] = {
		func = arg_12_1,
		params = packEx(...)
	}

	arg_12_0:HandleFuncQueue()
end

function var_0_0.ExecuteAction(arg_13_0, arg_13_1, ...)
	arg_13_0:Load()
	arg_13_0:ActionInvoke(arg_13_1, ...)
end

function var_0_0.GetLoaded(arg_14_0)
	return arg_14_0._state >= var_0_0.STATES.LOADED
end

function var_0_0.CheckState(arg_15_0, arg_15_1)
	return arg_15_0._state == arg_15_1
end

function var_0_0.Show(arg_16_0)
	setActive(arg_16_0._tf, true)
	arg_16_0:ShowOrHideResUI(true)
	arg_16_0:PlayBGM()
end

function var_0_0.Hide(arg_17_0)
	setActive(arg_17_0._tf, false)
	arg_17_0:ShowOrHideResUI(false)
	arg_17_0:StopBgm()
end

function var_0_0.isShowing(arg_18_0)
	return arg_18_0._tf and isActive(arg_18_0._tf)
end

function var_0_0.getBGM(arg_19_0, arg_19_1)
	return getBgm(arg_19_1 or arg_19_0.__cname)
end

function var_0_0.PlayBGM(arg_20_0)
	local var_20_0 = arg_20_0:getBGM()

	if var_20_0 then
		pg.BgmMgr.GetInstance():Push(arg_20_0.__cname, var_20_0)
	end
end

function var_0_0.StopBgm(arg_21_0)
	pg.BgmMgr.GetInstance():Pop(arg_21_0.__cname)
end

function var_0_0.findTF(arg_22_0, arg_22_1, arg_22_2)
	assert(arg_22_0._tf, "transform should exist")

	return findTF(arg_22_2 or arg_22_0._tf, arg_22_1)
end

function var_0_0.getTpl(arg_23_0, arg_23_1, arg_23_2)
	local var_23_0 = arg_23_0:findTF(arg_23_1, arg_23_2)

	var_23_0:SetParent(arg_23_0._tf, false)
	SetActive(var_23_0, false)

	return var_23_0
end

function var_0_0.getUIName(arg_24_0)
	return nil
end

function var_0_0.OnLoaded(arg_25_0)
	return
end

function var_0_0.OnInit(arg_26_0)
	return
end

function var_0_0.OnDestroy(arg_27_0)
	return
end

function var_0_0.ResUISettings(arg_28_0)
	return nil
end

function var_0_0.ShowOrHideResUI(arg_29_0, arg_29_1)
	local var_29_0 = arg_29_0:ResUISettings()

	if not var_29_0 then
		return
	end

	if var_29_0 == true then
		var_29_0 = {
			anim = true,
			showType = PlayerResUI.TYPE_ALL
		}
	end

	pg.playerResUI:SetActive(setmetatable({
		active = arg_29_1,
		weight = var_29_0.weight,
		groupName = var_29_0.groupName,
		canvasOrder = var_29_0.order or false
	}, {
		__index = var_29_0
	}))
end

return var_0_0
