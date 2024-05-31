local var_0_0 = class("BackYardGetPreviewImageMd5Command", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.type
	local var_1_2 = var_1_0.callback
	local var_1_3 = getProxy(DormProxy)
	local var_1_4 = arg_1_0.GetListByType(var_1_1)

	if table.getCount(var_1_4) == 0:
		if var_1_2:
			var_1_2()

		return

	local var_1_5 = {}

	for iter_1_0, iter_1_1 in pairs(var_1_4):
		table.insert(var_1_5, iter_1_1.id)

	pg.ConnectionMgr.GetInstance().Send(19131, {
		id_list = var_1_5
	}, 19132, function(arg_2_0)
		local var_2_0 = {}

		for iter_2_0, iter_2_1 in ipairs(arg_2_0.list):
			var_2_0[iter_2_1.id] = iter_2_1.md5

		for iter_2_2, iter_2_3 in pairs(var_1_4):
			if not var_2_0[iter_2_3.id]:
				arg_1_0.DeleteByType(var_1_1, iter_2_3.id)
			else
				arg_1_0.UpdateMd5ByType(var_1_1, iter_2_3.id, var_2_0[iter_2_3.id])

		if var_1_2:
			var_1_2())

def var_0_0.GetListByType(arg_3_0, arg_3_1):
	local var_3_0 = getProxy(DormProxy)

	if arg_3_1 == BackYardConst.THEME_TEMPLATE_TYPE_SHOP:
		return var_3_0.GetShopThemeTemplates()
	elif arg_3_1 == BackYardConst.THEME_TEMPLATE_TYPE_COLLECTION:
		return var_3_0.GetCollectionThemeTemplates()

	assert(False)

def var_0_0.DeleteByType(arg_4_0, arg_4_1, arg_4_2):
	local var_4_0 = getProxy(DormProxy)

	if arg_4_1 == BackYardConst.THEME_TEMPLATE_TYPE_SHOP:
		var_4_0.DeleteShopThemeTemplate(arg_4_2)
	elif arg_4_1 == BackYardConst.THEME_TEMPLATE_TYPE_COLLECTION:
		var_4_0.DeleteCollectionThemeTemplate(arg_4_2)

def var_0_0.UpdateMd5ByType(arg_5_0, arg_5_1, arg_5_2, arg_5_3):
	local var_5_0 = getProxy(DormProxy)
	local var_5_1

	if arg_5_1 == BackYardConst.THEME_TEMPLATE_TYPE_SHOP:
		var_5_1 = var_5_0.GetShopThemeTemplateById(arg_5_2)
	elif arg_5_1 == BackYardConst.THEME_TEMPLATE_TYPE_COLLECTION:
		var_5_1 = var_5_0.GetCollectionThemeTemplateById(arg_5_2)

	if var_5_1:
		var_5_1.UpdateIconMd5(arg_5_3)

return var_0_0
