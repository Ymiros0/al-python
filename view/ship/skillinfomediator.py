local var_0_0 = class("SkillInfoMediator", import("..base.ContextMediator"))

var_0_0.WARP_TO_TACTIC = "SkillInfoMediator.WARP_TO_TACTIC"
var_0_0.WARP_TO_META_TACTICS = "SkillInfoMediator.WARP_TO_METATASK"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.WARP_TO_TACTIC, function(arg_2_0)
		local var_2_0 = getProxy(NavalAcademyProxy)
		local var_2_1 = var_2_0.getStudents()
		local var_2_2 = 0
		local var_2_3 = 0
		local var_2_4 = var_2_0.MAX_SKILL_CLASS_NUM

		for iter_2_0 = 1, var_2_4:
			if var_2_1[iter_2_0]:
				var_2_2 = var_2_2 + 1
			else
				var_2_3 = iter_2_0

				break

		if var_2_2 >= var_2_0.getSkillClassNum():
			pg.TipsMgr.GetInstance().ShowTips(i18n("tactics_lesson_full"))
			arg_1_0.viewComponent.close()

			return

		local var_2_5 = getProxy(BagProxy).getItemsByType(Item.LESSON_TYPE)

		if table.getCount(var_2_5 or {}) <= 0:
			pg.TipsMgr.GetInstance().ShowTips(i18n("tactics_no_lesson"))
			arg_1_0.viewComponent.close()

			return

		for iter_2_1, iter_2_2 in pairs(var_2_1):
			if iter_2_2.shipId == arg_1_0.contextData.shipId:
				pg.TipsMgr.GetInstance().ShowTips(i18n("tactics_lesson_repeated"))
				arg_1_0.viewComponent.close()

				return

		arg_1_0.viewComponent.close()
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.NAVALACADEMYSCENE, {
			warp = NavalAcademyScene.WARP_TO_TACTIC,
			shipToLesson = {
				shipId = arg_1_0.contextData.shipId,
				skillIndex = arg_1_0.contextData.index,
				index = var_2_3
			}
		}))
	arg_1_0.bind(var_0_0.WARP_TO_META_TACTICS, function(arg_3_0, arg_3_1)
		arg_1_0.viewComponent.close()
		arg_1_0.sendNotification(GAME.GO_SCENE, SCENE.METACHARACTER, {
			autoOpenTactics = True,
			autoOpenShipConfigID = arg_3_1
		}))

def var_0_0.listNotificationInterests(arg_4_0):
	return {}

def var_0_0.handleNotification(arg_5_0, arg_5_1):
	local var_5_0 = arg_5_1.getName()
	local var_5_1 = arg_5_1.getBody()

return var_0_0
