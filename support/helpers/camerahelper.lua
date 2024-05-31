CameraHelper = {}

local var_0_0 = CameraHelper
local var_0_1 = YSTool.YSPermissionTool.Inst

function var_0_0.IsAndroid()
	return getProxy(UserProxy):GetCacheGatewayInServerLogined() == PLATFORM_ANDROID
end

function var_0_0.IsIOS()
	return getProxy(UserProxy):GetCacheGatewayInServerLogined() == PLATFORM_IPHONEPLAYER
end

function var_0_0.RequestCamera(arg_3_0, arg_3_1)
	if var_0_0.IsAndroid() then
		local var_3_0 = {
			"android.permission.CAMERA",
			"android.permission.RECORD_AUDIO"
		}

		if PathMgr.getOSVersionNum() < 10 then
			table.insert(var_3_0, "android.permission.WRITE_EXTERNAL_STORAGE")
		end

		local function var_3_1(arg_4_0, arg_4_1)
			local var_4_0 = true
			local var_4_1 = arg_4_1.Length

			for iter_4_0 = 0, var_4_1 - 1 do
				if not arg_4_1[iter_4_0] then
					var_4_0 = false

					break
				end
			end

			if var_4_0 then
				if arg_3_0 then
					arg_3_0()
				end
			elseif arg_3_1 then
				arg_3_1()
			end
		end

		var_0_1:RequestMulti(var_3_0, var_3_1)
	elseif var_0_0.IsIOS() then
		local var_3_2 = "camera"

		local function var_3_3(arg_5_0, arg_5_1)
			if arg_5_1 then
				if arg_3_0 then
					arg_3_0()
				end
			elseif arg_3_1 then
				arg_3_1()
			end
		end

		var_0_1:RequestSingle(var_3_2, var_3_3)
	elseif arg_3_0 then
		arg_3_0()
	end
end
