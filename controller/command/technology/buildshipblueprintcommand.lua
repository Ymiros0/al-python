local var_0_0 = class("BuildShipBluePrintCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.hideTip
	local var_1_3 = getProxy(TechnologyProxy)
	local var_1_4 = var_1_3:getBluePrintById(var_1_1)
	local var_1_5, var_1_6 = var_1_4:isFinishPrevTask()

	if not var_1_6 then
		pg.TipsMgr.GetInstance():ShowTips("without finish pre task")

		return
	end

	local var_1_7 = var_1_3:getColdTime()
	local var_1_8 = pg.TimeMgr.GetInstance():GetServerTime()

	if var_1_8 < var_1_7 then
		local var_1_9 = var_1_7 - var_1_8

		var_1_9 = var_1_9 < 0 and 0 or var_1_9

		local var_1_10 = math.floor(var_1_9 / 86400)
		local var_1_11

		if var_1_10 > 0 then
			var_1_11 = i18n("time_remaining_tip") .. var_1_10 .. i18n("word_date")
		else
			local var_1_12 = math.floor(var_1_9 / 3600)

			if var_1_12 > 0 then
				var_1_11 = i18n("time_remaining_tip") .. var_1_12 .. i18n("word_hour")
			else
				local var_1_13 = math.floor(var_1_9 / 60)

				if var_1_13 > 0 then
					var_1_11 = i18n("time_remaining_tip") .. var_1_13 .. i18n("word_minute")
				else
					var_1_11 = i18n("time_remaining_tip") .. var_1_9 .. i18n("word_second")
				end
			end
		end

		pg.TipsMgr.GetInstance():ShowTips(i18n("blueprint_cannot_build_tip", var_1_11))

		return
	end

	local var_1_14 = {}
	local var_1_15 = var_1_3:getBuildingBluePrint()

	if var_1_15 then
		table.insert(var_1_14, function(arg_2_0)
			local var_2_0 = var_1_15:getShipVO()
			local var_2_1 = var_1_4:getShipVO()

			pg.MsgboxMgr.GetInstance():ShowMsgBox({
				content = i18n("cannot_build_multiple_printblue", var_2_0:getConfig("name"), var_2_1:getConfig("name")),
				onYes = function()
					arg_1_0:sendNotification(GAME.STOP_BLUEPRINT, {
						id = var_1_15.id,
						callback = arg_2_0
					})
				end
			})
		end)
	else
		table.insert(var_1_14, function(arg_4_0)
			pg.MsgboxMgr.GetInstance():ShowMsgBox({
				content = i18n("blueprint_build_time_tip"),
				onYes = arg_4_0
			})
		end)
	end

	seriesAsync(var_1_14, function()
		pg.ConnectionMgr.GetInstance():Send(63200, {
			blueprint_id = var_1_1
		}, 63201, function(arg_6_0)
			if arg_6_0.result == 0 then
				var_1_3:updateColdTime()
				var_1_4:start(arg_6_0.time)
				var_1_3:updateBluePrint(var_1_4)
				arg_1_0:sendNotification(GAME.BUILD_SHIP_BLUEPRINT_DONE)
			else
				pg.TipsMgr.GetInstance():ShowTips(i18n("printblue_build_erro") .. arg_6_0.result)
			end
		end)
	end)
end

return var_0_0
