local var_0_0 = class("EducateMemoryLayer", import(".EducateCollectLayerTemplate"))

def var_0_0.getUIName(arg_1_0):
	return "EducateMemoryUI"

def var_0_0.initConfig(arg_2_0):
	arg_2_0.config = pg.child_memory

def var_0_0.didEnter(arg_3_0):
	setText(arg_3_0.findTF("review_btn/Text", arg_3_0.performTF), i18n("child_btn_review"))

	arg_3_0.memories = getProxy(EducateProxy).GetMemories()

	setText(arg_3_0.curCntTF, #arg_3_0.memories)
	setText(arg_3_0.allCntTF, "/" .. #arg_3_0.config.all)
	arg_3_0.updatePage()

def var_0_0.updateItem(arg_4_0, arg_4_1, arg_4_2):
	local var_4_0 = table.contains(arg_4_0.memories, arg_4_1.id)

	setActive(arg_4_0.findTF("lock", arg_4_2), not var_4_0)
	setActive(arg_4_0.findTF("unlock", arg_4_2), var_4_0)
	setActive(arg_4_0.findTF("unlock/new", arg_4_2), EducateTipHelper.IsShowNewTip(EducateTipHelper.NEW_MEMORY, arg_4_1.id))

	if var_4_0:
		LoadImageSpriteAsync("bg/" .. arg_4_1.pic, arg_4_0.findTF("unlock/mask/Image", arg_4_2))
		setText(arg_4_0.findTF("unlock/name", arg_4_2), arg_4_1.desc)
		onButton(arg_4_0, arg_4_2, function()
			arg_4_0.showPerformWindow(arg_4_1), SFX_PANEL)
	else
		removeOnButton(arg_4_2)
		setText(arg_4_0.findTF("lock/Text", arg_4_2), i18n("child_collect_lock"))

def var_0_0.showPerformWindow(arg_6_0, arg_6_1):
	EducateTipHelper.ClearNewTip(EducateTipHelper.NEW_MEMORY, arg_6_1.id)

	local var_6_0 = arg_6_0.findTF("Image", arg_6_0.performTF)

	LoadImageSpriteAsync("bg/" .. arg_6_1.pic, var_6_0)
	setActive(arg_6_0.performTF, True)
	onButton(arg_6_0, var_6_0, function()
		setActive(arg_6_0.performTF, False), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.findTF("review_btn", arg_6_0.performTF), function()
		pg.PerformMgr.GetInstance().PlayOne(arg_6_1.performance), SFX_PANEL)

def var_0_0.playAnimChange(arg_9_0):
	arg_9_0.anim.Stop()
	arg_9_0.anim.Play("anim_educate_memory_change")

def var_0_0.playAnimClose(arg_10_0):
	arg_10_0.anim.Play("anim_educate_memory_out")

return var_0_0
