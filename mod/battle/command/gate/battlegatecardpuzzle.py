local var_0_0 = class("BattleGateCardPuzzle")

ys.Battle.BattleGateCardPuzzle = var_0_0
var_0_0.__name = "BattleGateCardPuzzle"

def var_0_0.Entrance(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_0.combatID
	local var_1_1 = ys.Battle.BattleDataFunction.GetPuzzleDungeonTemplate(var_1_0)
	local var_1_2 = var_1_1.dungeon_id
	local var_1_3 = {
		CardPuzzleShip.New({
			configId = var_1_1.scout_id
		}),
		CardPuzzleShip.New({
			configId = var_1_1.main_id
		})
	}
	local var_1_4 = var_1_1.deck
	local var_1_5 = {}

	for iter_1_0, iter_1_1 in ipairs(var_1_1.relic):
		table.insert(var_1_5, CardPuzzleGift.New({
			configId = iter_1_1
		}))

	;(function(arg_2_0)
		local var_2_0 = {
			hp = 1,
			cardPuzzleFleet = var_1_3,
			prefabFleet = {},
			cards = var_1_4,
			relics = var_1_5,
			stageId = var_1_2,
			system = SYSTEM_CARDPUZZLE,
			puzzleCombatID = var_1_0
		}

		arg_1_1.sendNotification(GAME.BEGIN_STAGE_DONE, var_2_0))()

def var_0_0.Exit(arg_3_0, arg_3_1):
	local var_3_0 = arg_3_0.statistics._battleScore

	print(var_3_0)

	if var_3_0 >= ys.Battle.BattleConst.BattleScore.S:
		local var_3_1 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_CARD_PUZZLE)

		arg_3_1.sendNotification(GAME.ACT_CARD_PUZZLE, {
			cmd = 1,
			activity_id = var_3_1 and var_3_1.id,
			arg1 = arg_3_0.puzzleCombatID
		})

	local var_3_2 = {
		system = SYSTEM_CARDPUZZLE,
		score = var_3_0
	}

	arg_3_1.sendNotification(GAME.FINISH_STAGE_DONE, var_3_2)

return var_0_0
