local var_0_0 = class("BatchGetCommanderCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody().boxIds
	local var_1_1 = {}
	local var_1_2 = {}
	local var_1_3 = {}

	for iter_1_0, iter_1_1 in ipairs(var_1_0) do
		table.insert(var_1_3, function(arg_2_0)
			if arg_1_0:CheckFullCapacity() then
				arg_2_0()

				return
			end

			arg_1_0:sendNotification(GAME.COMMANDER_ON_OPEN_BOX, {
				notify = false,
				id = iter_1_1,
				callback = function(arg_3_0)
					if arg_3_0 then
						table.insert(var_1_1, arg_3_0)
						table.insert(var_1_2, iter_1_1)
					end

					arg_2_0()
				end
			})
		end)
	end

	seriesAsync(var_1_3, function()
		arg_1_0:sendNotification(GAME.COMMANDER_ON_BATCH_DONE, {
			boxIds = var_1_2,
			commanders = var_1_1
		})
	end)
end

function var_0_0.CheckFullCapacity(arg_5_0)
	if getProxy(PlayerProxy):getRawData().commanderBagMax <= getProxy(CommanderProxy):getCommanderCnt() then
		return true
	end

	return false
end

return var_0_0
