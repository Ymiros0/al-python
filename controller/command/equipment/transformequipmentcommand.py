local var_0_0 = class("TransformEquipmentCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.candicate

	seriesAsync({
		function(arg_2_0)
			if var_1_1.type == DROP_TYPE_ITEM:
				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					content = i18n("equipment_upgrade_feedback_compose_tip"),
					onYes = arg_2_0
				})

				return
			elif var_1_1.type == DROP_TYPE_EQUIP and var_1_1.template.shipId != None:
				local var_2_0 = var_1_1.template.shipId
				local var_2_1 = getProxy(BayProxy).getShipById(var_2_0)
				local var_2_2, var_2_3 = ShipStatus.ShipStatusCheck("onModify", var_2_1)

				if not var_2_2:
					pg.TipsMgr.GetInstance().ShowTips(var_2_3)

					return

				pg.MsgboxMgr.GetInstance().ShowMsgBox({
					content = i18n("equipment_upgrade_feedback_equipment_consume", var_2_1.getName(), var_1_1.template.getConfig("name")),
					onYes = arg_2_0
				})

				return

			arg_2_0(),
		function(arg_3_0)
			if var_1_1.type == DROP_TYPE_EQUIP:
				return arg_3_0({
					shipId = var_1_1.template.shipId,
					pos = var_1_1.template.shipPos,
					equipmentId = var_1_1.template.id,
					formulaIds = var_1_0.formulaIds
				})

			local var_3_0 = var_1_1.composeCfg.id
			local var_3_1 = 1
			local var_3_2 = getProxy(BagProxy)
			local var_3_3 = getProxy(PlayerProxy)
			local var_3_4 = var_3_3.getData()
			local var_3_5 = pg.compose_data_template[var_3_0]
			local var_3_6 = getProxy(EquipmentProxy)
			local var_3_7 = var_3_6.getCapacity()

			if var_3_4.getMaxEquipmentBag() < var_3_7 + var_3_1:
				NoPosMsgBox(i18n("switch_to_shop_tip_noPos"), openDestroyEquip, gotoChargeScene)

				return

			if var_3_4.gold < var_3_5.gold_num * var_3_1:
				GoShoppingMsgBox(i18n("switch_to_shop_tip_2", i18n("word_gold")), ChargeScene.TYPE_ITEM, {
					{
						59001,
						var_3_5.gold_num * var_3_1 - var_3_4.gold,
						var_3_5.gold_num * var_3_1
					}
				})

				return

			local var_3_8 = var_3_2.getItemById(var_3_5.material_id)

			if not var_3_8 or var_3_8.count < var_3_5.material_num * var_3_1:
				pg.TipsMgr.GetInstance().ShowTips(i18n("word_materal_no_enough"))

				return

			pg.ConnectionMgr.GetInstance().Send(14006, {
				id = var_3_0,
				num = var_3_1
			}, 14007, function(arg_4_0)
				if arg_4_0.result == 0:
					var_3_6.addEquipmentById(var_3_5.equip_id, var_3_1)
					var_3_4.consume({
						gold = var_3_5.gold_num * var_3_1
					})
					var_3_3.updatePlayer(var_3_4)
					var_3_2.removeItemById(var_3_5.material_id, var_3_5.material_num * var_3_1)
					arg_1_0.sendNotification(GAME.COMPOSITE_EQUIPMENT_DONE, {
						equipment = Equipment.New({
							id = var_3_5.equip_id
						}),
						count = var_3_1,
						composeId = var_3_0
					})
					arg_3_0({
						equipmentId = var_3_5.equip_id,
						formulaIds = var_1_0.formulaIds
					})
				else
					pg.TipsMgr.GetInstance().ShowTips(errorTip("equipment_compositeEquipment", arg_4_0.result))),
		function(arg_5_0, arg_5_1)
			arg_1_0.ExecuteEquipTransform(arg_5_1)
	})

def var_0_0.ExecuteEquipTransform(arg_6_0, arg_6_1):
	local var_6_0 = arg_6_1.shipId
	local var_6_1 = var_6_0
	local var_6_2 = arg_6_1.pos
	local var_6_3 = arg_6_1.equipmentId
	local var_6_4 = arg_6_1.formulaIds
	local var_6_5

	if var_6_0:
		var_6_5 = getProxy(BayProxy).getShipById(var_6_0).getEquip(var_6_2)

		assert(var_6_5, "can not find equipment at ship.")

		var_6_3 = var_6_5.id
	elif var_6_3 != 0:
		var_6_5 = getProxy(EquipmentProxy).getEquipmentById(var_6_3)

		assert(var_6_5, "can not find equipment. " .. var_6_3)

		var_6_3 = var_6_5.id

	local var_6_6, var_6_7 = EquipmentTransformUtil.CheckEquipmentFormulasSucceed(var_6_4, var_6_3)

	if not var_6_6:
		pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_x", var_6_7))

		return

	local var_6_8 = {}
	local var_6_9 = {}

	local function var_6_10()
		local var_7_0 = getProxy(BagProxy)
		local var_7_1 = getProxy(PlayerProxy)

		for iter_7_0, iter_7_1 in pairs(var_6_8):
			if iter_7_0 == "gold":
				local var_7_2 = var_7_1.getData()
				local var_7_3 = {
					gold = math.abs(iter_7_1)
				}

				if iter_7_1 > 0:
					var_7_2.consume(var_7_3)
					var_7_1.updatePlayer(var_7_2)
				elif iter_7_1 < 0:
					var_7_2.addResources(var_7_3)
					var_7_1.updatePlayer(var_7_2)
			elif iter_7_1 > 0:
				var_7_0.removeItemById(iter_7_0, iter_7_1)
			elif iter_7_1 < 0:
				var_7_0.addItemById(iter_7_0, -iter_7_1)

		table.clear(var_6_8)

	local var_6_11 = var_6_3

	local function var_6_12()
		var_6_10()

		local var_8_0 = getProxy(BayProxy)
		local var_8_1 = getProxy(EquipmentProxy)
		local var_8_2
		local var_8_3

		if var_6_0:
			var_8_2 = var_8_0.getShipById(var_6_0)
			var_8_3 = var_8_2.getEquip(var_6_2)
		else
			var_8_3 = var_8_1.getEquipmentById(var_6_3)

		assert(var_8_3, "Cant Get Equip " .. (var_6_0 and "Ship " .. var_6_0 .. " Pos " .. var_6_2 or "ID " .. var_6_3))

		local var_8_4 = var_8_3.MigrateTo(var_6_11)

		if var_8_2:
			if not var_8_2.isForbiddenAtPos(var_8_4, var_6_2):
				var_8_2.updateEquip(var_6_2, var_8_4)
				var_8_0.updateShip(var_8_2)
			else
				var_8_2.updateEquip(var_6_2, None)
				var_8_0.updateShip(var_8_2)

				var_6_0 = None

				var_8_1.addEquipment(var_8_4)
		else
			var_8_1.removeEquipmentById(var_8_3.id, 1)
			var_8_1.addEquipmentById(var_8_4.id, 1)

		return var_8_2, var_8_3, var_8_4

	local var_6_13 = var_6_5
	local var_6_14
	local var_6_15
	local var_6_16

	table.SerialIpairsAsync(var_6_4, function(arg_9_0, arg_9_1, arg_9_2)
		seriesAsync({
			function(arg_10_0)
				local var_10_0 = var_6_0 and 14013 or 14015
				local var_10_1 = var_6_0 and 14014 or 14016
				local var_10_2 = var_6_0 and {
					ship_id = var_6_0,
					pos = var_6_2,
					upgrade_id = arg_9_1
				} or {
					equip_id = var_6_11,
					upgrade_id = arg_9_1
				}

				pg.ConnectionMgr.GetInstance().Send(var_10_0, var_10_2, var_10_1, arg_10_0),
			function(arg_11_0, arg_11_1)
				if arg_11_1.result == 0:
					local var_11_0 = pg.equip_upgrade_data[arg_9_1]
					local var_11_1 = var_11_0.material_consume

					for iter_11_0, iter_11_1 in ipairs(var_11_1):
						local var_11_2 = iter_11_1[1]
						local var_11_3 = iter_11_1[2]

						var_6_8[var_11_2] = (var_6_8[var_11_2] or 0) + var_11_3

					var_6_8.gold = (var_6_8.gold or 0) + var_11_0.coin_consume

					local var_11_4 = Equipment.GetRevertRewardsStatic(var_6_11)

					for iter_11_2, iter_11_3 in pairs(var_11_4):
						if iter_11_2 != "gold":
							var_6_8[iter_11_2] = (var_6_8[iter_11_2] or 0) - iter_11_3
							var_6_9[iter_11_2] = (var_6_9[iter_11_2] or 0) + iter_11_3

					assert(Equipment.CanInBag(var_6_11), "Missing equip_data_template ID. " .. (var_6_11 or "NIL"))

					if Equipment.CanInBag(var_6_11):
						local var_11_5 = Equipment.getConfigData(var_6_11).destory_gold or 0

						var_6_8.gold = (var_6_8.gold or 0) - var_11_5
						var_6_9.gold = (var_6_9.gold or 0) + var_11_5

					var_6_3 = var_6_11
					var_6_11 = var_11_0.target_id
					var_6_14, var_6_15, var_6_16 = var_6_12()

					arg_9_2()
				else
					pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_11_1.result] .. arg_11_1.result)
					arg_6_0.sendNotification(GAME.TRANSFORM_EQUIPMENT_FAIL)
		}), function()
		if not var_6_0 and var_6_1:
			local var_12_0 = getProxy(BayProxy).getShipById(var_6_1)

			pg.TipsMgr.GetInstance().ShowTips(i18n("equipment_upgrade_equipped_unavailable", var_12_0.getName(), var_6_16.getConfig("name")))

		local var_12_1 = {
			ship = var_6_14,
			equip = var_6_15,
			newEquip = var_6_16
		}

		arg_6_0.sendNotification(GAME.TRANSFORM_EQUIPMENT_DONE, var_12_1)
		LoadContextCommand.LoadLayerOnTopContext(Context.New({
			mediator = EquipmentTransformInfoMediator,
			viewComponent = EquipmentTransformInfoLayer,
			data = {
				equipVO = var_6_13
			},
			def onRemoved:()
				local var_13_0 = getProxy(ContextProxy).getCurrentContext()
				local var_13_1 = var_13_0.getContextByMediator(EquipmentInfoMediator)

				if var_13_1:
					pg.m02.retrieveMediator(var_13_1.mediator.__cname).getViewComponent().closeView()

				local var_13_2 = pg.m02.retrieveMediator(var_13_0.mediator.__cname).getViewComponent()

				seriesAsync({
					function(arg_14_0)
						var_13_2.emit(BaseUI.ON_ACHIEVE, {
							{
								count = 1,
								id = var_6_16 and var_6_16.id or 0,
								type = DROP_TYPE_EQUIP
							}
						}, arg_14_0),
					function(arg_15_0)
						onNextTick(arg_15_0),
					function(arg_16_0)
						if not next(var_6_9):
							arg_16_0()

							return

						local var_16_0 = {}

						for iter_16_0, iter_16_1 in pairs(var_6_9):
							if iter_16_0 == "gold":
								table.insert(var_16_0, {
									type = DROP_TYPE_RESOURCE,
									id = res2id(iter_16_0),
									count = iter_16_1
								})
							else
								table.insert(var_16_0, {
									type = DROP_TYPE_ITEM,
									id = iter_16_0,
									count = iter_16_1
								})

						var_13_2.emit(BaseUI.ON_AWARD, {
							items = var_16_0,
							title = AwardInfoLayer.TITLE.REVERT,
							removeFunc = arg_16_0
						}),
					function(arg_17_0)
						arg_6_0.sendNotification(GAME.TRANSFORM_EQUIPMENT_AWARD_FINISHED, var_12_1)
				})
		})))

return var_0_0
