local var_0_0 = class("SelectFleetCommanderCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.fleetId
	local var_1_2 = var_1_0.pos
	local var_1_3 = var_1_0.commanderId
	local var_1_4 = var_1_0.callback
	local var_1_5 = getProxy(FleetProxy).getFleetById(var_1_1)
	local var_1_6 = var_1_5.getCommanderByPos(var_1_2)
	local var_1_7 = var_1_5.getCommanders()

	if not var_1_6 or var_1_6.id != var_1_3:
		local var_1_8 = getProxy(CommanderProxy).getCommanderById(var_1_3)

		for iter_1_0, iter_1_1 in pairs(var_1_7):
			if iter_1_1.groupId == var_1_8.groupId and iter_1_0 != var_1_2 and var_1_3 != iter_1_1.id:
				pg.TipsMgr.GetInstance().ShowTips(i18n("commander_can_not_select_same_group"))

				return

	local function var_1_9(arg_2_0)
		local var_2_0 = getProxy(FleetProxy).getCommanders()

		for iter_2_0, iter_2_1 in ipairs(var_2_0):
			if iter_2_1.fleetId != var_1_1 and iter_2_1.commanderId == arg_2_0:
				return True, iter_2_1

		return False

	local function var_1_10(arg_3_0)
		local var_3_0 = var_1_2 == 2 and 1 or 2
		local var_3_1 = var_1_7[var_3_0]

		if var_3_1 and var_3_1.id == arg_3_0:
			return True, var_3_0

		return False

	local var_1_11 = {}
	local var_1_12 = True
	local var_1_13, var_1_14 = var_1_9(var_1_3)

	if var_1_13:
		table.insert(var_1_11, function(arg_4_0)
			local var_4_0 = var_1_14.pos == 1 and i18n("commander_main_pos") or i18n("commander_assistant_pos")
			local var_4_1 = Fleet.DEFAULT_NAME[var_1_14.fleetId]

			pg.MsgboxMgr.GetInstance().ShowMsgBox({
				content = i18n("comander_repalce_tip", var_4_1, var_4_0),
				def onYes:()
					pg.m02.sendNotification(GAME.COOMMANDER_EQUIP_TO_FLEET, {
						commanderId = 0,
						fleetId = var_1_14.fleetId,
						pos = var_1_14.pos,
						callback = arg_4_0
					}),
				def onNo:()
					var_1_12 = False

					arg_4_0()
			}))

	local var_1_15, var_1_16 = var_1_10(var_1_3)

	if var_1_15:
		table.insert(var_1_11, function(arg_7_0)
			pg.m02.sendNotification(GAME.COOMMANDER_EQUIP_TO_FLEET, {
				commanderId = 0,
				fleetId = var_1_1,
				pos = var_1_16,
				callback = arg_7_0
			}))

	table.insert(var_1_11, function(arg_8_0)
		if var_1_12:
			pg.m02.sendNotification(GAME.COOMMANDER_EQUIP_TO_FLEET, {
				fleetId = var_1_1,
				pos = var_1_2,
				commanderId = var_1_3,
				def callback:(arg_9_0)
					arg_8_0()
			})
		else
			arg_8_0())
	seriesAsync(var_1_11, var_1_4)

return var_0_0
