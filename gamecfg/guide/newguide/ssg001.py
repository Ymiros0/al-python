return {
	LevelScene = {
		{
			id = "NG002",
			def condition:()
				local var_1_0 = getProxy(TaskProxy).getTaskById(10302)
				local var_1_1 = getProxy(FleetProxy).getFleetById(11)

				return var_1_0 and var_1_0.isFinish() and not var_1_0.isReceive() and var_1_1.isEmpty(),
			def args:(arg_2_0)
				if getProxy(ChapterProxy).getActiveChapter():
					arg_2_0.switchToMap()

				return _.any(getProxy(BayProxy).getShips(), function(arg_3_0)
					return arg_3_0 and arg_3_0.configId == 308031) and {
					2
				} or {
					2,
					1
				}
		},
		{
			id = "NG0030",
			def condition:()
				local var_4_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_ATELIER_LINK)

				if not tobool(var_4_0):
					return False

				local var_4_1 = getProxy(ChapterProxy)
				local var_4_2 = var_4_1.getChapterById(1690005)

				return var_4_2 and var_4_2.isClear() and var_4_1.getMapById(var_4_1.getLastMapForActivity()),
			def args:()
				local var_5_0 = getProxy(ChapterProxy)
				local var_5_1 = var_5_0.getLastMapForActivity()

				return var_5_0.getMapById(var_5_1).getConfig("type") == Map.ACTIVITY_HARD and {
					3
				} or {
					2,
					3
				}
		}
	},
	ChallengeMainScene = {
		{
			id = "NG0014",
			def condition:()
				return True,
			def args:()
				return {}
		}
	},
	InstagramLayer = {
		{
			id = "NG0018",
			def condition:()
				return True,
			def args:()
				return {}
		}
	},
	DockyardScene = {
		{
			id = "NG0019",
			def condition:(arg_10_0)
				return arg_10_0.contextData.mode == DockyardScene.MODE_DESTROY,
			def args:()
				return {}
		}
	},
	GameHallScene = {
		{
			id = "NG0039",
			def condition:(arg_12_0)
				return PLATFORM_CODE != PLATFORM_CHT,
			def args:()
				return {}
		},
		{
			id = "NG0040",
			def condition:(arg_14_0)
				return PLATFORM_CODE != PLATFORM_CHT,
			def args:()
				return {}
		}
	}
}
