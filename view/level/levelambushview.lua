local var_0_0 = class("LevelAmbushView", import("..base.BaseSubView"))

function var_0_0.getUIName(arg_1_0)
	return "LevelAmbushView"
end

function var_0_0.OnInit(arg_2_0)
	arg_2_0:InitData()
	arg_2_0:InitUI()
	setActive(arg_2_0._tf, true)
end

function var_0_0.InitData(arg_3_0)
	arg_3_0.chapter = arg_3_0.contextData.chapterVO
	arg_3_0.fleet = arg_3_0.chapter.fleet

	local var_3_0 = arg_3_0.chapter:getChapterCell(arg_3_0.fleet.line.row, arg_3_0.fleet.line.column)

	arg_3_0.template = pg.expedition_data_template[var_3_0.attachmentId]
end

function var_0_0.InitUI(arg_4_0)
	local var_4_0 = findTF(arg_4_0._tf, "window")
	local var_4_1 = findTF(arg_4_0._tf, "window/ship/lv/Text")
	local var_4_2 = findTF(arg_4_0._tf, "window/ship/icon")
	local var_4_3 = findTF(arg_4_0._tf, "window/evade/rate")
	local var_4_4 = findTF(arg_4_0._tf, "window/fight_button")
	local var_4_5 = findTF(arg_4_0._tf, "window/dodge_button")

	GetImageSpriteFromAtlasAsync("enemies/" .. arg_4_0.template.icon, "", var_4_2)
	setText(var_4_1, arg_4_0.template.level)
	setText(var_4_3, math.floor(arg_4_0.chapter:getAmbushDodge(arg_4_0.fleet) * 100) .. "%")
	onButton(arg_4_0, var_4_4, function()
		arg_4_0:emit(LevelMediator2.ON_OP, {
			arg1 = 0,
			type = ChapterConst.OpAmbush,
			id = arg_4_0.fleet.id
		})
		arg_4_0:Destroy()
	end, SFX_UI_WEIGHANCHOR_ATTACK)
	onButton(arg_4_0, var_4_5, function()
		arg_4_0:emit(LevelMediator2.ON_OP, {
			arg1 = 1,
			type = ChapterConst.OpAmbush,
			id = arg_4_0.fleet.id
		})
		arg_4_0:Destroy()
	end, SFX_UI_WEIGHANCHOR_AVOID)

	var_4_0.localScale = Vector3(1, 0, 1)

	LeanTween.scaleY(var_4_0.gameObject, 1, 0.3):setOnComplete(System.Action(arg_4_0.onComplete))
end

function var_0_0.OnDestroy(arg_7_0)
	return
end

function var_0_0.SetFuncOnComplete(arg_8_0, arg_8_1)
	arg_8_0.onComplete = arg_8_1
end

return var_0_0
