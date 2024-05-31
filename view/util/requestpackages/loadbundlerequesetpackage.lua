local var_0_0 = class("LoadBundleRequesetPackage", import(".RequestPackage"))

function var_0_0.__call(arg_1_0)
	if arg_1_0.stopped then
		return
	end

	seriesAsync({
		function(arg_2_0)
			pg.UIMgr.GetInstance():LoadingOn()

			local var_2_0 = arg_1_0.path

			xpcall(function()
				buildTempAB(var_2_0, function(arg_4_0)
					pg.UIMgr.GetInstance():LoadingOff()

					if arg_1_0.stopped then
						ResourceMgr.Inst:ClearBundleRef(var_2_0, false, false)

						return
					end

					arg_2_0(arg_4_0)
				end)
			end, function(...)
				debug.traceback(...)
				pg.UIMgr.GetInstance():LoadingOff()
			end)
		end,
		function(arg_6_0, arg_6_1)
			existCall(arg_1_0.onLoaded, arg_6_1)
		end
	})

	return arg_1_0
end

function var_0_0.Ctor(arg_7_0, arg_7_1, arg_7_2)
	arg_7_0.path = arg_7_1
	arg_7_0.onLoaded = arg_7_2
end

return var_0_0
