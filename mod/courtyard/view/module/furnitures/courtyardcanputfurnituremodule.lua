﻿local var_0_0 = class("CourtYardCanPutFurnitureModule", import(".CourtYardFurnitureModule"))
local var_0_1 = false

function var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2)
	var_0_0.super.Ctor(arg_1_0, arg_1_1, arg_1_2)

	arg_1_0.childModules = {}
end

function var_0_0.OnInit(arg_2_0)
	var_0_0.super.OnInit(arg_2_0)

	if var_0_1 then
		arg_2_0.mapDebug = CourtYardMapDebug.New(arg_2_0.data.placeableArea, Color.New(1, 0, 0))
		GetOrAddComponent(arg_2_0:GetParentTF(), typeof(CanvasGroup)).alpha = 0.3
	end

	arg_2_0:RefreshDepth()
end

function var_0_0.AddChild(arg_3_0, arg_3_1)
	arg_3_0:CancelPuddingAnim()
	arg_3_1:CancelPuddingAnim()

	local var_3_0 = arg_3_1.data:GetDeathType() .. arg_3_1.data.id

	arg_3_0.childModules[var_3_0] = arg_3_1

	arg_3_1._tf:SetParent(arg_3_0.childsTF)
end

function var_0_0.RemoveChild(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_1.data:GetDeathType() .. arg_4_1.data.id

	arg_4_0.childModules[var_4_0] = nil

	arg_4_1._tf:SetParent(arg_4_0:GetParentTF())
end

function var_0_0.AddListeners(arg_5_0)
	var_0_0.super.AddListeners(arg_5_0)
	arg_5_0:AddAreaListener(CourtYardEvent.REMOVE_ITEM, arg_5_0.OnRemoveItem)
	arg_5_0:AddAreaListener(CourtYardEvent.ADD_ITEM, arg_5_0.OnAddItem)
end

function var_0_0.RemoveListeners(arg_6_0)
	var_0_0.super.RemoveListeners(arg_6_0)
	arg_6_0:RemoveAreaListener(CourtYardEvent.REMOVE_ITEM, arg_6_0.OnRemoveItem)
	arg_6_0:RemoveAreaListener(CourtYardEvent.ADD_ITEM, arg_6_0.OnAddItem)
end

function var_0_0.AddAreaListener(arg_7_0, arg_7_1, arg_7_2)
	local function var_7_0(arg_8_0, arg_8_1, ...)
		arg_7_2(arg_7_0, ...)
	end

	arg_7_0.callbacks[arg_7_2] = var_7_0

	arg_7_0.data.placeableArea:AddListener(arg_7_1, var_7_0)
end

function var_0_0.RemoveAreaListener(arg_9_0, arg_9_1, arg_9_2)
	local var_9_0 = arg_9_0.callbacks[arg_9_2]

	if var_9_0 then
		arg_9_0.data.placeableArea:RemoveListener(arg_9_1, var_9_0)

		arg_9_0.callbacks[var_9_0] = nil
	end
end

function var_0_0.OnRemoveItem(arg_10_0, arg_10_1)
	local var_10_0 = arg_10_1:GetDeathType() .. arg_10_1.id

	arg_10_0.childModules[var_10_0]._tf:SetParent(arg_10_0:GetParentTF())

	if var_0_1 then
		arg_10_0.mapDebug:Flush()
	end
end

function var_0_0.OnAddItem(arg_11_0, arg_11_1)
	local var_11_0 = arg_11_1:GetDeathType() .. arg_11_1.id
	local var_11_1 = arg_11_0.childModules[var_11_0]

	var_11_1._tf:SetParent(arg_11_0.childsTF)

	local var_11_2 = arg_11_1:GetOffset()

	var_11_1._tf.localPosition = var_11_1._tf.localPosition + var_11_2

	arg_11_0:RefreshDepth()

	if var_0_1 then
		arg_11_0.mapDebug:Flush()
	end
end

function var_0_0.RefreshDepth(arg_12_0)
	for iter_12_0, iter_12_1 in ipairs(arg_12_0.data.placeableArea:GetItems()) do
		local var_12_0 = iter_12_1:GetDeathType() .. iter_12_1.id

		arg_12_0.childModules[var_12_0]:SetSiblingIndex(iter_12_0 - 1)
	end
end

function var_0_0.BlocksRaycasts(arg_13_0, arg_13_1)
	local var_13_0 = arg_13_0.data:CanClickWhenExitEditMode()
	local var_13_1 = #arg_13_0.data:GetUsingSlots() > 0 or table.getCount(arg_13_0.childModules) > 0

	if (var_13_0 or var_13_1) and arg_13_1 == false then
		return
	end

	arg_13_0.cg.blocksRaycasts = arg_13_1
end

function var_0_0.Dispose(arg_14_0)
	var_0_0.super.Dispose(arg_14_0)

	if var_0_1 then
		arg_14_0.mapDebug:Dispose()

		GetOrAddComponent(arg_14_0:GetParentTF(), typeof(CanvasGroup)).alpha = 1
	end
end

return var_0_0
