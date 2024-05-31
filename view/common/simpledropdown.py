local var_0_0 = class("SimpleDropdown", import("view.base.BaseSubView"))

def var_0_0.getUIName(arg_1_0):
	return "IndexDropdownUI"

def var_0_0.Ctor(arg_2_0, arg_2_1, arg_2_2, arg_2_3, arg_2_4, arg_2_5, arg_2_6, arg_2_7, arg_2_8, arg_2_9):
	var_0_0.super.Ctor(arg_2_0, arg_2_1, arg_2_2, arg_2_3)

	arg_2_0.tag = arg_2_4
	arg_2_0.virtualBtn = arg_2_5
	arg_2_0.virtualBtnTitle = findTF(arg_2_0.virtualBtn, "Image")
	arg_2_0.virtualBtnDropdownSign = findTF(arg_2_0.virtualBtn, "dropdown")
	arg_2_0.setting = arg_2_6
	arg_2_0.options = arg_2_0.setting.options
	arg_2_0.names = arg_2_0.setting.names
	arg_2_0.isSelected = True
	arg_2_0.onUpdate = arg_2_7
	arg_2_0.greySprite = arg_2_8
	arg_2_0.yellowSprite = arg_2_9

	arg_2_0.UpdateVirtualBtn()

def var_0_0.UpdateVirtualBtn(arg_3_0):
	local var_3_0 = arg_3_0.contextData.indexDatas[arg_3_0.tag]

	arg_3_0.preIndex = table.indexof(arg_3_0.options, var_3_0) or 1

	setText(arg_3_0.virtualBtnTitle, i18n(arg_3_0.names[arg_3_0.preIndex]))
	setImageSprite(arg_3_0.virtualBtn, arg_3_0.preIndex == 1 and arg_3_0.greySprite or arg_3_0.yellowSprite)

def var_0_0.OnInit(arg_4_0):
	arg_4_0.btnTpl = arg_4_0.findTF("resource/tpl")
	arg_4_0.btnList = {}
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
	GetComponent(arg_4_0.attrs, typeof(GridLayoutGroup)).constraintCount = 1

	for iter_4_0 = 1, #arg_4_0.options:
		local var_4_1 = arg_4_0.options[iter_4_0]

		if iter_4_0 == 1:
			-- block empty
		else
			local var_4_2 = tf(instantiate(arg_4_0.btnTpl))
			local var_4_3 = arg_4_0.findTF("Image", var_4_2)

			go(var_4_2).name = i18n(arg_4_0.names[iter_4_0])

			setActive(var_4_2, True)
			setActive(arg_4_0.findTF("dropdown", var_4_2), False)
			setText(var_4_3, i18n(arg_4_0.names[iter_4_0]))
			setParent(var_4_2, arg_4_0.attrs)
			onButton(arg_4_0, var_4_2, function()
				arg_4_0.UpdateData(iter_4_0)
				arg_4_0.UpdateBtnState(), SFX_UI_TAG)
			table.insert(arg_4_0.btnList, var_4_2)

	arg_4_0.UpdateVirtualBtn()
	arg_4_0.SelectLast()

def var_0_0.SelectLast(arg_8_0):
	arg_8_0.UpdateBtnState()

def var_0_0.UpdateData(arg_9_0, arg_9_1):
	arg_9_0.contextData.indexDatas[arg_9_0.tag] = arg_9_0.options[arg_9_1]

	if arg_9_0.onUpdate:
		arg_9_0.onUpdate()

def var_0_0.UpdateBtnState(arg_10_0):
	local function var_10_0(arg_11_0)
		setText(arg_10_0.mainTitle, i18n(arg_10_0.names[arg_11_0]))
		setText(arg_10_0.virtualBtnTitle, i18n(arg_10_0.names[arg_11_0]))

	local var_10_1 = False

	for iter_10_0, iter_10_1 in ipairs(arg_10_0.btnList):
		local var_10_2 = arg_10_0.options[iter_10_0 + 1] == arg_10_0.contextData.indexDatas[arg_10_0.tag]

		setImageSprite(iter_10_1, var_10_2 and arg_10_0.yellowSprite or arg_10_0.greySprite)

		if var_10_2:
			var_10_1 = True

			var_10_0(iter_10_0 + 1)

	if not var_10_1:
		var_10_0(1)

def var_0_0.Show(arg_12_0, arg_12_1):
	arg_12_0.attrs.localPosition = arg_12_1
	arg_12_0.mainBtn.anchoredPosition = arg_12_0.attrs.anchoredPosition
	arg_12_0.attrs.anchoredPosition = arg_12_0.attrs.anchoredPosition + Vector2.New(0, -45)

	setActive(arg_12_0._tf, True)
	setActive(arg_12_0.virtualBtnDropdownSign, False)
	arg_12_0.UpdateBtnState()

def var_0_0.Hide(arg_13_0):
	var_0_0.super.Hide(arg_13_0)
	setActive(arg_13_0.virtualBtnDropdownSign, True)

def var_0_0.OnDestroy(arg_14_0):
	arg_14_0.btnList = None

return var_0_0
