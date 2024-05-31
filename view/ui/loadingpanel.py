local var_0_0 = class("LoadingPanel", import("..base.BaseUI"))

def var_0_0.Ctor(arg_1_0, arg_1_1):
	var_0_0.super.Ctor(arg_1_0)
	seriesAsync({
		function(arg_2_0)
			arg_1_0.preload(arg_2_0)
	}, function()
		PoolMgr.GetInstance().GetUI("Loading", True, function(arg_4_0)
			local var_4_0 = GameObject.Find("Overlay/UIOverlay")

			arg_4_0.transform.SetParent(var_4_0.transform, False)
			arg_4_0.SetActive(False)
			arg_1_0.onUILoaded(arg_4_0)
			arg_1_1()))

def var_0_0.preload(arg_5_0, arg_5_1):
	arg_5_0.isCri, arg_5_0.bgPath = getLoginConfig()

	if arg_5_0.isCri:
		LoadAndInstantiateAsync("effect", arg_5_0.bgPath, function(arg_6_0)
			arg_5_0.criBgGo = arg_6_0

			if arg_5_1:
				arg_5_1())
	else
		LoadSpriteAsync("loadingbg/" .. arg_5_0.bgPath, function(arg_7_0)
			arg_5_0.staticBgSprite = arg_7_0

			if arg_5_1:
				arg_5_1())

def var_0_0.init(arg_8_0):
	arg_8_0.infos = arg_8_0.findTF("infos")
	arg_8_0.infoTpl = arg_8_0.getTpl("infos/info_tpl")
	arg_8_0.indicator = arg_8_0.findTF("load")
	arg_8_0.bg = arg_8_0.findTF("BG")

	arg_8_0.displayBG(True)

def var_0_0.appendInfo(arg_9_0, arg_9_1):
	local var_9_0 = cloneTplTo(arg_9_0.infoTpl, arg_9_0.infos)

	setText(var_9_0, arg_9_1)

	local var_9_1 = GetOrAddComponent(var_9_0, "CanvasGroup")
	local var_9_2 = LeanTween.alphaCanvas(var_9_1, 0, 0.3)

	var_9_2.setDelay(1.5)
	var_9_2.setOnComplete(System.Action(function()
		destroy(var_9_0)))

def var_0_0.onLoading(arg_11_0):
	return arg_11_0._go.activeInHierarchy

local var_0_1 = 0

def var_0_0.on(arg_12_0, arg_12_1):
	arg_12_1 = defaultValue(arg_12_1, True)

	setImageAlpha(arg_12_0._tf, arg_12_1 and 0.01 or 0)

	if not arg_12_1:
		setActive(arg_12_0.indicator, arg_12_1)
	elif not arg_12_0.delayTimer:
		arg_12_0.delayTimer = pg.TimeMgr.GetInstance().AddTimer("loading", 1, 0, function()
			setImageAlpha(arg_12_0._tf, 0.2)
			setActive(arg_12_0.indicator, True))

	var_0_1 = var_0_1 + 1

	if var_0_1 > 0:
		setActive(arg_12_0._go, True)
		arg_12_0._go.transform.SetAsLastSibling()

def var_0_0.off(arg_14_0):
	if var_0_1 > 0:
		var_0_1 = var_0_1 - 1

		if var_0_1 == 0:
			setActive(arg_14_0._go, False)
			setActive(arg_14_0.indicator, False)

			if arg_14_0.delayTimer:
				pg.TimeMgr.GetInstance().RemoveTimer(arg_14_0.delayTimer)

				arg_14_0.delayTimer = None

def var_0_0.displayBG(arg_15_0, arg_15_1):
	setActive(arg_15_0.bg, arg_15_1)

	local var_15_0 = GetComponent(arg_15_0.bg, "Image")

	if arg_15_1:
		if not arg_15_0.isCri:
			if IsNil(var_15_0.sprite):
				var_15_0.sprite = arg_15_0.staticBgSprite
		elif arg_15_0.bg.childCount == 0:
			var_15_0.enabled = False

			local var_15_1 = arg_15_0.criBgGo.transform

			var_15_1.SetParent(arg_15_0.bg.transform, False)
			var_15_1.SetAsFirstSibling()
	else
		if not arg_15_0.isCri:
			var_15_0.sprite = None
		else
			removeAllChildren(arg_15_0.bg)

		arg_15_0.criBgGo = None
		arg_15_0.staticBgSprite = None

def var_0_0.getRetainCount(arg_16_0):
	return var_0_1

return var_0_0
