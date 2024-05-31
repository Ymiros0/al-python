local var_0_0 = class("BuildCommaderCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.id
	local var_1_2 = var_1_0.callback
	local var_1_3 = var_1_0.tip
	local var_1_4 = getProxy(CommanderProxy)
	local var_1_5 = var_1_4.getPoolById(var_1_1)
	local var_1_6 = getProxy(PlayerProxy).getData()
	local var_1_7 = getProxy(BagProxy)
	local var_1_8 = var_1_5.getConsume()
	local var_1_9 = {}

	for iter_1_0, iter_1_1 in ipairs(var_1_8):
		if iter_1_1[1] == DROP_TYPE_RESOURCE:
			if var_1_6.getResById(iter_1_1[2]) < iter_1_1[3]:
				pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_resource"))

				return
		elif iter_1_1[1] == DROP_TYPE_ITEM:
			local var_1_10 = iter_1_1[2]

			if var_1_7.getItemCountById(var_1_10) < iter_1_1[3]:
				pg.TipsMgr.GetInstance().ShowTips(i18n("common_no_item_1"))

				return

		local var_1_11 = Drop.Create(iter_1_1)

		table.insert(var_1_9, var_1_11)

	pg.ConnectionMgr.GetInstance().Send(25002, {
		boxid = var_1_1
	}, 25003, function(arg_2_0)
		if arg_2_0.result == 0:
			local var_2_0 = CommanderBox.New(arg_2_0.box)

			var_1_4.updateBox(var_2_0)

			for iter_2_0, iter_2_1 in ipairs(var_1_9):
				arg_1_0.sendNotification(GAME.CONSUME_ITEM, iter_2_1)

			arg_1_0.sendNotification(GAME.COMMANDER_ON_BUILD_DONE)

			if var_1_3:
				pg.TipsMgr.GetInstance().ShowTips(i18n("commander_build_done"))
		else
			pg.TipsMgr.GetInstance().ShowTips(i18n("commander_build_erro", arg_2_0.result))

		if var_1_2:
			var_1_2())

return var_0_0
