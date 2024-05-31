local var_0_0 = class("ShopBgView")

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0._bg = arg_1_1
	arg_1_0.img = arg_1_0._bg:GetComponent(typeof(Image))

	setActive(arg_1_1, false)

	arg_1_0.bgs = {}
end

function var_0_0.Init(arg_2_0, arg_2_1)
	setActive(arg_2_0._bg, arg_2_1 ~= nil)

	if arg_2_1 then
		local var_2_0

		if arg_2_0.bgs[arg_2_1] then
			var_2_0 = arg_2_0.bgs[arg_2_1]
		else
			var_2_0 = GetSpriteFromAtlas(arg_2_1, "")
		end

		arg_2_0.img.sprite = var_2_0
	end
end

function var_0_0.Dispose(arg_3_0)
	UIUtil.ClearImageSprite(arg_3_0._bg.gameObject)

	arg_3_0.bgs = nil
end

return var_0_0
