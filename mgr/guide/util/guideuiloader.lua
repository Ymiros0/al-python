local var_0_0 = class("GuideUILoader")

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.root = arg_1_1
	arg_1_0.caches = {}
end

function var_0_0.Load(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0:LoadRes(arg_2_1, arg_2_2)
end

function var_0_0.LoadHighLightArea(arg_3_0, arg_3_1)
	local var_3_0 = arg_3_1.isWorld and "wShowArea" or "wShowArea1"

	arg_3_0:Load(var_3_0, function(arg_4_0)
		if not arg_3_1 then
			return
		end

		arg_4_0.sizeDelta = arg_3_1.sizeDelta
		arg_4_0.pivot = arg_3_1.pivot
		arg_4_0.localPosition = arg_3_1.position
	end)
end

function var_0_0.LoadRes(arg_5_0, arg_5_1, arg_5_2)
	ResourceMgr.Inst:getAssetAsync("guideitem/" .. arg_5_1, "", UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_6_0)
		if IsNil(arg_6_0) then
			return
		end

		local var_6_0 = Object.Instantiate(arg_6_0, arg_5_0.root).transform

		table.insert(arg_5_0.caches, var_6_0)

		if arg_5_2 then
			arg_5_2(var_6_0)
		end
	end), true, true)
end

function var_0_0.Clear(arg_7_0)
	if arg_7_0.caches and #arg_7_0.caches > 0 then
		for iter_7_0, iter_7_1 in ipairs(arg_7_0.caches) do
			Object.Destroy(iter_7_1.gameObject)
		end

		arg_7_0.caches = {}
	end
end

return var_0_0
