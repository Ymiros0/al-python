local var_0_0 = class("MetaCharacterLevelMaxBoxShowCommand", pm.SimpleCommand)

def var_0_0.execute(arg_1_0, arg_1_1):
	local var_1_0 = arg_1_1.getBody()
	local var_1_1 = getProxy(MetaCharacterProxy)

	if not var_1_1:
		return

	local var_1_2 = getProxy(ChapterProxy)
	local var_1_3 = var_1_2.getActiveChapter()
	local var_1_4

	if var_1_3:
		var_1_4 = var_1_2.GetChapterAutoFlag(var_1_3.id) == 1

	if var_1_4:
		return

	local var_1_5 = var_1_1.getMetaSkillLevelMaxInfoList()

	if var_1_5 and #var_1_5 > 0:
		local var_1_6 = ""

		for iter_1_0, iter_1_1 in ipairs(var_1_5):
			local var_1_7 = iter_1_1.metaShipVO
			local var_1_8 = iter_1_1.metaSkillID
			local var_1_9 = var_1_7.getName()
			local var_1_10 = setColorStr(var_1_9, COLOR_GREEN)

			if iter_1_0 < #var_1_5:
				var_1_6 = var_1_6 .. var_1_10 .. "、"
			else
				var_1_6 = var_1_6 .. var_1_10

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("meta_skill_maxtip", var_1_6),
			def onYes:()
				pg.m02.sendNotification(GAME.GO_SCENE, SCENE.METACHARACTER, {
					autoOpenTactics = True,
					autoOpenShipConfigID = var_1_5[1].metaShipVO.configId
				}),
			def onClose:()
				if var_1_0.closeFunc:
					var_1_0.closeFunc(),
			weight = LayerWeightConst.TOP_LAYER
		})

	var_1_1.clearMetaSkillLevelMaxInfoList()

return var_0_0
