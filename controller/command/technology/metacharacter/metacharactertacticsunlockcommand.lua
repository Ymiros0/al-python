﻿local var_0_0 = class("MetaCharacterTacticsUnlockCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.shipID
	local var_1_2 = var_1_0.skillID
	local var_1_3 = var_1_0.materialIndex
	local var_1_4 = var_1_0.materialInfo

	print("63311 unlock skill", tostring(var_1_1), tostring(var_1_2), tostring(var_1_3))
	pg.ConnectionMgr.GetInstance():Send(63311, {
		ship_id = var_1_1,
		skill_id = var_1_2,
		index = var_1_3
	}, 63312, function(arg_2_0)
		if arg_2_0.result == 0 then
			print("63312 unlock success")

			local var_2_0 = getProxy(BayProxy)
			local var_2_1 = var_2_0:getShipById(var_1_1)
			local var_2_2 = var_2_1:isAllMetaSkillLock()

			var_2_1:upSkillLevelForMeta(var_1_2)
			var_2_0:updateShip(var_2_1)
			arg_1_0:sendNotification(GAME.CONSUME_ITEM, Drop.New({
				type = DROP_TYPE_ITEM,
				id = var_1_4.id,
				count = var_1_4.count
			}))
			getProxy(MetaCharacterProxy):unlockMetaTacticsSkill(var_1_1, var_1_2, var_2_2)
			arg_1_0:sendNotification(GAME.TACTICS_META_UNLOCK_SKILL_DONE, {
				metaShipID = var_1_1,
				unlockSkillID = var_1_2
			})
		else
			pg.TipsMgr.GetInstance():ShowTips(errorTip("", arg_2_0.result))
		end
	end)
end

return var_0_0
