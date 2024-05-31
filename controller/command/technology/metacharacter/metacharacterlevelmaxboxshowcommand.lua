﻿local var_0_0 = class("MetaCharacterLevelMaxBoxShowCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = getProxy(MetaCharacterProxy)

	if not var_1_1 then
		return
	end

	local var_1_2 = getProxy(ChapterProxy)
	local var_1_3 = var_1_2:getActiveChapter()
	local var_1_4

	if var_1_3 then
		var_1_4 = var_1_2:GetChapterAutoFlag(var_1_3.id) == 1
	end

	if var_1_4 then
		return
	end

	local var_1_5 = var_1_1:getMetaSkillLevelMaxInfoList()

	if var_1_5 and #var_1_5 > 0 then
		local var_1_6 = ""

		for iter_1_0, iter_1_1 in ipairs(var_1_5) do
			local var_1_7 = iter_1_1.metaShipVO
			local var_1_8 = iter_1_1.metaSkillID
			local var_1_9 = var_1_7:getName()
			local var_1_10 = setColorStr(var_1_9, COLOR_GREEN)

			if iter_1_0 < #var_1_5 then
				var_1_6 = var_1_6 .. var_1_10 .. "、"
			else
				var_1_6 = var_1_6 .. var_1_10
			end
		end

		pg.MsgboxMgr.GetInstance():ShowMsgBox({
			content = i18n("meta_skill_maxtip", var_1_6),
			onYes = function()
				pg.m02:sendNotification(GAME.GO_SCENE, SCENE.METACHARACTER, {
					autoOpenTactics = true,
					autoOpenShipConfigID = var_1_5[1].metaShipVO.configId
				})
			end,
			onClose = function()
				if var_1_0.closeFunc then
					var_1_0.closeFunc()
				end
			end,
			weight = LayerWeightConst.TOP_LAYER
		})
	end

	var_1_1:clearMetaSkillLevelMaxInfoList()
end

return var_0_0
