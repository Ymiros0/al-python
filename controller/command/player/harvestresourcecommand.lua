﻿local var_0_0 = class("HarvestResourceCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = id2res(var_1_0)
	local var_1_2 = getProxy(PlayerProxy)
	local var_1_3 = var_1_2:getData()
	local var_1_4

	if var_1_0 == 1 then
		var_1_4 = var_1_3:getLevelMaxGold()
	elseif var_1_0 == 2 then
		var_1_4 = var_1_3:getLevelMaxOil()
	else
		assert(false)
	end

	if var_1_4 <= var_1_3[var_1_1] then
		pg.TipsMgr.GetInstance():ShowTips(i18n("player_harvestResource_error_fullBag"))

		return
	end

	pg.ConnectionMgr.GetInstance():Send(11013, {
		number = 0,
		type = var_1_0
	}, 11014, function(arg_2_0)
		if arg_2_0.result == 0 then
			local var_2_0 = var_1_4 - var_1_3[var_1_1]
			local var_2_1 = 0

			if var_2_0 < var_1_3[var_1_1 .. "Field"] then
				var_2_1 = var_2_0

				var_1_3:addResources({
					[var_1_1] = var_2_0
				})

				var_1_3[var_1_1 .. "Field"] = var_1_3[var_1_1 .. "Field"] - var_2_0
			else
				var_2_1 = var_1_3[var_1_1 .. "Field"]

				var_1_3:addResources({
					[var_1_1] = var_1_3[var_1_1 .. "Field"]
				})

				var_1_3[var_1_1 .. "Field"] = 0
			end

			var_1_2:updatePlayer(var_1_3)
			arg_1_0:sendNotification(GAME.HARVEST_RES_DONE, {
				type = var_1_0,
				outPut = var_2_1
			})
			pg.CriMgr.GetInstance():PlaySoundEffect_V3(SFX_UI_ACADEMY_GETMATERIAL)
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("player_harvestResource", arg_2_0.result))
		end
	end)
end

return var_0_0
