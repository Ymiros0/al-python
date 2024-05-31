local var_0_0 = class("MainServerNoticeSequence", import(".MainSublayerSequence"))

def var_0_0.Execute(arg_1_0, arg_1_1):
	local var_1_0 = getProxy(ServerNoticeProxy)

	if #var_1_0.getServerNotices(False) > 0 and var_1_0.needAutoOpen():
		arg_1_0.AddSubLayers(Context.New({
			mediator = NewBulletinBoardMediator,
			viewComponent = NewBulletinBoardLayer,
			onRemoved = arg_1_1
		}))
	else
		arg_1_1()

return var_0_0
