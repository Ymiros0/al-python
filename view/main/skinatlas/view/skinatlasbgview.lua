﻿local var_0_0 = class("SkinAtlasBgView")

function var_0_0.Ctor(arg_1_0, arg_1_1)
	arg_1_0._tf = arg_1_1
	arg_1_0._go = arg_1_1.gameObject
	arg_1_0.isSpecialBg = false
	arg_1_0.isloading = false
end

function var_0_0.getUIName(arg_2_0)
	return arg_2_0.__cname
end

function var_0_0.Init(arg_3_0, arg_3_1, arg_3_2, arg_3_3)
	arg_3_0.ship = arg_3_1

	arg_3_0:ClearSpecailBg()

	local var_3_0 = arg_3_0:getShipBgPrint(arg_3_2)

	arg_3_0:SetSpecailBg(var_3_0, arg_3_3)
end

function var_0_0.getShipBgPrint(arg_4_0, arg_4_1)
	local var_4_0 = arg_4_0.ship

	if not arg_4_1 then
		return var_4_0:rarity2bgPrintForGet()
	else
		return var_4_0:getShipBgPrint()
	end
end

function var_0_0.SetSpecailBg(arg_5_0, arg_5_1, arg_5_2)
	arg_5_0.isloading = true

	pg.DynamicBgMgr.GetInstance():LoadBg(arg_5_0, arg_5_1, arg_5_0._tf.parent, arg_5_0._tf, function(arg_6_0)
		arg_5_0.isSpecialBg = true
		arg_5_0.isloading = false
		arg_6_0.transform.localPosition = Vector3(0, 0, 200)

		if arg_5_2 then
			arg_5_2()
		end
	end, function()
		arg_5_0.isloading = false

		if arg_5_2 then
			arg_5_2()
		end
	end)
end

function var_0_0.ClearSpecailBg(arg_8_0)
	if arg_8_0.isSpecialBg then
		pg.DynamicBgMgr.GetInstance():ClearBg(arg_8_0:getUIName())

		arg_8_0.isSpecialBg = false
	end
end

function var_0_0.IsLoading(arg_9_0)
	return arg_9_0.isloading
end

function var_0_0.Clear(arg_10_0)
	arg_10_0:ClearSpecailBg()
end

function var_0_0.Dispose(arg_11_0)
	arg_11_0:Clear()
end

return var_0_0
