local var_0_0 = class("CourtYardPedestalStructure")
local var_0_1 = 0
local var_0_2 = 1
local var_0_3 = 2
local var_0_4 = 3
local var_0_5 = 4

function var_0_0.Ctor(arg_1_0, arg_1_1)
	pg.DelegateInfo.New(arg_1_0)

	arg_1_0.parent = arg_1_1
	arg_1_0.asset = nil
	arg_1_0.level = 0
	arg_1_0.isDirty = false
	arg_1_0.state = var_0_1
end

function var_0_0.GetRect(arg_2_0)
	return arg_2_0.parent:GetView():GetRect()
end

function var_0_0.IsEditModeOrIsVisit(arg_3_0)
	return arg_3_0.parent:GetController():IsEditModeOrIsVisit()
end

function var_0_0.IsEmpty(arg_4_0)
	return arg_4_0.state == var_0_1
end

function var_0_0.IsLoading(arg_5_0)
	return arg_5_0.state == var_0_2
end

function var_0_0.IsLoaded(arg_6_0)
	return arg_6_0.state == var_0_4
end

function var_0_0.IsExit(arg_7_0)
	return arg_7_0.state == var_0_5
end

function var_0_0.IsDirty(arg_8_0)
	return arg_8_0.state == var_0_3
end

function var_0_0.Update(arg_9_0, arg_9_1)
	arg_9_0:UpdateLevel(arg_9_1)

	if arg_9_0:IsEmpty() then
		arg_9_0:Load()
	elseif arg_9_0:IsLoading() then
		arg_9_0:SetDirty()
	elseif arg_9_0:IsLoaded() then
		arg_9_0:ReLoad()
	end
end

function var_0_0.UpdateLevel(arg_10_0, arg_10_1)
	if arg_10_0.level ~= arg_10_1 then
		arg_10_0.isDirty = true
	end

	arg_10_0.level = arg_10_1
end

function var_0_0.Load(arg_11_0, arg_11_1)
	arg_11_0.state = var_0_2

	ResourceMgr.Inst:getAssetAsync(arg_11_0:GetAssetPath(), "", typeof(GameObject), UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_12_0)
		if arg_11_0:IsExit() or IsNil(arg_12_0) then
			return
		end

		if arg_11_0:IsDirty() then
			arg_11_0:ReLoad()

			return
		end

		if arg_11_1 then
			arg_11_1()
		end

		arg_11_0.state = var_0_4

		local var_12_0 = Object.Instantiate(arg_12_0, arg_11_0.parent._tf)

		arg_11_0:OnLoaded(var_12_0)

		arg_11_0.asset = var_12_0
	end), true, true)
end

function var_0_0.SetDirty(arg_13_0)
	if arg_13_0.isDirty then
		arg_13_0.state = var_0_3
	end
end

function var_0_0.ReLoad(arg_14_0)
	arg_14_0:Load(function()
		arg_14_0:Unload()
	end)
end

function var_0_0.Unload(arg_16_0)
	if not IsNil(arg_16_0.asset) then
		Object.Destroy(arg_16_0.asset)
	end

	arg_16_0.asset = nil
	arg_16_0.state = var_0_1
end

function var_0_0.Dispose(arg_17_0)
	pg.DelegateInfo.Dispose(arg_17_0)
	arg_17_0:Unload()

	arg_17_0.state = var_0_5
end

function var_0_0.OnLoaded(arg_18_0)
	return
end

function var_0_0.GetAssetPath(arg_19_0)
	assert(false, "overwrite me !!!")
end

return var_0_0
