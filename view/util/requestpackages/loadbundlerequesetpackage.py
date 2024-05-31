local var_0_0 = class("LoadBundleRequesetPackage", import(".RequestPackage"))

def var_0_0.__call(arg_1_0):
	if arg_1_0.stopped:
		return

	seriesAsync({
		function(arg_2_0)
			pg.UIMgr.GetInstance().LoadingOn()

			local var_2_0 = arg_1_0.path

			xpcall(function()
				buildTempAB(var_2_0, function(arg_4_0)
					pg.UIMgr.GetInstance().LoadingOff()

					if arg_1_0.stopped:
						ResourceMgr.Inst.ClearBundleRef(var_2_0, False, False)

						return

					arg_2_0(arg_4_0)), function(...)
				debug.traceback(...)
				pg.UIMgr.GetInstance().LoadingOff()),
		function(arg_6_0, arg_6_1)
			existCall(arg_1_0.onLoaded, arg_6_1)
	})

	return arg_1_0

def var_0_0.Ctor(arg_7_0, arg_7_1, arg_7_2):
	arg_7_0.path = arg_7_1
	arg_7_0.onLoaded = arg_7_2

return var_0_0
