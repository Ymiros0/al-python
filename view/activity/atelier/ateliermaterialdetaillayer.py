local var_0_0 = class("AtelierMaterialDetailLayer", import("view.base.BaseUI"))

def var_0_0.getUIName(arg_1_0):
	return "AtelierMaterialDetailUI"

def var_0_0.init(arg_2_0):
	arg_2_0.layerItemDetail = arg_2_0._tf
	arg_2_0.loader = AutoLoader.New()

def var_0_0.didEnter(arg_3_0):
	onButton(arg_3_0, arg_3_0.layerItemDetail.Find("BG"), function()
		arg_3_0.closeView(), SFX_CANCEL)
	onButton(arg_3_0, arg_3_0.layerItemDetail.Find("Window/Close"), function()
		arg_3_0.closeView(), SFX_CANCEL)
	arg_3_0.UpdateItemDetail()
	pg.UIMgr.GetInstance().BlurPanel(arg_3_0.layerItemDetail, None, {
		weight = LayerWeightConst.SECOND_LAYER
	})

def var_0_0.UpdateItemDetail(arg_6_0):
	local var_6_0 = arg_6_0.contextData.material

	arg_6_0.UpdateRyzaItem(arg_6_0.layerItemDetail.Find("Window/IconBG"), var_6_0)
	setText(arg_6_0.layerItemDetail.Find("Window/Name"), var_6_0.GetName())
	setText(arg_6_0.layerItemDetail.Find("Window/Description/Text"), var_6_0.GetDesc())

	local var_6_1 = var_6_0.GetSource()

	setText(arg_6_0.layerItemDetail.Find("Window/Source"), var_6_1[1])
	onButton(arg_6_0, arg_6_0.layerItemDetail.Find("Window/Go"), function()
		if var_6_1.chapterid:
			local var_7_0 = getProxy(ChapterProxy).getChapterById(var_6_1.chapterid)
			local var_7_1 = getProxy(ChapterProxy).getMapById(var_7_0.getConfig("map"))
			local var_7_2, var_7_3 = var_7_1.isUnlock()

			if not var_7_2:
				pg.TipsMgr.GetInstance().ShowTips(var_7_3)

				return

			if not var_7_0.isUnlock():
				pg.TipsMgr.GetInstance().ShowTips(i18n("battle_levelScene_chapter_lock"))

				return

			arg_6_0.emit(GAME.GO_SCENE, SCENE.LEVEL, {
				openChapterId = var_6_1.chapterid,
				chapterId = var_6_1.chapterid,
				mapIdx = var_7_1.id
			})
		elif var_6_1.recipeid:
			local var_7_4 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_ATELIER_LINK)

			if not var_7_4 or var_7_4.isEnd():
				pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

				return

			local var_7_5 = var_7_4.GetFormulas()[var_6_1.recipeid]

			if var_7_5.GetType() != AtelierFormula.TYPE.TOOL and not var_7_4.IsCompleteAllTools():
				pg.TipsMgr.GetInstance().ShowTips(i18n("ryza_tip_unlock_all_tools"))

				return

			if not var_7_5.IsAvaliable():
				pg.TipsMgr.GetInstance().ShowTips(i18n("ryza_tip_composite_invalid"))

				return

			arg_6_0.emit(AtelierMaterialDetailMediator.GO_RECIPE, var_6_1.recipeid)
		elif var_6_1.taskid:
			local var_7_6 = getProxy(ActivityProxy).getActivityById(ActivityConst.RYZA_TASK)

			if not var_7_6 or var_7_6.isEnd():
				pg.TipsMgr.GetInstance().ShowTips(i18n("common_activity_end"))

				return

			arg_6_0.emit(GAME.GO_SCENE, SCENE.RYZA_TASK, {
				task_id = var_6_1.taskid
			}), SFX_PANEL)

local var_0_1 = "ui/AtelierCommonUI_atlas"

def var_0_0.UpdateRyzaItem(arg_8_0, arg_8_1, arg_8_2, arg_8_3):
	local var_8_0 = "icon_frame_" .. arg_8_2.GetRarity()

	if arg_8_3:
		var_8_0 = var_8_0 .. "_small"

	arg_8_0.loader.GetSpriteQuiet(var_0_1, var_8_0, arg_8_1)
	arg_8_0.loader.GetSpriteQuiet(arg_8_2.GetIconPath(), "", arg_8_1.Find("Icon"))

	if not IsNil(arg_8_1.Find("Lv")):
		setText(arg_8_1.Find("Lv/Text"), arg_8_2.GetLevel())

	local var_8_1 = arg_8_2.GetProps()
	local var_8_2 = CustomIndexLayer.Clone2Full(arg_8_1.Find("List"), #var_8_1)

	for iter_8_0, iter_8_1 in ipairs(var_8_2):
		arg_8_0.loader.GetSpriteQuiet(var_0_1, "element_" .. AtelierFormulaCircle.ELEMENT_NAME[var_8_1[iter_8_0]], iter_8_1)

	if not IsNil(arg_8_1.Find("Text")):
		setText(arg_8_1.Find("Text"), arg_8_2.count or "")

def var_0_0.willExit(arg_9_0):
	pg.UIMgr.GetInstance().UnblurPanel(arg_9_0.layerItemDetail, arg_9_0._tf)
	arg_9_0.loader.Clear()

return var_0_0
