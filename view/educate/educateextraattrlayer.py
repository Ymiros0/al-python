local var_0_0 = class("EducateExtraAttrLayer", import(".base.EducateBaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "EducateExtraAttrUI"

def var_0_0.init(arg_2_0):
	arg_2_0.initData()
	arg_2_0.findUI()
	arg_2_0.addListener()

def var_0_0.initData(arg_3_0):
	arg_3_0.char = getProxy(EducateProxy).GetCharData()
	arg_3_0.attrList = arg_3_0.char.GetAttrIdsByType(EducateChar.ATTR_TYPE_PERSONALITY)
	arg_3_0.selectedIndex = 0

def var_0_0.findUI(arg_4_0):
	arg_4_0.windowTF = arg_4_0.findTF("window")
	arg_4_0.attrUIList = UIItemList.New(arg_4_0.findTF("content", arg_4_0.windowTF), arg_4_0.findTF("content/tpl", arg_4_0.windowTF))
	arg_4_0.avatarTF = arg_4_0.findTF("avatar", arg_4_0.windowTF)
	arg_4_0.curPersonalText = arg_4_0.findTF("Text", arg_4_0.avatarTF)
	arg_4_0.sureBtn = arg_4_0.findTF("sure_btn", arg_4_0.windowTF)

def var_0_0.addListener(arg_5_0):
	onButton(arg_5_0, arg_5_0.sureBtn, function()
		if arg_5_0.selectedIndex == 0:
			return

		arg_5_0.emit(var_0_0.EDUCATE_ON_MSG_TIP, {
			content = i18n("child_extraAttr_sure_tip"),
			def onYes:()
				arg_5_0.emit(EducateExtraAttrMediator.ON_ATTR_ADD, {
					id = arg_5_0.attrList[arg_5_0.selectedIndex]
				})
				arg_5_0.emit(var_0_0.ON_CLOSE)
		}), SFX_PANEL)

def var_0_0.didEnter(arg_8_0):
	pg.UIMgr.GetInstance().OverlayPanel(arg_8_0._tf, {
		groupName = arg_8_0.getGroupNameFromData(),
		weight = arg_8_0.getWeightFromData() + 1
	})
	arg_8_0.attrUIList.make(function(arg_9_0, arg_9_1, arg_9_2)
		if arg_9_0 == UIItemList.EventInit:
			local var_9_0 = pg.child_attr[arg_8_0.attrList[arg_9_1 + 1]]

			LoadImageSpriteAsync("educateprops/" .. var_9_0.icon, arg_8_0.findTF("icon", arg_9_2), True)
			setText(arg_8_0.findTF("name", arg_9_2), var_9_0.name)
			onButton(arg_8_0, arg_9_2, function()
				if arg_8_0.selectedIndex == arg_9_1 + 1:
					return

				arg_8_0.selectedIndex = arg_9_1 + 1

				arg_8_0.updateView(), SFX_PANEL)
		elif arg_9_0 == UIItemList.EventUpdate:
			setActive(arg_8_0.findTF("selected", arg_9_2), arg_8_0.selectedIndex == arg_9_1 + 1))
	arg_8_0.updateView()

def var_0_0.updateView(arg_11_0):
	arg_11_0.attrUIList.align(#arg_11_0.attrList)

	local var_11_0 = arg_11_0.char.GetPaintingName()
	local var_11_1 = arg_11_0.char.GetPersonalityId()

	setText(arg_11_0.curPersonalText, "当前主导个性：" .. pg.child_attr[var_11_1].name)

def var_0_0.willExit(arg_12_0):
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_12_0._tf)

return var_0_0
