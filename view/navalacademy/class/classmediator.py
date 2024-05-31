local var_0_0 = class("ClassMediator", import("...base.ContextMediator"))

var_0_0.UPGRADE_FIELD = "ClassMediator.UPGRADE_FIELD"

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.UPGRADE_FIELD, function(arg_2_0, arg_2_1)
		arg_1_0.sendNotification(GAME.SHOPPING, {
			count = 1,
			id = arg_2_1
		}))

	local var_1_0 = getProxy(NavalAcademyProxy).getCourse()

	arg_1_0.viewComponent.SetCourse(var_1_0)

	local var_1_1 = getProxy(CollectionProxy).getGroups()

	arg_1_0.viewComponent.SetStudents(var_1_1)

	local var_1_2 = getProxy(NavalAcademyProxy).GetClassVO()

	arg_1_0.viewComponent.SetClass(var_1_2)

def var_0_0.listNotificationInterests(arg_3_0):
	return {
		NavalAcademyProxy.RESOURCE_UPGRADE_DONE,
		NavalAcademyProxy.RESOURCE_UPGRADE,
		NavalAcademyProxy.COURSE_UPDATED
	}

def var_0_0.handleNotification(arg_4_0, arg_4_1):
	local var_4_0 = arg_4_1.getName()
	local var_4_1 = arg_4_1.getBody()

	if var_4_0 == NavalAcademyProxy.RESOURCE_UPGRADE_DONE:
		local var_4_2 = var_4_1.field

		if isa(var_4_2, ClassResourceField):
			pg.TipsMgr.GetInstance().ShowTips(i18n("main_navalAcademyScene_class_upgrade_complete", pg.navalacademy_data_template[1].name, var_4_1.value, var_4_1.rate, var_4_1.exp))

		arg_4_0.viewComponent.OnUpdateResField(var_4_2)
	elif var_4_0 == NavalAcademyProxy.RESOURCE_UPGRADE:
		arg_4_0.viewComponent.OnUpdateResField(var_4_1.resVO)
	elif var_4_0 == NavalAcademyProxy.COURSE_UPDATED:
		local var_4_3 = getProxy(NavalAcademyProxy).getCourse()

		arg_4_0.viewComponent.SetCourse(var_4_3)
		arg_4_0.viewComponent.InitClassInfo()

return var_0_0
