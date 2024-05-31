local var_0_0 = class("ClassRoomBuilding", import(".NavalAcademyUpgradableBuilding"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0, arg_1_1)

	arg_1_0.bubbleImg = arg_1_0.bubble.Find("icon").GetComponent(typeof(Image))
	arg_1_0.floatImg = arg_1_0.floatTF.GetComponent(typeof(Image))
	arg_1_0.isUpdateIcon = False

def var_0_0.UpdateBubble(arg_2_0):
	local var_2_0 = arg_2_0.GetResField()
	local var_2_1 = var_2_0.GetGenResCnt() > 0

	setActive(arg_2_0.bubble, var_2_1)

	if var_2_1:
		arg_2_0.FloatAni()

	if not arg_2_0.isUpdateIcon:
		local var_2_2 = var_2_0.GetResourceType()
		local var_2_3 = Item.getConfigData(var_2_2).icon

		arg_2_0.bubbleImg.sprite = LoadSprite(var_2_3)
		arg_2_0.floatImg.sprite = LoadSprite(var_2_3)

		onButton(arg_2_0, arg_2_0.bubble, function()
			local var_3_0 = arg_2_0.GetResField()

			arg_2_0.emit(NavalAcademyMediator.ON_GET_CLASS_RES), SFX_PANEL)

		arg_2_0.isUpdateIcon = True

def var_0_0.GetGameObjectName(arg_4_0):
	return "classRoom"

def var_0_0.GetTitle(arg_5_0):
	return i18n("school_title_dajiangtang")

def var_0_0.OnClick(arg_6_0):
	arg_6_0.emit(NavalAcademyMediator.ON_OPEN_CLASSROOM)

def var_0_0.GetResField(arg_7_0):
	return arg_7_0.parent.classResField

return var_0_0
