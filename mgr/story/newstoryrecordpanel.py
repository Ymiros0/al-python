local var_0_0 = class("NewStoryRecordPanel")
local var_0_1 = 0
local var_0_2 = 1
local var_0_3 = 2
local var_0_4 = 3
local var_0_5 = 4
local var_0_6 = 5
local var_0_7 = 10

def var_0_0.Ctor(arg_1_0):
	arg_1_0.state = var_0_1

def var_0_0.Load(arg_2_0):
	arg_2_0.state = var_0_2
	arg_2_0.parentTF = pg.NewStoryMgr.GetInstance().frontTr

	ResourceMgr.Inst.getAssetAsync("ui/NewStoryRecordUI", "", UnityEngine.Events.UnityAction_UnityEngine_Object(function(arg_3_0)
		local var_3_0 = Object.Instantiate(arg_3_0, arg_2_0.parentTF)

		if arg_2_0.IsLoading():
			arg_2_0.state = var_0_3

			arg_2_0.Init(var_3_0)), True, True)

def var_0_0.IsEmptyOrUnload(arg_4_0):
	return arg_4_0.state == var_0_1 or arg_4_0.state == var_0_6

def var_0_0.IsLoading(arg_5_0):
	return arg_5_0.state == var_0_2

def var_0_0.IsShowing(arg_6_0):
	return arg_6_0.state == var_0_4

def var_0_0.CanOpen(arg_7_0):
	return arg_7_0.state == var_0_1 or arg_7_0.state == var_0_5 or arg_7_0.state == var_0_6

def var_0_0.Init(arg_8_0, arg_8_1):
	arg_8_0._go = arg_8_1
	arg_8_0._tf = arg_8_1.transform
	arg_8_0.pageAnim = arg_8_0._tf.GetComponent(typeof(Animation))
	arg_8_0.pageAniEvent = arg_8_0._tf.GetComponent(typeof(DftAniEvent))
	arg_8_0.container = arg_8_0._tf.Find("content")
	arg_8_0.tpl = arg_8_0._tf.Find("content/tpl")
	arg_8_0.cg = GetOrAddComponent(arg_8_0._tf, typeof(CanvasGroup))
	arg_8_0.tplPools = {
		arg_8_0.tpl
	}
	arg_8_0.closeBtn = arg_8_0._tf.Find("close")
	arg_8_0.scrollrect = arg_8_0._tf.GetComponent(typeof(ScrollRect))
	arg_8_0.contentSizeFitter = arg_8_0._tf.Find("content").GetComponent(typeof(ContentSizeFitter))

	onButton(None, arg_8_0.closeBtn, function()
		setButtonEnabled(arg_8_0.closeBtn, False)
		arg_8_0.Hide(), SFX_PANEL)
	arg_8_0.pageAniEvent.SetEndEvent(function()
		arg_8_0.OnHide())

	arg_8_0.state = var_0_4

	arg_8_0.UpdateAll()

def var_0_0.UpdateAll(arg_11_0):
	arg_11_0.cg.blocksRaycasts = False

	seriesAsync({
		function(arg_12_0)
			arg_11_0.cg.alpha = 0

			arg_11_0.UpdateList(arg_12_0),
		function(arg_13_0)
			onNextTick(arg_13_0),
		function(arg_14_0)
			arg_11_0.cg.alpha = 1

			arg_11_0.PlayAnimation(arg_14_0)
	}, function()
		arg_11_0.cg.blocksRaycasts = True

		arg_11_0.BlurPanel())

local function var_0_8(arg_16_0)
	setActive(arg_16_0._tf, True)
	setButtonEnabled(arg_16_0.closeBtn, True)
	arg_16_0.pageAnim.Play("anim_storyrecordUI_record_in")

	arg_16_0.state = var_0_4

	arg_16_0.UpdateAll()

def var_0_0.Show(arg_17_0, arg_17_1):
	arg_17_0.displays = arg_17_1.GetContentList()

	if arg_17_0.IsEmptyOrUnload():
		arg_17_0.Load()
	elif arg_17_0.IsLoading():
		-- block empty
	else
		var_0_8(arg_17_0)

local function var_0_9(arg_18_0)
	local var_18_0
	local var_18_1 = False

	if #arg_18_0.tplPools <= 0:
		var_18_0 = Object.Instantiate(arg_18_0.tpl, arg_18_0.tpl.parent)
	else
		var_18_1 = True
		var_18_0 = table.remove(arg_18_0.tplPools, 1)

	GetOrAddComponent(var_18_0, typeof(CanvasGroup)).alpha = 1

	return var_18_0, var_18_1

local function var_0_10(arg_19_0, arg_19_1)
	setActive(arg_19_1, False)

	GetOrAddComponent(arg_19_1, typeof(CanvasGroup)).alpha = 1

	if #arg_19_0.tplPools >= 5 and arg_19_1 != arg_19_0.tpl:
		Object.Destroy(arg_19_1.gameObject)
	else
		table.insert(arg_19_0.tplPools, arg_19_1)

def var_0_0.UpdateList(arg_20_0, arg_20_1):
	if not arg_20_0.IsShowing():
		return

	local var_20_0 = arg_20_0.displays
	local var_20_1 = {}
	local var_20_2 = 1

	arg_20_0.usingTpls = {}

	local var_20_3 = #var_20_0 < var_0_7 and #var_20_0 or var_0_7

	for iter_20_0, iter_20_1 in ipairs(var_20_0):
		local var_20_4 = #var_20_0

		table.insert(var_20_1, function(arg_21_0)
			local var_21_0, var_21_1 = var_0_9(arg_20_0)

			if not var_21_1:
				var_20_2 = var_20_2 + 1

			arg_20_0.UpdateRecord(var_21_0, iter_20_1)
			table.insert(arg_20_0.usingTpls, var_21_0)
			tf(var_21_0).SetAsLastSibling()

			if var_20_2 % 5 == 0:
				var_20_2 = 1

				onNextTick(arg_21_0)
			else
				arg_21_0()

			local var_21_2 = var_21_0.GetComponent(typeof(Animation))

			if iter_20_0 + var_20_3 <= var_20_4:
				setActive(var_21_0, True)
				var_21_2.Play("anim_storyrecordUI_tql_reset")
			else
				GetOrAddComponent(var_21_0, typeof(CanvasGroup)).alpha = 0

				setActive(var_21_0, True))

	table.insert(var_20_1, function(arg_22_0)
		onDelayTick(function()
			arg_20_0.contentSizeFitter.enabled = False
			arg_20_0.contentSizeFitter.enabled = True

			scrollToBottom(arg_20_0._tf)
			arg_22_0(), 0.05))
	seriesAsync(var_20_1, arg_20_1)

def var_0_0.PlayAnimation(arg_24_0, arg_24_1):
	local var_24_0 = arg_24_0.displays
	local var_24_1 = #var_24_0 < var_0_7 and #var_24_0 or var_0_7
	local var_24_2 = {}

	for iter_24_0 = 1, var_24_1:
		table.insert(var_24_2, function(arg_25_0)
			local var_25_0 = #arg_24_0.usingTpls - var_24_1 + iter_24_0

			arg_24_0.usingTpls[var_25_0].GetComponent(typeof(Animation)).Play("anim_storyrecordUI_tpl_in")
			onDelayTick(function()
				arg_25_0(), 0.033))

	seriesAsync(var_24_2)
	arg_24_1()

def var_0_0.UpdateRecord(arg_27_0, arg_27_1, arg_27_2):
	GetOrAddComponent(arg_27_1, typeof(CanvasGroup)).alpha = 1

	setActive(arg_27_1.Find("icon"), arg_27_2.icon)

	if arg_27_2.icon:
		local var_27_0 = arg_27_2.icon

		GetImageSpriteFromAtlasAsync("SquareIcon/" .. var_27_0, "", arg_27_1.Find("icon/Image"))

	if arg_27_2.name and arg_27_2.nameColor:
		local var_27_1 = string.gsub(arg_27_2.nameColor, "#", "")

		arg_27_1.Find("name").GetComponent(typeof(Outline)).effectColor = Color.NewHex(var_27_1)

		setText(arg_27_1.Find("name"), setColorStr(arg_27_2.name, arg_27_2.nameColor))
	else
		setText(arg_27_1.Find("name"), arg_27_2.name or "")

	local var_27_2 = arg_27_2.list
	local var_27_3 = UIItemList.New(arg_27_1.Find("content"), arg_27_1.Find("content/Text"))

	var_27_3.make(function(arg_28_0, arg_28_1, arg_28_2)
		if arg_28_0 == UIItemList.EventUpdate:
			setText(arg_28_2, var_27_2[arg_28_1 + 1]))
	var_27_3.align(#var_27_2)
	setActive(arg_27_1.Find("player"), arg_27_2.icon == None and arg_27_2.isPlayer)

	local var_27_4 = arg_27_2.icon == None and arg_27_2.name == None
	local var_27_5 = var_27_3.container.GetComponent(typeof(UnityEngine.UI.HorizontalOrVerticalLayoutGroup))
	local var_27_6 = UnityEngine.RectOffset.New()

	var_27_6.left = 170
	var_27_6.right = 0
	var_27_6.top = var_27_4 and 25 or 90
	var_27_6.bottom = var_27_4 and 25 or 50
	var_27_5.padding = var_27_6

def var_0_0.OnHide(arg_29_0):
	arg_29_0.Clear()
	arg_29_0.UnblurPanel()
	setActive(arg_29_0._tf, False)
	setButtonEnabled(arg_29_0.closeBtn, True)

	arg_29_0.state = var_0_5

def var_0_0.Hide(arg_30_0):
	if arg_30_0.IsShowing():
		arg_30_0.pageAnim.Play("anim_storyrecordUI_record_out")

def var_0_0.BlurPanel(arg_31_0):
	setParent(pg.NewStoryMgr.GetInstance()._tf, pg.UIMgr.GetInstance().UIMain)

	local var_31_0 = pg.UIMgr.GetInstance().OverlayMain

	arg_31_0.hideNodes = {}

	for iter_31_0 = 1, var_31_0.childCount:
		local var_31_1 = var_31_0.GetChild(iter_31_0 - 1)

		if isActive(var_31_1):
			table.insert(arg_31_0.hideNodes, var_31_1)
			setActive(var_31_1, False)

	pg.UIMgr.GetInstance().BlurPanel(arg_31_0._tf, False, {
		weight = LayerWeightConst.TOP_LAYER
	})

def var_0_0.UnblurPanel(arg_32_0):
	setParent(pg.NewStoryMgr.GetInstance()._tf, pg.UIMgr.GetInstance().OverlayToast)

	if arg_32_0.hideNodes and #arg_32_0.hideNodes > 0:
		for iter_32_0, iter_32_1 in ipairs(arg_32_0.hideNodes):
			setActive(iter_32_1, True)

	arg_32_0.hideNodes = {}

	pg.UIMgr.GetInstance().UnblurPanel(arg_32_0._tf, arg_32_0.parentTF)

def var_0_0.Clear(arg_33_0):
	for iter_33_0, iter_33_1 in ipairs(arg_33_0.usingTpls):
		var_0_10(arg_33_0, iter_33_1)

	arg_33_0.usingTpls = {}

def var_0_0.Unload(arg_34_0):
	if arg_34_0.state > var_0_2:
		arg_34_0.state = var_0_6

		if not IsNil(arg_34_0.closeBtn):
			removeOnButton(arg_34_0.closeBtn)

		Object.Destroy(arg_34_0._go)

		arg_34_0._go = None
		arg_34_0._tf = None
		arg_34_0.container = None
		arg_34_0.tpl = None

def var_0_0.Dispose(arg_35_0):
	arg_35_0.Hide()
	arg_35_0.Unload()

return var_0_0
