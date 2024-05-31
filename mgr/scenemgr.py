pg = pg or {}

local var_0_0 = pg

var_0_0.SceneMgr = singletonClass("SceneMgr")

local var_0_1 = var_0_0.SceneMgr

def var_0_1.Ctor(arg_1_0):
	arg_1_0._cacheUI = {}
	arg_1_0._gcLimit = 3
	arg_1_0._gcCounter = 0

def var_0_1.prepare(arg_2_0, arg_2_1, arg_2_2, arg_2_3):
	local var_2_0 = arg_2_2.mediator
	local var_2_1 = arg_2_2.viewComponent
	local var_2_2
	local var_2_3

	if arg_2_0._cacheUI[var_2_0.__cname] != None:
		var_2_3 = arg_2_0._cacheUI[var_2_0.__cname]
		arg_2_0._cacheUI[var_2_0.__cname] = None
		var_2_2 = var_2_0.New(var_2_3)

		var_2_2.setContextData(arg_2_2.data)
		arg_2_1.registerMediator(var_2_2)
		arg_2_3(var_2_2)
	else
		var_2_3 = var_2_1.New()

		assert(isa(var_2_3, BaseUI), "should be an instance of BaseUI. " .. var_2_3.__cname)
		var_2_3.setContextData(arg_2_2.data)

		local var_2_4

		local function var_2_5()
			var_2_3.event.disconnect(BaseUI.LOADED, var_2_5)

			var_2_2 = var_2_0.New(var_2_3)

			var_2_2.setContextData(arg_2_2.data)
			arg_2_1.registerMediator(var_2_2)
			arg_2_3(var_2_2)

		if var_2_3.isLoaded():
			var_2_5()
		else
			var_2_3.event.connect(BaseUI.LOADED, var_2_5)
			var_2_3.load()

def var_0_1.prepareLayer(arg_4_0, arg_4_1, arg_4_2, arg_4_3, arg_4_4):
	local var_4_0 = {}
	local var_4_1 = {}

	if arg_4_2 != None:
		if arg_4_2.getContextByMediator(arg_4_3.mediator):
			originalPrint("mediator already exist. " .. arg_4_3.mediator.__cname)
			arg_4_4(var_4_1)

			return

		table.insert(var_4_0, arg_4_3)
		arg_4_2.addChild(arg_4_3)
	else
		for iter_4_0, iter_4_1 in ipairs(arg_4_3.children):
			table.insert(var_4_0, iter_4_1)

	local var_4_2

	local function var_4_3()
		if #var_4_0 > 0:
			local var_5_0 = table.remove(var_4_0, 1)

			for iter_5_0, iter_5_1 in ipairs(var_5_0.children):
				table.insert(var_4_0, iter_5_1)

			local var_5_1 = var_5_0.parent
			local var_5_2 = arg_4_1.retrieveMediator(var_5_1.mediator.__cname).getViewComponent()

			arg_4_0.prepare(arg_4_1, var_5_0, function(arg_6_0)
				arg_6_0.viewComponent.attach(var_5_2)
				table.insert(var_4_1, arg_6_0)
				var_4_3())
		else
			arg_4_4(var_4_1)

	var_4_3()

def var_0_1.enter(arg_7_0, arg_7_1, arg_7_2):
	if #arg_7_1 == 0:
		arg_7_2()

	local var_7_0 = #arg_7_1

	for iter_7_0, iter_7_1 in ipairs(arg_7_1):
		local var_7_1 = iter_7_1.viewComponent

		if var_7_1._isCachedView:
			var_7_1.setVisible(True)

		local var_7_2

		local function var_7_3()
			var_7_1.event.disconnect(BaseUI.AVALIBLE, var_7_3)

			var_7_0 = var_7_0 - 1

			if var_7_0 == 0:
				arg_7_2()

		var_7_1.event.connect(BaseUI.AVALIBLE, var_7_3)
		var_7_1.enter()

def var_0_1.removeLayer(arg_9_0, arg_9_1, arg_9_2, arg_9_3):
	local var_9_0 = {
		arg_9_2
	}
	local var_9_1 = {}

	while #var_9_0 > 0:
		local var_9_2 = table.remove(var_9_0, 1)

		if var_9_2.mediator:
			table.insert(var_9_1, var_9_2)

		for iter_9_0, iter_9_1 in ipairs(var_9_2.children):
			table.insert(var_9_0, iter_9_1)

	if arg_9_2.parent == None:
		table.remove(var_9_1, 1)
	else
		arg_9_2.parent.removeChild(arg_9_2)

	local var_9_3 = {}

	for iter_9_2 = #var_9_1, 1, -1:
		local var_9_4 = var_9_1[iter_9_2]
		local var_9_5 = arg_9_1.removeMediator(var_9_4.mediator.__cname)

		table.insert(var_9_3, function(arg_10_0)
			if var_9_5:
				arg_9_0.clearTempCache(var_9_5)
				arg_9_0.remove(var_9_5, function()
					var_9_4.onContextRemoved()
					arg_10_0())
			else
				arg_10_0())

	seriesAsync(var_9_3, arg_9_3)

def var_0_1.removeLayerMediator(arg_12_0, arg_12_1, arg_12_2, arg_12_3):
	local var_12_0 = {
		arg_12_2
	}
	local var_12_1 = {}

	while #var_12_0 > 0:
		local var_12_2 = table.remove(var_12_0, 1)

		if var_12_2.mediator:
			table.insert(var_12_1, var_12_2)

		for iter_12_0, iter_12_1 in ipairs(var_12_2.children):
			table.insert(var_12_0, iter_12_1)

	if arg_12_2.parent != None:
		arg_12_2.parent.removeChild(arg_12_2)

	local var_12_3 = {}

	for iter_12_2 = #var_12_1, 1, -1:
		local var_12_4 = var_12_1[iter_12_2]
		local var_12_5 = arg_12_1.removeMediator(var_12_4.mediator.__cname)

		if var_12_5:
			table.insert(var_12_3, {
				mediator = var_12_5,
				context = var_12_4
			})

	arg_12_3(var_12_3)

def var_0_1.clearTempCache(arg_13_0, arg_13_1):
	local var_13_0 = arg_13_1.getViewComponent()

	if var_13_0.tempCache():
		var_13_0.RemoveTempCache()

def var_0_1.remove(arg_14_0, arg_14_1, arg_14_2, arg_14_3):
	local var_14_0 = arg_14_1.getViewComponent()
	local var_14_1 = arg_14_0._cacheUI[arg_14_1.__cname]

	if var_14_1 != None and var_14_1 != var_14_0:
		var_14_1.event.clear()
		arg_14_0.gc(var_14_1)

	if var_14_0 == None:
		arg_14_2()
	elif var_14_0.needCache() and not arg_14_3:
		var_14_0.setVisible(False)

		arg_14_0._cacheUI[arg_14_1.__cname] = var_14_0
		var_14_0._isCachedView = True

		arg_14_2()
	else
		var_14_0._isCachedView = False

		var_14_0.event.connect(BaseUI.DID_EXIT, function()
			var_14_0.event.clear()
			arg_14_0.gc(var_14_0)
			arg_14_2())
		var_14_0.exit()

def var_0_1.gc(arg_16_0, arg_16_1):
	local var_16_0 = arg_16_1.forceGC()

	table.clear(arg_16_1)

	arg_16_1.exited = True

	if not GCThread.GetInstance().running:
		arg_16_0._gcCounter = arg_16_0._gcCounter + 1

		if arg_16_0._gcCounter >= arg_16_0._gcLimit or var_16_0:
			arg_16_0._gcCounter = 0

			gcAll(False)
		else
			GCThread.GetInstance().LuaGC(False)
