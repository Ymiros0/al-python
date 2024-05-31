local var_0_0 = class("EducateAwardInfoLayer", import("..base.EducateBaseUI"))
local var_0_1 = {
	Vector2(0, 115),
	Vector2(0, 162)
}
local var_0_2 = {
	Vector2(0, -280),
	Vector2(0, -315)
}
local var_0_3 = 0.4

def var_0_0.getUIName(arg_1_0):
	return "EducateAwardInfoUI"

def var_0_0.init(arg_2_0):
	pg.UIMgr.GetInstance().BlurPanel(arg_2_0._tf, False, {
		weight = LayerWeightConst.THIRD_LAYER
	})

	arg_2_0.drops = arg_2_0.contextData.items or {}
	arg_2_0.awardWindow = arg_2_0.findTF("award_window")
	arg_2_0.anim = arg_2_0.awardWindow.GetComponent(typeof(Animation))
	arg_2_0.animEvent = arg_2_0.awardWindow.GetComponent(typeof(DftAniEvent))

	arg_2_0.animEvent.SetEndEvent(function()
		if #arg_2_0.showPolaroidDrops > 0:
			setActive(arg_2_0.awardWindow, False)
			setActive(arg_2_0.polaroidWindow, True)

			arg_2_0.polaroidIndex = 1

			arg_2_0.showPolaroidAnim()
		else
			arg_2_0.emit(var_0_0.ON_CLOSE))

	arg_2_0.tipTF = arg_2_0.findTF("tip", arg_2_0.awardWindow)

	setText(arg_2_0.tipTF, i18n("child_close_tip"))

	arg_2_0.itemContent = arg_2_0.findTF("content/items", arg_2_0.awardWindow)
	arg_2_0.itemContainer = arg_2_0.findTF("items_scroll/content", arg_2_0.itemContent)
	arg_2_0.itemTpl = arg_2_0.findTF("item_tpl", arg_2_0.awardWindow)

	setActive(arg_2_0.itemTpl, False)

	arg_2_0.attrContent = arg_2_0.findTF("content/attrs", arg_2_0.awardWindow)
	arg_2_0.attrContainer = arg_2_0.findTF("attrs_scroll/content", arg_2_0.attrContent)
	arg_2_0.attrTpl = arg_2_0.findTF("attr_tpl", arg_2_0.awardWindow)

	setActive(arg_2_0.attrTpl, False)

	arg_2_0.polaroidWindow = arg_2_0.findTF("polaroid_window")
	arg_2_0.polaroidIconTF = arg_2_0.findTF("content/mask/icon", arg_2_0.polaroidWindow)
	arg_2_0.polaroidDescTF = arg_2_0.findTF("content/desc", arg_2_0.polaroidWindow)

	setActive(arg_2_0.awardWindow, False)
	setActive(arg_2_0.polaroidWindow, False)
	arg_2_0._tf.SetAsLastSibling()

def var_0_0.didEnter(arg_4_0):
	onButton(arg_4_0, arg_4_0.findTF("close", arg_4_0.awardWindow), function()
		arg_4_0._close(), SFX_CANCEL)
	onButton(arg_4_0, arg_4_0.polaroidWindow, function()
		if arg_4_0.playing:
			return

		pg.TipsMgr.GetInstance().ShowTips(i18n("child_polaroid_get_tip"))

		if arg_4_0.polaroidIndex <= #arg_4_0.showPolaroidDrops:
			arg_4_0.showPolaroidAnim()
		else
			arg_4_0.emit(var_0_0.ON_CLOSE), SFX_CANCEL)

	arg_4_0.showAwardDrops = arg_4_0.getAwardDrops()
	arg_4_0.showAttrDrops = arg_4_0.getAttrDrops()
	arg_4_0.showPolaroidDrops = arg_4_0.getPolaroidDrops()

	local var_4_0 = #arg_4_0.showAttrDrops > 0

	setActive(arg_4_0.attrContent, var_4_0)
	arg_4_0.showWindow()

def var_0_0.showWindow(arg_7_0):
	if #arg_7_0.showAwardDrops > 0:
		arg_7_0.inAnimPlaying = True

		setActive(arg_7_0.awardWindow, True)

		local var_7_0 = #arg_7_0.showAttrDrops > 0 and "anim_educate_awardinfo_awardattr_in" or "anim_educate_awardinfo_award_in"

		arg_7_0.anim.Play(var_7_0)

		local var_7_1 = {}

		table.insert(var_7_1, function(arg_8_0)
			arg_7_0.managedTween(LeanTween.delayedCall, function()
				arg_8_0(), 0.33, None))

		local var_7_2 = math.max(#arg_7_0.showAttrDrops, #arg_7_0.showAwardDrops)

		for iter_7_0 = 1, var_7_2:
			table.insert(var_7_1, function(arg_10_0)
				local var_10_0 = arg_7_0.showAwardDrops[iter_7_0]

				if var_10_0:
					local var_10_1 = cloneTplTo(arg_7_0.itemTpl, arg_7_0.itemContainer)

					EducateHelper.UpdateDropShow(var_10_1, var_10_0)
					onButton(arg_7_0, var_10_1, function()
						arg_7_0.emit(var_0_0.EDUCATE_ON_ITEM, {
							drop = var_10_0
						}))

				local var_10_2 = arg_7_0.showAttrDrops[iter_7_0]

				if var_10_2:
					local var_10_3 = cloneTplTo(arg_7_0.attrTpl, arg_7_0.attrContainer)

					EducateHelper.UpdateDropShowForAttr(var_10_3, var_10_2)

				arg_7_0.managedTween(LeanTween.delayedCall, function()
					arg_10_0(), 0.066, None))

		seriesAsync(var_7_1, function()
			arg_7_0.managedTween(LeanTween.delayedCall, function()
				arg_7_0.inAnimPlaying = False, 0.066, None))
	elif #arg_7_0.showPolaroidDrops > 0:
		setActive(arg_7_0.polaroidWindow, True)

		arg_7_0.polaroidIndex = 1

		arg_7_0.showPolaroidAnim()
	else
		assert(None, "不合法掉落, award/polaroid都为空, 请检查对应配置~")

def var_0_0.getAwardDrops(arg_15_0):
	return EducateHelper.FilterDropByTypes(arg_15_0.drops, {
		EducateConst.DROP_TYPE_ATTR,
		EducateConst.DROP_TYPE_RES,
		EducateConst.DROP_TYPE_ITEM,
		EducateConst.DROP_TYPE_BUFF
	})

def var_0_0.getAttrDrops(arg_16_0):
	local var_16_0 = EducateHelper.FilterDropByTypes(arg_16_0.drops, {
		EducateConst.DROP_TYPE_ITEM
	})
	local var_16_1 = {}

	underscore.each(var_16_0, function(arg_17_0)
		var_16_1 = table.mergeArray(var_16_1, EducateHelper.GetItemAddDrops(arg_17_0)))

	return var_16_1

def var_0_0.getPolaroidDrops(arg_18_0):
	return EducateHelper.FilterDropByTypes(arg_18_0.drops, {
		EducateConst.DROP_TYPE_POLAROID
	})

def var_0_0.showPolaroidAnim(arg_19_0):
	arg_19_0.playing = True

	local var_19_0 = arg_19_0.showPolaroidDrops[arg_19_0.polaroidIndex]

	setActive(arg_19_0.polaroidDescTF, False)

	local var_19_1 = pg.child_polaroid[var_19_0.id]

	LoadImageSpriteAsync("educatepolaroid/" .. var_19_1.pic, arg_19_0.polaroidIconTF)
	setText(arg_19_0.polaroidDescTF, var_19_1.title)

	local var_19_2 = {}

	table.insert(var_19_2, function(arg_20_0)
		arg_19_0.managedTween(LeanTween.delayedCall, function()
			setActive(arg_19_0.polaroidDescTF, True)
			arg_20_0(), var_0_3, None))

	if getProxy(EducateProxy).CheckNewSecretaryTip():
		table.insert(var_19_2, function(arg_22_0)
			arg_19_0.emit(var_0_0.EDUCATE_ON_UNLOCK_TIP, {
				type = EducateUnlockTipLayer.UNLOCK_NEW_SECRETARY,
				onExit = arg_22_0
			}))

	seriesAsync(var_19_2, function()
		arg_19_0.playing = False
		arg_19_0.polaroidIndex = arg_19_0.polaroidIndex + 1)

def var_0_0._close(arg_24_0):
	if pg.NewGuideMgr.GetInstance().IsBusy():
		arg_24_0.emit(var_0_0.ON_CLOSE)

		return

	if arg_24_0.inAnimPlaying or arg_24_0.isCloseAnim:
		return

	arg_24_0.anim.Play("anim_educate_awardinfo_award_out")

	arg_24_0.isCloseAnim = True

def var_0_0.onBackPressed(arg_25_0):
	arg_25_0._close()

def var_0_0.willExit(arg_26_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_26_0._tf)

	if arg_26_0.contextData.removeFunc:
		arg_26_0.contextData.removeFunc()

		arg_26_0.contextData.removeFunc = None

return var_0_0
