local var_0_0 = class("MiniGameProxy", import(".NetProxy"))

var_0_0.ON_HUB_DATA_UPDATE = "on hub data update"
var_0_0.ON_MINI_GAME_DATA_UPDATE = "on_mini_game_data_update"

function var_0_0.register(arg_1_0)
	arg_1_0.miniGameHubDataDic = {}
	arg_1_0.miniGameDataDic = {}
end

function var_0_0.CheckHasHub(arg_2_0, arg_2_1)
	return arg_2_0.miniGameHubDataDic[arg_2_1] ~= nil
end

function var_0_0.GetMiniGameData(arg_3_0, arg_3_1)
	if arg_3_0.miniGameDataDic[arg_3_1] == nil then
		local var_3_0 = {
			id = arg_3_1
		}

		arg_3_0.miniGameDataDic[arg_3_1] = MiniGameData.New(var_3_0)
	end

	return arg_3_0.miniGameDataDic[arg_3_1]
end

function var_0_0.GetMiniGameDataByType(arg_4_0, arg_4_1)
	for iter_4_0, iter_4_1 in pairs(arg_4_0.miniGameDataDic) do
		if iter_4_1:getConfig("type") == arg_4_1 and iter_4_1:CheckInTime() then
			return iter_4_1
		end
	end
end

function var_0_0.GetHubByHubId(arg_5_0, arg_5_1)
	if arg_5_0.miniGameHubDataDic[arg_5_1] == nil then
		local var_5_0 = {
			id = arg_5_1
		}

		arg_5_0.miniGameHubDataDic[arg_5_1] = MiniGameHubData.New(var_5_0)
	end

	return arg_5_0.miniGameHubDataDic[arg_5_1]
end

function var_0_0.GetHubByGameId(arg_6_0, arg_6_1)
	local var_6_0 = arg_6_0:GetMiniGameData(arg_6_1):getConfig("hub_id")

	if arg_6_0.miniGameHubDataDic[var_6_0] == nil then
		local var_6_1 = {
			id = var_6_0
		}

		arg_6_0.miniGameHubDataDic[var_6_0] = MiniGameHubData.New(var_6_1)
	end

	return arg_6_0.miniGameHubDataDic[var_6_0]
end

function var_0_0.UpdataHubData(arg_7_0, arg_7_1)
	local var_7_0 = arg_7_1.id
	local var_7_1 = arg_7_0:GetHubByHubId(var_7_0)

	var_7_1:UpdateData(arg_7_1)
	arg_7_0.facade:sendNotification(var_0_0.ON_HUB_DATA_UPDATE, var_7_1)
end

function var_0_0.GetHighScore(arg_8_0, arg_8_1)
	return arg_8_0:GetHubByGameId(arg_8_1).highScores[arg_8_1] or {}
end

function var_0_0.UpdataHighScore(arg_9_0, arg_9_1, arg_9_2)
	local var_9_0 = arg_9_0:GetHubByGameId(arg_9_1)
	local var_9_1 = 0

	if var_9_0.highScores[arg_9_1] and var_9_0.highScores[arg_9_1][1] then
		var_9_1 = var_9_0.highScores[arg_9_1][1]
	end

	if var_9_1 <= arg_9_2[1] then
		var_9_0.highScores[arg_9_1] = arg_9_2

		arg_9_0:UpdataHubData(var_9_0)

		local var_9_2 = {
			arg_9_1
		}

		for iter_9_0, iter_9_1 in ipairs(arg_9_2) do
			table.insert(var_9_2, iter_9_1)
		end

		arg_9_0:sendNotification(GAME.SEND_MINI_GAME_OP, {
			hubid = var_9_0.id,
			cmd = MiniGameOPCommand.CMD_HIGH_SCORE,
			args1 = var_9_2
		})
	end
end

function var_0_0.GetRank(arg_10_0, arg_10_1)
	return arg_10_0:GetMiniGameData(arg_10_1):GetRank()
end

function var_0_0.SetRank(arg_11_0, arg_11_1, arg_11_2)
	arg_11_0:GetMiniGameData(arg_11_1):SetRank(arg_11_2)
end

function var_0_0.CanFetchRank(arg_12_0, arg_12_1)
	return arg_12_0:GetMiniGameData(arg_12_1):CanFetchRank()
end

function var_0_0.RequestInitData(arg_13_0, arg_13_1, arg_13_2)
	local var_13_0 = arg_13_0:GetMiniGameData(arg_13_1)
	local var_13_1 = var_13_0:getConfig("request_data") == 1

	if arg_13_2 and not var_13_1 then
		return
	end

	if var_13_0:CheckInTime() then
		local var_13_2 = arg_13_0:GetHubByGameId(arg_13_1)
		local var_13_3 = var_13_0:getConfig("type")

		if (var_13_3 == MiniGameConst.MG_TYPE_2 or var_13_3 == MiniGameConst.MG_TYPE_3 or var_13_3 == MiniGameConst.MG_TYPE_5) and not var_13_0:GetRuntimeData("fetchData") then
			arg_13_0:sendNotification(GAME.SEND_MINI_GAME_OP, {
				hubid = var_13_2.id,
				cmd = MiniGameOPCommand.CMD_SPECIAL_GAME,
				args1 = {
					var_13_0.id,
					1
				}
			})
			var_13_0:SetRuntimeData("fetchData", true)
		end
	end
end

function var_0_0.remove(arg_14_0)
	return
end

return var_0_0
