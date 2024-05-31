local var_0_0 = class("SelectEliteCommanderCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = var_1_0.chapterId
	local var_1_2 = var_1_0.index
	local var_1_3 = var_1_0.pos
	local var_1_4 = var_1_0.commanderId
	local var_1_5 = var_1_0.callback
	local var_1_6 = getProxy(ChapterProxy)
	local var_1_7 = var_1_6.getChapterById(var_1_1)

	if var_1_4:
		local var_1_8, var_1_9 = Commander.canEquipToEliteChapter(var_1_1, var_1_2, var_1_3, var_1_4)

		if not var_1_8:
			pg.TipsMgr.GetInstance().ShowTips(var_1_9)

			return

	var_1_7.updateCommander(var_1_2, var_1_3, var_1_4)
	var_1_6.updateChapter(var_1_7)
	var_1_6.duplicateEliteFleet(var_1_7)

	if var_1_5:
		var_1_5()

return var_0_0
