local var_0_0 = class("CustomIndexLayer", import("..base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "CustomIndexUI"

var_0_0.Mode = {
	OR = 2,
	AND = 1,
	NUM = 3
}

def var_0_0.init(arg_2_0):
	arg_2_0.panel = arg_2_0._tf.Find("index_panel")
	arg_2_0.layout = arg_2_0.panel.Find("layout")
	arg_2_0.contianer = arg_2_0.layout.Find("container")

	eachChild(arg_2_0.contianer, function(arg_3_0)
		setActive(arg_3_0, False))

	arg_2_0.panelTemplate = arg_2_0.layout.Find("container/Template")
	arg_2_0.displayList = {}
	arg_2_0.typeList = {}
	arg_2_0.btnConfirm = arg_2_0.findTF("layout/btns/ok", arg_2_0.panel)
	arg_2_0.btnCancel = arg_2_0.findTF("layout/btns/cancel", arg_2_0.panel)

	setText(arg_2_0.findTF("Image", arg_2_0.btnConfirm), i18n("text_confirm"))
	setText(arg_2_0.findTF("Image", arg_2_0.btnCancel), i18n("text_cancel"))

	arg_2_0.greySprite = arg_2_0.findTF("resource/grey", arg_2_0.panel).GetComponent(typeof(Image)).sprite
	arg_2_0.blueSprite = arg_2_0.findTF("resource/blue", arg_2_0.panel).GetComponent(typeof(Image)).sprite
	arg_2_0.yellowSprite = arg_2_0.findTF("resource/yellow", arg_2_0.panel).GetComponent(typeof(Image)).sprite

def var_0_0.didEnter(arg_4_0):
	onButton(arg_4_0, arg_4_0.btnConfirm, function()
		if arg_4_0.contextData.callback:
			arg_4_0.contextData.callback(arg_4_0.contextData.indexDatas)

			arg_4_0.contextData.callback = None

		arg_4_0.emit(var_0_0.ON_CLOSE), SFX_CONFIRM)
	onButton(arg_4_0, arg_4_0.btnCancel, function()
		arg_4_0.emit(var_0_0.ON_CLOSE), SFX_CANCEL)
	onButton(arg_4_0, arg_4_0.findTF("btn", arg_4_0.panel), function()
		arg_4_0.emit(var_0_0.ON_CLOSE), SFX_CANCEL)

	arg_4_0.panel.localScale = Vector3.zero

	LeanTween.scale(arg_4_0.panel, Vector3(1, 1, 1), 0.2)
	setText(arg_4_0.panel.Find("layout/tip"), arg_4_0.contextData.tip or "")
	arg_4_0.InitGroup()
	arg_4_0.BlurPanel()

def var_0_0.BlurPanel(arg_8_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_8_0._tf)

def var_0_0.InitGroup(arg_9_0):
	arg_9_0.onInit = True
	arg_9_0.contextData.indexDatas = arg_9_0.contextData.indexDatas or {}
	arg_9_0.dropdownDic = {}
	arg_9_0.updateList = {}
	arg_9_0.simpleDropdownDic = {}

	for iter_9_0, iter_9_1 in pairs(arg_9_0.contextData.groupList):
		if iter_9_1.dropdown:
			arg_9_0.InitDropdown(iter_9_1)
		else
			arg_9_0.InitCustoms(iter_9_1)

	for iter_9_2, iter_9_3 in ipairs(arg_9_0.updateList):
		iter_9_3()

	if arg_9_0.contextData.customPanels.minHeight:
		GetOrAddComponent(arg_9_0.layout, typeof(LayoutElement)).minHeight = arg_9_0.contextData.customPanels.minHeight

	if arg_9_0.contextData.customPanels.layoutPos:
		setLocalPosition(arg_9_0.layout, arg_9_0.contextData.customPanels.layoutPos)

	arg_9_0.onInit = False

def var_0_0.InitDropdown(arg_10_0, arg_10_1):
	local var_10_0 = arg_10_1.tags
	local var_10_1 = tf(Instantiate(arg_10_0.panelTemplate))

	setParent(var_10_1, arg_10_0.contianer, False)
	setActive(var_10_1, True)

	local var_10_2 = var_0_0.Clone2Full(var_10_1.Find("bg"), #var_10_0)

	go(var_10_1).name = arg_10_1.titleTxt

	setText(var_10_1.Find("title/Image"), i18n(arg_10_1.titleTxt))
	setText(var_10_1.Find("title/Image/Image_en"), i18n(arg_10_1.titleENTxt))

	var_10_1.Find("bg").GetComponent(typeof(ScrollRect)).enabled = False

	for iter_10_0, iter_10_1 in ipairs(var_10_0):
		local var_10_3 = var_10_2[iter_10_0]

		setActive(arg_10_0.findTF("dropdown", var_10_3), True)

		local var_10_4 = CustomDropdown.New(arg_10_0.panel, arg_10_0.event, arg_10_0.contextData, iter_10_1, var_10_3)

		onButton(arg_10_0, var_10_3, function()
			local var_11_0 = arg_10_0.panel.InverseTransformPoint(var_10_3.position)

			if not var_10_4.GetLoaded():
				var_10_4.Load()

			var_10_4.ActionInvoke("Show", var_11_0))

		arg_10_0.dropdownDic[iter_10_1] = var_10_4

def var_0_0.InitCustoms(arg_12_0, arg_12_1):
	local var_12_0 = arg_12_1.tags[1]
	local var_12_1 = arg_12_0.contextData.customPanels[var_12_0]
	local var_12_2 = tf(Instantiate(arg_12_0.panelTemplate))

	setParent(var_12_2, arg_12_0.contianer, False)
	setActive(var_12_2, True)

	go(var_12_2).name = arg_12_1.titleTxt

	setText(var_12_2.Find("title/Image"), i18n(arg_12_1.titleTxt))
	setText(var_12_2.Find("title/Image/Image_en"), i18n(arg_12_1.titleENTxt))

	var_12_2.Find("bg").GetComponent(typeof(ScrollRect)).enabled = False

	local var_12_3 = var_12_1.options
	local var_12_4 = var_12_1.mode or var_0_0.Mode.OR
	local var_12_5 = 0
	local var_12_6 = var_12_1.blueSeleted and arg_12_0.blueSprite or arg_12_0.yellowSprite

	for iter_12_0, iter_12_1 in ipairs(var_12_3):
		var_12_5 = bit.bor(iter_12_1, var_12_5)

	arg_12_0.contextData.indexDatas[var_12_0] = arg_12_0.contextData.indexDatas[var_12_0] or var_12_3[1]

	local var_12_7
	local var_12_8 = var_0_0.Clone2Full(var_12_2.Find("bg"), #var_12_3)

	for iter_12_2, iter_12_3 in ipairs(var_12_8):
		local var_12_9 = var_12_3[iter_12_2]

		setText(findTF(iter_12_3, "Image"), i18n(var_12_1.names[iter_12_2]))
		setImageSprite(iter_12_3, arg_12_0.greySprite)
		onButton(arg_12_0, iter_12_3, function()
			switch(var_12_4, {
				[var_0_0.Mode.AND] = function()
					if iter_12_2 == 1 or arg_12_0.contextData.indexDatas[var_12_0] == var_12_3[1]:
						arg_12_0.contextData.indexDatas[var_12_0] = var_12_9
					else
						arg_12_0.contextData.indexDatas[var_12_0] = bit.bxor(arg_12_0.contextData.indexDatas[var_12_0], var_12_9)

					if arg_12_0.contextData.indexDatas[var_12_0] == 0 or arg_12_0.contextData.indexDatas[var_12_0] == var_12_5:
						arg_12_0.contextData.indexDatas[var_12_0] = var_12_3[1],
				[var_0_0.Mode.OR] = function()
					if var_12_1.isSort:
						arg_12_0.contextData.indexDatas[var_12_0] = var_12_9
					else
						local var_15_0 = arg_12_0.contextData.indexDatas[var_12_0]

						arg_12_0.contextData.indexDatas[var_12_0] = var_12_9 == var_15_0 and var_12_3[1] or var_12_9,
				[var_0_0.Mode.NUM] = function()
					local var_16_0 = arg_12_0.contextData.indexDatas[var_12_0]
					local var_16_1 = 0

					while var_16_0 > 0:
						var_16_1 = var_16_1 + 1
						var_16_0 = bit.band(var_16_0, var_16_0 - 1)

					if var_16_1 < var_12_1.num or bit.band(arg_12_0.contextData.indexDatas[var_12_0], var_12_9) > 0:
						arg_12_0.contextData.indexDatas[var_12_0] = bit.bxor(arg_12_0.contextData.indexDatas[var_12_0], var_12_9)
					else
						pg.TipsMgr.GetInstance().ShowTips(i18n("equipcode_share_exceedlimit"))
			})
			var_12_7(), SFX_UI_TAG)

	function var_12_7()
		switch(var_12_4, {
			[var_0_0.Mode.AND] = function()
				if arg_12_0.contextData.indexDatas[var_12_0] == var_12_3[1]:
					for iter_18_0, iter_18_1 in ipairs(var_12_8):
						local var_18_0 = var_12_3[iter_18_0] == var_12_3[1]
						local var_18_1 = findTF(iter_18_1, "Image")

						setImageSprite(iter_18_1, var_18_0 and var_12_6 or arg_12_0.greySprite)
				else
					for iter_18_2, iter_18_3 in ipairs(var_12_8):
						local var_18_2 = var_12_3[iter_18_2] != var_12_3[1] and bit.band(arg_12_0.contextData.indexDatas[var_12_0], var_12_3[iter_18_2]) > 0
						local var_18_3 = findTF(iter_18_3, "Image")

						setImageSprite(iter_18_3, var_18_2 and var_12_6 or arg_12_0.greySprite),
			[var_0_0.Mode.OR] = function()
				for iter_19_0, iter_19_1 in ipairs(var_12_8):
					local var_19_0 = var_12_3[iter_19_0] == arg_12_0.contextData.indexDatas[var_12_0]
					local var_19_1 = findTF(iter_19_1, "Image")

					setImageSprite(iter_19_1, var_19_0 and var_12_6 or arg_12_0.greySprite),
			[var_0_0.Mode.NUM] = function()
				for iter_20_0, iter_20_1 in ipairs(var_12_8):
					local var_20_0 = bit.band(arg_12_0.contextData.indexDatas[var_12_0], var_12_3[iter_20_0]) > 0
					local var_20_1 = findTF(iter_20_1, "Image")

					setImageSprite(iter_20_1, var_20_0 and var_12_6 or arg_12_0.greySprite)
		})
		arg_12_0.OnDatasChange(var_12_0)

		if arg_12_0.simpleDropdownDic[var_12_0]:
			for iter_17_0, iter_17_1 in pairs(arg_12_0.simpleDropdownDic[var_12_0]):
				iter_17_1.UpdateVirtualBtn()

	table.insert(arg_12_0.updateList, var_12_7)

	if arg_12_1.simpleDropdown:
		assert(var_12_4 == var_0_0.Mode.OR, "simpleDropdown目前只支持OR模式")

		local var_12_10 = var_12_2.Find("bg").GetChild(0)

		for iter_12_4, iter_12_5 in ipairs(arg_12_1.simpleDropdown):
			local var_12_11 = arg_12_0.contextData.customPanels[iter_12_5]
			local var_12_12 = cloneTplTo(var_12_10, var_12_2.Find("bg"))

			var_12_12.name = iter_12_5 .. "_simple"

			local var_12_13 = SimpleDropdown.New(arg_12_0.panel, arg_12_0.event, arg_12_0.contextData, var_12_0, var_12_12, var_12_11, var_12_7, arg_12_0.greySprite, arg_12_0.yellowSprite)

			setActive(arg_12_0.findTF("dropdown", var_12_12), True)
			onButton(arg_12_0, var_12_12, function()
				local var_21_0 = arg_12_0.panel.InverseTransformPoint(var_12_12.position)

				if not var_12_13.GetLoaded():
					var_12_13.Load()

				var_12_13.ActionInvoke("Show", var_21_0))

			arg_12_0.simpleDropdownDic[var_12_0] = arg_12_0.simpleDropdownDic[var_12_0] or {}
			arg_12_0.simpleDropdownDic[var_12_0][iter_12_5] = var_12_13

def var_0_0.OnDatasChange(arg_22_0, arg_22_1):
	local var_22_0 = arg_22_0.contextData.dropdownLimit or {}

	for iter_22_0, iter_22_1 in pairs(arg_22_0.dropdownDic):
		if var_22_0[iter_22_0] != None:
			local var_22_1 = var_22_0[iter_22_0].include
			local var_22_2 = var_22_0[iter_22_0].exclude

			if var_22_2[arg_22_1] != None or var_22_1[arg_22_1] != None:
				local var_22_3 = arg_22_0.contextData.indexDatas[arg_22_1]
				local var_22_4 = False

				if var_22_2[arg_22_1] != None and var_22_3 == var_22_2[arg_22_1]:
					var_22_4 = False
				elif var_22_1[arg_22_1] != None:
					var_22_4 = bit.band(var_22_3, var_22_1[arg_22_1]) > 0

				setActive(arg_22_0.dropdownDic[iter_22_0].virtualBtn, var_22_4)

				if not arg_22_0.onInit:
					arg_22_0.contextData.indexDatas[iter_22_0] = arg_22_0.contextData.customPanels[iter_22_0].options[1]

				arg_22_0.dropdownDic[iter_22_0].UpdateVirtualBtn()
				arg_22_0.dropdownDic[iter_22_0].ActionInvoke("SelectLast")

def var_0_0.willExit(arg_23_0):
	LeanTween.cancel(go(arg_23_0.panel))

	for iter_23_0, iter_23_1 in pairs(arg_23_0.dropdownDic):
		iter_23_1.Destroy()

	for iter_23_2, iter_23_3 in pairs(arg_23_0.simpleDropdownDic):
		for iter_23_4, iter_23_5 in pairs(iter_23_3):
			iter_23_5.Destroy()

	arg_23_0.updateList = None

	pg.UIMgr.GetInstance().UnblurPanel(arg_23_0._tf)

def var_0_0.Clone2Full(arg_24_0, arg_24_1):
	local var_24_0 = {}
	local var_24_1 = arg_24_0.GetChild(0)
	local var_24_2 = arg_24_0.childCount

	for iter_24_0 = 0, var_24_2 - 1:
		table.insert(var_24_0, arg_24_0.GetChild(iter_24_0))

	for iter_24_1 = var_24_2, arg_24_1 - 1:
		local var_24_3 = cloneTplTo(var_24_1, arg_24_0)

		var_24_3.name = iter_24_1

		table.insert(var_24_0, tf(var_24_3))

	local var_24_4 = arg_24_0.childCount

	for iter_24_2 = 0, var_24_4 - 1:
		setActive(arg_24_0.GetChild(iter_24_2), iter_24_2 < arg_24_1)

	for iter_24_3 = var_24_4, arg_24_1 + 1, -1:
		table.remove(var_24_0)

	return var_24_0

return var_0_0
