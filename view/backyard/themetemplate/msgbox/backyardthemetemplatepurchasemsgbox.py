local var_0_0 = class("BackYardThemeTemplatePurchaseMsgbox", import("...Shop.msgbox.BackYardThemeMsgBoxPage"))

def var_0_0.SetUp(arg_1_0, arg_1_1, arg_1_2, arg_1_3):
	arg_1_0.dorm = arg_1_2
	arg_1_0.template = arg_1_1
	arg_1_0.player = arg_1_3
	arg_1_0.count = 1
	arg_1_0.maxCount = 1

	arg_1_0.UpdateMainInfo()
	arg_1_0.UpdateBtns()
	arg_1_0.UpdatePrice()
	arg_1_0.Show()

	arg_1_0.purchase.text = i18n("purchase_backyard_theme_desc_for_onekey")

	setText(arg_1_0.goldPurchaseBtn.Find("content/Text"), i18n("fur_onekey_buy"))

def var_0_0.UpdateMainInfo(arg_2_0):
	arg_2_0.nameTxt.text = arg_2_0.template.GetName()
	arg_2_0.descTxt.text = arg_2_0.template.GetDesc()

	setActive(arg_2_0.icon.gameObject, False)
	setActive(arg_2_0.rawIcon.gameObject, False)

	local var_2_0 = arg_2_0.template.GetIconMd5()

	BackYardThemeTempalteUtil.GetTexture(arg_2_0.template.GetTextureIconName(), var_2_0, function(arg_3_0)
		if not IsNil(arg_2_0.rawIcon) and arg_3_0:
			setActive(arg_2_0.rawIcon.gameObject, True)

			arg_2_0.rawIcon.texture = arg_3_0)

def var_0_0.GetAddList(arg_4_0):
	local var_4_0 = {}
	local var_4_1 = arg_4_0.template.GetFurnitureCnt()
	local var_4_2 = arg_4_0.dorm.GetPurchasedFurnitures()

	for iter_4_0, iter_4_1 in pairs(var_4_1):
		if pg.furniture_data_template[iter_4_0]:
			local var_4_3 = var_4_2[iter_4_0]
			local var_4_4 = 0

			if not var_4_3:
				var_4_3 = Furniture.New({
					id = iter_4_0
				})
			else
				var_4_4 = var_4_3.count

			if var_4_3.canPurchase() and var_4_3.inTime() and var_4_3.canPurchaseByDormMoeny():
				for iter_4_2 = 1, iter_4_1 - var_4_4:
					table.insert(var_4_0, var_4_3)

	return var_4_0

def var_0_0.OnDestroy(arg_5_0):
	var_0_0.super.OnDestroy(arg_5_0)

	if not IsNil(arg_5_0.rawIcon.texture):
		Object.Destroy(arg_5_0.rawIcon.texture)

		arg_5_0.rawIcon.texture = None

return var_0_0
