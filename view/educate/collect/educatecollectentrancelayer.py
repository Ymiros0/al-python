local var_0_0 = class("EducateCollectEntranceLayer", import("..base.EducateBaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "EducateCollectEntranceUI"

def var_0_0.init(arg_2_0):
	arg_2_0.initData()
	arg_2_0.findUI()
	arg_2_0.addListener()

def var_0_0.initData(arg_3_0):
	local var_3_0 = getProxy(EducateProxy)

	arg_3_0.memories = var_3_0.GetMemories()
	arg_3_0.endings = var_3_0.GetFinishEndings()

def var_0_0.findUI(arg_4_0):
	arg_4_0.anim = arg_4_0.findTF("anim_root").GetComponent(typeof(Animation))
	arg_4_0.animEvent = arg_4_0.findTF("anim_root").GetComponent(typeof(DftAniEvent))

	arg_4_0.animEvent.SetEndEvent(function()
		arg_4_0.emit(var_0_0.ON_CLOSE))

	arg_4_0.contentTF = arg_4_0.findTF("anim_root/content")
	arg_4_0.memoryBtn = arg_4_0.findTF("memory_btn", arg_4_0.contentTF)
	arg_4_0.polaroidBtn = arg_4_0.findTF("polaroid_btn", arg_4_0.contentTF)
	arg_4_0.endingBtn = arg_4_0.findTF("ending_btn", arg_4_0.contentTF)
	arg_4_0.reviewBtn = arg_4_0.findTF("review_btn", arg_4_0.contentTF)

def var_0_0.addListener(arg_6_0):
	onButton(arg_6_0, arg_6_0._tf, function()
		arg_6_0._close(), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.memoryBtn, function()
		arg_6_0.emit(var_0_0.EDUCATE_GO_SUBLAYER, Context.New({
			mediator = EducateCollectMediatorTemplate,
			viewComponent = EducateMemoryLayer
		})), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.polaroidBtn, function()
		if isActive(arg_6_0.findTF("lock", arg_6_0.polaroidBtn)):
			return

		arg_6_0.emit(var_0_0.EDUCATE_GO_SUBLAYER, Context.New({
			mediator = EducateCollectMediatorTemplate,
			viewComponent = EducatePolaroidLayer
		}))
		setActive(arg_6_0.findTF("new", arg_6_0.polaroidBtn), False), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.endingBtn, function()
		if isActive(arg_6_0.findTF("lock", arg_6_0.endingBtn)):
			return

		arg_6_0.emit(var_0_0.EDUCATE_GO_SUBLAYER, Context.New({
			mediator = EducateCollectMediatorTemplate,
			viewComponent = EducateEndingLayer
		})), SFX_PANEL)
	onButton(arg_6_0, arg_6_0.reviewBtn, function()
		arg_6_0.emit(var_0_0.ON_CLOSE)
		pg.m02.sendNotification(GAME.GO_SCENE, SCENE.WORLD_COLLECTION, {
			page = WorldMediaCollectionScene.PAGE_MEMORTY,
			memoryGroup = EducateConst.REVIEW_GROUP_ID
		}), SFX_PANEL)

def var_0_0.didEnter(arg_12_0):
	local var_12_0 = #pg.child_memory.all

	setText(arg_12_0.findTF("Text", arg_12_0.memoryBtn), #arg_12_0.memories .. "/" .. var_12_0)
	arg_12_0.updateMemoryTip()

	local var_12_1, var_12_2 = getProxy(EducateProxy).GetPolaroidGroupCnt()

	setText(arg_12_0.findTF("Text", arg_12_0.polaroidBtn), var_12_1 .. "/" .. var_12_2)
	setActive(arg_12_0.findTF("lock", arg_12_0.polaroidBtn), not EducateHelper.IsSystemUnlock(EducateConst.SYSTEM_POLAROID))
	setActive(arg_12_0.findTF("new", arg_12_0.polaroidBtn), EducateTipHelper.IsShowNewTip(EducateTipHelper.NEW_POLAROID))

	local var_12_3 = #pg.child_ending.all

	setText(arg_12_0.findTF("unlock/Text", arg_12_0.endingBtn), #arg_12_0.endings .. "/" .. var_12_3)

	local var_12_4 = EducateHelper.IsSystemUnlock(EducateConst.SYSTEM_ENDING) or #arg_12_0.endings > 0

	setActive(arg_12_0.findTF("unlock", arg_12_0.endingBtn), var_12_4)
	setActive(arg_12_0.findTF("lock", arg_12_0.endingBtn), not var_12_4)
	pg.UIMgr.GetInstance().BlurPanel(arg_12_0._tf)
	EducateGuideSequence.CheckGuide(arg_12_0.__cname, function()
		return)

def var_0_0.updateMemoryTip(arg_14_0):
	local var_14_0 = underscore.any(pg.child_memory.all, function(arg_15_0)
		return EducateTipHelper.IsShowNewTip(EducateTipHelper.NEW_MEMORY, arg_15_0))

	setActive(arg_14_0.findTF("new", arg_14_0.memoryBtn), var_14_0)

def var_0_0._close(arg_16_0):
	arg_16_0.anim.Play("anim_educate_collectentrance_out")

def var_0_0.onBackPressed(arg_17_0):
	arg_17_0._close()

def var_0_0.willExit(arg_18_0):
	arg_18_0.animEvent.SetEndEvent(None)
	pg.UIMgr.GetInstance().UnblurPanel(arg_18_0._tf)

return var_0_0
