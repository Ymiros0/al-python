﻿local var_0_0 = class("GetShipCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.type or 1
	local var_1_2 = var_1_0.pos_list
	local var_1_3 = getProxy(BuildShipProxy)
	local var_1_4 = underscore.filter(var_1_2, function(arg_2_0)
		return var_1_3:getBuildShip(arg_2_0).state == BuildShip.FINISH
	end)

	if #var_1_4 == 0 then
		pg.TipsMgr.GetInstance():ShowTips(i18n("ship_getShip_error_notFinish"))

		return
	end

	local var_1_5 = getProxy(BayProxy)
	local var_1_6 = getProxy(PlayerProxy):getData():getMaxShipBag() - var_1_5:getShipCount()

	if var_1_6 <= 0 then
		NoPosMsgBox(i18n("switch_to_shop_tip_noDockyard"), openDockyardClear, gotoChargeScene, openDockyardIntensify)

		return
	else
		var_1_4 = underscore.slice(var_1_4, 1, var_1_6)
	end

	local var_1_7 = {}

	table.insert(var_1_7, function(arg_3_0)
		pg.ConnectionMgr.GetInstance():Send(12043, {
			type = 0
		}, 12044, function(arg_4_0)
			local var_4_0 = {}

			for iter_4_0, iter_4_1 in ipairs(arg_4_0.infoList) do
				var_4_0[iter_4_1.pos] = iter_4_1.tid
			end

			arg_3_0(underscore.map(var_1_4, function(arg_5_0)
				return var_4_0[arg_5_0]
			end))
		end)
	end)
	table.insert(var_1_7, function(arg_6_0, arg_6_1)
		local var_6_0 = {}

		for iter_6_0, iter_6_1 in ipairs(arg_6_1) do
			PaintingGroupConst.AddPaintingNameByShipConfigID(var_6_0, iter_6_1)
		end

		local var_6_1 = {
			isShowBox = true,
			paintingNameList = var_6_0,
			finishFunc = arg_6_0
		}

		PaintingGroupConst.PaintingDownload(var_6_1)
	end)
	seriesAsync(var_1_7, function()
		local var_7_0 = var_1_3:getBuildShip(var_1_4[1]).type

		pg.ConnectionMgr.GetInstance():Send(12025, {
			type = var_1_1,
			pos_list = var_1_4
		}, 12026, function(arg_8_0)
			local var_8_0 = {}

			for iter_8_0, iter_8_1 in ipairs(arg_8_0.ship_list) do
				var_1_3:removeBuildShipByIndex(var_1_4[1])

				local var_8_1 = Ship.New(iter_8_1)

				table.insert(var_8_0, var_8_1)

				if var_8_1:isMetaShip() and not var_8_1.virgin and Player.isMetaShipNeedToTrans(var_8_1.configId) then
					local var_8_2 = MetaCharacterConst.addReMetaTransItem(var_8_1)

					if var_8_2 then
						var_8_1:setReMetaSpecialItemVO(var_8_2)
					end
				else
					var_1_5:addShip(var_8_1)
				end
			end

			if #var_8_0 > 0 then
				var_1_3:setBuildShipState()
				arg_1_0:sendNotification(GAME.GET_SHIP_DONE, {
					ships = var_8_0,
					type = var_7_0
				})
			end

			if arg_8_0.result == 0 then
				-- block empty
			else
				pg.TipsMgr.GetInstance():ShowTips(errorTip("ship_getShip", arg_8_0.result))
			end
		end)
	end)
end

return var_0_0
