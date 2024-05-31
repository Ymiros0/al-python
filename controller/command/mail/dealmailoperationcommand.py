local var_0_0 = class("DealMailOperationCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.cmd
	local var_1_2 = var_1_0.filter
	local var_1_3 = var_1_0.ignoreTips
	local var_1_4 = var_1_0.noAttachTip
	local var_1_5 = switch(var_1_2.type, {
		def all:()
			return {},
		def ids:()
			return {
				{
					type = 1,
					arg_list = underscore.rest(var_1_2.list, 1)
				}
			},
		def drops:()
			local var_4_0 = {}
			local var_4_1 = {}

			for iter_4_0, iter_4_1 in ipairs(var_1_2.list):
				if iter_4_1.type == DROP_TYPE_RESOURCE:
					table.insert(var_4_0, iter_4_1.id)
				elif iter_4_1.type == DROP_TYPE_ITEM:
					table.insert(var_4_1, iter_4_1.id)
				else
					assert(False)

			return {
				{
					type = 2,
					arg_list = var_4_0
				},
				{
					type = 3,
					arg_list = var_4_1
				}
			}
	})

	local function var_1_6(arg_5_0, arg_5_1)
		pg.ConnectionMgr.GetInstance().Send(30006, {
			cmd = table.indexof(MailProxy.DEAL_CMD_LIST, arg_5_0),
			match_list = var_1_5
		}, 30007, function(arg_6_0)
			if arg_6_0.result == 0:
				local var_6_0 = getProxy(MailProxy)
				local var_6_1 = underscore.rest(arg_6_0.mail_id_list, 1)

				table.sort(var_6_1, CompareFuncs({
					function(arg_7_0)
						return -arg_7_0
				}))

				for iter_6_0, iter_6_1 in ipairs(var_6_1):
					var_6_0.DealMailOperation(iter_6_1, arg_5_0)

				var_6_0.unpdateUnreadCount(arg_6_0.unread_number)
				arg_5_1(arg_6_0)
			elif arg_6_0.result == 6:
				pg.TipsMgr.GetInstance().ShowTips(i18n("mail_moveto_markroom_max"))
			else
				pg.TipsMgr.GetInstance().ShowTips(errorTip("", arg_6_0.result)))

	local var_1_7 = {}

	if var_1_1 == "attachment" or var_1_1 == "move":
		local var_1_8 = {}

		table.insert(var_1_8, function(arg_8_0, arg_8_1)
			local var_8_0 = GetItemsOverflowDic(arg_8_1)
			local var_8_1, var_8_2 = CheckOverflow(var_8_0, True)

			if not var_8_1:
				switch(var_8_2, {
					def gold:()
						pg.TipsMgr.GetInstance().ShowTips(i18n("gold_max_tip_title")),
					def oil:()
						pg.TipsMgr.GetInstance().ShowTips(i18n("oil_max_tip_title")),
					def equip:()
						pg.TipsMgr.GetInstance().ShowTips(i18n("mail_takeAttachment_error_magazine_full")),
					def ship:()
						pg.TipsMgr.GetInstance().ShowTips(i18n("mail_takeAttachment_error_dockYrad_full"))
				})
			else
				arg_8_0(var_8_2))
		table.insert(var_1_8, function(arg_13_0, arg_13_1)
			if arg_13_1.isStoreOverflow:
				table.insert(var_1_8, function(arg_14_0)
					local var_14_0, var_14_1 = unpack(arg_13_1.isStoreOverflow)
					local var_14_2 = {}

					if var_14_0 > 0:
						table.insert(var_14_2, Drop.New({
							type = DROP_TYPE_RESOURCE,
							id = PlayerConst.ResGold,
							count = var_14_0
						}))

					if var_14_1 > 0:
						table.insert(var_14_2, Drop.New({
							type = DROP_TYPE_RESOURCE,
							id = PlayerConst.ResOil,
							count = var_14_1
						}))

					arg_1_0.sendNotification(GAME.MAIL_DOUBLE_CONFIREMATION_MSGBOX, {
						type = MailProxy.MailMessageBoxType.OverflowConfirm,
						content = i18n("mail_storeroom_max_1"),
						onYes = arg_14_0,
						dropList = var_14_2
					}))

			for iter_13_0, iter_13_1 in ipairs(arg_13_1.isExpBookOverflow):
				table.insert(var_1_8, function(arg_15_0)
					arg_1_0.sendNotification(GAME.MAIL_DOUBLE_CONFIREMATION_MSGBOX, {
						type = MailProxy.MailMessageBoxType.ShowTips,
						content = i18n("player_expResource_mail_overflow", Item.getConfigData(iter_13_1).name),
						onYes = arg_15_0
					}))

			arg_13_0())

		if var_1_2.type == "ids":
			table.insert(var_1_7, function(arg_16_0)
				arg_16_0(getProxy(MailProxy).GetMailsAttachments(var_1_2.list), var_1_2.list))
		else
			table.insert(var_1_7, function(arg_17_0)
				var_1_6("overflow", arg_17_0))
			table.insert(var_1_7, function(arg_18_0, arg_18_1)
				arg_18_0(underscore.map(arg_18_1.drop_list, function(arg_19_0)
					return Drop.New({
						type = arg_19_0.type,
						id = arg_19_0.id,
						count = arg_19_0.number
					})), arg_18_1.mail_id_list))

		if not var_1_4:
			table.insert(var_1_7, function(arg_20_0, arg_20_1, arg_20_2)
				if #arg_20_2 > 0:
					arg_1_0.sendNotification(GAME.MAIL_DOUBLE_CONFIREMATION_MSGBOX, {
						type = MailProxy.MailMessageBoxType.ReceiveAward,
						content = i18n("mail_take_all_mail_msgbox"),
						def onYes:()
							arg_20_0(arg_20_1),
						items = arg_20_1,
						mailids = arg_20_2
					})
				else
					arg_1_0.sendNotification(GAME.MAIL_DOUBLE_CONFIREMATION_MSGBOX, {
						type = MailProxy.MailMessageBoxType.ShowTips,
						content = i18n("mail_manage_3")
					}))

		table.insert(var_1_7, function(arg_22_0, arg_22_1)
			if arg_22_1 and #arg_22_1 > 0:
				seriesAsyncExtend(var_1_8, arg_22_0, arg_22_1)
			else
				arg_22_0())

	table.insert(var_1_7, function(arg_23_0)
		var_1_6(var_1_1, arg_23_0))
	seriesAsync(var_1_7, function(arg_24_0)
		local var_24_0 = PlayerConst.addTranDrop(arg_24_0.drop_list)

		arg_1_0.sendNotification(GAME.DEAL_MAIL_OPERATION_DONE, {
			cmd = var_1_1,
			ids = underscore.rest(arg_24_0.mail_id_list, 1),
			items = var_24_0,
			ignoreTips = var_1_3
		}))

return var_0_0
