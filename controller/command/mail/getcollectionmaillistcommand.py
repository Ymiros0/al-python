local var_0_0 = class("GetCollectionMailListCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody().callback
	local var_1_1 = getProxy(MailProxy)

	if var_1_1.collectionIds:
		return

	var_1_1.collectionIds = {}

	local var_1_2

	local function var_1_3(arg_2_0)
		local var_2_0 = #var_1_1.collectionIds + 1
		local var_2_1 = #var_1_1.collectionIds + SINGLE_MAIL_REQUIRE_SIZE

		pg.ConnectionMgr.GetInstance().Send(30004, {
			index_begin = var_2_0,
			index_end = var_2_1
		}, 30005, function(arg_3_0)
			local var_3_0 = underscore.map(arg_3_0.mail_list, function(arg_4_0)
				return BaseMail.New(arg_4_0))

			var_1_1.AddCollectionMails(var_3_0)

			if #var_3_0 < SINGLE_MAIL_REQUIRE_SIZE:
				arg_2_0()
			else
				var_1_3(arg_2_0))

	var_1_3(function()
		existCall(var_1_0)
		arg_1_0.sendNotification(GAME.GET_COLLECTION_MAIL_LIST_DONE))

return var_0_0
