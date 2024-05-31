local var_0_0 = class("EducateCollectLayerTemplate", import("..base.EducateBaseUI"))

def var_0_0.getUIName(arg_1_0):
	assert(None, "getUIName方法必须由子类实现")

def var_0_0.initConfig(arg_2_0):
	assert(None, "initConfig方法必须由子类实现")

def var_0_0.init(arg_3_0):
	arg_3_0.anim = arg_3_0.findTF("anim_root").GetComponent(typeof(Animation))
	arg_3_0.animEvent = arg_3_0.findTF("anim_root").GetComponent(typeof(DftAniEvent))

	arg_3_0.animEvent.SetEndEvent(function()
		arg_3_0.emit(var_0_0.ON_CLOSE))

	arg_3_0.closeBtn = arg_3_0.findTF("anim_root/bg")
	arg_3_0.windowTF = arg_3_0.findTF("anim_root/window")
	arg_3_0.curCntTF = arg_3_0.findTF("collect/cur", arg_3_0.windowTF)
	arg_3_0.allCntTF = arg_3_0.findTF("collect/all", arg_3_0.windowTF)
	arg_3_0.pageTF = arg_3_0.findTF("page", arg_3_0.windowTF)
	arg_3_0.nextBtn = arg_3_0.findTF("next_btn", arg_3_0.windowTF)
	arg_3_0.lastBtn = arg_3_0.findTF("last_btn", arg_3_0.windowTF)
	arg_3_0.paginationTF = arg_3_0.findTF("pagination", arg_3_0.windowTF)
	arg_3_0.performTF = arg_3_0.findTF("anim_root/perform")

	setActive(arg_3_0.performTF, False)
	arg_3_0.initConfig()

	arg_3_0.onePageCnt = arg_3_0.pageTF.childCount
	arg_3_0.pages = math.ceil(#arg_3_0.config.all / arg_3_0.onePageCnt)
	arg_3_0.curPageIndex = 1

	onButton(arg_3_0, arg_3_0.closeBtn, function()
		arg_3_0.playAnimClose(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.nextBtn, function()
		arg_3_0.playAnimChange()

		arg_3_0.curPageIndex = arg_3_0.curPageIndex + 1

		arg_3_0.updatePage(), SFX_PANEL)
	onButton(arg_3_0, arg_3_0.lastBtn, function()
		arg_3_0.playAnimChange()

		arg_3_0.curPageIndex = arg_3_0.curPageIndex - 1

		arg_3_0.updatePage(), SFX_PANEL)
	pg.UIMgr.GetInstance().OverlayPanel(arg_3_0._tf, {
		groupName = arg_3_0.getGroupNameFromData(),
		weight = arg_3_0.getWeightFromData() + 2
	})

def var_0_0.updatePage(arg_8_0):
	setActive(arg_8_0.nextBtn, arg_8_0.pages != 1 and arg_8_0.curPageIndex < arg_8_0.pages)
	setActive(arg_8_0.lastBtn, arg_8_0.pages != 1 and arg_8_0.curPageIndex > 1)
	setText(arg_8_0.paginationTF, arg_8_0.curPageIndex .. "/" .. arg_8_0.pages)

	local var_8_0 = (arg_8_0.curPageIndex - 1) * arg_8_0.onePageCnt

	for iter_8_0 = 1, arg_8_0.onePageCnt:
		local var_8_1 = arg_8_0.findTF("frame_" .. iter_8_0, arg_8_0.pageTF)
		local var_8_2 = arg_8_0.config[arg_8_0.config.all[var_8_0 + iter_8_0]]

		if var_8_2:
			setActive(var_8_1, True)
			arg_8_0.updateItem(var_8_2, var_8_1)
		else
			setActive(var_8_1, False)

def var_0_0.updateItem(arg_9_0, arg_9_1, arg_9_2):
	assert(None, "updateItem方法必须由子类实现")

def var_0_0.playAnimChange(arg_10_0):
	assert(None, "playAnimClose方法必须由子类实现")

def var_0_0.playAnimClose(arg_11_0):
	assert(None, "playAnimClose方法必须由子类实现")

def var_0_0.onBackPressed(arg_12_0):
	arg_12_0.playAnimClose()

def var_0_0.willExit(arg_13_0):
	arg_13_0.animEvent.SetEndEvent(None)
	pg.UIMgr.GetInstance().UnOverlayPanel(arg_13_0._tf)

return var_0_0
