local var_0_0 = class("ActivityShopWithProgressRewardCommand", pm.SimpleCommand)

var_0_0.SHOW_SHOP_REWARD = "ActivityShopWithProgressRewardCommand Show shop reward"

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = getProxy(ActivityProxy).getActivityById(var_1_0.activity_id)
	local var_1_2 = var_1_1.getConfig("type")

	assert(var_1_2 == ActivityConst.ACTIVITY_TYPE_SHOP_PROGRESS_REWARD, "Operation Cant Fit ActivityType " .. var_1_2)

	if var_1_2 == ActivityConst.ACTIVITY_TYPE_SHOP_PROGRESS_REWARD:
		if var_1_0.cmd == 1:
			local var_1_3 = getProxy(PlayerProxy).getData()
			local var_1_4 = pg.activity_shop_template[var_1_0.arg1]
			local var_1_5 = var_1_0.arg2 or 1

			if var_1_3[id2res(var_1_4.resource_type)] < var_1_4.resource_num * var_1_5:
				pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_resource"))

				return

			if var_1_4.commodity_type == 1:
				if var_1_4.commodity_id == 1 and var_1_3.GoldMax(var_1_4.num * var_1_5):
					pg.TipsMgr.GetInstance().ShowTips(i18n("gold_max_tip_title") .. i18n("resource_max_tip_shop"))

					return

				if var_1_4.commodity_id == 2 and var_1_3.OilMax(var_1_4.num * var_1_5):
					pg.TipsMgr.GetInstance().ShowTips(i18n("oil_max_tip_title") .. i18n("resource_max_tip_shop"))

					return
		elif var_1_0.cmd == 2 and table.contains(var_1_1.data3_list, var_1_0.arg1):
			pg.TipsMgr.GetInstance().ShowTips(i18n("common_count_noenough"))

			return

	pg.ConnectionMgr.GetInstance().Send(11202, {
		activity_id = var_1_0.activity_id,
		cmd = var_1_0.cmd,
		arg1 = var_1_0.arg1,
		arg2 = var_1_0.arg2,
		arg_list = {}
	}, 11203, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = arg_1_0.getAwards(var_1_0, arg_2_0)
			local var_2_1 = getProxy(ActivityProxy).getActivityById(var_1_0.activity_id)
			local var_2_2 = arg_1_0.updateActivityData(var_1_0, arg_2_0, var_2_1, var_2_0)

			arg_1_0.performance(var_1_0, arg_2_0, var_2_2, var_2_0)
		else
			print("activity op ret code. " .. arg_2_0.result)

			if arg_2_0.result == 3 or arg_2_0.result == 4:
				pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))
			else
				pg.TipsMgr.GetInstance().ShowTips(errorTip("activity_op_error", arg_2_0.result))

			arg_1_0.sendNotification(ActivityProxy.ACTIVITY_OPERATION_ERRO, {
				actId = var_1_0.activity_id,
				code = arg_2_0.result
			}))

def var_0_0.getAwards(arg_3_0, arg_3_1, arg_3_2):
	local var_3_0 = {}

	for iter_3_0, iter_3_1 in ipairs(arg_3_2.award_list):
		local var_3_1 = {
			type = iter_3_1.type,
			id = iter_3_1.id,
			count = iter_3_1.number
		}

		table.insert(var_3_0, var_3_1)

	local var_3_2 = PlayerConst.addTranDrop(var_3_0)

	for iter_3_2, iter_3_3 in ipairs(var_3_0):
		if iter_3_3.type == DROP_TYPE_SHIP:
			local var_3_3 = pg.ship_data_template[iter_3_3.id]

			if not getProxy(CollectionProxy).getShipGroup(var_3_3.group_type) and Ship.inUnlockTip(iter_3_3.id):
				pg.TipsMgr.GetInstance().ShowTips(i18n("collection_award_ship", var_3_3.name))

	if arg_3_1.isAwardMerge:
		local var_3_4 = {}
		local var_3_5

		for iter_3_4, iter_3_5 in ipairs(var_3_2):
			if (function()
				for iter_4_0, iter_4_1 in ipairs(var_3_4):
					if iter_3_5.id == iter_4_1.id:
						var_3_4[iter_4_0].count = var_3_4[iter_4_0].count + iter_3_5.count

						return False

				return True)():
				table.insert(var_3_4, iter_3_5)

		var_3_2 = var_3_4

	return var_3_2

def var_0_0.updateActivityData(arg_5_0, arg_5_1, arg_5_2, arg_5_3, arg_5_4):
	local var_5_0 = arg_5_3.getConfig("type")
	local var_5_1 = getProxy(PlayerProxy)
	local var_5_2 = getProxy(TaskProxy)

	if var_5_0 == ActivityConst.ACTIVITY_TYPE_SHOP_PROGRESS_REWARD:
		if arg_5_1.cmd == 1:
			if table.contains(arg_5_3.data1_list, arg_5_1.arg1):
				for iter_5_0, iter_5_1 in ipairs(arg_5_3.data1_list):
					if iter_5_1 == arg_5_1.arg1:
						arg_5_3.data2_list[iter_5_0] = arg_5_3.data2_list[iter_5_0] + arg_5_1.arg2

						break
			else
				table.insert(arg_5_3.data1_list, arg_5_1.arg1)
				table.insert(arg_5_3.data2_list, arg_5_1.arg2)

			local var_5_3 = pg.activity_shop_template[arg_5_1.arg1]
			local var_5_4 = var_5_3.resource_num * arg_5_1.arg2
			local var_5_5 = var_5_1.getData()

			var_5_5.consume({
				[id2res(var_5_3.resource_type)] = var_5_4
			})
			var_5_1.updatePlayer(var_5_5)
		elif arg_5_1.cmd == 2:
			table.insert(arg_5_3.data3_list, arg_5_1.arg1)

	return arg_5_3

def var_0_0.performance(arg_6_0, arg_6_1, arg_6_2, arg_6_3, arg_6_4):
	arg_6_0.sendNotification(var_0_0.SHOW_SHOP_REWARD, {
		activityId = arg_6_1.activity_id,
		shopType = arg_6_1.cmd,
		awards = arg_6_4,
		def callback:()
			getProxy(ActivityProxy).updateActivity(arg_6_3)
	})

return var_0_0
