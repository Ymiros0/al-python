local var_0_0 = class("BackYardThemeCard")

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0._go = arg_1_1
	arg_1_0._tf = arg_1_1.transform
	arg_1_0.content = arg_1_0._tf:Find("content")
	arg_1_0.icon = arg_1_0.content:Find("icon_mask/icon"):GetComponent(typeof(Image))
	arg_1_0.nameTxt = arg_1_0.content:Find("Text"):GetComponent(typeof(Text))
	arg_1_0.discountTF = arg_1_0.content:Find("discount")
	arg_1_0.discountTxt = arg_1_0.discountTF:Find("Text"):GetComponent(typeof(Text))
	arg_1_0.hotTF = arg_1_0.content:Find("hot")
	arg_1_0.newTF = arg_1_0.content:Find("new")
	arg_1_0.maskPurchased = arg_1_0.content:Find("mask1")
end

function var_0_0.Update(arg_2_0, arg_2_1, arg_2_2)
	arg_2_0.themeVO = arg_2_1

	LoadSpriteAtlasAsync("BackYardTheme/" .. arg_2_1.id, "", function(arg_3_0)
		arg_2_0.icon.sprite = arg_3_0
	end)

	local var_2_0 = shortenString(arg_2_1:GetName(), 7)
	local var_2_1 = string.gsub(var_2_0, "<size=%d+>", "")

	arg_2_0.nameTxt.text = string.gsub(var_2_1, "</size>", "")

	local var_2_2 = arg_2_1:GetDiscount()
	local var_2_3 = arg_2_1:HasDiscount()

	setActive(arg_2_0.discountTF, var_2_3)

	if var_2_3 then
		arg_2_0.discountTxt.text = var_2_2 .. "%"
	end

	local var_2_4 = false
	local var_2_5 = arg_2_1:getConfig("new") > 0

	if not var_2_5 then
		var_2_4 = arg_2_1:getConfig("hot") > 0
	end

	setActive(arg_2_0.hotTF, var_2_4 and not arg_2_2)
	setActive(arg_2_0.newTF, var_2_5 and not arg_2_2)
	setActive(arg_2_0.maskPurchased, arg_2_2)
end

function var_0_0.UpdateSelected(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_1 and arg_4_1.id == arg_4_0.themeVO.id

	if IsNil(arg_4_0.content) then
		return
	end

	if LeanTween.isTweening(arg_4_0.content.gameObject) then
		LeanTween.cancel(arg_4_0.content.gameObject)
	end

	local var_4_1 = arg_4_0.content.anchoredPosition.y
	local var_4_2 = var_4_0 and 0 or -70

	LeanTween.value(arg_4_0.content.gameObject, var_4_1, var_4_2, 0.264):setOnUpdate(System.Action_float(function(arg_5_0)
		setAnchoredPosition(arg_4_0.content, {
			y = arg_5_0
		})
	end))
end

function var_0_0.Dispose(arg_6_0)
	if LeanTween.isTweening(arg_6_0.content.gameObject) then
		LeanTween.cancel(arg_6_0.content.gameObject)
	end
end

return var_0_0
