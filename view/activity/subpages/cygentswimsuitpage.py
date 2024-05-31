local var_0_0 = class("CygentSwimsuitPage", import(".TemplatePage.SkinTemplatePage"))

def var_0_0.OnFirstFlush(arg_1_0):
	var_0_0.super.OnFirstFlush(arg_1_0)
	PoolMgr.GetInstance().GetSpineChar("xiaotiane_2", False, function(arg_2_0)
		arg_2_0.transform.localScale = Vector3(0.7, 0.7, 1)

		arg_2_0.transform.SetParent(arg_1_0.findTF("char", arg_1_0.bg), False)
		arg_2_0.GetComponent(typeof(SpineAnimUI)).SetAction("stand", 0)

		arg_1_0.model = arg_2_0)

def var_0_0.OnUpdateFlush(arg_3_0):
	var_0_0.super.OnUpdateFlush(arg_3_0)
	GetImageSpriteFromAtlasAsync("numbericon/t1/" .. arg_3_0.nday, "", arg_3_0.findTF("day1", arg_3_0.bg))
	setText(arg_3_0.findTF("progress", arg_3_0.bg), "進度." .. arg_3_0.nday .. "/10")

def var_0_0.OnDestroy(arg_4_0):
	var_0_0.super.OnDestroy(arg_4_0)

	if arg_4_0.model:
		arg_4_0.model.transform.localScale = Vector3.one

		PoolMgr.GetInstance().ReturnSpineChar("xiaotiane_2", arg_4_0.model)

		arg_4_0.model = None

return var_0_0
