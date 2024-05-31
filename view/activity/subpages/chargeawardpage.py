local var_0_0 = class("ChargeAwardPage", import("...base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("bg")
	arg_1_0.charge = arg_1_0.findTF("charge")
	arg_1_0.take = arg_1_0.findTF("take")
	arg_1_0.finish = arg_1_0.findTF("finish")

def var_0_0.OnDataSetting(arg_2_0):
	return

def var_0_0.OnFirstFlush(arg_3_0):
	onButton(arg_3_0, arg_3_0.charge, function()
		arg_3_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.CHARGE, {
			wrap = ChargeScene.TYPE_DIAMOND
		}))
	onButton(arg_3_0, arg_3_0.take, function()
		arg_3_0.emit(ActivityMediator.EVENT_OPERATION, {
			cmd = 1,
			activity_id = arg_3_0.activity.id
		}))

def var_0_0.OnUpdateFlush(arg_6_0):
	setActive(arg_6_0.charge, arg_6_0.activity.data2 == 0 and arg_6_0.activity.data1 == 0)
	setButtonEnabled(arg_6_0.take, arg_6_0.activity.data2 == 0)
	setActive(arg_6_0.take, arg_6_0.activity.data1 > 0)
	setActive(arg_6_0.finish, arg_6_0.activity.data2 == 1)

def var_0_0.OnDestroy(arg_7_0):
	clearImageSprite(arg_7_0.bg)

return var_0_0
