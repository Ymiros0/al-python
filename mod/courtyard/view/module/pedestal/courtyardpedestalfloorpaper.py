local var_0_0 = class("CourtYardPedestalFloorPaper", import(".CourtYardPedestalStructure"))
local var_0_1 = {
	0.5,
	0.67,
	0.83,
	1
}

def var_0_0.Update(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.paper = arg_1_1

	var_0_0.super.Update(arg_1_0, arg_1_2)

def var_0_0.GetAssetPath(arg_2_0):
	if not arg_2_0.paper:
		return "furniTrues/base/floor_4"

	local var_2_0 = arg_2_0.paper.GetObjType()

	if var_2_0 == CourtYardConst.OBJ_TYPE_COMMOM:
		return "furniTrues/" .. arg_2_0.paper.GetPicture()
	elif var_2_0 == CourtYardConst.OBJ_TYPE_SPINE:
		local var_2_1, var_2_2 = arg_2_0.paper.GetSpineNameAndAction()

		return "sfurniture/" .. var_2_1

def var_0_0.OnLoaded(arg_3_0, arg_3_1):
	rtf(arg_3_1).sizeDelta = Vector2(1888, 944)
	rtf(arg_3_1).anchorMin = Vector2(0.5, 1)
	rtf(arg_3_1).anchorMax = Vector2(0.5, 1)
	rtf(arg_3_1).pivot = Vector2(0.5, 1)
	rtf(arg_3_1).localScale = Vector3(1, 1, 1)

	setAnchoredPosition(rtf(arg_3_1), Vector3(0, -280, 0))

	if arg_3_0.paper and arg_3_0.paper.GetObjType() == CourtYardConst.OBJ_TYPE_SPINE:
		arg_3_0.InitSpine(arg_3_1)

	local var_3_0 = arg_3_0.GetRect().GetSiblingIndex()

	tf(arg_3_1).SetSiblingIndex(var_3_0)

	local var_3_1 = var_0_1[arg_3_0.level]

	arg_3_1.transform.localScale = Vector3(var_3_1, var_3_1, 1)

def var_0_0.InitSpine(arg_4_0, arg_4_1):
	local var_4_0, var_4_1 = arg_4_0.paper.GetSpineNameAndAction()

	if var_4_1:
		GetOrAddComponent(tf(arg_4_1).GetChild(0), typeof(SpineAnimUI)).SetAction(var_4_1, 0)

return var_0_0
