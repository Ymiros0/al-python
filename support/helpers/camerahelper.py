CameraHelper = {}

local var_0_0 = CameraHelper
local var_0_1 = YSTool.YSPermissionTool.Inst

def var_0_0.IsAndroid():
	return getProxy(UserProxy).GetCacheGatewayInServerLogined() == PLATFORM_ANDROID

def var_0_0.IsIOS():
	return getProxy(UserProxy).GetCacheGatewayInServerLogined() == PLATFORM_IPHONEPLAYER

def var_0_0.RequestCamera(arg_3_0, arg_3_1):
	if var_0_0.IsAndroid():
		local var_3_0 = {
			"android.permission.CAMERA",
			"android.permission.RECORD_AUDIO"
		}

		if PathMgr.getOSVersionNum() < 10:
			table.insert(var_3_0, "android.permission.WRITE_EXTERNAL_STORAGE")

		local function var_3_1(arg_4_0, arg_4_1)
			local var_4_0 = True
			local var_4_1 = arg_4_1.Length

			for iter_4_0 = 0, var_4_1 - 1:
				if not arg_4_1[iter_4_0]:
					var_4_0 = False

					break

			if var_4_0:
				if arg_3_0:
					arg_3_0()
			elif arg_3_1:
				arg_3_1()

		var_0_1.RequestMulti(var_3_0, var_3_1)
	elif var_0_0.IsIOS():
		local var_3_2 = "camera"

		local function var_3_3(arg_5_0, arg_5_1)
			if arg_5_1:
				if arg_3_0:
					arg_3_0()
			elif arg_3_1:
				arg_3_1()

		var_0_1.RequestSingle(var_3_2, var_3_3)
	elif arg_3_0:
		arg_3_0()
