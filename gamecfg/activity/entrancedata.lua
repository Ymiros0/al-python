﻿return {
	{
		banner = "summary",
		event = ActivityMediator.EVENT_GO_SCENE,
		data = {
			SCENE.SUMMARY
		},
		isShow = function()
			local var_1_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_SUMMARY)

			return var_1_0 and not var_1_0:isEnd()
		end
	},
	{
		banner = "build_pray",
		event = ActivityMediator.GO_PRAY_POOL,
		data = {},
		isShow = function()
			local var_2_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.ACTIVITY_PRAY_POOL)

			return var_2_0 and not var_2_0:isEnd()
		end
	},
	{
		banner = "build_bisimai",
		event = ActivityMediator.EVENT_GO_SCENE,
		data = {
			SCENE.GETBOAT,
			{
				projectName = BuildShipScene.PROJECTS.ACTIVITY
			}
		},
		isShow = function()
			local var_3_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.BUILD_BISMARCK_ID)

			return var_3_0 and not var_3_0:isEnd()
		end
	},
	{
		banner = "activity_boss",
		event = ActivityMediator.EVENT_GO_SCENE,
		data = {
			SCENE.ACT_BOSS_BATTLE,
			{
				showAni = true
			}
		},
		isShow = function()
			local var_4_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_BOSS_BATTLE_MARK_2)

			return var_4_0 and not var_4_0:isEnd()
		end,
		isTip = function()
			local var_5_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_BOSS_BATTLE_MARK_2)

			if not var_5_0 then
				return
			end

			local var_5_1 = false

			if var_5_0:checkBattleTimeInBossAct() then
				var_5_1 = var_5_0.data2 ~= 1
			else
				local var_5_2 = var_5_0:GetBindPtActID()
				local var_5_3 = getProxy(ActivityProxy):getActivityById(var_5_2)

				if var_5_3 then
					var_5_1 = ActivityBossPtData.New(var_5_3):CanGetAward()
				end
			end

			return var_5_1
		end
	},
	{
		banner = "ming_paint",
		event = ActivityMediator.EVENT_GO_SCENE,
		data = {
			SCENE.COLORING
		},
		isShow = function()
			local var_6_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_COLORING_ALPHA)

			return var_6_0 and not var_6_0:isEnd()
		end,
		isTip = function()
			return getProxy(ColoringProxy):CheckTodayTip()
		end
	},
	{
		banner = "limit_skin",
		event = ActivityMediator.EVENT_GO_SCENE,
		data = {
			SCENE.SKINSHOP,
			{
				mode = NewSkinShopScene.MODE_EXPERIENCE
			}
		},
		isShow = function()
			local var_8_0 = pg.activity_banner.get_id_list_by_type[GAMEUI_BANNER_12]

			return var_8_0 and #var_8_0 > 0 and _.any(var_8_0, function(arg_9_0)
				local var_9_0 = pg.activity_banner[arg_9_0].time

				return pg.TimeMgr.GetInstance():inTime(var_9_0)
			end)
		end,
		isTip = function()
			local var_10_0 = pg.gameset.skin_ticket.key_value
			local var_10_1 = getProxy(PlayerProxy):getRawData():getResource(var_10_0)

			if not var_10_1 or not (var_10_1 > 0) then
				return false
			end

			local var_10_2 = getProxy(ShipSkinProxy)
			local var_10_3 = var_10_2:GetAllSkins()

			return _.any(var_10_3, function(arg_11_0)
				return arg_11_0:getConfig("genre") == ShopArgs.SkinShopTimeLimit and not var_10_2:hasSkin(arg_11_0:getSkinId())
			end) and getProxy(SettingsProxy):ShouldTipTimeLimitSkinShop()
		end
	},
	{
		banner = "banai_shop",
		event = ActivityMediator.GO_SHOPS_LAYER,
		data = {
			{
				warp = NewShopsScene.TYPE_ACTIVITY,
				actId = ActivityConst.BISMARCK_PT_SHOP_ID
			}
		},
		isShow = function()
			local var_12_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.BISMARCK_PT_SHOP_ID)

			return var_12_0 and not var_12_0:isEnd()
		end
	},
	{
		banner = "bili_shop",
		event = ActivityMediator.GO_SHOPS_LAYER,
		data = {
			{
				warp = NewShopsScene.TYPE_ACTIVITY,
				actId = ActivityConst.BILIBILI_PT_SHOP_ID
			}
		},
		isShow = function()
			local var_13_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.BILIBILI_PT_SHOP_ID)

			return var_13_0 and not var_13_0:isEnd()
		end
	},
	{},
	{
		banner = "commom_build",
		event = ActivityMediator.EVENT_GO_SCENE,
		data = {
			SCENE.GETBOAT,
			{
				projectName = BuildShipScene.PROJECTS.ACTIVITY
			}
		},
		isShow = function()
			local var_14_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.FRANCE_RE_BUILD)

			return var_14_0 and not var_14_0:isEnd()
		end
	},
	{
		banner = "commom_pt_shop",
		event = ActivityMediator.GO_SHOPS_LAYER,
		data = {
			{
				warp = NewShopsScene.TYPE_ACTIVITY,
				actId = ActivityConst.FRANCE_RE_PT_SHOP
			}
		},
		isShow = function()
			local var_15_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.FRANCE_RE_PT_SHOP)

			return var_15_0 and not var_15_0:isEnd()
		end
	},
	{
		banner = "commom_skin_shop",
		event = ActivityMediator.EVENT_GO_SCENE,
		data = {
			SCENE.SKINSHOP
		},
		isShow = function()
			return pg.TimeMgr.GetInstance():inTime({
				{
					{
						2019,
						6,
						27
					},
					{
						0,
						0,
						0
					}
				},
				{
					{
						2019,
						7,
						10
					},
					{
						23,
						59,
						59
					}
				}
			})
		end
	},
	{
		banner = "summer_feast",
		event = ActivityMediator.EVENT_GO_SCENE,
		data = {
			SCENE.SUMMER_FEAST
		},
		isShow = function()
			local var_17_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.SUMMER_FEAST_ID)

			return var_17_0 and not var_17_0:isEnd()
		end
	},
	{
		banner = "event_square",
		event = ActivityMediator.EVENT_GO_SCENE,
		data = {
			SCENE.NEWYEAR_SQUARE
		},
		isShow = function()
			local var_18_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.NEWYEAR_ACTIVITY)

			return var_18_0 and not var_18_0:isEnd()
		end
	},
	{
		banner = "activity_redpacket",
		event = ActivityMediator.OPEN_RED_PACKET_LAYER,
		data = {},
		isShow = function()
			local var_19_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_RED_PACKETS)

			return var_19_0 and not var_19_0:isEnd()
		end,
		isTip = function()
			return RedPacketLayer.isShowRedPoint()
		end
	},
	{
		banner = "LanternFestival",
		event = ActivityMediator.GO_MINI_GAME,
		data = {
			MainLanternFestivalBtn.LANTERNFESTIVAL_MINIGAME_ID
		},
		isShow = function()
			local var_21_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.LANTERNFESTIVAL)

			return var_21_0 and not var_21_0:isEnd()
		end,
		isTip = function()
			local var_22_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.LANTERNFESTIVAL)

			if var_22_0 and not var_22_0:isEnd() then
				local var_22_1 = getProxy(MiniGameProxy):GetHubByHubId(var_22_0:getConfig("config_id"))

				return var_22_1.count > 0 and var_22_1.usedtime < 7
			end
		end
	},
	{
		banner = "encode_game",
		event = ActivityMediator.GO_DECODE_MINI_GAME,
		data = {
			11
		},
		isShow = function()
			local var_23_0 = getProxy(ActivityProxy):getActivitiesByType(ActivityConst.ACTIVITY_TYPE_MINIGAME)
			local var_23_1 = _.detect(var_23_0, function(arg_24_0)
				return arg_24_0:getConfig("config_id") == 7
			end)

			return var_23_1 and not var_23_1:isEnd()
		end,
		isTip = function()
			local var_25_0 = getProxy(ActivityProxy):getActivitiesByType(ActivityConst.ACTIVITY_TYPE_MINIGAME)
			local var_25_1 = _.detect(var_25_0, function(arg_26_0)
				return arg_26_0:getConfig("config_id") == 7
			end)

			if var_25_1 and not var_25_1:isEnd() then
				local var_25_2 = getProxy(MiniGameProxy):GetHubByHubId(var_25_1:getConfig("config_id"))

				return var_25_2 and var_25_2.id == 7 and var_25_2.count > 0
			end
		end
	},
	{
		banner = "air_fight",
		event = ActivityMediator.EVENT_GO_SCENE,
		data = {
			SCENE.AIRFORCE_DRAGONEMPERY
		},
		isShow = function()
			local var_27_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_AIRFIGHT_BATTLE)

			return var_27_0 and not var_27_0:isEnd()
		end,
		isTip = function()
			local var_28_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_AIRFIGHT_BATTLE)

			if var_28_0 and not var_28_0:isEnd() then
				local var_28_1 = 0
				local var_28_2 = var_28_0:getConfig("config_client")[1]

				for iter_28_0 = 1, var_28_2 do
					var_28_1 = var_28_1 + (var_28_0:getKVPList(1, iter_28_0) or 0)
				end

				local var_28_3 = pg.TimeMgr.GetInstance()
				local var_28_4 = var_28_3:DiffDay(var_28_0.data1, var_28_3:GetServerTime()) + 1

				return var_28_1 < math.min(var_28_4 * 2, var_28_2 * 3)
			end
		end
	},
	{
		banner = "doa_medal",
		event = ActivityMediator.EVENT_GO_SCENE,
		data = {
			SCENE.DOA2_MEDAL_COLLECTION_SCENE
		},
		isShow = function()
			local var_29_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.DOA_MEDAL_ACT_ID)

			return var_29_0 and not var_29_0:isEnd()
		end,
		isTip = function()
			local var_30_0 = getProxy(ActivityProxy):getActivityById(ActivityConst.DOA_MEDAL_ACT_ID)

			return Activity.IsActivityReady(var_30_0)
		end
	},
	{
		banner = "meta_entrance_970505",
		event = ActivityMediator.EVENT_GO_SCENE,
		data = {
			SCENE.METACHARACTER,
			{
				autoOpenShipConfigID = 9705051
			}
		},
		isShow = function()
			local var_31_0 = 970505
			local var_31_1 = getProxy(MetaCharacterProxy):getMetaProgressVOByID(var_31_0)

			return var_31_1 and var_31_1:isInAct()
		end,
		isTip = function()
			local var_32_0 = 970505
			local var_32_1 = getProxy(MetaCharacterProxy):getMetaProgressVOByID(var_32_0)

			if var_32_1:isPassType() then
				return false
			end

			if not var_32_1:isShow() then
				return false
			end

			local var_32_2 = false

			if var_32_1.metaPtData then
				var_32_2 = var_32_1.metaPtData:CanGetAward()
			end

			if var_32_2 == false then
				var_32_2 = getProxy(MetaCharacterProxy):getRedTag(var_32_0)
			end

			return var_32_2
		end
	},
	{
		banner = "activity_permanent",
		event = ActivityMediator.ACTIVITY_PERMANENT,
		data = {},
		isShow = function()
			return not LOCK_PERMANENT_ENTER
		end,
		isTip = function()
			return PlayerPrefs.GetString("permanent_time", "") ~= pg.gameset.permanent_mark.description
		end
	}
}
