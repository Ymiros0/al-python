local var_0_0 = class("MainBattleBtn", import(".MainBaseBtn"))

def var_0_0.OnClick(arg_1_0):
	local var_1_0 = getProxy(ChapterProxy).getActiveChapter()

	arg_1_0.emit(NewMainMediator.GO_SCENE, SCENE.LEVEL, {
		chapterId = var_1_0 and var_1_0.id,
		mapIdx = var_1_0 and var_1_0.getConfig("map")
	})

def var_0_0.IsFixed(arg_2_0):
	return True

return var_0_0
