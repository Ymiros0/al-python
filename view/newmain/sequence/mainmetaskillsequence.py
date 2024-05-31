local var_0_0 = class("MainMetaSkillSequence")

def var_0_0.Execute(arg_1_0, arg_1_1):
	arg_1_1 = arg_1_1 or function()
		return

	local var_1_0 = getProxy(MetaCharacterProxy)

	if not var_1_0:
		arg_1_1()

		return

	local var_1_1 = getProxy(ChapterProxy)
	local var_1_2 = var_1_1.getActiveChapter()
	local var_1_3

	if var_1_2:
		var_1_3 = var_1_1.GetChapterAutoFlag(var_1_2.id) == 1

	if var_1_3:
		arg_1_1()

		return

	local var_1_4 = var_1_0.getMetaSkillLevelMaxInfoList()

	if var_1_4 and #var_1_4 > 0:
		local var_1_5 = arg_1_0.GetShipName(var_1_4)

		pg.MsgboxMgr.GetInstance().ShowMsgBox({
			content = i18n("meta_skill_maxtip", var_1_5),
			def onYes:()
				pg.m02.sendNotification(GAME.GO_SCENE, SCENE.METACHARACTER, {
					autoOpenTactics = True,
					autoOpenShipConfigID = var_1_4[1].metaShipVO.configId
				}),
			onClose = arg_1_1,
			weight = LayerWeightConst.TOP_LAYER
		})
	else
		arg_1_1()

	var_1_0.clearMetaSkillLevelMaxInfoList()

def var_0_0.GetShipName(arg_4_0, arg_4_1):
	local var_4_0 = ""

	for iter_4_0, iter_4_1 in ipairs(arg_4_1):
		local var_4_1 = iter_4_1.metaShipVO
		local var_4_2 = iter_4_1.metaSkillID
		local var_4_3 = var_4_1.getName()
		local var_4_4 = setColorStr(var_4_3, COLOR_GREEN)

		if iter_4_0 < #arg_4_1:
			var_4_0 = var_4_0 .. var_4_4 .. "、"
		else
			var_4_0 = var_4_0 .. var_4_4

	return var_4_0

return var_0_0
