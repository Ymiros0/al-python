local var_0_0 = class("GetMailListCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.cmd
	local var_1_2 = var_1_0.callback
	local var_1_3, var_1_4, var_1_5 = switch(var_1_1, {
		def new:()
			return 1, getProxy(MailProxy).GetNewIndex(),
		def next:()
			return 1, getProxy(MailProxy).GetNextIndex(),
		def important:()
			return 2, 0, 0,
		def rare:()
			return 3, 0, 0
	})

	if var_1_5 < var_1_4:
		warning("without mail can require")

		return

	pg.ConnectionMgr.GetInstance().Send(30002, {
		type = var_1_3,
		index_begin = var_1_4,
		index_end = var_1_5
	}, 30003, function(arg_6_0)
		local var_6_0 = underscore.map(arg_6_0.mail_list, function(arg_7_0)
			return Mail.New(arg_7_0))

		switch(var_1_1, {
			def new:()
				getProxy(MailProxy).AddNewMails(var_6_0),
			def next:()
				getProxy(MailProxy).AddNextMails(var_6_0),
			def important:()
				getProxy(MailProxy).SetImportantMails(var_6_0),
			def rare:()
				getProxy(MailProxy).SetRareMails(var_6_0)
		})
		existCall(var_1_2)
		arg_1_0.sendNotification(GAME.GET_MAIL_LIST_DONE))

return var_0_0
