local var_0_0 = class("SixthAnniversaryJPHotSpringMediator", import("view.activity.BackHills.NewYearFestival.NewYearHotSpringMediator"))

def var_0_0.register(arg_1_0):
	arg_1_0.bind(var_0_0.UNLOCK_SLOT, function(arg_2_0, arg_2_1)
		local var_2_0, var_2_1 = arg_1_0.activity.GetUpgradeCost()

		MsgboxMediator.ShowMsgBox({
			type = MSGBOX_TYPE_NORMAL,
			content = i18n("jp6th_spring_tip1", var_2_1),
			contextSprites = {
				{
					name = "wenquanshoupai",
					path = "props/wenquanshoupai"
				}
			},
			def onYes:()
				if arg_1_0.activity.GetCoins() < var_2_1:
					pg.TipsMgr.GetInstance().ShowTips(i18n("jp6th_spring_tip2"))

					return

				arg_1_0.sendNotification(GAME.ACTIVITY_OPERATION, {
					activity_id = arg_2_1,
					cmd = SpringActivity.OPERATION_UNLOCK
				})
		}))
	arg_1_0.bind(var_0_0.OPEN_CHUANWU, function(arg_4_0, arg_4_1, arg_4_2)
		arg_1_0.OnSelShips(arg_4_1, arg_4_2))

	local var_1_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_HOTSPRING)

	arg_1_0.activity = var_1_0

	arg_1_0.viewComponent.SetActivity(var_1_0)
	arg_1_0.bind(var_0_0.OPEN_INFO, function()
		arg_1_0.addSubLayers(Context.New({
			mediator = NewYearHotSpringShipSelectMediator,
			viewComponent = NewYearHotSpringShipSelectLayer,
			data = {
				actId = var_1_0.id
			}
		})))

return var_0_0
