﻿local var_0_0 = class("LogoutCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()

	arg_1_0:sendNotification(GAME.WILL_LOGOUT)

	if PLATFORM ~= PLATFORM_WINDOWSEDITOR and PLATFORM_CHT == PLATFORM_CODE and var_1_0.code ~= SDK_EXIT_CODE then
		pg.SdkMgr.GetInstance():LogoutSDK()

		return
	end

	pg.TrackerMgr.GetInstance():Tracking(TRACKING_ROLE_LOGOUT)

	local var_1_1 = ys.Battle.BattleState.GetInstance()

	if var_1_1:GetState() ~= ys.Battle.BattleState.BATTLE_STATE_IDLE then
		warning("stop and clean battle.")
		var_1_1:Stop("kick")
	end

	arg_1_0:sendNotification(GAME.STOP_BATTLE_LOADING, {})
	pg.NewStoryMgr:GetInstance():Quit()

	if pg.MsgboxMgr.GetInstance()._go.activeSelf then
		pg.MsgboxMgr.GetInstance():hide()
	end

	getProxy(SettingsProxy):Reset()
	originalPrint("disconnect from server...-" .. tostring(var_1_0.code))
	pg.ConnectionMgr.GetInstance():Disconnect()

	BillboardMediator.time = nil
	Map.lastMap = nil
	Map.lastMapForActivity = nil
	BuildShipScene.projectName = nil
	DockyardScene.selectAsc = nil
	DockyardScene.sortIndex = nil
	DockyardScene.typeIndex = nil
	DockyardScene.campIndex = nil
	DockyardScene.rarityIndex = nil
	DockyardScene.extraIndex = nil
	DockyardScene.commonTag = nil
	LevelMediator2.prevRefreshBossTimeTime = nil
	ActivityMainScene.FetchReturnersTime = nil
	ActivityMainScene.Data2Time = nil

	pg.BrightnessMgr.GetInstance():ExitManualMode()
	pg.SeriesGuideMgr.GetInstance():dispose()
	pg.NewGuideMgr.GetInstance():Exit()
	PoolMgr.GetInstance():DestroyAllPrefab()
	pg.GuildMsgBoxMgr.GetInstance():Hide()

	local var_1_2 = getProxy(UserProxy)

	if var_1_2 then
		local var_1_3 = var_1_2:getRawData()

		if var_1_3 then
			var_1_3:clear()
		end

		var_1_2:SetLoginedFlag(false)
	end

	local function var_1_4()
		arg_1_0.facade:removeProxy(PlayerProxy.__cname)
		arg_1_0.facade:removeProxy(BayProxy.__cname)
		arg_1_0.facade:removeProxy(FleetProxy.__cname)
		arg_1_0.facade:removeProxy(EquipmentProxy.__cname)
		arg_1_0.facade:removeProxy(ChapterProxy.__cname)
		arg_1_0.facade:removeProxy(WorldProxy.__cname)
		arg_1_0.facade:removeProxy(BagProxy.__cname)
		arg_1_0.facade:removeProxy(TaskProxy.__cname)
		arg_1_0.facade:removeProxy(MailProxy.__cname)
		arg_1_0.facade:removeProxy(NavalAcademyProxy.__cname)
		arg_1_0.facade:removeProxy(DormProxy.__cname)
		arg_1_0.facade:removeProxy(ChatProxy.__cname)
		arg_1_0.facade:removeProxy(FriendProxy.__cname)
		arg_1_0.facade:removeProxy(NotificationProxy.__cname)
		arg_1_0.facade:removeProxy(BuildShipProxy.__cname)
		arg_1_0.facade:removeProxy(CollectionProxy.__cname)
		arg_1_0.facade:removeProxy(EventProxy.__cname)
		arg_1_0.facade:removeProxy(ActivityProxy.__cname)
		arg_1_0.facade:removeProxy(MilitaryExerciseProxy.__cname)
		arg_1_0.facade:removeProxy(ServerNoticeProxy.__cname)
		arg_1_0.facade:removeProxy(DailyLevelProxy.__cname)
		arg_1_0.facade:removeProxy(ShopsProxy.__cname)
		arg_1_0.facade:removeProxy(GuildProxy.__cname)
		arg_1_0.facade:removeProxy(VoteProxy.__cname)
		arg_1_0.facade:removeProxy(ChallengeProxy.__cname)
		arg_1_0.facade:removeProxy(ColoringProxy.__cname)
		arg_1_0.facade:removeProxy(AnswerProxy.__cname)
		arg_1_0.facade:removeProxy(TechnologyProxy.__cname)
		arg_1_0.facade:removeProxy(BillboardProxy.__cname)
		arg_1_0.facade:removeProxy(TechnologyNationProxy.__cname)
		arg_1_0.facade:removeProxy(AttireProxy.__cname)
		arg_1_0.facade:removeProxy(ShipSkinProxy.__cname)
		arg_1_0.facade:removeProxy(PrayProxy.__cname)
		arg_1_0.facade:removeProxy(SecondaryPWDProxy.__cname)
		arg_1_0.facade:removeProxy(SkirmishProxy.__cname)
		arg_1_0.facade:removeProxy(InstagramProxy.__cname)
		arg_1_0.facade:removeProxy(MiniGameProxy.__cname)
		arg_1_0.facade:removeProxy(EmojiProxy.__cname)
		arg_1_0.facade:removeProxy(AppreciateProxy.__cname)
		arg_1_0.facade:removeProxy(MetaCharacterProxy.__cname)
		arg_1_0.facade:removeProxy(AvatarFrameProxy.__cname)
		arg_1_0.facade:removeProxy(RefluxProxy.__cname)
		arg_1_0.facade:removeProxy(IslandProxy.__cname)
		arg_1_0.facade:removeProxy(ActivityTaskProxy.__cname)
		arg_1_0.facade:removeProxy(FeastProxy.__cname)
		arg_1_0.facade:removeProxy(EducateProxy.__cname)
		arg_1_0.facade:removeProxy(ApartmentProxy.__cname)
		arg_1_0.facade:removeCommand(GAME.LOAD_SCENE_DONE)
	end

	arg_1_0:sendNotification(GAME.LOAD_SCENE, {
		context = Context.New({
			cleanStack = true,
			scene = SCENE.LOGIN,
			mediator = LoginMediator,
			viewComponent = LoginScene,
			data = var_1_0
		}),
		callback = var_1_4
	})

	if var_1_0.code ~= SDK_EXIT_CODE then
		pg.SdkMgr.GetInstance():LogoutSDK(var_1_0.code)
	end
end

return var_0_0
