local var_0_0 = class("LoadContextCommand", pm.SimpleCommand)

var_0_0.queue = {}

def var_0_0.execute(arg_1_0, arg_1_1):
	arg_1_0.load(arg_1_1.getBody())

def var_0_0.load(arg_2_0, arg_2_1):
	table.insert(var_0_0.queue, arg_2_1)

	if #var_0_0.queue == 1:
		arg_2_0.loadNext()

def var_0_0.loadNext(arg_3_0):
	if #var_0_0.queue > 0:
		local var_3_0 = var_0_0.queue[1]

		local function var_3_1()
			if var_3_0.callback:
				var_3_0.callback()

			table.remove(var_0_0.queue, 1)
			arg_3_0.loadNext()

		if var_3_0.type == LOAD_TYPE_SCENE:
			if var_3_0.isReload:
				arg_3_0.reloadScene(var_3_0.context, var_3_1)
			else
				arg_3_0.loadScene(var_3_0.context, var_3_0.prevContext, var_3_0.isBack, var_3_1)
		elif var_3_0.type == LOAD_TYPE_LAYER:
			arg_3_0.loadLayer(var_3_0.context, var_3_0.parentContext, var_3_0.removeContexts, var_3_1)
		else
			assert(False, "context load type not support. " .. var_3_0.type)

def var_0_0.reloadScene(arg_5_0, arg_5_1, arg_5_2):
	assert(isa(arg_5_1, Context), "should be an instance of Context")

	local var_5_0 = getProxy(ContextProxy)
	local var_5_1 = pg.SceneMgr.GetInstance()
	local var_5_2
	local var_5_3
	local var_5_4 = {}

	seriesAsync({
		function(arg_6_0)
			pg.UIMgr.GetInstance().LoadingOn(arg_5_1.data.showLoading)
			var_5_1.removeLayerMediator(arg_5_0.facade, arg_5_1, function(arg_7_0)
				var_5_2 = arg_7_0

				arg_6_0()),
		function(arg_8_0)
			if var_5_2:
				table.SerialIpairsAsync(var_5_2, function(arg_9_0, arg_9_1, arg_9_2)
					var_5_1.remove(arg_9_1.mediator, function()
						if arg_9_0 == #var_5_2:
							arg_9_1.context.onContextRemoved()

						arg_9_2(), False), arg_8_0)
			else
				arg_8_0(),
		function(arg_11_0)
			if arg_5_1.cleanStack:
				var_5_0.cleanContext()

			var_5_0.pushContext(arg_5_1)
			arg_11_0(),
		function(arg_12_0)
			local var_12_0 = arg_5_1.GetHierarchy()

			_.each(var_12_0, function(arg_13_0)
				pg.PoolMgr.GetInstance().BuildUIPlural(arg_13_0.viewComponent.getUIName()))
			var_5_1.prepare(arg_5_0.facade, arg_5_1, function(arg_14_0)
				arg_5_0.sendNotification(GAME.START_LOAD_SCENE, arg_14_0)

				var_5_3 = arg_14_0

				arg_12_0()),
		function(arg_15_0)
			var_5_1.prepareLayer(arg_5_0.facade, None, arg_5_1, function(arg_16_0)
				arg_5_0.sendNotification(GAME.WILL_LOAD_LAYERS, #arg_16_0)

				var_5_4 = arg_16_0

				arg_15_0()),
		function(arg_17_0)
			var_5_1.enter({
				var_5_3
			}, arg_17_0),
		function(arg_18_0)
			var_5_1.enter(var_5_4, arg_18_0),
		function()
			if arg_5_2:
				arg_5_2()

			pg.UIMgr.GetInstance().LoadingOff()
			arg_5_0.sendNotification(GAME.LOAD_SCENE_DONE, arg_5_1.scene)
	})

def var_0_0.loadScene(arg_20_0, arg_20_1, arg_20_2, arg_20_3, arg_20_4):
	assert(isa(arg_20_1, Context), "should be an instance of Context")

	local var_20_0 = getProxy(ContextProxy)
	local var_20_1 = pg.SceneMgr.GetInstance()
	local var_20_2
	local var_20_3
	local var_20_4 = {}
	local var_20_5 = arg_20_3 and arg_20_2 or None

	seriesAsync({
		function(arg_21_0)
			pg.UIMgr.GetInstance().LoadingOn(arg_20_1.data.showLoading)

			if arg_20_2 != None:
				arg_20_1.extendData({
					fromMediatorName = arg_20_2.mediator.__cname
				})
				var_20_1.removeLayerMediator(arg_20_0.facade, arg_20_2, function(arg_22_0)
					var_20_2 = arg_22_0

					arg_21_0())
			else
				arg_21_0(),
		function(arg_23_0)
			if arg_20_1.cleanStack:
				var_20_0.cleanContext()

			var_20_0.pushContext(arg_20_1)
			arg_23_0(),
		function(arg_24_0)
			local var_24_0 = arg_20_1.GetHierarchy()

			_.each(var_24_0, function(arg_25_0)
				pg.PoolMgr.GetInstance().BuildUIPlural(arg_25_0.viewComponent.getUIName()))
			var_20_1.prepare(arg_20_0.facade, arg_20_1, function(arg_26_0)
				arg_20_0.sendNotification(GAME.START_LOAD_SCENE, arg_26_0)

				var_20_3 = arg_26_0

				arg_24_0()),
		function(arg_27_0)
			var_20_1.prepareLayer(arg_20_0.facade, None, arg_20_1, function(arg_28_0)
				arg_20_0.sendNotification(GAME.WILL_LOAD_LAYERS, #arg_28_0)

				var_20_4 = arg_28_0

				arg_27_0()),
		function(arg_29_0)
			if var_20_2:
				table.SerialIpairsAsync(var_20_2, function(arg_30_0, arg_30_1, arg_30_2)
					local var_30_0 = False

					if var_20_5:
						var_30_0 = var_20_5.mediator.__cname == arg_30_1.mediator.__cname

						if var_30_0:
							var_20_1.clearTempCache(arg_30_1.mediator)

					var_20_1.remove(arg_30_1.mediator, function()
						if arg_30_0 == #var_20_2:
							arg_30_1.context.onContextRemoved()

						arg_30_2(), var_30_0), arg_29_0)
			else
				arg_29_0(),
		function(arg_32_0)
			var_20_1.enter({
				var_20_3
			}, arg_32_0),
		function(arg_33_0)
			var_20_1.enter(var_20_4, arg_33_0),
		function()
			if arg_20_4:
				arg_20_4()

			pg.UIMgr.GetInstance().LoadingOff()
			arg_20_0.sendNotification(GAME.LOAD_SCENE_DONE, arg_20_1.scene)
	})

def var_0_0.loadLayer(arg_35_0, arg_35_1, arg_35_2, arg_35_3, arg_35_4):
	assert(isa(arg_35_1, Context), "should be an instance of Context")

	local var_35_0 = pg.SceneMgr.GetInstance()
	local var_35_1 = {}
	local var_35_2

	seriesAsync({
		function(arg_36_0)
			pg.UIMgr.GetInstance().LoadingOn(arg_35_1.data.showLoading)

			if arg_35_3 != None:
				table.ParallelIpairsAsync(arg_35_3, function(arg_37_0, arg_37_1, arg_37_2)
					var_35_0.removeLayerMediator(arg_35_0.facade, arg_37_1, function(arg_38_0)
						var_35_2 = var_35_2 or {}

						table.insertto(var_35_2, arg_38_0)
						arg_37_2()), arg_36_0)
			else
				arg_36_0(),
		function(arg_39_0)
			local var_39_0 = arg_35_1.GetHierarchy()

			_.each(var_39_0, function(arg_40_0)
				pg.PoolMgr.GetInstance().BuildUIPlural(arg_40_0.viewComponent.getUIName()))
			var_35_0.prepareLayer(arg_35_0.facade, arg_35_2, arg_35_1, function(arg_41_0)
				for iter_41_0, iter_41_1 in ipairs(arg_41_0):
					table.insert(var_35_1, iter_41_1)

				arg_39_0()),
		function(arg_42_0)
			if var_35_2:
				table.SerialIpairsAsync(var_35_2, function(arg_43_0, arg_43_1, arg_43_2)
					var_35_0.remove(arg_43_1.mediator, function()
						arg_43_1.context.onContextRemoved()
						arg_43_2()), arg_42_0)
			else
				arg_42_0(),
		function(arg_45_0)
			arg_35_0.sendNotification(GAME.WILL_LOAD_LAYERS, #var_35_1)
			var_35_0.enter(var_35_1, arg_45_0),
		function()
			if arg_35_4:
				arg_35_4()

			pg.UIMgr.GetInstance().LoadingOff()
			arg_35_0.sendNotification(GAME.LOAD_LAYER_DONE, arg_35_1)
	})

def var_0_0.LoadLayerOnTopContext(arg_47_0):
	local var_47_0 = getProxy(ContextProxy).getCurrentContext()

	pg.m02.sendNotification(GAME.LOAD_LAYERS, {
		parentContext = var_47_0,
		context = arg_47_0
	})

def var_0_0.RemoveLayerByMediator(arg_48_0):
	local var_48_0 = getProxy(ContextProxy).getCurrentContext().getContextByMediator(arg_48_0)

	if var_48_0:
		pg.m02.sendNotification(GAME.REMOVE_LAYERS, {
			context = var_48_0
		})

		return True

return var_0_0
