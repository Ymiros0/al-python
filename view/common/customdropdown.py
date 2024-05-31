local var_0_0 = class("CustomDropdown", import("view.base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "IndexDropdownUI"

def var_0_0.Ctor(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4, arg_2_5):
	var_0_0.super.Ctor(arg_2_0, arg_2_1, arg_2_2, arg_2_3)

	arg_2_0.tag = arg_2_4
	arg_2_0.virtualBtn = arg_2_5
	arg_2_0.virtualBtnTitle = findTF(arg_2_0.virtualBtn, "Image")
	arg_2_0.virtualBtnDropdownSign = findTF(arg_2_0.virtualBtn, "dropdown")
	arg_2_0.setting = arg_2_0.contextData.customPanels[arg_2_0.tag]
	arg_2_0.mode = arg_2_0.setting.mode or CustomIndexLayer.Mode.OR
	arg_2_0.options = arg_2_0.setting.options
	arg_2_0.names = arg_2_0.setting.names

	arg_2_0.UpdateVirtualBtn()

def var_0_0.UpdateVirtualBtn(arg_3_0):
	arg_3_0.contextData.indexDatas[arg_3_0.tag] = arg_3_0.contextData.indexDatas[arg_3_0.tag] or arg_3_0.options[1]
	arg_3_0.preIndex = table.indexof(arg_3_0.options, arg_3_0.contextData.indexDatas[arg_3_0.tag])

	setText(arg_3_0.virtualBtnTitle, i18n(arg_3_0.names[arg_3_0.preIndex]))

def var_0_0.OnInit(arg_4_0):
	arg_4_0.btnTpl = arg_4_0.findTF("resource/tpl")
	arg_4_0.btnList = {}
	arg_4_0.greySprite = arg_4_0.findTF("resource/grey").GetComponent(typeof(Image)).sprite
	arg_4_0.yellowSprite = arg_4_0.findTF("resource/yellow").GetComponent(typeof(Image)).sprite
	arg_4_0.mainBtn = tf(instantiate(arg_4_0.btnTpl))
	arg_4_0.mainTitle = arg_4_0.findTF("Image", arg_4_0.mainBtn)

	setImageSprite(arg_4_0.mainBtn, arg_4_0.yellowSprite)
	setParent(arg_4_0.mainBtn, arg_4_0._tf)
	setActive(arg_4_0.mainBtn, True)

	arg_4_0.findTF("dropdown", arg_4_0.mainBtn).localEulerAngles = Vector3.New(0, 0, 0)

	onButton(arg_4_0, arg_4_0.mainBtn, function()
		arg_4_0.Hide())

	local var_4_0 = arg_4_0.findTF("mask", arg_4_0._tf)

	onButton(arg_4_0, var_4_0, function()
		arg_4_0.Hide())

	arg_4_0.attrs = arg_4_0.findTF("Attrs", arg_4_0._tf)

	local var_4_1 = GetComponent(arg_4_0.attrs, typeof(GridLayoutGroup))

	if #arg_4_0.options > 6:
		var_4_1.constraintCount = 2
	else
		var_4_1.constraintCount = 1

	for iter_4_0 = 1, #arg_4_0.options:
		local var_4_2 = arg_4_0.options[iter_4_0]

		if iter_4_0 == 1:
			-- block empty
		else
			local var_4_3 = tf(instantiate(arg_4_0.btnTpl))
			local var_4_4 = arg_4_0.findTF("Image", var_4_3)

			go(var_4_3).name = i18n(arg_4_0.names[iter_4_0])

			setActive(var_4_3, True)
			setActive(arg_4_0.findTF("dropdown", var_4_3), False)
			setText(var_4_4, i18n(arg_4_0.names[iter_4_0]))
			setParent(var_4_3, arg_4_0.attrs)
			onButton(arg_4_0, var_4_3, function()
				arg_4_0.UpdateData(iter_4_0)
				arg_4_0.UpdateBtnState(), SFX_UI_TAG)
			table.insert(arg_4_0.btnList, var_4_3)

	arg_4_0.SelectLast()

def var_0_0.SelectLast(arg_8_0):
	arg_8_0.UpdateBtnState()

def var_0_0.UpdateData(arg_9_0, arg_9_1):
	local var_9_0 = arg_9_0.contextData.indexDatas[arg_9_0.tag]
	local var_9_1 = bit.band(var_9_0, arg_9_0.options[arg_9_1]) > 0

	if arg_9_0.mode == CustomIndexLayer.Mode.AND:
		if var_9_1:
			arg_9_0.contextData.indexDatas[arg_9_0.tag] = var_9_0 - arg_9_0.options[arg_9_1]
		else
			arg_9_0.contextData.indexDatas[arg_9_0.tag] = bit.bxor(var_9_0, arg_9_0.options[arg_9_1])
	elif arg_9_0.mode == CustomIndexLayer.Mode.OR:
		if var_9_0 != arg_9_0.options[1] and var_9_1:
			arg_9_0.contextData.indexDatas[arg_9_0.tag] = var_9_0 - arg_9_0.options[arg_9_1]
		else
			arg_9_0.contextData.indexDatas[arg_9_0.tag] = arg_9_0.options[arg_9_1]

		if arg_9_0.contextData.indexDatas[arg_9_0.tag] == 0:
			arg_9_0.contextData.indexDatas[arg_9_0.tag] = arg_9_0.options[1]

def var_0_0.UpdateBtnState(arg_10_0):
	local function var_10_0(arg_11_0)
		setText(arg_10_0.mainTitle, i18n(arg_10_0.names[arg_11_0]))
		setText(arg_10_0.virtualBtnTitle, i18n(arg_10_0.names[arg_11_0]))

	if arg_10_0.mode == CustomIndexLayer.Mode.AND:
		if arg_10_0.contextData.indexDatas[arg_10_0.tag] == arg_10_0.options[1]:
			for iter_10_0, iter_10_1 in ipairs(arg_10_0.btnList):
				setImageSprite(iter_10_1, arg_10_0.greySprite)
		else
			for iter_10_2, iter_10_3 in ipairs(arg_10_0.btnList):
				local var_10_1 = bit.band(arg_10_0.contextData.indexDatas[arg_10_0.tag], arg_10_0.options[iter_10_2 + 1]) > 0

				setImageSprite(iter_10_3, var_10_1 and arg_10_0.yellowSprite or arg_10_0.greySprite)

		var_10_0(1)
	elif arg_10_0.mode == CustomIndexLayer.Mode.OR:
		local var_10_2 = False

		for iter_10_4, iter_10_5 in ipairs(arg_10_0.btnList):
			local var_10_3 = arg_10_0.options[iter_10_4 + 1] == arg_10_0.contextData.indexDatas[arg_10_0.tag]

			setImageSprite(iter_10_5, var_10_3 and arg_10_0.yellowSprite or arg_10_0.greySprite)

			if var_10_3:
				var_10_2 = True

				var_10_0(iter_10_4 + 1)

		if not var_10_2:
			var_10_0(1)

def var_0_0.Show(arg_12_0, arg_12_1):
	arg_12_0.attrs.localPosition = arg_12_1
	arg_12_0.mainBtn.anchoredPosition = arg_12_0.attrs.anchoredPosition
	arg_12_0.attrs.anchoredPosition = arg_12_0.attrs.anchoredPosition + Vector2.New(0, -45)

	setActive(arg_12_0._tf, True)
	setActive(arg_12_0.virtualBtnDropdownSign, False)

def var_0_0.Hide(arg_13_0):
	var_0_0.super.Hide(arg_13_0)
	setActive(arg_13_0.virtualBtnDropdownSign, True)

def var_0_0.OnDestroy(arg_14_0):
	arg_14_0.btnList = None

return var_0_0
