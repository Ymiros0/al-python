local var_0_0 = import(".MapBuilder")
local var_0_1 = class("MapBuilderEscort", var_0_0)

def var_0_1.GetType(arg_1_0):
	return var_0_0.TYPEESCORT

def var_0_1.getUIName(arg_2_0):
	return "escort_levels"

def var_0_1.OnInit(arg_3_0):
	arg_3_0.tpl = arg_3_0._tf.Find("escort_level_tpl")
	arg_3_0.itemHolder = arg_3_0._tf.Find("items")

def var_0_1.Update(arg_4_0, arg_4_1):
	arg_4_0.map.pivot = Vector2(0.5, 0.5)
	arg_4_0.float.pivot = Vector2(0.5, 0.5)

	local var_4_0 = arg_4_0.map.rect.width / arg_4_0.map.rect.height
	local var_4_1 = arg_4_0._parentTf.rect.width / arg_4_0._parentTf.rect.height
	local var_4_2 = 1

	if var_4_0 < var_4_1:
		var_4_2 = arg_4_0._parentTf.rect.width / 1280
		arg_4_0._tf.localScale = Vector3(var_4_2, var_4_2, 1)
	else
		var_4_2 = arg_4_0._parentTf.rect.height / 720
		arg_4_0._tf.localScale = Vector3(var_4_2, var_4_2, 1)

	arg_4_0.scaleRatio = var_4_2

	local var_4_3 = string.split(arg_4_1.getConfig("name"), "||")

	setText(arg_4_0.sceneParent.chapterName, var_4_3[1])
	arg_4_0.sceneParent.loader.GetSprite("chapterno", "chapterex", arg_4_0.sceneParent.chapterNoTitle, True)
	var_0_1.super.Update(arg_4_0, arg_4_1)

def var_0_1.UpdateButtons(arg_5_0):
	arg_5_0.sceneParent.updateDifficultyBtns()
	arg_5_0.sceneParent.updateActivityBtns()

def var_0_1.UpdateEscortInfo(arg_6_0):
	local var_6_0 = getProxy(ChapterProxy)
	local var_6_1 = var_6_0.getMaxEscortChallengeTimes()

	setText(arg_6_0.sceneParent.escortBar.Find("times/text"), var_6_1 - var_6_0.escortChallengeTimes .. "/" .. var_6_1)
	onButton(arg_6_0.sceneParent, arg_6_0.sceneParent.mapHelpBtn, function()
		arg_6_0.InvokeParent("HandleShowMsgBox", {
			type = MSGBOX_TYPE_HELP,
			helps = i18n("levelScene_escort_help_tip")
		}), SFX_PANEL)

def var_0_1.UpdateMapItems(arg_8_0):
	var_0_1.super.UpdateMapItems(arg_8_0)
	arg_8_0.UpdateEscortInfo()

	local var_8_0 = arg_8_0.data

	setActive(arg_8_0.sceneParent.escortBar, True)
	setActive(arg_8_0.sceneParent.mapHelpBtn, True)

	local var_8_1 = getProxy(ChapterProxy)
	local var_8_2 = getProxy(ChapterProxy).getEscortChapterIds()
	local var_8_3 = _.filter(var_8_0.getChapters(), function(arg_9_0)
		return table.contains(var_8_2, arg_9_0.id))
	local var_8_4 = UIItemList.New(arg_8_0.itemHolder, arg_8_0.tpl)

	var_8_4.make(function(arg_10_0, arg_10_1, arg_10_2)
		if arg_10_0 == UIItemList.EventUpdate:
			arg_8_0.UpdateEscortItem(arg_10_2, var_8_3[arg_10_1 + 1].id, var_8_3[arg_10_1 + 1]))
	var_8_4.align(#var_8_3)

def var_0_1.UpdateEscortItem(arg_11_0, arg_11_1, arg_11_2, arg_11_3):
	local var_11_0 = pg.escort_template[arg_11_2]

	assert(var_11_0, "escort template not exist. " .. arg_11_2)

	local var_11_1 = getProxy(ChapterProxy).getActiveChapter(True)

	arg_11_1.name = "chapter_" .. arg_11_3.id

	local var_11_2 = arg_11_0.map.rect

	arg_11_1.anchoredPosition = Vector2(var_11_2.width / arg_11_0.scaleRatio * (tonumber(var_11_0.pos_x) - 0.5), var_11_2.height / arg_11_0.scaleRatio * (tonumber(var_11_0.pos_y) - 0.5))

	local var_11_3 = arg_11_1.Find("fighting")
	local var_11_4 = var_11_1 and var_11_1.id == arg_11_3.id

	setActive(var_11_3, var_11_4)
	arg_11_0.DeleteTween("fighting" .. arg_11_3.id)

	if var_11_4:
		setImageAlpha(var_11_3, 1)
		arg_11_0.RecordTween("fighting" .. arg_11_3.id, LeanTween.alpha(var_11_3, 0, 0.5).setEase(LeanTweenType.easeInOutSine).setLoopPingPong().uniqueId)

	GetImageSpriteFromAtlasAsync("levelmap/mapquad/" .. var_11_0.pic, "", arg_11_1, True)

	local var_11_5 = arg_11_1.Find("anim")
	local var_11_6 = getProxy(ChapterProxy).getEscortChapterIds()
	local var_11_7 = table.indexof(var_11_6, arg_11_2)
	local var_11_8 = ({
		Color.green,
		Color.yellow,
		Color.red
	})[var_11_7 or 1]
	local var_11_9 = var_11_5.GetComponentsInChildren(typeof(Image))

	for iter_11_0 = 0, var_11_9.Length - 1:
		var_11_9[iter_11_0].color = var_11_8

	setImageColor(arg_11_1, var_11_8)

	local var_11_10 = arg_11_3.id

	onButton(arg_11_0.sceneParent, arg_11_1, function()
		local var_12_0 = getProxy(ChapterProxy).getChapterById(var_11_10)

		arg_11_0.InvokeParent("TrySwitchChapter", var_12_0), SFX_PANEL)

def var_0_1.OnShow(arg_13_0):
	setActive(arg_13_0.sceneParent.mainLayer.Find("title_chapter_lines"), True)
	setActive(arg_13_0.sceneParent.topChapter.Find("title_chapter"), True)
	setActive(arg_13_0.sceneParent.topChapter.Find("type_escort"), True)

def var_0_1.OnHide(arg_14_0):
	setActive(arg_14_0.sceneParent.mainLayer.Find("title_chapter_lines"), False)
	setActive(arg_14_0.sceneParent.topChapter.Find("title_chapter"), False)
	setActive(arg_14_0.sceneParent.topChapter.Find("type_escort"), False)
	setActive(arg_14_0.sceneParent.escortBar, False)
	setActive(arg_14_0.sceneParent.mapHelpBtn, False)

return var_0_1
