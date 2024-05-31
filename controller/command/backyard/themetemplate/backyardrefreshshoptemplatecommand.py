local var_0_0 = class("BackYardRefreshShopTemplateCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.type
	local var_1_2 = var_1_0.page
	local var_1_3 = var_1_0.force
	local var_1_4 = var_1_0.timeType
	local var_1_5 = getProxy(DormProxy)
	local var_1_6 = False

	if var_1_2 == var_1_5.MAX_PAGE:
		pg.TipsMgr.GetInstance().ShowTips(i18n("backyard_shop_reach_last_page"))

		return

	if var_1_2 > var_1_5.lastPages[var_1_1]:
		arg_1_0.sendNotification(GAME.BACKYARD_REFRESH_SHOP_TEMPLATE_ERRO)

		return

	local function var_1_7(arg_2_0, arg_2_1)
		local var_2_0 = {}

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.theme_id_list or {}):
			local var_2_1 = var_1_5.GetShopThemeTemplateById(iter_2_1)

			if not var_2_1:
				var_1_6 = True

				local var_2_2 = BackYardThemeTemplate.New({
					id = iter_2_1
				})

				var_2_2.SetSortIndex(iter_2_0)

				var_2_0[var_2_2.id] = var_2_2
			else
				var_2_1.SetSortIndex(iter_2_0)

				var_2_0[var_2_1.id] = var_2_1

		if table.getCount(var_2_0) > 0:
			var_1_5.SetShopThemeTemplates(var_2_0)

			var_1_5.TYPE = var_1_1
			var_1_5.PAGE = var_1_2

		if table.getCount(var_2_0) < BackYardConst.THEME_TEMPLATE_SHOP_REFRSH_CNT:
			var_1_5.lastPages[var_1_1] = var_1_2

			if not var_1_3:
				-- block empty

		if arg_2_1:
			arg_2_1()

	local function var_1_8(arg_3_0)
		arg_1_0.sendNotification(GAME.BACKYARD_GET_IMG_MD5, {
			type = BackYardConst.THEME_TEMPLATE_TYPE_SHOP,
			callback = arg_3_0
		})

	local function var_1_9(arg_4_0)
		seriesAsync({
			function(arg_5_0)
				var_1_7(arg_4_0, arg_5_0),
			function(arg_6_0)
				var_1_8(arg_6_0)
		}, function()
			arg_1_0.sendNotification(GAME.BACKYARD_REFRESH_SHOP_TEMPLATE_DONE, {
				existNew = var_1_6
			}))

	pg.ConnectionMgr.GetInstance().Send(19117, {
		typ = var_1_1,
		page = var_1_2,
		num = BackYardConst.THEME_TEMPLATE_SHOP_REFRSH_CNT
	}, 19118, function(arg_8_0)
		if arg_8_0.result == 0:
			var_1_9(arg_8_0)
		else
			pg.TipsMgr.GetInstance().ShowTips(ERROR_MESSAGE[arg_8_0.result] .. arg_8_0.result))

return var_0_0
