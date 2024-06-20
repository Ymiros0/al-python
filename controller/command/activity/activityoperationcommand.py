local var_0_0 = class("ActivityOperationCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = getProxy(ActivityProxy).getActivityById(var_1_0.activity_id)

	assert(var_1_1)

	local var_1_2 = var_1_1.getConfig("type")

	if var_1_2 == ActivityConst.ACTIVITY_TYPE_BUILDSHIP_1 or var_1_2 == ActivityConst.ACTIVITY_TYPE_BUILDSHIP_PRAY or var_1_2 == ActivityConst.ACTIVITY_TYPE_NEWSERVER_BUILD:
		local var_1_3, var_1_4, var_1_5 = BuildShip.canBuildShipByBuildId(var_1_0.buildId, var_1_0.arg1, var_1_0.arg2 == 1)

		if not var_1_3:
			if var_1_5:
				GoShoppingMsgBox(i18n("switch_to_shop_tip_1"), ChargeScene.TYPE_ITEM, var_1_5)
			else
				pg.TipsMgr.GetInstance().ShowTips(var_1_4)

			return
	elif var_1_2 == ActivityConst.ACTIVITY_TYPE_SHOP:
		local var_1_6 = getProxy(PlayerProxy).getData()
		local var_1_7 = getProxy(ShopsProxy).getActivityShopById(var_1_1.id).bindConfigTable()[var_1_0.arg1]
		local var_1_8 = var_1_0.arg2 or 1

		if var_1_6[id2res(var_1_7.resource_type)] < var_1_7.resource_num * var_1_8:
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_resource"))

			return

		if var_1_7.commodity_type == 1:
			if var_1_7.commodity_id == 1 and var_1_6.GoldMax(var_1_7.num * var_1_8):
				pg.TipsMgr.GetInstance().ShowTips(i18n("gold_max_tip_title") .. i18n("resource_max_tip_shop"))

				return

			if var_1_7.commodity_id == 2 and var_1_6.OilMax(var_1_7.num * var_1_8):
				pg.TipsMgr.GetInstance().ShowTips(i18n("oil_max_tip_title") .. i18n("resource_max_tip_shop"))

				return
	elif var_1_2 == ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2 and var_1_0.cmd == 2 and not var_1_1.CanRequest():
		return

	print(var_1_0.activity_id, var_1_0.cmd, var_1_0.arg1, var_1_0.arg2)
	pg.ConnectionMgr.GetInstance().Send(11202, {
		activity_id = var_1_0.activity_id,
		cmd = var_1_0.cmd,
		arg1 = var_1_0.arg1,
		arg2 = var_1_0.arg2,
		arg_list = var_1_0.arg_list or {},
		kvargs1 = var_1_0.kvargs1
	}, 11203, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = PlayerConst.GetTranAwards(var_1_0, arg_2_0)
			local var_2_1 = arg_1_0.updateActivityData(var_1_0, arg_2_0, var_1_1, var_2_0)

			getProxy(ActivityTaskProxy).checkAutoSubmit()
			arg_1_0.performance(var_1_0, arg_2_0, var_2_1, var_2_0)
		else
			originalPrint("activity op ret code. " .. arg_2_0.result)
			print("activity op ret code. " .. arg_2_0.result, var_1_0.cmd, var_1_0.arg1)

			if var_1_2 == ActivityConst.ACTIVITY_TYPE_7DAYSLOGIN or var_1_2 == ActivityConst.ACTIVITY_TYPE_PROGRESSLOGIN or var_1_2 == ActivityConst.ACTIVITY_TYPE_MONTHSIGN or var_1_2 == ActivityConst.ACTIVITY_TYPE_REFLUX:
				var_1_1.autoActionForbidden = True

				getProxy(ActivityProxy).updateActivity(var_1_1)
			elif var_1_2 == ActivityConst.ACTIVITY_TYPE_BUILDSHIP_1 or var_1_2 == ActivityConst.ACTIVITY_TYPE_NEWSERVER_BUILD:
				if arg_2_0.result == 1:
					pg.TipsMgr.GetInstance().ShowTips(i18n("activity_build_end_tip"))
			elif var_1_2 == 17:
				pg.TipsMgr.GetInstance().ShowTips("错误!." .. arg_2_0.result)
			elif var_1_2 == ActivityConst.ACTIVITY_TYPE_FRESH_TEC_CATCHUP:
				-- block empty
			elif arg_2_0.result == 3 or arg_2_0.result == 4:
				pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))
			else
				pg.TipsMgr.GetInstance().ShowTips(errorTip("activity_op_error", arg_2_0.result))

			arg_1_0.sendNotification(ActivityProxy.ACTIVITY_OPERATION_ERRO, {
				actId = var_1_0.activity_id,
				code = arg_2_0.result
			}))

def var_0_0.updateActivityData(arg_3_0, arg_3_1, arg_3_2, arg_3_3, arg_3_4):
	local var_3_0 = arg_3_3.getConfig("type")
	local var_3_1 = getProxy(PlayerProxy)
	local var_3_2 = getProxy(TaskProxy)

	if var_3_0 == ActivityConst.ACTIVITY_TYPE_7DAYSLOGIN:
		arg_3_3.data1 = arg_3_3.data1 + 1
		arg_3_3.data2 = pg.TimeMgr.GetInstance().GetServerTime()
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_PROGRESSLOGIN:
		if arg_3_1.cmd == 1:
			arg_3_3.data1 = arg_3_3.data1 + 1
			arg_3_3.data2 = pg.TimeMgr.GetInstance().GetServerTime()
		elif arg_3_1.cmd == 2:
			arg_3_3.achieved = True
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_LEVELAWARD:
		table.insert(arg_3_3.data1_list, arg_3_1.arg1)
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_STORY_AWARD:
		table.insert(arg_3_3.data1_list, arg_3_1.arg1)
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_LEVELPLAN:
		if arg_3_1.cmd == 1:
			arg_3_3.data1 = True
		elif arg_3_1.cmd == 2:
			table.insert(arg_3_3.data1_list, arg_3_1.arg1)
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_MONTHSIGN:
		local var_3_3 = pg.TimeMgr.GetInstance().GetServerTime()
		local var_3_4 = pg.TimeMgr.GetInstance().STimeDescS(var_3_3, "*t")
		local var_3_5

		if arg_3_3.getSpecialData("reMonthSignDay") != None:
			var_3_5 = arg_3_3.getSpecialData("reMonthSignDay")
			arg_3_3.data3 = arg_3_3.data3 and arg_3_3.data3 + 1 or 1
		else
			var_3_5 = var_3_4.day

		getProxy(ActivityProxy).updateActivity(arg_3_3)
		table.insert(arg_3_3.data1_list, var_3_5)
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_CHARGEAWARD:
		arg_3_3.data2 = 1
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_BUILDSHIP_1 or var_3_0 == ActivityConst.ACTIVITY_TYPE_BUILDSHIP_PRAY or var_3_0 == ActivityConst.ACTIVITY_TYPE_NEWSERVER_BUILD:
		pg.TrackerMgr.GetInstance().Tracking(TRACKING_BUILD_SHIP, arg_3_1.arg1)

		local var_3_6 = pg.ship_data_create_material[arg_3_1.buildId]

		if arg_3_1.arg2 == 1:
			local var_3_7 = getProxy(ActivityProxy)
			local var_3_8 = var_3_7.getBuildFreeActivityByBuildId(arg_3_1.buildId)

			var_3_8.data1 = var_3_8.data1 - arg_3_1.arg1

			var_3_7.updateActivity(var_3_8)
		else
			getProxy(BagProxy).removeItemById(var_3_6.use_item, var_3_6.number_1 * arg_3_1.arg1)

			local var_3_9 = var_3_1.getData()

			var_3_9.consume({
				gold = var_3_6.use_gold * arg_3_1.arg1
			})
			var_3_1.updatePlayer(var_3_9)

		local var_3_10 = getProxy(BuildShipProxy)

		if var_3_6.exchange_count > 0:
			var_3_10.changeRegularExchangeCount(arg_3_1.arg1 * var_3_6.exchange_count)

		for iter_3_0, iter_3_1 in ipairs(arg_3_2.build):
			local var_3_11 = BuildShip.New(iter_3_1)

			var_3_10.addBuildShip(var_3_11)

		arg_3_3.data1 = arg_3_3.data1 + arg_3_1.arg1

		arg_3_0.sendNotification(GAME.BUILD_SHIP_DONE)
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_SHOP:
		local var_3_12 = getProxy(ShopsProxy)
		local var_3_13 = var_3_12.getActivityShopById(arg_3_3.id)

		var_3_12.UpdateActivityGoods(arg_3_3.id, arg_3_1.arg1, arg_3_1.arg2)

		if table.contains(arg_3_3.data1_list, arg_3_1.arg1):
			for iter_3_2, iter_3_3 in ipairs(arg_3_3.data1_list):
				if iter_3_3 == arg_3_1.arg1:
					arg_3_3.data2_list[iter_3_2] = arg_3_3.data2_list[iter_3_2] + arg_3_1.arg2

					break
		else
			table.insert(arg_3_3.data1_list, arg_3_1.arg1)
			table.insert(arg_3_3.data2_list, arg_3_1.arg2)

		local var_3_14 = var_3_13.bindConfigTable()[arg_3_1.arg1]
		local var_3_15 = var_3_14.resource_num * arg_3_1.arg2
		local var_3_16 = var_3_1.getData()

		var_3_16.consume({
			[id2res(var_3_14.resource_type)] = var_3_15
		})
		var_3_1.updatePlayer(var_3_16)
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_ZPROJECT:
		-- block empty
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_TASK_LIST:
		if arg_3_1.cmd == 1:
			local var_3_17, var_3_18 = getActivityTask(arg_3_3)

			if var_3_18 and not var_3_18.isReceive():
				local var_3_19 = arg_3_3.getConfig("config_data")

				for iter_3_4, iter_3_5 in ipairs(var_3_19):
					local var_3_20 = _.flatten({
						iter_3_5
					})

					if table.contains(var_3_20, var_3_17):
						arg_3_3.data3 = iter_3_4

						break
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_TASK_RES:
		if arg_3_1.cmd == 1:
			local var_3_21, var_3_22 = getActivityTask(arg_3_3)

			if var_3_22 and not var_3_22.isReceive():
				local var_3_23 = arg_3_3.getConfig("config_data")

				for iter_3_6, iter_3_7 in ipairs(var_3_23):
					local var_3_24 = _.flatten({
						iter_3_7
					})

					if table.contains(var_3_24, var_3_21):
						arg_3_3.data3 = iter_3_6

						break
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_PUZZLA:
		if arg_3_1.cmd == 1:
			arg_3_3.data1 = 1
		elif arg_3_1.cmd == 4:
			arg_3_3.data1 = 2

		getProxy(ActivityProxy).updateActivity(arg_3_3)
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_BB:
		arg_3_3.data1 = arg_3_3.data1 + 1
		arg_3_3.data2 = arg_3_3.data2 - 1
		arg_3_3.data1_list = arg_3_2.number
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_LOTTERY:
		if arg_3_1.cmd == 1:
			local var_3_25 = ActivityItemPool.New({
				id = arg_3_1.arg2
			})
			local var_3_26 = var_3_25.getComsume()
			local var_3_27 = arg_3_1.arg1 * var_3_26.count

			if var_3_26.type == DROP_TYPE_RESOURCE:
				local var_3_28 = var_3_1.getData()

				var_3_28.consume({
					[id2res(var_3_26.id)] = var_3_27
				})
				var_3_1.updatePlayer(var_3_28)
			elif var_3_26.type == DROP_TYPE_ITEM:
				getProxy(BagProxy).removeItemById(var_3_26.id, var_3_27)

			arg_3_3.updateData(var_3_25.id, arg_3_2.number)
		elif arg_3_1.cmd == 2:
			arg_3_3.data1 = arg_3_1.arg1
		elif arg_3_1.cmd == 3:
			arg_3_3.data2_list = _.map(arg_3_1.arg_list, function(arg_4_0)
				return arg_4_0)
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_CARD_PAIRS or var_3_0 == ActivityConst.ACTIVITY_TYPE_LINK_LINK:
		if arg_3_1.cmd == 1:
			local var_3_29 = arg_3_3.getConfig("config_data")[4]

			if #arg_3_4 > 0:
				arg_3_3.data2 = arg_3_3.data2 + 1

				if var_3_29 <= arg_3_3.data2:
					arg_3_3.data1 = 1

			if arg_3_3.data4 == 0:
				arg_3_3.data4 = arg_3_1.arg2
			elif arg_3_1.arg2 < arg_3_3.data4:
				arg_3_3.data4 = arg_3_1.arg2
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_REFLUX:
		if arg_3_1.cmd == 1:
			arg_3_3.data1_list[1] = pg.TimeMgr.GetInstance().GetServerTime()
			arg_3_3.data1_list[2] = arg_3_3.data1_list[2] + 1
		elif arg_3_1.cmd == 2:
			arg_3_3.data4 = arg_3_1.arg1
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_LOTTERY_AWARD:
		if arg_3_1.cmd == 1:
			arg_3_3.data1 = arg_3_3.data1 + 1
			arg_3_3.data2 = arg_3_2.number[1]
		elif arg_3_1.cmd == 2:
			table.insert(arg_3_3.data1_list, arg_3_3.data1)
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_DODGEM:
		if arg_3_1.cmd == 1:
			arg_3_0.sendNotification(GAME.FINISH_STAGE_DONE, {
				statistics = arg_3_1.statistics,
				score = arg_3_1.statistics._battleScore,
				system = SYSTEM_DODGEM
			})

			arg_3_3.data1_list[1] = math.max(arg_3_3.data1_list[1], arg_3_1.arg2)
			arg_3_3.data2_list[1] = arg_3_2.number[1]
			arg_3_3.data2_list[2] = arg_3_2.number[2]
		elif arg_3_1.cmd == 2:
			arg_3_3.data2 = arg_3_2.number[1]
			arg_3_3.data3 = arg_3_2.number[2]
			arg_3_3.data2_list[1] = 0
			arg_3_3.data2_list[2] = 0
		elif arg_3_1.cmd == 3:
			arg_3_3.data4 = defaultValue(arg_3_3.data4, 0) + 1
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_SUBMARINE_RUN:
		if arg_3_1.cmd == 1:
			arg_3_0.sendNotification(GAME.FINISH_STAGE_DONE, {
				statistics = arg_3_1.statistics,
				score = arg_3_1.statistics._battleScore,
				system = SYSTEM_SUBMARINE_RUN
			})

			arg_3_3.data1_list[1] = math.max(arg_3_3.data1_list[1], arg_3_1.arg2)
			arg_3_3.data2_list[1] = arg_3_2.number[1]
			arg_3_3.data2_list[2] = arg_3_2.number[2]
		elif arg_3_1.cmd == 2:
			arg_3_3.data2 = arg_3_2.number[1]
			arg_3_3.data3 = arg_3_2.number[2]
			arg_3_3.data2_list[1] = 0
			arg_3_3.data2_list[2] = 0
		elif arg_3_1.cmd == 3:
			arg_3_3.data4 = defaultValue(arg_3_3.data4, 0) + 1
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_TURNTABLE:
		if arg_3_1.cmd == 2:
			arg_3_3.data4 = 0
		elif arg_3_1.cmd == 1:
			local var_3_30 = arg_3_3.getConfig("config_id")
			local var_3_31 = pg.activity_event_turning[var_3_30].total_num

			if arg_3_3.data3 == var_3_31:
				arg_3_3.data2 = 1
				arg_3_3.data3 = arg_3_3.data3 + 1
			else
				arg_3_3.data3 = arg_3_3.data3 + 1
				arg_3_3.data4 = arg_3_2.number[1]
				arg_3_3.data1_list[arg_3_1.arg1] = arg_3_3.data4
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_SHRINE:
		arg_3_3.data1 = 1
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_RED_PACKETS:
		arg_3_3.data1 = arg_3_3.data1 - 1

		if arg_3_3.data2 > 0:
			arg_3_3.data2 = arg_3_3.data2 - 1

		arg_3_3.data1_list[2] = arg_3_3.data1_list[2] + 1

		local var_3_32 = getProxy(ActivityProxy)
		local var_3_33 = var_3_32.getActivityByType(ActivityConst.ACTIVITY_TYPE_MONOPOLY)

		if var_3_33 and not var_3_33.isEnd() and var_3_33.data2_list[1] > var_3_33.data2_list[2]:
			var_3_33.data2_list[2] = var_3_33.data2_list[2] + 1

			var_3_32.updateActivity(var_3_33)
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_RED_PACKET_LOTTER:
		arg_3_3.data1 = arg_3_3.data1 + 1

		if not table.contains(arg_3_3.data2_list, arg_3_1.arg1):
			table.insert(arg_3_3.data2_list, arg_3_1.arg1)

		if not table.contains(arg_3_3.data1_list, arg_3_2.number[1]):
			table.insert(arg_3_3.data1_list, arg_3_2.number[1])
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF or var_3_0 == ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2:
		if arg_3_1.cmd == 1:
			local var_3_34 = pg.activity_event_building[arg_3_1.arg1]
			local var_3_35 = arg_3_3.GetBuildingLevel(arg_3_1.arg1)

			arg_3_3.SetBuildingLevel(arg_3_1.arg1, var_3_35 + 1)

			if var_3_35 < #var_3_34.buff:
				_.each(var_3_34.material[var_3_35], function(arg_5_0)
					local var_5_0 = arg_5_0[1]
					local var_5_1 = arg_5_0[2]
					local var_5_2 = arg_5_0[3]
					local var_5_3

					if var_5_0 == DROP_TYPE_VITEM:
						local var_5_4 = AcessWithinNull(Item.getConfigData(var_5_1), "link_id")

						assert(var_5_4 == arg_3_3.id)

						var_5_3 = arg_3_3
					elif var_5_0 > DROP_TYPE_USE_ACTIVITY_DROP:
						local var_5_5 = AcessWithinNull(pg.activity_drop_type[var_5_0], "activity_id")

						var_5_3 = getProxy(ActivityProxy).getActivityById(var_5_5)

					local var_5_6 = var_5_3.data1KeyValueList[1][var_5_1] or 0
					local var_5_7 = math.max(0, var_5_6 - var_5_2)

					var_5_3.data1KeyValueList[1][var_5_1] = var_5_7

					if var_5_0 > DROP_TYPE_USE_ACTIVITY_DROP:
						getProxy(ActivityProxy).updateActivity(var_5_3))
		elif arg_3_1.cmd == 2 and var_3_0 == ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2:
			arg_3_3.RecordLastRequestTime()
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_EXPEDITION:
		if arg_3_1.cmd == 0:
			return arg_3_3

		if arg_3_1.cmd == 3:
			arg_3_0.sendNotification(GAME.FINISH_STAGE_DONE, {
				statistics = arg_3_1.statistics,
				score = arg_3_1.statistics._battleScore,
				system = SYSTEM_REWARD_PERFORM
			})

			return arg_3_3

		if arg_3_1.cmd == 4:
			arg_3_3.data2_list[1] = arg_3_3.data2_list[1] + 1

			return arg_3_3

		if arg_3_1.cmd == 1:
			arg_3_3.data3 = arg_3_3.data3 - 1

		local var_3_36 = arg_3_1.arg1

		if arg_3_1.cmd != 2:
			arg_3_3.data2 = var_3_36

		local var_3_37 = arg_3_2.number[1]

		arg_3_3.data1_list[var_3_36] = var_3_37

		print("格子." .. var_3_36 .. " 值." .. arg_3_2.number[1])

		if arg_3_2.number[2] and arg_3_3.data1 != arg_3_2.number[2]:
			print("关卡变更" .. arg_3_2.number[2])

			arg_3_3.data1 = arg_3_3.data1 + 1
			arg_3_3.data2 = 0

			for iter_3_8 = 1, #arg_3_3.data1_list:
				arg_3_3.data1_list[iter_3_8] = 0
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_AIRFIGHT_BATTLE:
		if arg_3_1.cmd == 1:
			arg_3_0.sendNotification(GAME.FINISH_STAGE_DONE, {
				statistics = arg_3_1.statistics,
				score = arg_3_1.statistics._battleScore,
				system = SYSTEM_AIRFIGHT
			})

			arg_3_3.data1KeyValueList[1] = arg_3_3.data1KeyValueList[1] or {}
			arg_3_3.data1KeyValueList[1][arg_3_1.arg1] = (arg_3_3.data1KeyValueList[1][arg_3_1.arg1] or 0) + 1
		elif arg_3_1.cmd == 2:
			arg_3_3.data1KeyValueList[2] = arg_3_3.data1KeyValueList[2] or {}
			arg_3_3.data1KeyValueList[2][arg_3_1.arg1] = 1
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_SHAKE_BEADS:
		if arg_3_1.cmd == 1:
			arg_3_3.data1 = arg_3_3.data1 - 1

			local var_3_38 = arg_3_2.number[1]

			arg_3_3.data1KeyValueList[1][var_3_38] = arg_3_3.data1KeyValueList[1][var_3_38] + 1
		elif arg_3_1.cmd == 2:
			arg_3_3.data2 = 1
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_PT_OTHER:
		if arg_3_1.cmd == 1:
			arg_3_3.data2 = 1
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_HOTSPRING:
		if arg_3_1.cmd == SpringActivity.OPERATION_UNLOCK:
			arg_3_3.AddSlotCount()
		elif arg_3_1.cmd == SpringActivity.OPERATION_SETSHIP:
			arg_3_3.SetShipIds(arg_3_1.kvargs1)
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_HOTSPRING_2:
		if arg_3_1.cmd == Spring2Activity.OPERATION_SETSHIP:
			arg_3_3.SetShipIds(arg_3_1.kvargs1)
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_FIREWORK:
		if arg_3_1.cmd == 1:
			arg_3_3.data1 = arg_3_3.data1 - 1

			if not table.contains(arg_3_3.data1_list, arg_3_1.arg1):
				table.insert(arg_3_3.data1_list, arg_3_1.arg1)

			local var_3_39 = Item.getConfigData(arg_3_1.arg1).link_id

			if var_3_39 > 0:
				local var_3_40 = getProxy(ActivityProxy)
				local var_3_41 = var_3_40.getActivityById(var_3_39)

				if var_3_41 and not var_3_41.isEnd():
					var_3_41.data1 = var_3_41.data1 + 1

					var_3_40.updateActivity(var_3_41)

			local var_3_42 = getProxy(PlayerProxy)
			local var_3_43 = var_3_42.getRawData()
			local var_3_44 = arg_3_3.getConfig("config_data")[2][1]
			local var_3_45 = arg_3_3.getConfig("config_data")[2][2]

			var_3_43.consume({
				[id2res(var_3_44)] = var_3_45
			})
			var_3_42.updatePlayer(var_3_43)
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_CARD_PUZZLE:
		if not table.contains(arg_3_3.data1_list, arg_3_1.arg1):
			table.insert(arg_3_3.data1_list, arg_3_1.arg1)
	elif var_3_0 == ActivityConst.ACTIVITY_TYPE_ZUMA:
		if arg_3_1.cmd == 1:
			if arg_3_1.arg1 == LaunchBallGameConst.round_type_juqing:
				arg_3_3.data1 = arg_3_3.data1 + 1
			elif arg_3_1.arg1 == 2:
				if not arg_3_3.data1_list:
					arg_3_3.data1_list = {}

				table.insert(arg_3_3.data1_list, arg_3_1.arg2)
			elif arg_3_1.arg1 == 3:
				arg_3_3.data2 = arg_3_1.arg2
		elif arg_3_1.cmd == 2:
			arg_3_3.data3 = 1

		getProxy(ActivityProxy).updateActivity(arg_3_3)

	return arg_3_3

def var_0_0.performance(arg_6_0, arg_6_1, arg_6_2, arg_6_3, arg_6_4):
	local var_6_0 = arg_6_3.getConfig("type")
	local var_6_1

	local function var_6_2()
		if var_6_1 and coroutine.status(var_6_1) == "suspended":
			local var_7_0, var_7_1 = coroutine.resume(var_6_1)

			assert(var_7_0, var_7_1)

	var_6_1 = coroutine.create(function()
		if var_6_0 == ActivityConst.ACTIVITY_TYPE_7DAYSLOGIN:
			local var_8_0 = arg_6_3.getConfig("config_client").story

			if var_8_0 and var_8_0[arg_6_3.data1] and var_8_0[arg_6_3.data1][1]:
				pg.NewStoryMgr.GetInstance().Play(var_8_0[arg_6_3.data1][1], var_6_2)
				coroutine.yield()
		elif var_6_0 == ActivityConst.ACTIVITY_TYPE_BB:
			local var_8_1 = pg.gameset.bobing_memory.description[arg_6_3.data1]

			if var_8_1 and #var_8_1 > 0:
				pg.NewStoryMgr.GetInstance().Play(var_8_1, var_6_2)
				coroutine.yield()

			arg_6_0.sendNotification(ActivityProxy.ACTIVITY_SHOW_BB_RESULT, {
				numbers = arg_6_2.number,
				callback = var_6_2,
				awards = arg_6_4
			})
			coroutine.yield()
		elif var_6_0 == ActivityConst.ACTIVITY_TYPE_LOTTERY_AWARD:
			if arg_6_1.cmd == 1:
				local var_8_2 = arg_6_3.getConfig("config_client").story

				if var_8_2 and var_8_2[arg_6_3.data1] and var_8_2[arg_6_3.data1][1]:
					pg.NewStoryMgr.GetInstance().Play(var_8_2[arg_6_3.data1][1], var_6_2)
					coroutine.yield()

				arg_6_0.sendNotification(ActivityProxy.ACTIVITY_SHOW_LOTTERY_AWARD_RESULT, {
					activityID = arg_6_3.id,
					awards = arg_6_4,
					number = arg_6_2.number[1],
					callback = var_6_2
				})

				arg_6_4 = {}

				coroutine.yield()
		elif var_6_0 == ActivityConst.ACTIVITY_TYPE_CARD_PAIRS or var_6_0 == ActivityConst.ACTIVITY_TYPE_LINK_LINK:
			if arg_6_3.getConfig("config_client")[1]:
				local var_8_3 = arg_6_3.getConfig("config_client")[1][arg_6_3.data2 + 1]

				if var_8_3:
					pg.NewStoryMgr.GetInstance().Play(var_8_3, var_6_2)
					coroutine.yield()
		elif var_6_0 == ActivityConst.ACTIVITY_TYPE_DODGEM or var_6_0 == ActivityConst.ACTIVITY_TYPE_SUBMARINE_RUN:
			if arg_6_1.cmd == 2 and arg_6_2.number[3] > 0:
				local var_8_4 = arg_6_3.getConfig("config_client")[1]
				local var_8_5 = {
					type = var_8_4[1],
					id = var_8_4[2],
					count = var_8_4[3]
				}

				table.insert(arg_6_4, var_8_5)
		elif var_6_0 == ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF or var_6_0 == ActivityConst.ACTIVITY_TYPE_BUILDING_BUFF_2:
			if arg_6_1.cmd == 1:
				pg.TipsMgr.GetInstance().ShowTips(i18n("building_complete_tip"))
		elif var_6_0 == ActivityConst.ACTIVITY_TYPE_MONTHSIGN:
			if arg_6_1.cmd == 3:
				local var_8_6 = arg_6_3.getSpecialData("month_sign_awards") or {}

				for iter_8_0 = 1, #arg_6_4:
					table.insert(var_8_6, arg_6_4[iter_8_0])

				arg_6_3.setSpecialData("month_sign_awards", var_8_6)

				arg_6_4 = {}
		elif var_6_0 == ActivityConst.ACTIVITY_TYPE_SHAKE_BEADS:
			if arg_6_1.cmd == 1:
				arg_6_0.sendNotification(ActivityProxy.ACTIVITY_SHOW_SHAKE_BEADS_RESULT, {
					number = arg_6_2.number[1],
					callback = var_6_2,
					awards = arg_6_4
				})
				coroutine.yield()
		elif var_6_0 == ActivityConst.ACTIVITY_TYPE_APRIL_REWARD:
			if arg_6_1.cmd == 1:
				arg_6_3.data1 = arg_6_1.arg1
			elif arg_6_1.cmd == 2:
				arg_6_3.data2 = 1
		elif var_6_0 == ActivityConst.ACTIVITY_TYPE_FIREWORK:
			pg.TipsMgr.GetInstance().ShowTips(i18n("activity_yanhua_tip8"))

			local var_8_7 = #arg_6_3.getData1List()
			local var_8_8 = arg_6_3.getConfig("config_client").story

			if var_8_8 and type(var_8_8) == "table":
				for iter_8_1, iter_8_2 in ipairs(var_8_8):
					if var_8_7 == iter_8_2[1]:
						pg.NewStoryMgr.GetInstance().Play(iter_8_2[2], var_6_2)
						coroutine.yield()

		if #arg_6_4 > 0:
			arg_6_0.sendNotification(arg_6_3.getNotificationMsg(), {
				activityId = arg_6_1.activity_id,
				awards = arg_6_4,
				callback = var_6_2
			})
			coroutine.yield()

		if var_6_0 == 17 and arg_6_1.cmd and arg_6_1.cmd == 2:
			pg.TipsMgr.GetInstance().ShowTips(i18n("mingshi_get_tip"))

		getProxy(ActivityProxy).updateActivity(arg_6_3)
		arg_6_0.sendNotification(ActivityProxy.ACTIVITY_OPERATION_DONE, arg_6_1.activity_id))

	var_6_2()

return var_0_0