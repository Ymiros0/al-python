local var_0_0 = class("PlayerProxy", import(".NetProxy"))

var_0_0.UPDATED = "PlayerProxy.UPDATED"

function var_0_0.register(arg_1_0)
	arg_1_0._flags = {}
	arg_1_0.combatFleetId = 1
	arg_1_0.mainBGShiftFlag = false
	arg_1_0.inited = false
	arg_1_0.botHelp = false
	arg_1_0.playerAssists = {}
	arg_1_0.playerGuildAssists = {}
	arg_1_0.summaryInfo = nil

	arg_1_0:on(11000, function(arg_2_0)
		arg_1_0:sendNotification(GAME.TIME_SYNCHRONIZATION, arg_2_0)
	end)
	arg_1_0:on(11003, function(arg_3_0)
		local var_3_0 = Player.New(arg_3_0)

		var_3_0.resUpdateTm = pg.TimeMgr.GetInstance():GetServerTime()

		arg_1_0:updatePlayer(var_3_0)
		pg.ShipFlagMgr.GetInstance():UpdateFlagShips("inAdmiral")
		pg.NewStoryMgr.GetInstance():SetData(arg_3_0.story_list or {})
		print("days from regist time to new :" .. arg_1_0.data:GetDaysFromRegister())

		if arg_1_0.data:GetDaysFromRegister() == 1 then
			pg.TrackerMgr.GetInstance():Tracking(TRACKING_2D_RETENTION)
		elseif arg_1_0.data:GetDaysFromRegister() == 6 then
			pg.TrackerMgr.GetInstance():Tracking(TRACKING_7D_RETENTION)
		end

		arg_1_0:flushTimesListener()
	end)
	arg_1_0:on(11004, function(arg_4_0)
		if not arg_1_0.data then
			return
		end

		local var_4_0 = arg_1_0.data:clone()

		var_4_0:updateResources(arg_4_0.resource_list)

		var_4_0.resUpdateTm = pg.TimeMgr.GetInstance():GetServerTime()

		arg_1_0:updatePlayer(var_4_0)

		if arg_1_0.data:isFull() then
			-- block empty
		end
	end)
	arg_1_0:on(10999, function(arg_5_0)
		if arg_5_0.reason == LOGOUT_NEW_VERSION then
			getProxy(SettingsProxy).lastRequestVersionTime = nil
		else
			arg_1_0:sendNotification(GAME.LOGOUT, {
				code = arg_5_0.reason
			})
		end
	end)
	arg_1_0:on(11015, function(arg_6_0)
		local var_6_0 = arg_1_0.data:clone()

		var_6_0.buff_list = {}

		for iter_6_0, iter_6_1 in ipairs(arg_6_0.buff_list) do
			local var_6_1 = {
				id = iter_6_1.id,
				timestamp = iter_6_1.timestamp
			}

			table.insert(var_6_0.buff_list, var_6_1)
		end

		arg_1_0:updatePlayer(var_6_0)
	end)
	arg_1_0:on(11503, function(arg_7_0)
		getProxy(ShopsProxy):removeChargeTimer(arg_7_0.pay_id)
		arg_1_0:sendNotification(GAME.CHARGE_SUCCESS, {
			shopId = arg_7_0.shop_id,
			payId = arg_7_0.pay_id,
			gem = arg_7_0.gem,
			gem_free = arg_7_0.gem_free
		})
	end)
	arg_1_0:on(11802, function(arg_8_0)
		local var_8_0 = arg_1_0.data:clone()

		var_8_0:SetCommonFlag(arg_8_0.id, arg_8_0.value == 1)
		arg_1_0:updatePlayer(var_8_0)
	end)
end

function var_0_0.remove(arg_9_0)
	arg_9_0:clearTimesListener()
end

function var_0_0.getSummaryInfo(arg_10_0)
	return arg_10_0.summaryInfo
end

function var_0_0.setSummaryInfo(arg_11_0, arg_11_1)
	arg_11_0.summaryInfo = arg_11_1
end

function var_0_0.flushTimesListener(arg_12_0)
	arg_12_0:clearTimesListener()

	local var_12_0 = pg.TimeMgr.GetInstance()

	arg_12_0.fourClockId = var_12_0:AddTimer("daily_four", var_12_0:GetNextTime(4, 0, 0) - var_12_0:GetServerTime(), 86400, function()
		arg_12_0:sendNotification(GAME.FOUR_HOUR)
	end)
end

function var_0_0.clearTimesListener(arg_14_0)
	if arg_14_0.fourClockId then
		pg.TimeMgr.GetInstance():RemoveTimer(arg_14_0.fourClockId)

		arg_14_0.fourClockId = nil
	end
end

function var_0_0.updatePlayer(arg_15_0, arg_15_1)
	assert(isa(arg_15_1, Player), "should be an instance of Player")

	if arg_15_0.data then
		arg_15_0:sendNotification(GAME.ON_PLAYER_RES_CHANGE, {
			oldPlayer = arg_15_0.data,
			newPlayer = arg_15_1
		})
	end

	arg_15_0.data = arg_15_1:clone()

	arg_15_0.data:display("updated")
	arg_15_0:sendNotification(var_0_0.UPDATED, arg_15_1:clone())
end

function var_0_0.UpdatePlayerRes(arg_16_0, arg_16_1)
	if not arg_16_0.data then
		return
	end

	local var_16_0 = {}
	local var_16_1 = {}

	for iter_16_0, iter_16_1 in ipairs(arg_16_1) do
		local var_16_2 = id2res(iter_16_1.id)

		if iter_16_1.count < 0 then
			var_16_1[var_16_2] = defaultValue(var_16_1[var_16_2], 0) - iter_16_1.count
		else
			var_16_0[var_16_2] = defaultValue(var_16_0[var_16_2], 0) + iter_16_1.count
		end
	end

	arg_16_0.data:addResources(var_16_0)
	arg_16_0.data:consume(var_16_1)
	arg_16_0:updatePlayer(arg_16_0.data)
end

function var_0_0.updatePlayerMedalDisplay(arg_17_0, arg_17_1)
	arg_17_0.data.displayTrophyList = arg_17_1
end

function var_0_0.getPlayerId(arg_18_0)
	return arg_18_0.data.id
end

function var_0_0.setFlag(arg_19_0, arg_19_1, arg_19_2)
	arg_19_0._flags[arg_19_1] = arg_19_2
end

function var_0_0.getFlag(arg_20_0, arg_20_1)
	return arg_20_0._flags[arg_20_1]
end

function var_0_0.isSelf(arg_21_0, arg_21_1)
	return arg_21_0.data.id == arg_21_1
end

function var_0_0.setInited(arg_22_0, arg_22_1)
	arg_22_0.inited = arg_22_1
end

function var_0_0.getInited(arg_23_0)
	return arg_23_0.inited
end

function var_0_0.setRefundInfo(arg_24_0, arg_24_1)
	local var_24_0

	if arg_24_1 and #arg_24_1 > 0 then
		var_24_0 = {}

		for iter_24_0, iter_24_1 in ipairs(arg_24_1) do
			table.insert(var_24_0, {
				shopId = iter_24_1.shop_id,
				buyTime = iter_24_1.buy_time,
				refundTime = iter_24_1.refund_time
			})
		end
	end

	arg_24_0.refundInfo = var_24_0
end

function var_0_0.getRefundInfo(arg_25_0)
	if not arg_25_0.refundInfo then
		return nil
	end

	if #arg_25_0.refundInfo <= 0 then
		return nil
	end

	return arg_25_0.refundInfo
end

function var_0_0.IsShowCommssionTip(arg_26_0)
	local var_26_0 = getProxy(EventProxy):hasFinishState()
	local var_26_1 = getProxy(NavalAcademyProxy)
	local var_26_2 = arg_26_0:getRawData()
	local var_26_3 = var_26_1:GetOilVO()
	local var_26_4 = var_26_1:GetGoldVO()
	local var_26_5 = var_26_1:GetClassVO()
	local var_26_6 = var_26_3:isCommissionNotify(var_26_2.oilField)
	local var_26_7 = var_26_4:isCommissionNotify(var_26_2.goldField)
	local var_26_8 = var_26_5:GetGenResCnt()
	local var_26_9 = var_26_5:GetEffectAttrs()
	local var_26_10 = 0

	for iter_26_0, iter_26_1 in ipairs(var_26_9) do
		if iter_26_1.attrName == "stock" then
			var_26_10 = iter_26_1.value
		end
	end

	local var_26_11 = NotifyTipHelper.ShouldShowUrTip()
	local var_26_12 = var_26_1:getStudents()
	local var_26_13 = 0

	_.each(_.values(var_26_12), function(arg_27_0)
		if arg_27_0:getFinishTime() <= pg.TimeMgr.GetInstance():GetServerTime() then
			var_26_13 = var_26_13 + 1
		end
	end)

	local var_26_14 = 0

	_.each(getProxy(TechnologyProxy):getPlanningTechnologys(), function(arg_28_0)
		if arg_28_0:isCompleted() then
			var_26_14 = var_26_14 + 1
		end
	end)

	local var_26_15 = WorldBossConst.GetCommissionSceneMetaBossBtnState()
	local var_26_16 = CommissionMetaBossBtn.STATE_GET_AWARDS == var_26_15 or CommissionMetaBossBtn.STATE_FINSH_BATTLE == var_26_15
	local var_26_17 = getProxy(ActivityProxy):getAliveActivityByType(ActivityConst.ACTIVITY_TYPE_PT_CRUSING)
	local var_26_18 = false

	if var_26_17 and not var_26_17:isEnd() then
		var_26_18 = #var_26_17:GetCrusingUnreceiveAward() > 0
	end

	return var_26_16 or var_26_0 or var_26_6 or var_26_7 or var_26_10 ~= 0 and var_26_8 > var_26_10 - 10 or var_26_11 or var_26_13 > 0 or var_26_14 > 0 or var_26_18
end

return var_0_0
