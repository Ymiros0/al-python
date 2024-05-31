local var_0_0 = class("WorldMediaCollectionFileLayer", import(".WorldMediaCollectionTemplateLayer"))

def var_0_0.getUIName(arg_1_0):
	return "WorldMediaCollectionFileUI"

def var_0_0.OnInit(arg_2_0):
	arg_2_0._top = arg_2_0.findTF("Top")

def var_0_0.GetDetailLayer(arg_3_0):
	if not arg_3_0.detailLayer:
		arg_3_0.detailLayer = WorldMediaCollectionFileDetailLayer.New(arg_3_0, arg_3_0._tf, arg_3_0.event, arg_3_0.contextData)

		arg_3_0.detailLayer.Load()

	return arg_3_0.detailLayer

def var_0_0.OpenDetailLayer(arg_4_0, arg_4_1, arg_4_2):
	local var_4_0 = arg_4_0.GetDetailLayer()

	arg_4_0.contextData.FileGroupIndex = arg_4_1

	var_4_0.buffer.Show()

	if arg_4_2:
		var_4_0.buffer.Openning()
	else
		var_4_0.buffer.Enter()

	arg_4_0.HideGroupLayer()

def var_0_0.HideDetailLayer(arg_5_0):
	if not arg_5_0.detailLayer:
		return

	arg_5_0.detailLayer.buffer.Hide()

def var_0_0.CloseDetailLayer(arg_6_0):
	if arg_6_0.detailLayer:
		arg_6_0.detailLayer.Destroy()

		arg_6_0.detailLayer = None

def var_0_0.GetGroupLayer(arg_7_0):
	if not arg_7_0.groupLayer:
		arg_7_0.groupLayer = WorldMediaCollectionFileGroupLayer.New(arg_7_0, arg_7_0._tf, arg_7_0.event, arg_7_0.contextData)

		arg_7_0.groupLayer.Load()

	return arg_7_0.groupLayer

def var_0_0.OpenGroupLayer(arg_8_0):
	local var_8_0 = arg_8_0.GetGroupLayer()

	var_8_0.buffer.Show()
	var_8_0.buffer.UpdateGroupList()
	arg_8_0.HideDetailLayer()

def var_0_0.HideGroupLayer(arg_9_0):
	if not arg_9_0.groupLayer:
		return

	arg_9_0.groupLayer.buffer.Hide()

def var_0_0.CloseGroupLayer(arg_10_0):
	if arg_10_0.groupLayer:
		arg_10_0.groupLayer.Destroy()

		arg_10_0.groupLayer = None

def var_0_0.OnSelected(arg_11_0):
	var_0_0.super.OnSelected(arg_11_0)

	if arg_11_0.contextData.FileGroupIndex:
		arg_11_0.OpenDetailLayer(arg_11_0.contextData.FileGroupIndex)
	else
		arg_11_0.OpenGroupLayer()

def var_0_0.OnReselected(arg_12_0):
	var_0_0.super.OnReselected(arg_12_0)
	arg_12_0.Backward()

def var_0_0.OnDeselected(arg_13_0):
	arg_13_0.contextData.FileGroupIndex = None
	arg_13_0.contextData.SelectedFile = None

	var_0_0.super.OnDeselected(arg_13_0)

def var_0_0.Hide(arg_14_0):
	arg_14_0.HideDetailLayer()
	arg_14_0.HideGroupLayer()
	var_0_0.super.Hide(arg_14_0)

def var_0_0.Backward(arg_15_0):
	if not arg_15_0.contextData.FileGroupIndex:
		return

	arg_15_0.contextData.FileGroupIndex = None
	arg_15_0.contextData.SelectedFile = None

	arg_15_0.OpenGroupLayer()

	return True

def var_0_0.OnBackward(arg_16_0):
	return arg_16_0.Backward()

def var_0_0.OnDestroy(arg_17_0):
	arg_17_0.CloseDetailLayer()
	arg_17_0.CloseGroupLayer()
	var_0_0.super.OnDestroy(arg_17_0)

return var_0_0
