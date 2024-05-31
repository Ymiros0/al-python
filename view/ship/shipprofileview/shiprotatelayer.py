local var_0_0 = class("ShipRotateLayer", import("...base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "ShipRotateUI"

def var_0_0.init(arg_2_0):
	arg_2_0.initData()
	arg_2_0.findUI()

def var_0_0.didEnter(arg_3_0):
	local var_3_0 = arg_3_0.skin and arg_3_0.skin.id or arg_3_0.shipGroup.GetSkin(arg_3_0.showTrans).id

	arg_3_0.SetPainting(var_3_0, arg_3_0.showTrans)
	arg_3_0.paintingView.setBGCallback(function()
		arg_3_0.closeView())
	arg_3_0.paintingView.Start()
	setActive(arg_3_0.findTF("Enc"), True)

def var_0_0.willExit(arg_5_0):
	arg_5_0.paintingView.Dispose()
	arg_5_0.RecyclePainting()

def var_0_0.initData(arg_6_0):
	arg_6_0.paintingName = None
	arg_6_0.shipGroup = arg_6_0.contextData.shipGroup
	arg_6_0.showTrans = arg_6_0.contextData.showTrans
	arg_6_0.skin = arg_6_0.contextData.skin

def var_0_0.findUI(arg_7_0):
	arg_7_0.painting = arg_7_0.findTF("paint")
	arg_7_0.paintingFitter = findTF(arg_7_0.painting, "fitter")
	arg_7_0.paintingInitPos = arg_7_0.painting.transform.localPosition
	arg_7_0.paintingView = ShipProfilePaintingView.New(arg_7_0._tf, arg_7_0.painting, True)

def var_0_0.SetPainting(arg_8_0, arg_8_1, arg_8_2):
	arg_8_0.RecyclePainting()

	local var_8_0 = pg.ship_skin_template[arg_8_1].painting

	setPaintingPrefabAsync(arg_8_0.painting, var_8_0, "chuanwu")

	arg_8_0.paintingName = var_8_0

def var_0_0.RecyclePainting(arg_9_0):
	if arg_9_0.paintingName:
		retPaintingPrefab(arg_9_0.painting, arg_9_0.paintingName)

return var_0_0
