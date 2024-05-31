local var_0_0 = class("BuildShip", import(".BaseVO"))

var_0_0.INACTIVE = 1
var_0_0.ACTIVE = 2
var_0_0.FINISH = 3

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0.type = arg_1_1.build_id
	arg_1_0.time = arg_1_1.time
	arg_1_0.finishTime = arg_1_1.finish_time
	arg_1_0.state = arg_1_0.INACTIVE
end

function var_0_0.setId(arg_2_0, arg_2_1)
	arg_2_0.id = arg_2_1
end

function var_0_0.setState(arg_3_0, arg_3_1)
	arg_3_0.state = arg_3_1
end

function var_0_0.isFinish(arg_4_0)
	return pg.TimeMgr.GetInstance():GetServerTime() >= arg_4_0.finishTime
end

function var_0_0.finish(arg_5_0)
	arg_5_0.time = 0
	arg_5_0.finishTime = pg.TimeMgr.GetInstance():GetServerTime()
	arg_5_0.state = arg_5_0.FINISH
end

function var_0_0.active(arg_6_0)
	arg_6_0.finishTime = pg.TimeMgr.GetInstance():GetServerTime() + arg_6_0.time
	arg_6_0.state = arg_6_0.ACTIVE
end

function var_0_0.setIsStart(arg_7_0, arg_7_1)
	arg_7_0.isStart = arg_7_1
end

function var_0_0.getLeftTime(arg_8_0)
	return arg_8_0.finishTime - pg.TimeMgr.GetInstance():GetServerTime()
end

function var_0_0.getBuildConsume(arg_9_0, arg_9_1, arg_9_2)
	local var_9_0 = pg.draw_data_template[arg_9_0]
	local var_9_1

	if arg_9_1 == 1 then
		arg_9_2 = math.min(arg_9_2 + 1, #var_9_0.use_gem_1)
		var_9_1 = var_9_0.use_gem_1[arg_9_2]
	else
		arg_9_2 = math.min(arg_9_2 + 1, #var_9_0.use_gem_10)
		var_9_1 = var_9_0.use_gem_10[arg_9_2]
	end

	return var_9_1
end

function var_0_0.canBuildShipByBuildId(arg_10_0, arg_10_1, arg_10_2)
	arg_10_1 = arg_10_1 or 1

	local var_10_0 = pg.ship_data_create_material[arg_10_0]

	if not var_10_0 then
		return false, i18n("ship_buildShip_error_noTemplate", arg_10_0)
	end

	local var_10_1 = getProxy(BuildShipProxy):getData()

	if table.getCount(var_10_1) + arg_10_1 > MAX_BUILD_WORK_COUNT then
		return false, i18n("ship_buildShip_not_position")
	end

	if arg_10_2 then
		local var_10_2 = getProxy(ActivityProxy):getBuildFreeActivityByBuildId(arg_10_0)
		local var_10_3 = var_10_2:getConfig("config_client")[1]
		local var_10_4 = Drop.New({
			type = DROP_TYPE_VITEM,
			id = var_10_3
		}):getName()

		if not var_10_2 or var_10_2:isEnd() then
			return false, i18n("tip_build_ticket_expired", var_10_4)
		elseif arg_10_1 > var_10_2.data1 then
			return false, i18n("tip_build_ticket_not_enough", var_10_4)
		end
	else
		local var_10_5 = {}
		local var_10_6 = getProxy(PlayerProxy):getData()

		if var_10_6.gold < var_10_0.use_gold * arg_10_1 then
			table.insert(var_10_5, {
				59001,
				var_10_0.use_gold * arg_10_1 - var_10_6.gold,
				var_10_0.use_gold * arg_10_1
			})
		end

		local var_10_7 = getProxy(BagProxy):getData()

		if not var_10_7[var_10_0.use_item] or var_10_7[var_10_0.use_item].count < var_10_0.number_1 * arg_10_1 then
			local var_10_8 = var_10_0.number_1 * arg_10_1
			local var_10_9 = var_10_0.use_item

			if var_10_7[var_10_0.use_item] then
				var_10_8 = var_10_0.number_1 * arg_10_1 - var_10_7[var_10_9].count
			end

			table.insert(var_10_5, {
				var_10_9,
				var_10_8,
				var_10_0.number_1 * arg_10_1
			})
		end

		if #var_10_5 > 0 then
			return false, i18n("ship_buildShip_error_notEnoughItem"), var_10_5
		end
	end

	return true
end

function var_0_0.canQuickBuildShip(arg_11_0)
	local var_11_0 = getProxy(BuildShipProxy):getBuildShip(arg_11_0)

	if not var_11_0 then
		return false, i18n("ship_buildShipImmediately_error_noSHip")
	end

	if var_11_0:isFinish() then
		return false, i18n("ship_buildShipImmediately_error_finished")
	end

	local var_11_1 = getProxy(BagProxy):getItemById(ITEM_ID_EQUIP_QUICK_FINISH) or {
		count = 0
	}

	if var_11_1.count <= 0 then
		local var_11_2 = {
			{
				ITEM_ID_EQUIP_QUICK_FINISH,
				1 - var_11_1.count,
				1
			}
		}

		return false, i18n("ship_buildShip_error_notEnoughItem"), var_11_2
	end

	return true
end

function var_0_0.getPageFromPoolType(arg_12_0)
	local var_12_0 = {
		[BuildShipScene.PAGE_BUILD] = {
			1,
			2,
			3,
			4,
			5
		},
		[BuildShipScene.PAGE_PRAY] = {
			6,
			7,
			8
		},
		[BuildShipScene.PAGE_NEWSERVER] = {
			11
		}
	}

	for iter_12_0, iter_12_1 in pairs(var_12_0) do
		if table.contains(iter_12_1, arg_12_0) then
			return iter_12_0
		end
	end
end

return var_0_0
