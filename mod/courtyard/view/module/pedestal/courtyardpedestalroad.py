local var_0_0 = class("CourtYardPedestalRoad", import(".CourtYardPedestalStructure"))
local var_0_1 = {
	-920,
	-1080,
	-1230,
	-1230
}

def var_0_0.GetAssetPath(arg_1_0):
	return "furniTrues/base/road_" .. arg_1_0.level

def var_0_0.OnLoaded(arg_2_0, arg_2_1):
	setAnchoredPosition(arg_2_1, Vector3(0, var_0_1[arg_2_0.level], 0))

	if arg_2_0.level != 4:
		onButton(arg_2_0, arg_2_1.transform.Find("warn"), function()
			if CourtYardConst.MAX_STOREY_LEVEL + 1 == arg_2_0.level:
				return

			if arg_2_0.IsEditModeOrIsVisit():
				return

			arg_2_0.parent.msgBox.ExecuteAction("Show"), SFX_PANEL)
		onButton(arg_2_0, arg_2_1, function()
			if CourtYardConst.MAX_STOREY_LEVEL + 1 == arg_2_0.level:
				return

			if arg_2_0.IsEditModeOrIsVisit():
				return

			arg_2_0.parent.msgBox.ExecuteAction("Show"), SFX_PANEL)

	tf(arg_2_1).SetSiblingIndex(0)

return var_0_0
