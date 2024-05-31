local var_0_0 = class("TacticsShipItem", import(".DockyardShipItem"))

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2, arg_1_3, arg_1_4):
	arg_1_0.isLoaded = False

	if IsNil(arg_1_2):
		local function var_1_0(arg_2_0)
			arg_2_0.name = "ShipCardTpl"

			setParent(arg_2_0, arg_1_1)

			arg_2_0.transform.localScale = Vector3(1.28, 1.28, 1)
			arg_2_0.transform.localPosition = Vector3(0, 251, 0)

			var_0_0.super.Ctor(arg_1_0, arg_2_0, arg_1_3, arg_1_4)

			arg_1_0.isLoaded = True

			if arg_1_0.cacheShipVO:
				arg_1_0.update(arg_1_0.cacheShipVO)

		ResourceMgr.Inst.getAssetAsync("template/shipcardtpl", "", UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_3_0)
			local var_3_0 = Instantiate(arg_3_0)

			var_1_0(var_3_0)), True, True)
	else
		var_0_0.super.Ctor(arg_1_0, arg_1_2, arg_1_3, arg_1_4)

		arg_1_0.isLoaded = True

def var_0_0.update(arg_4_0, arg_4_1):
	if not arg_4_0.isLoaded:
		arg_4_0.cacheShipVO = arg_4_1
	else
		var_0_0.super.update(arg_4_0, arg_4_1)

def var_0_0.UpdateExpBuff(arg_5_0):
	return

return var_0_0
