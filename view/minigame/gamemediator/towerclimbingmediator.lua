local var_0_0 = class("TowerClimbingMediator", import("...base.ContextMediator"))

var_0_0.ON_FINISH = "TowerClimbingMediator:ON_FINISH"
var_0_0.ON_MODIFY_DATA = "TowerClimbingMediator:ON_MODIFY_DATA"
var_0_0.ON_COLLECTION = "TowerClimbingMediator:ON_COLLECTION"
var_0_0.ON_RECORD_MAP_SCORE = "TowerClimbingMediator:ON_RECORD_MAP_SCORE"

function var_0_0.register(arg_1_0)
	arg_1_0:bind(var_0_0.ON_RECORD_MAP_SCORE, function(arg_2_0, arg_2_1, arg_2_2)
		arg_1_0:sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = 9,
			cmd = MiniGameOPCommand.CMD_SPECIAL_GAME,
			args1 = {
				MiniGameDataCreator.TowerClimbingGameID,
				4,
				arg_2_2,
				arg_2_1
			}
		})
	end)
	arg_1_0:bind(var_0_0.ON_COLLECTION, function(arg_3_0)
		arg_1_0:addSubLayers(Context.New({
			viewComponent = TowerClimbingCollectionLayer,
			mediator = TowerClimbingCollectionMediator
		}))
	end)
	arg_1_0:bind(var_0_0.ON_FINISH, function(arg_4_0, arg_4_1, arg_4_2, arg_4_3)
		if arg_4_3 < arg_4_1 then
			arg_1_0:sendNotification(GAME.SEND_MINI_GAME_OP, {
				hubid = 9,
				cmd = MiniGameOPCommand.CMD_SPECIAL_GAME,
				args1 = {
					MiniGameDataCreator.TowerClimbingGameID,
					3,
					arg_4_1,
					arg_4_2
				}
			})
		end

		if getProxy(MiniGameProxy):GetHubByGameId(MiniGameDataCreator.TowerClimbingGameID).count <= 0 then
			return
		end

		arg_1_0:sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = 9,
			cmd = MiniGameOPCommand.CMD_COMPLETE,
			args1 = {},
			id = MiniGameDataCreator.TowerClimbingGameID
		})
	end)
	arg_1_0:bind(var_0_0.ON_MODIFY_DATA, function(arg_5_0, arg_5_1)
		arg_1_0:sendNotification(GAME.MODIFY_MINI_GAME_DATA, {
			id = MiniGameDataCreator.TowerClimbingGameID,
			map = arg_5_1
		})
	end)

	local var_1_0 = getProxy(MiniGameProxy):GetMiniGameData(MiniGameDataCreator.TowerClimbingGameID)

	if var_1_0 and not var_1_0:GetRuntimeData("isInited") then
		arg_1_0:sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = 9,
			cmd = MiniGameOPCommand.CMD_SPECIAL_GAME,
			args1 = {
				MiniGameDataCreator.TowerClimbingGameID,
				1
			}
		})
	else
		arg_1_0.viewComponent:Start()
	end
end

function var_0_0.listNotificationInterests(arg_6_0)
	return {
		GAME.SEND_MINI_GAME_OP_DONE,
		GAME.REMOVE_LAYERS
	}
end

function var_0_0.handleNotification(arg_7_0, arg_7_1)
	local var_7_0 = arg_7_1:getName()
	local var_7_1 = arg_7_1:getBody()

	if var_7_0 == GAME.SEND_MINI_GAME_OP_DONE then
		local var_7_2 = {
			function(arg_8_0)
				local var_8_0 = var_7_1.awards

				if #var_8_0 > 0 then
					arg_7_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_8_0, arg_8_0)
				else
					arg_8_0()
				end
			end
		}

		seriesAsync(var_7_2)
		arg_7_0.viewComponent:OnSendMiniGameOPDone(var_7_1)
	elseif var_7_0 == GAME.REMOVE_LAYERS and var_7_1.context.mediator == TowerClimbingCollectionMediator then
		arg_7_0.viewComponent:UpdateTip()
	end
end

return var_0_0
