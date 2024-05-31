local var_0_0 = class("CourtYardBaseView")

def var_0_0.Ctor(arg_1_0, arg_1_1, arg_1_2):
	arg_1_0.name = arg_1_1
	arg_1_0.storey = arg_1_2

	arg_1_0.Init()

def var_0_0.Init(arg_2_0):
	arg_2_0.isInit = False

	local var_2_0 = arg_2_0.GetStoreyModule()
	local var_2_1

	seriesAsync({
		function(arg_3_0)
			arg_2_0.LoadUI(var_2_0.__cname, function(arg_4_0)
				var_2_1 = arg_4_0

				arg_3_0()),
		function(arg_5_0)
			arg_2_0.InitObjPool(arg_5_0)
	}, function()
		arg_2_0.storeyModule = var_2_0.New(arg_2_0.storey, var_2_1)
		arg_2_0.isInit = True)

def var_0_0.IsInit(arg_7_0):
	return arg_7_0.isInit == True

def var_0_0.LoadUI(arg_8_0, arg_8_1, arg_8_2):
	arg_8_0.resName = arg_8_1

	ResourceMgr.Inst.getAssetAsync("UI/" .. arg_8_0.resName, "", UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_9_0)
		local var_9_0

		if arg_8_0.storey.GetStyle() == CourtYardConst.STYLE_PREVIEW:
			var_9_0 = pg.UIMgr.GetInstance().OverlayMain.Find("BackYardInterActionPreview(Clone)/frame/view")
		else
			var_9_0 = pg.UIMgr.GetInstance().UIMain.Find(arg_8_0.name .. "(Clone)")

		local var_9_1 = Object.Instantiate(arg_9_0, var_9_0)

		arg_8_0._go = var_9_1

		var_9_1.transform.SetSiblingIndex(1)
		setActive(var_9_1, True)

		arg_8_0.poolRoot = var_9_1.transform.Find("root")

		arg_8_2(var_9_1)), True, True)

def var_0_0.GetRect(arg_10_0):
	assert(arg_10_0.storeyModule)

	return arg_10_0.storeyModule.rectTF

def var_0_0.GetStoreyModule(arg_11_0):
	local var_11_0 = arg_11_0.storey

	return ({
		[CourtYardConst.STYLE_INNER] = CourtYardStoreyModule,
		[CourtYardConst.STYLE_OUTSIDE] = CourtYardOutStoreyModule,
		[CourtYardConst.STYLE_FEAST] = CourtYardFeastStoreyModule,
		[CourtYardConst.STYLE_PREVIEW] = CourtYardStoreyPreviewModule
	})[var_11_0.GetStyle()]

def var_0_0.InitObjPool(arg_12_0, arg_12_1):
	local var_12_0 = arg_12_0.storey
	local var_12_1 = ({
		[CourtYardConst.STYLE_INNER] = CourtYardPoolMgr,
		[CourtYardConst.STYLE_OUTSIDE] = CourtYardPoolMgr,
		[CourtYardConst.STYLE_FEAST] = CourtYardFeastPoolMgr,
		[CourtYardConst.STYLE_PREVIEW] = CourtYardPoolMgr
	})[var_12_0.GetStyle()].New()

	var_12_1.Init(arg_12_0.poolRoot, arg_12_1)

	arg_12_0.poolMgr = var_12_1

def var_0_0.GetCurrStorey(arg_13_0):
	return arg_13_0.storeyModule

def var_0_0.Dispose(arg_14_0):
	if arg_14_0.storeyModule:
		arg_14_0.storeyModule.Dispose()

		arg_14_0.storeyModule = None

	arg_14_0.storey = None

	arg_14_0.poolMgr.Dispose()

	arg_14_0.poolMgr = None

return var_0_0
