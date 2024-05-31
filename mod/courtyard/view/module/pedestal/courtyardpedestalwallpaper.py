local var_0_0 = class("CourtYardPedestalWallPaper", import(".CourtYardPedestalStructure"))

def var_0_0.Update(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.paper = arg_1_1

	if not arg_1_0.paper:
		arg_1_0.Unload()

		return

	var_0_0.super.Update(arg_1_0, arg_1_2)

def var_0_0.GetAssetPath(arg_2_0):
	local var_2_0 = arg_2_0.paper.GetObjType()

	if var_2_0 == CourtYardConst.OBJ_TYPE_COMMOM:
		return "furniTrues/" .. arg_2_0.paper.GetPicture() .. arg_2_0.level
	elif var_2_0 == CourtYardConst.OBJ_TYPE_SPINE:
		local var_2_1, var_2_2 = arg_2_0.paper.GetSpineNameAndAction()

		return "sfurniture/" .. var_2_1 .. arg_2_0.level

def var_0_0.OnLoaded(arg_3_0, arg_3_1):
	rtf(arg_3_1).anchorMin = Vector2(0.5, 1)
	rtf(arg_3_1).anchorMax = Vector2(0.5, 1)
	rtf(arg_3_1).pivot = Vector2(0.5, 1)
	rtf(arg_3_1).localScale = Vector3(1, 1, 1)

	local var_3_0 = arg_3_0.paper.GetObjType()

	if var_3_0 == CourtYardConst.OBJ_TYPE_COMMOM:
		arg_3_0.InitCommon(arg_3_1)
	elif var_3_0 == CourtYardConst.OBJ_TYPE_SPINE:
		arg_3_0.InitSpine(arg_3_1)

	tf(arg_3_1).SetSiblingIndex(1)

def var_0_0.InitCommon(arg_4_0, arg_4_1):
	setAnchoredPosition(arg_4_1, {
		x = 0,
		y = -6
	})

def var_0_0.InitSpine(arg_5_0, arg_5_1):
	setAnchoredPosition(arg_5_1, Vector3(0, -10, 0))

	local var_5_0, var_5_1 = arg_5_0.paper.GetSpineNameAndAction()

	if var_5_1:
		GetOrAddComponent(tf(arg_5_1).GetChild(0), typeof(SpineAnimUI)).SetAction(var_5_1, 0)

return var_0_0
