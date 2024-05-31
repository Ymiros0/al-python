local var_0_0 = class("XiaotianeSwimsuitSkinPage", import(".TemplatePage.SkinTemplatePage"))

def var_0_0.OnInit(arg_1_0):
	var_0_0.super.OnInit(arg_1_0)

	arg_1_0.rtDayImage = arg_1_0.bg.Find("day_image")
	arg_1_0.rtCharacter = arg_1_0.bg.Find("character")

def var_0_0.OnUpdateFlush(arg_2_0):
	var_0_0.super.OnUpdateFlush(arg_2_0)
	setText(arg_2_0.dayTF, i18n("activity_permanent_progress") .. arg_2_0.nday .. "/" .. #arg_2_0.taskGroup)
	GetImageSpriteFromAtlasAsync("ui/activityuipage/xiaotianeswimsuitskinpage_atlas", tostring(arg_2_0.nday), arg_2_0.rtDayImage, True)

	if not arg_2_0.model:
		PoolMgr.GetInstance().GetSpineChar("xiaotiane_2", True, function(arg_3_0)
			if arg_2_0.model:
				return

			arg_2_0.model = arg_3_0
			tf(arg_3_0).localScale = Vector3(1, 1, 1)

			arg_3_0.GetComponent("SpineAnimUI").SetAction("stand2", 0)
			setParent(arg_3_0, arg_2_0.rtCharacter))

def var_0_0.OnDestroy(arg_4_0):
	if arg_4_0.model:
		PoolMgr.GetInstance().ReturnSpineChar("xiaotiane_2", arg_4_0.model)

		arg_4_0.prefab1 = None
		arg_4_0.model1 = None

	var_0_0.super.OnDestroy(arg_4_0)

return var_0_0
