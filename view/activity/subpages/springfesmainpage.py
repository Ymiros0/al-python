local var_0_0 = class("SpringFesMainPage", import("...base.BaseActivityPage"))

def var_0_0.OnInit(arg_1_0):
	arg_1_0.bg = arg_1_0.findTF("AD")
	arg_1_0.go1 = arg_1_0.findTF("1", arg_1_0.bg)
	arg_1_0.go2 = arg_1_0.findTF("2", arg_1_0.bg)
	arg_1_0.go3 = arg_1_0.findTF("3", arg_1_0.bg)
	arg_1_0.go4 = arg_1_0.findTF("4", arg_1_0.bg)

def var_0_0.OnFirstFlush(arg_2_0):
	onButton(arg_2_0, arg_2_0.go1, function()
		arg_2_0.emit(ActivityMediator.SELECT_ACTIVITY, 470))
	onButton(arg_2_0, arg_2_0.go2, function()
		arg_2_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.COLORING))
	onButton(arg_2_0, arg_2_0.go3, function()
		arg_2_0.emit(ActivityMediator.EVENT_GO_SCENE, SCENE.CHARGE, {
			wrap = 4
		}))
	onButton(arg_2_0, arg_2_0.go4, function()
		arg_2_0.emit(ActivityMediator.SELECT_ACTIVITY, 473))

return var_0_0
