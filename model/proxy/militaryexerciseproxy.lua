local var_0_0 = class("MilitaryExerciseProxy", import(".NetProxy"))

var_0_0.SEASON_INFO_ADDED = "MilitaryExerciseProxy SEASON_INFO_ADDED"
var_0_0.SEASON_INFO_UPDATED = "MilitaryExerciseProxy SEASON_INFO_UPDATED"
var_0_0.ARENARANK_UPDATED = "MilitaryExerciseProxy ARENARANK_UPDATED"
var_0_0.EXERCISE_FLEET_UPDATED = "MilitaryExerciseProxy EXERCISE_FLEET_UPDATED"
var_0_0.RIVALS_UPDATED = "MilitaryExerciseProxy RIVALS_UPDATED"

function var_0_0.register(arg_1_0)
	arg_1_0:on(18005, function(arg_2_0)
		local var_2_0 = {}

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.target_list) do
			table.insert(var_2_0, Rival.New(iter_2_1))
		end

		local var_2_1 = arg_1_0:getSeasonInfo()

		var_2_1:updateScore(arg_2_0.score + SeasonInfo.INIT_POINT)
		var_2_1:updateRank(arg_2_0.rank)
		var_2_1:updateRivals(var_2_0)
		arg_1_0:updateSeasonInfo(var_2_1)

		local var_2_2 = getProxy(PlayerProxy)
		local var_2_3 = var_2_2:getData()

		var_2_3:updateScoreAndRank(var_2_1.score, var_2_1.rank)
		var_2_2:updatePlayer(var_2_3)
	end)
end

function var_0_0.addSeasonInfo(arg_3_0, arg_3_1)
	assert(isa(arg_3_1, SeasonInfo), "seasonInfo be an instance of SeasonInfo")

	arg_3_0.seasonInfo = arg_3_1

	pg.ShipFlagMgr.GetInstance():UpdateFlagShips("inExercise")
	arg_3_0:sendNotification(var_0_0.SEASON_INFO_ADDED, arg_3_1:clone())
	arg_3_0:addRefreshCountTimer()
end

function var_0_0.addRefreshCountTimer(arg_4_0)
	arg_4_0:removeRefreshTimer()

	local function var_4_0()
		arg_4_0:sendNotification(GAME.EXERCISE_COUNT_RECOVER_UP)
	end

	local var_4_1 = arg_4_0.seasonInfo.resetTime - pg.TimeMgr.GetInstance():GetServerTime()

	if var_4_1 > 0 then
		arg_4_0.refreshCountTimer = Timer.New(function()
			var_4_0()
		end, var_4_1, 1)

		arg_4_0.refreshCountTimer:Start()
	else
		var_4_0()
	end
end

function var_0_0.addSeasonOverTimer(arg_7_0)
	arg_7_0:removeSeasonOverTimer()

	local var_7_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_MILITARY_EXERCISE)

	if var_7_0 and not var_7_0:isEnd() then
		local function var_7_1()
			arg_7_0:removeSeasonOverTimer()

			local var_8_0 = arg_7_0:getSeasonInfo()

			var_8_0:setExerciseCount(0)
			arg_7_0:updateSeasonInfo(var_8_0)
		end

		local var_7_2 = var_7_0.stopTime - pg.TimeMgr.GetInstance():GetServerTime()

		if var_7_2 > 0 then
			arg_7_0.SeasonOverTimer = Timer.New(function()
				var_7_1()
			end, var_7_2, 1)

			arg_7_0.SeasonOverTimer:Start()
		else
			var_7_1()
		end
	end
end

function var_0_0.removeRefreshTimer(arg_10_0)
	if arg_10_0.refreshCountTimer then
		arg_10_0.refreshCountTimer:Stop()

		arg_10_0.refreshCountTimer = nil
	end
end

function var_0_0.removeSeasonOverTimer(arg_11_0)
	if arg_11_0.SeasonOverTimer then
		arg_11_0.SeasonOverTimer:Stop()

		arg_11_0.SeasonOverTimer = nil
	end
end

function var_0_0.remove(arg_12_0)
	arg_12_0:removeRefreshTimer()
	arg_12_0:removeSeasonOverTimer()
end

function var_0_0.updateSeasonInfo(arg_13_0, arg_13_1)
	assert(isa(arg_13_1, SeasonInfo), "seasonInfo be an instance of SeasonInfo")

	arg_13_0.seasonInfo = arg_13_1

	pg.ShipFlagMgr.GetInstance():UpdateFlagShips("inExercise")
	arg_13_0:sendNotification(var_0_0.SEASON_INFO_UPDATED, arg_13_1:clone())
end

function var_0_0.getSeasonInfo(arg_14_0)
	return Clone(arg_14_0.seasonInfo)
end

function var_0_0.RawGetSeasonInfo(arg_15_0)
	return arg_15_0.seasonInfo
end

function var_0_0.updateRivals(arg_16_0, arg_16_1)
	arg_16_0.seasonInfo:updateRivals(arg_16_1)
	arg_16_0:sendNotification(var_0_0.RIVALS_UPDATED, Clone(arg_16_1))
end

function var_0_0.getRivals(arg_17_0)
	return Clone(arg_17_0.seasonInfo.rivals)
end

function var_0_0.getRivalById(arg_18_0, arg_18_1)
	for iter_18_0, iter_18_1 in ipairs(arg_18_0:getRivals()) do
		if iter_18_1.id == arg_18_1 then
			return iter_18_1
		end
	end
end

function var_0_0.getPreRivalById(arg_19_0, arg_19_1)
	for iter_19_0, iter_19_1 in pairs(arg_19_0.seasonInfo:GetPreRivals()) do
		if arg_19_1 == iter_19_0 then
			return Clone(iter_19_1)
		end
	end
end

function var_0_0.getExerciseFleet(arg_20_0)
	return Clone(arg_20_0.seasonInfo.fleet)
end

function var_0_0.updateExerciseFleet(arg_21_0, arg_21_1)
	arg_21_0.seasonInfo:updateFleet(arg_21_1)
	pg.ShipFlagMgr.GetInstance():UpdateFlagShips("inExercise")
	arg_21_0:sendNotification(var_0_0.EXERCISE_FLEET_UPDATED, arg_21_1:clone())
end

function var_0_0.increaseExerciseCount(arg_22_0)
	arg_22_0.seasonInfo:increaseExerciseCount()
end

function var_0_0.reduceExerciseCount(arg_23_0)
	arg_23_0.seasonInfo:reduceExerciseCount()
end

function var_0_0.updateArenaRankLsit(arg_24_0, arg_24_1)
	assert(arg_24_1, "should exist arenaRankLsit")

	arg_24_0.arenaRankLsit = arg_24_1

	arg_24_0:sendNotification(var_0_0.ARENARANK_UPDATED, Clone(arg_24_1))
end

function var_0_0.getArenaRankList(arg_25_0)
	return arg_25_0.arenaRankLsit
end

function var_0_0.getData(arg_26_0)
	return Clone(arg_26_0.seasonInfo)
end

return var_0_0
