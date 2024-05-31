local var_0_0 = class("LoadPlayerDataCommand", pm.SimpleCommand)

function var_0_0.execute(arg_1_0, arg_1_1)
	local var_1_0 = arg_1_1:getBody()
	local var_1_1 = var_1_0.isNewPlayer
	local var_1_2 = var_1_0.id

	originalPrint("loading player data: " .. var_1_2)
	arg_1_0.facade:registerProxy(PlayerProxy.New())
	arg_1_0.facade:registerProxy(BayProxy.New({}))
	arg_1_0.facade:registerProxy(FleetProxy.New({}))
	arg_1_0.facade:registerProxy(EquipmentProxy.New({}))
	arg_1_0.facade:registerProxy(ChapterProxy.New({}))
	arg_1_0.facade:registerProxy(WorldProxy.New({}))
	arg_1_0.facade:registerProxy(BagProxy.New({}))
	arg_1_0.facade:registerProxy(TaskProxy.New({}))
	arg_1_0.facade:registerProxy(MailProxy.New({}))
	arg_1_0.facade:registerProxy(NavalAcademyProxy.New({}))
	arg_1_0.facade:registerProxy(DormProxy.New({}))
	arg_1_0.facade:registerProxy(ChatProxy.New({}))
	arg_1_0.facade:registerProxy(FriendProxy.New({}))
	arg_1_0.facade:registerProxy(NotificationProxy.New({}))
	arg_1_0.facade:registerProxy(BuildShipProxy.New({}))
	arg_1_0.facade:registerProxy(CollectionProxy.New({}))
	arg_1_0.facade:registerProxy(EventProxy.New({}))
	arg_1_0.facade:registerProxy(ActivityProxy.New({}))
	arg_1_0.facade:registerProxy(ActivityPermanentProxy.New({}))
	arg_1_0.facade:registerProxy(MilitaryExerciseProxy.New({}))
	arg_1_0.facade:registerProxy(ServerNoticeProxy.New())
	arg_1_0.facade:registerProxy(DailyLevelProxy.New())
	arg_1_0.facade:registerProxy(ShopsProxy.New())
	arg_1_0.facade:registerProxy(GuildProxy.New())
	arg_1_0.facade:registerProxy(VoteProxy.New())
	arg_1_0.facade:registerProxy(ChallengeProxy.New())
	arg_1_0.facade:registerProxy(CommanderProxy.New())
	arg_1_0.facade:registerProxy(ColoringProxy.New())
	arg_1_0.facade:registerProxy(AnswerProxy.New())
	arg_1_0.facade:registerProxy(TechnologyProxy.New())
	arg_1_0.facade:registerProxy(BillboardProxy.New())
	arg_1_0.facade:registerProxy(MetaCharacterProxy.New())
	arg_1_0.facade:registerProxy(TechnologyNationProxy.New())
	arg_1_0.facade:registerProxy(AttireProxy.New())
	arg_1_0.facade:registerProxy(ShipSkinProxy.New())
	arg_1_0.facade:registerProxy(SecondaryPWDProxy.New({}))
	arg_1_0.facade:registerProxy(SkirmishProxy.New())
	arg_1_0.facade:registerProxy(PrayProxy.New())
	arg_1_0.facade:registerProxy(EmojiProxy.New())
	arg_1_0.facade:registerProxy(MiniGameProxy.New())
	arg_1_0.facade:registerProxy(InstagramProxy.New())
	arg_1_0.facade:registerProxy(AppreciateProxy.New())
	arg_1_0.facade:registerProxy(AvatarFrameProxy.New())
	arg_1_0.facade:registerProxy(ActivityTaskProxy.New())
	arg_1_0.facade:registerProxy(RefluxProxy.New())
	arg_1_0.facade:registerProxy(IslandProxy.New())
	arg_1_0.facade:registerProxy(LimitChallengeProxy.New())
	arg_1_0.facade:registerProxy(GameRoomProxy.New())
	arg_1_0.facade:registerProxy(FeastProxy.New())

	if not LOCK_EDUCATE_SYSTEM then
		arg_1_0.facade:registerProxy(EducateProxy.New())
	end

	arg_1_0.facade:registerProxy(ApartmentProxy.New())
	pg.ConnectionMgr.GetInstance():setPacketIdx(1)
	pg.ConnectionMgr.GetInstance():Send(11001, {
		timestamp = 0
	}, 11002, function(arg_2_0)
		originalPrint("player loaded: " .. arg_2_0.timestamp)
		pg.TimeMgr.GetInstance():SetServerTime(arg_2_0.timestamp, arg_2_0.monday_0oclock_timestamp)

		local var_2_0 = getProxy(PlayerProxy):getRawData()
		local var_2_1, var_2_2 = getProxy(ActivityProxy):isSurveyOpen()

		if var_2_1 then
			arg_1_0:sendNotification(GAME.GET_SURVEY_STATE, {
				surveyID = var_2_2
			})
		end

		if var_1_1 then
			pg.PushNotificationMgr.GetInstance():Reset()
			pg.SdkMgr.GetInstance():CreateRole(var_2_0.id, var_2_0.name, var_2_0.level, var_2_0.registerTime, var_2_0:getTotalGem())
		end

		pg.SeriesGuideMgr.GetInstance():setPlayer(var_2_0)
		WorldGuider.GetInstance():Init()

		local var_2_3 = getProxy(UserProxy):getData()
		local var_2_4 = getProxy(ServerProxy)
		local var_2_5 = var_2_4:getLastServer(var_2_3.uid)

		pg.SdkMgr.GetInstance():EnterServer(tostring(var_2_5.id), var_2_5.name, var_2_0.id, var_2_0.name, var_2_0.registerTime, var_2_0.level, var_2_0:getTotalGem())
		var_2_4:recordLoginedServer(var_2_3.uid, var_2_5.id)
		getProxy(MetaCharacterProxy):requestMetaTacticsInfo(nil, true)
		arg_1_0:sendNotification(GAME.REQUEST_META_PT_DATA, {
			isAll = true
		})
		arg_1_0:sendNotification(GAME.GET_SEASON_INFO)
		arg_1_0:sendNotification(GAME.GET_GUILD_INFO)
		arg_1_0:sendNotification(GAME.GET_PUBLIC_GUILD_USER_DATA, {})
		arg_1_0:sendNotification(GAME.REQUEST_MINI_GAME, {
			type = MiniGameRequestCommand.REQUEST_HUB_DATA
		})
		LimitChallengeConst.RequestInfo()

		if not LOCK_EDUCATE_SYSTEM then
			arg_1_0:sendNotification(GAME.EDUCATE_REQUEST)
		end

		pg.SdkMgr.GetInstance():BindCPU()
		pg.SecondaryPWDMgr.GetInstance():FetchData()
		MonthCardOutDateTipPanel.SetMonthCardEndDateLocal()
		pg.NewStoryMgr.GetInstance():Fix()
		getProxy(SettingsProxy):ResetTimeLimitSkinShopTip()
		getProxy(SettingsProxy):ResetContinuousOperationAutoSub()
		getProxy(PlayerProxy):setInited(true)

		if MainCheckShipNumSequence.New():Check(arg_2_0.ship_count) then
			arg_1_0:sendNotification(GAME.LOAD_PLAYER_DATA_DONE)
		end
	end, nil, 60)
end

return var_0_0
