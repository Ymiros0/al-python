local var_0_0 = class("SnapshotSelectCharMediator", import("..base.ContextMediator"))

var_0_0.SELECT_CHAR = "SnapshotSelectCharMediator.SELECT_CHAR"

function var_0_0.register(arg_1_0)
	local var_1_0 = getProxy(CollectionProxy)

	arg_1_0.viewComponent:setShipGroups(var_1_0:getGroups())

	local var_1_1 = getProxy(BayProxy)

	arg_1_0.viewComponent:setProposeList(var_1_1:getProposeGroupList())
	arg_1_0:bind(SnapshotSelectCharLayer.ON_INDEX, function(arg_2_0, arg_2_1)
		arg_1_0:addSubLayers(Context.New({
			viewComponent = CustomIndexLayer,
			mediator = CustomIndexMediator,
			data = arg_2_1
		}))
	end)
	arg_1_0:bind(SnapshotSelectCharLayer.SELECT_CHAR, function(arg_3_0, arg_3_1)
		arg_1_0:sendNotification(var_0_0.SELECT_CHAR, arg_3_1)
	end)
end

return var_0_0
