﻿local var_0_0 = class("CollectionMediator", import("..base.ContextMediator"))

var_0_0.EVENT_OBTAIN_SKIP = "CollectionMediator:EVENT_OBTAIN_SKIP"
var_0_0.EVENT_OPEN_FULL_SCREEN_PIC_VIEW = "CollectionMediator:EVENT_OPEN_FULL_SCREEN_PIC_VIEW"

function var_0_0.register(arg_1_0)
	arg_1_0.collectionProxy = getProxy(CollectionProxy)

	arg_1_0.viewComponent:setShipGroups(arg_1_0.collectionProxy:getGroups())
	arg_1_0.viewComponent:setAwards(arg_1_0.collectionProxy:getAwards())
	arg_1_0.viewComponent:setCollectionRate(arg_1_0.collectionProxy:getCollectionRate())
	arg_1_0.viewComponent:setLinkCollectionCount(arg_1_0.collectionProxy:getLinkCollectionCount())

	local var_1_0 = getProxy(PlayerProxy)

	arg_1_0.viewComponent:setPlayer(var_1_0:getRawData())

	local var_1_1 = getProxy(BayProxy)

	arg_1_0.viewComponent:setProposeList(var_1_1:getProposeGroupList())
	arg_1_0:bind(CollectionScene.GET_AWARD, function(arg_2_0, arg_2_1, arg_2_2)
		arg_1_0:sendNotification(GAME.COLLECT_GET_AWARD, {
			id = arg_2_1,
			index = arg_2_2
		})
	end)
	arg_1_0:bind(CollectionScene.SHOW_DETAIL, function(arg_3_0, arg_3_1, arg_3_2)
		arg_1_0:sendNotification(GAME.GO_SCENE, SCENE.SHIP_PROFILE, {
			showTrans = arg_3_1,
			groupId = arg_3_2
		})
	end)
	arg_1_0:bind(CollectionScene.ACTIVITY_OP, function(arg_4_0, arg_4_1)
		arg_1_0:sendNotification(GAME.ACTIVITY_OPERATION, arg_4_1)
	end)
	arg_1_0:bind(CollectionScene.BEGIN_STAGE, function(arg_5_0, arg_5_1)
		arg_1_0:sendNotification(GAME.BEGIN_STAGE, arg_5_1)
	end)
	arg_1_0:bind(CollectionScene.ON_INDEX, function(arg_6_0, arg_6_1)
		arg_1_0:addSubLayers(Context.New({
			viewComponent = CustomIndexLayer,
			mediator = CustomIndexMediator,
			data = arg_6_1
		}))
	end)
	arg_1_0:bind(var_0_0.EVENT_OPEN_FULL_SCREEN_PIC_VIEW, function(arg_7_0, arg_7_1)
		arg_1_0:addSubLayers(Context.New({
			mediator = GalleryFullScreenMediator,
			viewComponent = GalleryFullScreenLayer,
			data = {
				picID = arg_7_1
			}
		}))
	end)
	arg_1_0.viewComponent:updateCollectNotices(arg_1_0.collectionProxy:hasFinish())
end

function var_0_0.listNotificationInterests(arg_8_0)
	return {
		CollectionProxy.AWARDS_UPDATE,
		GAME.COLLECT_GET_AWARD_DONE,
		PlayerProxy.UPDATED,
		GAME.BEGIN_STAGE_DONE,
		var_0_0.EVENT_OBTAIN_SKIP
	}
end

function var_0_0.handleNotification(arg_9_0, arg_9_1)
	local var_9_0 = arg_9_1:getName()
	local var_9_1 = arg_9_1:getBody()

	if var_9_0 == CollectionProxy.AWARDS_UPDATE then
		arg_9_0.viewComponent:setAwards(var_9_1)
	elseif var_9_0 == GAME.COLLECT_GET_AWARD_DONE then
		arg_9_0.viewComponent:sortDisplay()
		arg_9_0.viewComponent:updateCollectNotices(arg_9_0.collectionProxy:hasFinish())
		arg_9_0.viewComponent:emit(BaseUI.ON_ACHIEVE, var_9_1.items)
	elseif var_9_0 == PlayerProxy.UPDATED then
		arg_9_0.viewComponent:setPlayer(var_9_1)
	elseif var_9_0 == GAME.BEGIN_STAGE_DONE then
		arg_9_0:sendNotification(GAME.GO_SCENE, SCENE.COMBATLOAD, var_9_1)
	elseif var_9_0 == var_0_0.EVENT_OBTAIN_SKIP then
		arg_9_0.viewComponent:skipIn(var_9_1.toggle, var_9_1.displayGroupId)
	end
end

return var_0_0
