local var_0_0 = class("MainGuideSequence")
local var_0_1 = {
	{
		id = "NG002",
		condition = function()
			local var_1_0 = getProxy(TaskProxy):getTaskById(10302)
			local var_1_1 = getProxy(FleetProxy):getFleetById(11)

			return var_1_0 and var_1_0:isFinish() and not var_1_0:isReceive() and var_1_1:isEmpty()
		end,
		args = function()
			return _.any(getProxy(BayProxy):getShips(), function(arg_3_0)
				return arg_3_0 and arg_3_0.configId == 308031
			end) and {} or {
				1
			}
		end
	},
	{
		id = "NG004",
		condition = function()
			local var_4_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_GUIDE_TASKS)
			local var_4_1 = var_4_0 and not var_4_0:isEnd()
			local var_4_2 = false

			if var_4_1 then
				local var_4_3 = var_4_0:getConfig("config_data")[1]
				local var_4_4 = getProxy(ChapterProxy):getChapterById(var_4_3)

				var_4_2 = var_4_4 and var_4_4:isClear()
			end

			return var_4_1 and var_4_2
		end,
		args = function()
			return {}
		end
	},
	{
		id = "NG005",
		condition = function()
			local var_6_0 = getProxy(PlayerProxy):getRawData().level

			return pg.SystemOpenMgr.GetInstance():isOpenSystem(var_6_0, "CommanderCatMediator")
		end,
		args = function()
			return {}
		end
	},
	{
		id = "NG0022",
		condition = function()
			local var_8_0 = getProxy(PlayerProxy):getRawData().level

			return pg.SystemOpenMgr.GetInstance():isOpenSystem(var_8_0, "EquipmentTransformTreeMediator")
		end,
		args = function()
			return {}
		end
	},
	{
		id = "NG0023",
		condition = function()
			return pg.NewStoryMgr.GetInstance():IsPlayed("WorldG192")
		end,
		args = function()
			return {}
		end
	},
	{
		id = "NG0030",
		condition = function()
			local var_12_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_ATELIER_LINK)

			if not tobool(var_12_0) then
				return false
			end

			local var_12_1 = getProxy(ChapterProxy)
			local var_12_2 = var_12_1:getChapterById(1690005)

			return var_12_2 and var_12_2:isClear() and var_12_1:getMapById(var_12_1:getLastMapForActivity())
		end,
		args = function()
			local var_13_0 = getProxy(ChapterProxy)
			local var_13_1 = var_13_0:getLastMapForActivity()

			return var_13_0:getMapById(var_13_1):getConfig("type") == Map.ACTIVITY_HARD and {
				1,
				3
			} or {
				1,
				2,
				3
			}
		end
	},
	{
		id = "NG0031",
		condition = function()
			return pg.NewStoryMgr.GetInstance():IsPlayed("NG0030")
		end,
		args = function()
			local var_15_0 = PlayerPrefs.GetInt("ryza_task_help_" .. getProxy(PlayerProxy):getRawData().id, 0) == 0

			warning(var_15_0)

			return var_15_0 and {
				1,
				2
			} or {
				1
			}
		end
	},
	{
		id = "NG0032_1",
		condition = function()
			return pg.NewStoryMgr.GetInstance():IsPlayed("NG0031")
		end,
		args = function()
			return PlayerPrefs.GetInt("first_enter_ryza_atelier_" .. getProxy(PlayerProxy):getRawData().id, 0) == 0 and {
				1,
				2
			} or {
				1
			}
		end,
		nextOne = function()
			local var_18_0 = getProxy(ActivityProxy):getActivityByType(ActivityConst.ACTIVITY_TYPE_TASK_RYZA)

			if var_18_0 and not var_18_0:isEnd() and table.contains(var_18_0.data1_list, 56205) then
				return "NG0032_2", {}
			else
				return nil
			end
		end
	},
	{
		id = "NG0037",
		condition = function()
			return NewServerCarnivalScene.isShow()
		end,
		args = function()
			return {}
		end
	},
	{
		id = "NG0038",
		condition = function()
			return getProxy(PlayerProxy):getRawData().level >= 30 and PLATFORM_CODE ~= PLATFORM_CHT
		end,
		args = function()
			return {}
		end
	},
	{
		id = "tb_20",
		condition = function()
			return not LOCK_EDUCATE_SYSTEM and getProxy(EducateProxy):IsUnlockSecretary()
		end,
		args = function()
			return {}
		end
	}
}

function var_0_0.Execute(arg_25_0, arg_25_1)
	if IsUnityEditor and not ENABLE_GUIDE then
		if arg_25_1 then
			arg_25_1()
		end

		return
	end

	local var_25_0 = _.detect(var_0_1, function(arg_26_0)
		local var_26_0 = arg_26_0.id
		local var_26_1 = arg_26_0.condition

		return not pg.NewStoryMgr.GetInstance():IsPlayed(var_26_0) and var_26_1()
	end)

	if not var_25_0 then
		arg_25_1()

		return
	end

	local var_25_1 = var_25_0.id
	local var_25_2 = var_25_0.args()

	if pg.SeriesGuideMgr.GetInstance():isRunning() then
		arg_25_1()

		return
	end

	if not pg.NewGuideMgr.GetInstance():CanPlay() then
		arg_25_1()

		return
	end

	pg.m02:sendNotification(GAME.STORY_UPDATE, {
		storyId = var_25_1
	})
	pg.NewGuideMgr.GetInstance():Play(var_25_1, var_25_2, function()
		if var_25_0.nextOne then
			local var_27_0, var_27_1 = var_25_0.nextOne()

			arg_25_0:PlayNextOne(var_27_0, var_27_1)
		end
	end, arg_25_1)
end

function var_0_0.PlayNextOne(arg_28_0, arg_28_1, arg_28_2)
	if not arg_28_1 then
		return
	end

	pg.NewGuideMgr.GetInstance():Play(arg_28_1, arg_28_2, function()
		return
	end)
	pg.m02:sendNotification(GAME.STORY_UPDATE, {
		storyId = arg_28_1
	})
end

return var_0_0
