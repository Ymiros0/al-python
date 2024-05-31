local var_0_0 = class("BaseSubPanel", import("view.base.BaseSubView"))
local var_0_1 = import("view.util.FuncBuffer")
local var_0_2 = import("view.util.AutoLoader")

function var_0_0.Ctor(arg_1_0, arg_1_1)
	assert(arg_1_1, "NIL Parent View")

	local var_1_0 = arg_1_1 and arg_1_1._tf
	local var_1_1 = arg_1_1 and isa(arg_1_1, BaseEventLogic) and arg_1_1.event or nil
	local var_1_2 = {}

	var_0_0.super.Ctor(arg_1_0, var_1_0, var_1_1, var_1_2)

	arg_1_0.buffer = var_0_1.New()
	arg_1_0.loader = var_0_2.New()
	arg_1_0.viewParent = arg_1_1
end

function var_0_0.InvokeParent(arg_2_0, arg_2_1, ...)
	if arg_2_0.viewParent then
		arg_2_0.viewParent[arg_2_1](arg_2_0.viewParent, ...)
	end
end

function var_0_0.Init(arg_3_0)
	if arg_3_0._state ~= var_0_0.STATES.LOADED then
		return
	end

	arg_3_0._state = var_0_0.STATES.INITED

	arg_3_0:OnInit()
	arg_3_0:Show()
	arg_3_0:HandleFuncQueue()
	arg_3_0.buffer:SetNotifier(arg_3_0)
	arg_3_0.buffer:ExcuteAll()
end

function var_0_0.Destroy(arg_4_0)
	if arg_4_0._state == var_0_0.STATES.DESTROY then
		return
	end

	if not arg_4_0:GetLoaded() then
		arg_4_0._state = var_0_0.STATES.DESTROY

		return
	end

	arg_4_0._state = var_0_0.STATES.DESTROY

	pg.DelegateInfo.Dispose(arg_4_0)
	arg_4_0:Hide()
	arg_4_0:OnDestroy()
	arg_4_0.loader:Clear()
	arg_4_0.buffer:Clear()
	arg_4_0:disposeEvent()
	arg_4_0:cleanManagedTween()

	arg_4_0._tf = nil

	local var_4_0 = PoolMgr.GetInstance()
	local var_4_1 = arg_4_0:getUIName()

	if arg_4_0._go ~= nil and var_4_1 then
		var_4_0:ReturnUI(var_4_1, arg_4_0._go)

		arg_4_0._go = nil
	end
end

function var_0_0.Hide(arg_5_0)
	arg_5_0:OnHide()
	var_0_0.super.Hide(arg_5_0)
end

function var_0_0.RawHide(arg_6_0)
	var_0_0.super.Hide(arg_6_0)
end

function var_0_0.Show(arg_7_0)
	var_0_0.super.Show(arg_7_0)
	arg_7_0:OnShow()
end

function var_0_0.RawShow(arg_8_0)
	var_0_0.super.Show(arg_8_0)
end

function var_0_0.IsShowing(arg_9_0)
	return arg_9_0:GetLoaded() and isActive(arg_9_0._go)
end

function var_0_0.IsHiding(arg_10_0)
	return arg_10_0:GetLoaded() and not isActive(arg_10_0._go)
end

function var_0_0.SetParent(arg_11_0, arg_11_1, ...)
	setParent(arg_11_0._tf, arg_11_1, ...)
end

function var_0_0.OnShow(arg_12_0)
	return
end

function var_0_0.OnHide(arg_13_0)
	return
end

return var_0_0
