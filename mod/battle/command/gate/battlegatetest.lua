local var_0_0 = class("BattleGateTest")

ys.Battle.BattleGateTest = var_0_0
var_0_0.__name = "BattleGateTest"

function var_0_0.Entrance(arg_1_0, arg_1_1)
	if not arg_1_1.LegalFleet(arg_1_0.mainFleetId) then
		return
	end

	local var_1_0 = getProxy(BayProxy)
	local var_1_1 = getProxy(FleetProxy)
	local var_1_2 = {}
	local var_1_3 = var_1_1:getFleetById(arg_1_0.mainFleetId)
	local var_1_4 = var_1_0:getSortShipsByFleet(var_1_3)

	for iter_1_0, iter_1_1 in ipairs(var_1_4) do
		var_1_2[#var_1_2 + 1] = iter_1_1.id
	end

	local var_1_5 = arg_1_0.mainFleetId
	local var_1_6 = arg_1_0.stageId
	local var_1_7 = pg.expedition_data_template[var_1_6].dungeon_id

	local function var_1_8(arg_2_0)
		local var_2_0 = {
			mainFleetId = var_1_5,
			prefabFleet = {},
			stageId = var_1_6,
			system = SYSTEM_TEST,
			token = arg_2_0.key
		}

		arg_1_1:sendNotification(GAME.BEGIN_STAGE_DONE, var_2_0)
	end

	local function var_1_9(arg_3_0)
		arg_1_1:RequestFailStandardProcess(arg_3_0)
	end

	BeginStageCommand.SendRequest(SYSTEM_TEST, var_1_2, {
		var_1_6
	}, var_1_8, var_1_9)
end

function var_0_0.Exit(arg_4_0, arg_4_1)
	local var_4_0 = pg.battle_cost_template[SYSTEM_TEST]
	local var_4_1 = getProxy(FleetProxy)
	local var_4_2 = getProxy(BayProxy)
	local var_4_3 = arg_4_0.statistics._battleScore
	local var_4_4 = 0
	local var_4_5 = {}
	local var_4_6 = var_4_1:getFleetById(arg_4_0.mainFleetId)
	local var_4_7 = var_4_2:getSortShipsByFleet(var_4_6)
	local var_4_8 = arg_4_1.GeneralPackage(arg_4_0, var_4_7)

	local function var_4_9(arg_5_0)
		arg_4_0.statistics.mvpShipID = -1

		local var_5_0 = {
			system = SYSTEM_TEST,
			statistics = arg_4_0.statistics,
			score = var_4_3,
			drops = {},
			commanderExps = {},
			result = arg_5_0.result,
			extraDrops = {}
		}

		arg_4_1:sendNotification(GAME.FINISH_STAGE_DONE, var_5_0)
	end

	arg_4_1:SendRequest(var_4_8, var_4_9)
end

return var_0_0
