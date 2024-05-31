local var_0_0 = class("ContextMediator", pm.Mediator)

def var_0_0.Ctor(arg_1_0, arg_1_1):
	arg_1_0.initNotificationHandleDic()
	var_0_0.super.Ctor(arg_1_0, None, arg_1_1)

def var_0_0.initNotificationHandleDic(arg_2_0):
	arg_2_0.handleDic, arg_2_0.handleElse = None

def var_0_0.listNotificationInterests(arg_3_0):
	if arg_3_0.handleDic:
		return underscore.keys(arg_3_0.handleDic)
	else
		return var_0_0.super.listNotificationInterests(arg_3_0)

def var_0_0.handleNotification(arg_4_0, arg_4_1):
	if arg_4_0.handleDic:
		switch(arg_4_1.getName(), arg_4_0.handleDic, arg_4_0.handleElse, arg_4_0, arg_4_1)
	else
		var_0_0.super.handleNotification(arg_4_0, arg_4_1)

def var_0_0.onRegister(arg_5_0):
	arg_5_0.event = {}

	arg_5_0.bind(BaseUI.ON_BACK_PRESSED, function(arg_6_0, arg_6_1)
		arg_5_0.onBackPressed(arg_6_1))
	arg_5_0.bind(BaseUI.AVALIBLE, function(arg_7_0, arg_7_1)
		arg_5_0.onUIAvalible())
	arg_5_0.bind(BaseUI.ON_BACK, function(arg_8_0, arg_8_1, arg_8_2)
		if arg_8_2 and arg_8_2 > 0:
			pg.UIMgr.GetInstance().LoadingOn(False)
			LeanTween.delayedCall(arg_8_2, System.Action(function()
				pg.UIMgr.GetInstance().LoadingOff()
				arg_5_0.sendNotification(GAME.GO_BACK, None, arg_8_1)))
		else
			arg_5_0.sendNotification(GAME.GO_BACK, None, arg_8_1))
	arg_5_0.bind(BaseUI.ON_RETURN, function(arg_10_0, arg_10_1)
		arg_5_0.sendNotification(GAME.GO_BACK, arg_10_1))
	arg_5_0.bind(BaseUI.ON_HOME, function(arg_11_0)
		local var_11_0 = getProxy(ContextProxy).getCurrentContext()

		if var_11_0.mediator == NewMainMediator:
			for iter_11_0 = #var_11_0.children, 1, -1:
				local var_11_1 = var_11_0.children[iter_11_0]

				arg_5_0.sendNotification(GAME.REMOVE_LAYERS, {
					context = var_11_1
				})

			return

		local var_11_2 = var_11_0.retriveLastChild()

		if var_11_2 and var_11_2 != var_11_0:
			arg_5_0.sendNotification(GAME.REMOVE_LAYERS, {
				onHome = True,
				context = var_11_2
			})

		arg_5_0.sendNotification(GAME.GO_SCENE, SCENE.MAINUI))
	arg_5_0.bind(BaseUI.ON_CLOSE, function(arg_12_0)
		local var_12_0 = getProxy(ContextProxy).getCurrentContext().getContextByMediator(arg_5_0.class)

		if var_12_0:
			arg_5_0.sendNotification(GAME.REMOVE_LAYERS, {
				context = var_12_0
			}))
	arg_5_0.bind(BaseUI.ON_AWARD, function(arg_13_0, arg_13_1)
		local var_13_0 = {}

		if _.all(arg_13_1.items, function(arg_14_0)
			return arg_14_0.type == DROP_TYPE_ICON_FRAME or arg_14_0.type == DROP_TYPE_CHAT_FRAME):
			table.insert(var_13_0, function(arg_15_0)
				onNextTick(arg_15_0))
		else
			table.insert(var_13_0, function(arg_16_0)
				arg_5_0.addSubLayers(Context.New({
					mediator = AwardInfoMediator,
					viewComponent = AwardInfoLayer,
					data = setmetatable({
						removeFunc = arg_16_0
					}, {
						__index = arg_13_1
					})
				})))

		seriesAsync(var_13_0, arg_13_1.removeFunc))

	local function var_5_0(arg_17_0, arg_17_1)
		local var_17_0 = getProxy(BayProxy)
		local var_17_1 = var_17_0.getNewShip(True)
		local var_17_2 = {}

		for iter_17_0, iter_17_1 in pairs(var_17_1):
			if iter_17_1.isMetaShip():
				table.insert(var_17_2, iter_17_1.configId)

		local var_17_3 = #var_17_1

		underscore.each(arg_17_0, function(arg_18_0)
			if arg_18_0.type == DROP_TYPE_OPERATION:
				table.insert(var_17_1, var_17_0.getShipById(arg_18_0.count))
			elif arg_18_0.type == DROP_TYPE_SHIP:
				local var_18_0 = arg_18_0.configId or arg_18_0.id

				if Ship.isMetaShipByConfigID(var_18_0):
					local var_18_1 = table.indexof(var_17_2, var_18_0)

					if var_18_1:
						table.remove(var_17_2, var_18_1)

						var_17_3 = var_17_3 - 1
					else
						local var_18_2 = Ship.New({
							configId = var_18_0
						})
						local var_18_3 = getProxy(BayProxy).getMetaTransItemMap(var_18_2.configId)

						if var_18_3:
							var_18_2.setReMetaSpecialItemVO(var_18_3)

						table.insert(var_17_1, var_18_2)
				else
					var_17_3 = var_17_3 - 1)

		var_17_1 = underscore.rest(var_17_1, var_17_3 + 1)

		if (pg.gameset.award_ship_limit and pg.gameset.award_ship_limit.key_value or 20) >= #var_17_1:
			for iter_17_2, iter_17_3 in ipairs(var_17_1):
				table.insert(arg_17_1, function(arg_19_0)
					arg_5_0.addSubLayers(Context.New({
						mediator = NewShipMediator,
						viewComponent = NewShipLayer,
						data = {
							ship = iter_17_3
						},
						onRemoved = arg_19_0
					})))

	local function var_5_1(arg_20_0, arg_20_1)
		for iter_20_0, iter_20_1 in pairs(arg_20_0):
			if iter_20_1.type == DROP_TYPE_SKIN and pg.ship_skin_template[iter_20_1.id].skin_type != ShipSkin.SKIN_TYPE_REMAKE and not getProxy(ShipSkinProxy).hasOldNonLimitSkin(iter_20_1.id):
				table.insert(arg_20_1, function(arg_21_0)
					arg_5_0.addSubLayers(Context.New({
						mediator = NewSkinMediator,
						viewComponent = NewSkinLayer,
						data = {
							skinId = iter_20_1.id,
							LayerWeightMgr_weight = LayerWeightConst.SECOND_LAYER
						},
						onRemoved = arg_21_0
					})))

			if iter_20_1.type == DROP_TYPE_SKIN_TIMELIMIT:
				if iter_20_1.count > 0 and not getProxy(ShipSkinProxy).hasOldNonLimitSkin(iter_20_1.id):
					table.insert(arg_20_1, function(arg_22_0)
						arg_5_0.addSubLayers(Context.New({
							mediator = NewSkinMediator,
							viewComponent = NewSkinLayer,
							data = {
								timeLimit = True,
								skinId = iter_20_1.id,
								LayerWeightMgr_weight = LayerWeightConst.SECOND_LAYER
							},
							onRemoved = arg_22_0
						})))
				else
					table.insert(arg_20_1, function(arg_23_0)
						pg.TipsMgr.GetInstance().ShowTips(i18n("already_have_the_skin"))
						arg_23_0())

	local function var_5_2(arg_24_0, arg_24_1)
		local var_24_0 = 0

		for iter_24_0, iter_24_1 in ipairs(arg_24_0):
			if iter_24_1.type == DROP_TYPE_COMMANDER_CAT:
				var_24_0 = var_24_0 + 1

		if var_24_0 == 0:
			return

		local var_24_1 = getProxy(CommanderProxy).GetNewestCommander(var_24_0)

		for iter_24_2, iter_24_3 in ipairs(var_24_1):
			table.insert(arg_24_1, function(arg_25_0)
				arg_5_0.addSubLayers(Context.New({
					viewComponent = NewCommanderScene,
					mediator = NewCommanderMediator,
					data = {
						commander = iter_24_3,
						onExit = arg_25_0
					}
				})))

	arg_5_0.bind(BaseUI.ON_ACHIEVE, function(arg_26_0, arg_26_1, arg_26_2)
		local var_26_0 = {}

		if #arg_26_1 > 0:
			table.insert(var_26_0, function(arg_27_0)
				arg_5_0.viewComponent.emit(BaseUI.ON_AWARD, {
					items = arg_26_1,
					removeFunc = arg_27_0
				}))
			table.insert(var_26_0, function(arg_28_0)
				var_5_0(arg_26_1, var_26_0)
				var_5_1(arg_26_1, var_26_0)
				var_5_2(arg_26_1, var_26_0)
				arg_28_0())

		seriesAsyncExtend(var_26_0, arg_26_2))
	arg_5_0.bind(BaseUI.ON_WORLD_ACHIEVE, function(arg_29_0, arg_29_1)
		local var_29_0 = {}
		local var_29_1 = arg_29_1.items

		if #var_29_1 > 0:
			table.insert(var_29_0, function(arg_30_0)
				arg_5_0.viewComponent.emit(BaseUI.ON_AWARD, setmetatable({
					removeFunc = arg_30_0
				}, {
					__index = arg_29_1
				})))
			table.insert(var_29_0, function(arg_31_0)
				var_5_0(var_29_1, var_29_0)
				var_5_1(var_29_1, var_29_0)
				var_5_2(var_29_1, var_29_0)
				arg_31_0())

		seriesAsyncExtend(var_29_0, arg_29_1.removeFunc))
	arg_5_0.bind(BaseUI.ON_SHIP_EXP, function(arg_32_0, arg_32_1, arg_32_2)
		arg_5_0.addSubLayers(Context.New({
			mediator = ShipExpMediator,
			viewComponent = ShipExpLayer,
			data = arg_32_1,
			onRemoved = arg_32_2
		})))
	arg_5_0.bind(BaseUI.ON_SPWEAPON, function(arg_33_0, arg_33_1)
		arg_33_1.type = defaultValue(arg_33_1.type, SpWeaponInfoLayer.TYPE_DEFAULT)

		arg_5_0.addSubLayers(Context.New({
			mediator = SpWeaponInfoMediator,
			viewComponent = SpWeaponInfoLayer,
			data = arg_33_1
		})))
	arg_5_0.commonBind()
	arg_5_0.register()

def var_0_0.commonBind(arg_34_0):
	var_0_0.CommonBindDic = var_0_0.CommonBindDic or {
		[BaseUI.ON_DROP] = function(arg_35_0, arg_35_1, arg_35_2, arg_35_3)
			if arg_35_2.type == DROP_TYPE_EQUIP:
				arg_35_0.addSubLayers(Context.New({
					mediator = EquipmentInfoMediator,
					viewComponent = EquipmentInfoLayer,
					data = {
						equipmentId = arg_35_2.getConfig("id"),
						type = EquipmentInfoMediator.TYPE_DISPLAY,
						onRemoved = arg_35_3,
						LayerWeightMgr_weight = LayerWeightConst.TOP_LAYER
					}
				}))
			elif arg_35_2.type == DROP_TYPE_SPWEAPON:
				arg_35_0.addSubLayers(Context.New({
					mediator = SpWeaponInfoMediator,
					viewComponent = SpWeaponInfoLayer,
					data = {
						spWeaponConfigId = arg_35_2.getConfig("id"),
						type = SpWeaponInfoLayer.TYPE_DISPLAY,
						onRemoved = arg_35_3,
						LayerWeightMgr_weight = LayerWeightConst.TOP_LAYER
					}
				}))
			elif arg_35_2.type == DROP_TYPE_EQUIPMENT_SKIN:
				arg_35_0.addSubLayers(Context.New({
					mediator = EquipmentSkinMediator,
					viewComponent = EquipmentSkinLayer,
					data = {
						skinId = arg_35_2.getConfig("id"),
						mode = EquipmentSkinLayer.DISPLAY,
						weight = LayerWeightConst.TOP_LAYER
					}
				}))
			elif arg_35_2.type == DROP_TYPE_EMOJI:
				arg_35_0.addSubLayers(Context.New({
					mediator = ContextMediator,
					viewComponent = EmojiInfoLayer,
					data = {
						id = arg_35_2.cfg.id
					}
				}))
			else
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					type = MSGBOX_TYPE_SINGLE_ITEM,
					drop = arg_35_2,
					onNo = arg_35_3,
					onYes = arg_35_3,
					weight = LayerWeightConst.TOP_LAYER
				}),
		[BaseUI.ON_DROP_LIST] = function(arg_36_0, arg_36_1, arg_36_2)
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				hideNo = True,
				type = MSGBOX_TYPE_ITEM_BOX,
				items = arg_36_2.itemList,
				content = arg_36_2.content,
				item2Row = arg_36_2.item2Row,
				def itemFunc:(arg_37_0)
					arg_36_0.viewComponent.emit(BaseUI.ON_DROP, arg_37_0, function()
						arg_36_0.viewComponent.emit(BaseUI.ON_DROP_LIST, arg_36_2)),
				weight = LayerWeightConst.TOP_LAYER
			}),
		[BaseUI.ON_DROP_LIST_OWN] = function(arg_39_0, arg_39_1, arg_39_2)
			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				hideNo = True,
				type = MSGBOX_TYPE_DROP_ITEM_ESKIN,
				items = arg_39_2.itemList,
				content = arg_39_2.content,
				item2Row = arg_39_2.item2Row,
				def itemFunc:(arg_40_0)
					arg_39_0.viewComponent.emit(BaseUI.ON_DROP, arg_40_0, function()
						arg_39_0.viewComponent.emit(BaseUI.ON_DROP_LIST, arg_39_2)),
				weight = LayerWeightConst.TOP_LAYER
			}),
		[BaseUI.ON_ITEM] = function(arg_42_0, arg_42_1, arg_42_2, arg_42_3)
			arg_42_0.addSubLayers(Context.New({
				mediator = ItemInfoMediator,
				viewComponent = ItemInfoLayer,
				data = {
					drop = Drop.New({
						type = DROP_TYPE_ITEM,
						id = arg_42_2
					}),
					confirmCall = arg_42_3
				}
			})),
		[BaseUI.ON_ITEM_EXTRA] = function(arg_43_0, arg_43_1, arg_43_2, arg_43_3)
			arg_43_0.addSubLayers(Context.New({
				mediator = ItemInfoMediator,
				viewComponent = ItemInfoLayer,
				data = {
					drop = Drop.New({
						type = DROP_TYPE_ITEM,
						id = arg_43_2,
						extra = arg_43_3
					})
				}
			})),
		[BaseUI.ON_SHIP] = function(arg_44_0, arg_44_1, arg_44_2)
			arg_44_0.addSubLayers(Context.New({
				mediator = ItemInfoMediator,
				viewComponent = ItemInfoLayer,
				data = {
					drop = Drop.New({
						type = DROP_TYPE_SHIP,
						id = arg_44_2
					})
				}
			})),
		[BaseUI.ON_EQUIPMENT] = function(arg_45_0, arg_45_1, arg_45_2)
			arg_45_2.type = defaultValue(arg_45_2.type, EquipmentInfoMediator.TYPE_DEFAULT)

			arg_45_0.addSubLayers(Context.New({
				mediator = EquipmentInfoMediator,
				viewComponent = EquipmentInfoLayer,
				data = arg_45_2
			}))
	}

	for iter_34_0, iter_34_1 in pairs(var_0_0.CommonBindDic):
		arg_34_0.bind(iter_34_0, function(...)
			return iter_34_1(arg_34_0, ...))

def var_0_0.register(arg_47_0):
	return

def var_0_0.onUIAvalible(arg_48_0):
	return

def var_0_0.setContextData(arg_49_0, arg_49_1):
	arg_49_0.contextData = arg_49_1

def var_0_0.bind(arg_50_0, arg_50_1, arg_50_2):
	arg_50_0.viewComponent.event.connect(arg_50_1, arg_50_2)
	table.insert(arg_50_0.event, {
		event = arg_50_1,
		callback = arg_50_2
	})

def var_0_0.onRemove(arg_51_0):
	arg_51_0.remove()

	for iter_51_0, iter_51_1 in ipairs(arg_51_0.event):
		arg_51_0.viewComponent.event.disconnect(iter_51_1.event, iter_51_1.callback)

	arg_51_0.event = {}

def var_0_0.remove(arg_52_0):
	return

def var_0_0.addSubLayers(arg_53_0, arg_53_1, arg_53_2, arg_53_3, arg_53_4):
	assert(isa(arg_53_1, Context), "should be an instance of Context")

	local var_53_0 = arg_53_0.GetContext()

	if arg_53_2:
		while var_53_0.parent:
			var_53_0 = var_53_0.parent

	local var_53_1 = {
		parentContext = var_53_0,
		context = arg_53_1,
		callback = arg_53_3
	}

	var_53_1 = arg_53_4 and table.merge(var_53_1, arg_53_4) or var_53_1

	arg_53_0.sendNotification(GAME.LOAD_LAYERS, var_53_1)

def var_0_0.switchLayersOnParent(arg_54_0, arg_54_1, arg_54_2):
	assert(isa(arg_54_1, Context), "should be an instance of Context")

	local var_54_0 = arg_54_0.GetContext()
	local var_54_1 = var_54_0.parent

	if not arg_54_1.data.isSubView:
		while var_54_1.data.isSubView:
			var_54_1 = var_54_1.parent

	local var_54_2 = {
		parentContext = var_54_1,
		context = arg_54_1,
		removeContexts = {
			var_54_0
		}
	}

	var_54_2 = arg_54_2 and table.merge(var_54_2, arg_54_2) or var_54_2

	arg_54_0.sendNotification(GAME.LOAD_LAYERS, var_54_2)

def var_0_0.GetContext(arg_55_0):
	return getProxy(ContextProxy).getCurrentContext().getContextByMediator(arg_55_0.class)

def var_0_0.blockEvents(arg_56_0):
	if arg_56_0.event:
		for iter_56_0, iter_56_1 in ipairs(arg_56_0.event):
			arg_56_0.viewComponent.event.block(iter_56_1.event, iter_56_1.callback)

def var_0_0.unblockEvents(arg_57_0):
	if arg_57_0.event:
		for iter_57_0, iter_57_1 in ipairs(arg_57_0.event):
			arg_57_0.viewComponent.event.unblock(iter_57_1.event, iter_57_1.callback)

def var_0_0.onBackPressed(arg_58_0, arg_58_1):
	pg.CriMgr.GetInstance().PlaySoundEffect_V3(SFX_CANCEL)

	local var_58_0 = getProxy(ContextProxy)

	if arg_58_1:
		local var_58_1 = var_58_0.getContextByMediator(arg_58_0.class).parent

		if var_58_1:
			local var_58_2 = pg.m02.retrieveMediator(var_58_1.mediator.__cname)

			if var_58_2 and var_58_2.viewComponent:
				var_58_2.viewComponent.onBackPressed()
	else
		arg_58_0.viewComponent.closeView()

def var_0_0.removeSubLayers(arg_59_0, arg_59_1, arg_59_2):
	assert(isa(arg_59_1, var_0_0), "should be a ContextMediator Class")

	local var_59_0 = getProxy(ContextProxy).getContextByMediator(arg_59_0.class or arg_59_0)

	if not var_59_0:
		return

	local var_59_1 = var_59_0.getContextByMediator(arg_59_1)

	if not var_59_1:
		return

	arg_59_0.sendNotification(GAME.REMOVE_LAYERS, {
		context = var_59_1,
		callback = arg_59_2
	})

return var_0_0
