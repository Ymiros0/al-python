﻿local var_0_0 = class("SpineCellView")

function var_0_0.Ctor(arg_1_0)
	return
end

function var_0_0.InitCellTransform(arg_2_0)
	arg_2_0.tfShip = arg_2_0.tf:Find("ship")
	arg_2_0.tfShadow = arg_2_0.tf:Find("shadow")
end

function var_0_0.GetRotatePivot(arg_3_0)
	return arg_3_0.tfShip
end

function var_0_0.GetAction(arg_4_0)
	return arg_4_0.action
end

function var_0_0.SetAction(arg_5_0, arg_5_1)
	arg_5_0.action = arg_5_1

	if arg_5_0.spineRole then
		arg_5_0.spineRole:SetAction(arg_5_1)
	end
end

function var_0_0.GetSpineRole(arg_6_0)
	return arg_6_0.spineRole
end

function var_0_0.LoadSpine(arg_7_0, arg_7_1, arg_7_2, arg_7_3, arg_7_4)
	if arg_7_0.lastPrefab == arg_7_1 then
		if arg_7_0.spineRole:CheckInited() then
			existCall(arg_7_4)
		end

		return
	end

	arg_7_0.UnloadSpine(arg_7_0)

	arg_7_0.lastPrefab = arg_7_1
	arg_7_0.spineRole = SpineRole.New()

	arg_7_0.spineRole:SetData(arg_7_1, arg_7_3)
	arg_7_0.spineRole:Load(function()
		arg_7_0.spineRole:SetParent(arg_7_0.tfShip)
		arg_7_0.spineRole:SetRaycastTarget(false)
		arg_7_0.spineRole:SetLocalPos(Vector3.zero)

		arg_7_2 = arg_7_2 and arg_7_2 * 0.01 or 1

		arg_7_0.spineRole:SetLocalScale(Vector3(0.4 * arg_7_2, 0.4 * arg_7_2, 1))
		arg_7_0:SetAction(arg_7_0:GetAction())
		existCall(arg_7_4)
	end, nil, arg_7_0.spineRole.ORBIT_KEY_SLG)
end

function var_0_0.UnloadSpine(arg_9_0)
	arg_9_0.lastPrefab = nil

	if arg_9_0.spineRole then
		arg_9_0.spineRole:Dispose()

		arg_9_0.spineRole = nil
	end
end

function var_0_0.SetSpineVisible(arg_10_0, arg_10_1)
	if arg_10_0.spineRole then
		arg_10_0.spineRole:SetVisible(arg_10_1)
	end
end

function var_0_0.ClearSpine(arg_11_0)
	arg_11_0.UnloadSpine(arg_11_0)
end

return var_0_0
