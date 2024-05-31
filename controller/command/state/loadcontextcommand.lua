local var_0_0 = class("LoadContextCommand", pm.SimpleCommand)

var_0_0.queue = {}

function var_0_0.execute(arg_1_0, arg_1_1)
	arg_1_0:load(arg_1_1:getBody())
end

function var_0_0.load(arg_2_0, arg_2_1)
	table.insert(var_0_0.queue, arg_2_1)

	if #var_0_0.queue == 1 then
		arg_2_0:loadNext()
	end
end

function var_0_0.loadNext(arg_3_0)
	if #var_0_0.queue > 0 then
		local var_3_0 = var_0_0.queue[1]

		local function var_3_1()
			if var_3_0.callback then
				var_3_0.callback()
			end

			table.remove(var_0_0.queue, 1)
			arg_3_0:loadNext()
		end

		if var_3_0.type == LOAD_TYPE_SCENE then
			if var_3_0.isReload then
				arg_3_0:reloadScene(var_3_0.context, var_3_1)
			else
				arg_3_0:loadScene(var_3_0.context, var_3_0.prevContext, var_3_0.isBack, var_3_1)
			end
		elseif var_3_0.type == LOAD_TYPE_LAYER then
			arg_3_0:loadLayer(var_3_0.context, var_3_0.parentContext, var_3_0.removeContexts, var_3_1)
		else
			assert(false, "context load type not support: " .. var_3_0.type)
		end
	end
end

function var_0_0.reloadScene(arg_5_0, arg_5_1, arg_5_2)
	assert(isa(arg_5_1, Context), "should be an instance of Context")

	local var_5_0 = getProxy(ContextProxy)
	local var_5_1 = pg.SceneMgr.GetInstance()
	local var_5_2
	local var_5_3
	local var_5_4 = {}

	seriesAsync({
		function(arg_6_0)
			pg.UIMgr.GetInstance():LoadingOn(arg_5_1.data.showLoading)
			var_5_1:removeLayerMediator(arg_5_0.facade, arg_5_1, function(arg_7_0)
				var_5_2 = arg_7_0

				arg_6_0()
			end)
		end,
		function(arg_8_0)
			if var_5_2 then
				table.SerialIpairsAsync(var_5_2, function(arg_9_0, arg_9_1, arg_9_2)
					var_5_1:remove(arg_9_1.mediator, function()
						if arg_9_0 == #var_5_2 then
							arg_9_1.context:onContextRemoved()
						end

						arg_9_2()
					end, false)
				end, arg_8_0)
			else
				arg_8_0()
			end
		end,
		function(arg_11_0)
			if arg_5_1.cleanStack then
				var_5_0:cleanContext()
			end

			var_5_0:pushContext(arg_5_1)
			arg_11_0()
		end,
		function(arg_12_0)
			local var_12_0 = arg_5_1:GetHierarchy()

			_.each(var_12_0, function(arg_13_0)
				pg.PoolMgr.GetInstance():BuildUIPlural(arg_13_0.viewComponent.getUIName())
			end)
			var_5_1:prepare(arg_5_0.facade, arg_5_1, function(arg_14_0)
				arg_5_0:sendNotification(GAME.START_LOAD_SCENE, arg_14_0)

				var_5_3 = arg_14_0

				arg_12_0()
			end)
		end,
		function(arg_15_0)
			var_5_1:prepareLayer(arg_5_0.facade, nil, arg_5_1, function(arg_16_0)
				arg_5_0:sendNotification(GAME.WILL_LOAD_LAYERS, #arg_16_0)

				var_5_4 = arg_16_0

				arg_15_0()
			end)
		end,
		function(arg_17_0)
			var_5_1:enter({
				var_5_3
			}, arg_17_0)
		end,
		function(arg_18_0)
			var_5_1:enter(var_5_4, arg_18_0)
		end,
		function()
			if arg_5_2 then
				arg_5_2()
			end

			pg.UIMgr.GetInstance():LoadingOff()
			arg_5_0:sendNotification(GAME.LOAD_SCENE_DONE, arg_5_1.scene)
		end
	})
end

function var_0_0.loadScene(arg_20_0, arg_20_1, arg_20_2, arg_20_3, arg_20_4)
	assert(isa(arg_20_1, Context), "should be an instance of Context")

	local var_20_0 = getProxy(ContextProxy)
	local var_20_1 = pg.SceneMgr.GetInstance()
	local var_20_2
	local var_20_3
	local var_20_4 = {}
	local var_20_5 = arg_20_3 and arg_20_2 or nil

	seriesAsync({
		function(arg_21_0)
			pg.UIMgr.GetInstance():LoadingOn(arg_20_1.data.showLoading)

			if arg_20_2 ~= nil then
				arg_20_1:extendData({
					fromMediatorName = arg_20_2.mediator.__cname
				})
				var_20_1:removeLayerMediator(arg_20_0.facade, arg_20_2, function(arg_22_0)
					var_20_2 = arg_22_0

					arg_21_0()
				end)
			else
				arg_21_0()
			end
		end,
		function(arg_23_0)
			if arg_20_1.cleanStack then
				var_20_0:cleanContext()
			end

			var_20_0:pushContext(arg_20_1)
			arg_23_0()
		end,
		function(arg_24_0)
			local var_24_0 = arg_20_1:GetHierarchy()

			_.each(var_24_0, function(arg_25_0)
				pg.PoolMgr.GetInstance():BuildUIPlural(arg_25_0.viewComponent.getUIName())
			end)
			var_20_1:prepare(arg_20_0.facade, arg_20_1, function(arg_26_0)
				arg_20_0:sendNotification(GAME.START_LOAD_SCENE, arg_26_0)

				var_20_3 = arg_26_0

				arg_24_0()
			end)
		end,
		function(arg_27_0)
			var_20_1:prepareLayer(arg_20_0.facade, nil, arg_20_1, function(arg_28_0)
				arg_20_0:sendNotification(GAME.WILL_LOAD_LAYERS, #arg_28_0)

				var_20_4 = arg_28_0

				arg_27_0()
			end)
		end,
		function(arg_29_0)
			if var_20_2 then
				table.SerialIpairsAsync(var_20_2, function(arg_30_0, arg_30_1, arg_30_2)
					local var_30_0 = false

					if var_20_5 then
						var_30_0 = var_20_5.mediator.__cname == arg_30_1.mediator.__cname

						if var_30_0 then
							var_20_1:clearTempCache(arg_30_1.mediator)
						end
					end

					var_20_1:remove(arg_30_1.mediator, function()
						if arg_30_0 == #var_20_2 then
							arg_30_1.context:onContextRemoved()
						end

						arg_30_2()
					end, var_30_0)
				end, arg_29_0)
			else
				arg_29_0()
			end
		end,
		function(arg_32_0)
			var_20_1:enter({
				var_20_3
			}, arg_32_0)
		end,
		function(arg_33_0)
			var_20_1:enter(var_20_4, arg_33_0)
		end,
		function()
			if arg_20_4 then
				arg_20_4()
			end

			pg.UIMgr.GetInstance():LoadingOff()
			arg_20_0:sendNotification(GAME.LOAD_SCENE_DONE, arg_20_1.scene)
		end
	})
end

function var_0_0.loadLayer(arg_35_0, arg_35_1, arg_35_2, arg_35_3, arg_35_4)
	assert(isa(arg_35_1, Context), "should be an instance of Context")

	local var_35_0 = pg.SceneMgr.GetInstance()
	local var_35_1 = {}
	local var_35_2

	seriesAsync({
		function(arg_36_0)
			pg.UIMgr.GetInstance():LoadingOn(arg_35_1.data.showLoading)

			if arg_35_3 ~= nil then
				table.ParallelIpairsAsync(arg_35_3, function(arg_37_0, arg_37_1, arg_37_2)
					var_35_0:removeLayerMediator(arg_35_0.facade, arg_37_1, function(arg_38_0)
						var_35_2 = var_35_2 or {}

						table.insertto(var_35_2, arg_38_0)
						arg_37_2()
					end)
				end, arg_36_0)
			else
				arg_36_0()
			end
		end,
		function(arg_39_0)
			local var_39_0 = arg_35_1:GetHierarchy()

			_.each(var_39_0, function(arg_40_0)
				pg.PoolMgr.GetInstance():BuildUIPlural(arg_40_0.viewComponent.getUIName())
			end)
			var_35_0:prepareLayer(arg_35_0.facade, arg_35_2, arg_35_1, function(arg_41_0)
				for iter_41_0, iter_41_1 in ipairs(arg_41_0) do
					table.insert(var_35_1, iter_41_1)
				end

				arg_39_0()
			end)
		end,
		function(arg_42_0)
			if var_35_2 then
				table.SerialIpairsAsync(var_35_2, function(arg_43_0, arg_43_1, arg_43_2)
					var_35_0:remove(arg_43_1.mediator, function()
						arg_43_1.context:onContextRemoved()
						arg_43_2()
					end)
				end, arg_42_0)
			else
				arg_42_0()
			end
		end,
		function(arg_45_0)
			arg_35_0:sendNotification(GAME.WILL_LOAD_LAYERS, #var_35_1)
			var_35_0:enter(var_35_1, arg_45_0)
		end,
		function()
			if arg_35_4 then
				arg_35_4()
			end

			pg.UIMgr.GetInstance():LoadingOff()
			arg_35_0:sendNotification(GAME.LOAD_LAYER_DONE, arg_35_1)
		end
	})
end

function var_0_0.LoadLayerOnTopContext(arg_47_0)
	local var_47_0 = getProxy(ContextProxy):getCurrentContext()

	pg.m02:sendNotification(GAME.LOAD_LAYERS, {
		parentContext = var_47_0,
		context = arg_47_0
	})
end

function var_0_0.RemoveLayerByMediator(arg_48_0)
	local var_48_0 = getProxy(ContextProxy):getCurrentContext():getContextByMediator(arg_48_0)

	if var_48_0 then
		pg.m02:sendNotification(GAME.REMOVE_LAYERS, {
			context = var_48_0
		})

		return true
	end
end

return var_0_0
