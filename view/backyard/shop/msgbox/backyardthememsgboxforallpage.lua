local var_0_0 = class("BackYardThemeMsgBoxForAllPage", import(".BackYardThemeMsgBoxPage"))

function var_0_0.SetUp(arg_1_0, arg_1_1, arg_1_2, arg_1_3)
	var_0_0.super.SetUp(arg_1_0, arg_1_1, arg_1_2, arg_1_3)

	arg_1_0.purchase.text = i18n("purchase_backyard_theme_desc_for_all")

	setActive(arg_1_0.purchaseTr, true)
	setText(arg_1_0.gemPurchaseBtn:Find("content/Text"), i18n("word_buy"))
	setText(arg_1_0.goldPurchaseBtn:Find("content/Text"), i18n("word_buy"))
end

function var_0_0.GetAddList(arg_2_0)
	local var_2_0 = {}
	local var_2_1 = arg_2_0.themeVO:GetFurnitures()
	local var_2_2 = arg_2_0.dorm:GetPurchasedFurnitures()

	for iter_2_0, iter_2_1 in ipairs(var_2_1) do
		local var_2_3 = pg.furniture_data_template[iter_2_1].count

		if var_2_3 > 1 then
			local var_2_4 = arg_2_0.dorm:GetOwnFurnitureCount(iter_2_1)

			for iter_2_2 = 1, var_2_3 - var_2_4 do
				table.insert(var_2_0, Furniture.New({
					id = iter_2_1
				}))
			end
		elseif not var_2_2[iter_2_1] then
			table.insert(var_2_0, Furniture.New({
				id = iter_2_1
			}))
		end
	end

	return var_2_0
end

return var_0_0
