local var_0_0 = class("AttireIconFramePanel", import(".AttireFramePanel"))
local var_0_1 = setmetatable

local function var_0_2(arg_1_0)
	local var_1_0 = {}
	local var_1_1 = AttireFramePanel.Card(arg_1_0)

	local function var_1_2(arg_2_0)
		return

	local function var_1_3(arg_3_0, arg_3_1, arg_3_2)
		return

	function var_1_0.Update(arg_4_0, arg_4_1, arg_4_2, arg_4_3)
		var_1_1.Update(arg_4_1, arg_4_2, arg_4_3)
		arg_4_0.ReturnIconFrame(AttireConst.TYPE_ICON_FRAME)

		if arg_4_0.isEmpty():
			return

		arg_4_0.LoadPrefab(arg_4_1, function(arg_5_0)
			var_1_3(arg_4_0, arg_5_0, arg_4_1))

	function var_1_0.Dispose(arg_6_0)
		arg_6_0.ReturnIconFrame(AttireConst.TYPE_ICON_FRAME)

	var_1_2(var_1_0)

	return var_0_1(var_1_0, {
		__index = var_1_1
	})

def var_0_0.getUIName(arg_7_0):
	return "AttireIconFrameUI"

def var_0_0.GetData(arg_8_0):
	return arg_8_0.rawAttireVOs.iconFrames

def var_0_0.OnInitItem(arg_9_0, arg_9_1):
	local var_9_0 = var_0_2(arg_9_1)

	arg_9_0.cards[arg_9_1] = var_9_0

	onButton(arg_9_0, var_9_0._go, function()
		if not var_9_0.isEmpty():
			if arg_9_0.card:
				arg_9_0.card.UpdateSelected(False)

			arg_9_0.contextData.iconFrameId = var_9_0.attireFrame.id

			arg_9_0.UpdateDesc(var_9_0)
			var_9_0.UpdateSelected(True)

			arg_9_0.card = var_9_0, SFX_PANEL)

def var_0_0.GetColumn(arg_11_0):
	return 2

def var_0_0.OnUpdateItem(arg_12_0, arg_12_1, arg_12_2):
	var_0_0.super.OnUpdateItem(arg_12_0, arg_12_1, arg_12_2)

	local var_12_0 = arg_12_0.contextData.iconFrameId or arg_12_0.displayVOs[1].id
	local var_12_1 = arg_12_0.cards[arg_12_2]

	if var_12_1.attireFrame.id == var_12_0:
		triggerButton(var_12_1._go)
		var_12_1.UpdateSelected(True)

return var_0_0
