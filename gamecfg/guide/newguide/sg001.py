return {
	{
		index = 1,
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S001",
				12003
			}
		}
	},
	{
		index = 2,_segment = "S003",
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S002",
				12009
			},
			{
				"S002_1",
				12026
			}
		},
		def getSegment:()
			return getProxy(BuildShipProxy).getFinishCount() > 0 and 2 or 1
	},
	{
		index = 3,
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S004",
				12103
			}
		}
	},
	{
		index = 4,
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S005",
				13102
			}
		}
	},
	{
		index = 5,
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S006",
				13104
			}
		}
	},
	{
		index = 6,
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S007",
				13104
			}
		}
	},
	{
		index = 7,
		interrupt = True,
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S008",
				40002
			}
		}
	},
	{
		index = 8,
		view = {
			"NewMainScene",
			"LevelScene"
		},
		condition = {
			arg = {
				1,
				40004
			},
			def func:(arg_2_0, arg_2_1)
				if arg_2_0 == "NewMainScene":
					return pg.SeriesGuideMgr.CODES.MAINUI, 7
				elif arg_2_0 == "LevelScene":
					if not arg_2_1:
						return pg.SeriesGuideMgr.CODES.CONDITION, 7
					elif arg_2_1:
						if arg_2_1.score > 1:
							return pg.SeriesGuideMgr.CODES.CONDITION, 9
						elif arg_2_1.total_time >= 180:
							return pg.SeriesGuideMgr.CODES.CONDITION, 7
						else
							return pg.SeriesGuideMgr.CODES.CONDITION, 4
		}
	},
	{
		index = 9,_segment = "S010",
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S009",
				13104
			}
		}
	},
	{
		index = 10,_segment = "S012",
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S011",
				20006
			}
		}
	},
	{
		index = 11,_segment = "S014",
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S013",
				15003
			}
		}
	},
	{
		index = 12,_segment = "S016",
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S015",
				14007
			}
		}
	},
	{
		index = 13,_segment = "S012",
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S011",
				20006
			}
		}
	},
	{
		index = 14,
		view = {
			"NewMainScene"
		},
		condition = {
			arg = {
				2
			},
			def func:(arg_3_0)
				if arg_3_0.getEquip(2):
					return pg.SeriesGuideMgr.CODES.MAINUI, 15

				return pg.SeriesGuideMgr.CODES.MAINUI, 14
		},
		segment = {
			{
				"S017",
				12007
			}
		}
	},
	{
		index = 15,_segment = "S019",
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S018",
				14003
			}
		}
	},
	{
		index = 16,_segment = "S012",
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S011",
				20006
			}
		}
	},
	{
		index = 17,
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S020",
				12003
			},
			{
				"S020_1",
				12003
			}
		},
		def getSegment:()
			local var_4_0 = getProxy(ActivityProxy).getActivityByType(ActivityConst.ACTIVITY_TYPE_BUILDSHIP_1)
			local var_4_1 = var_4_0 and not var_4_0.isEnd()

			if not BuildShipScene.projectName:
				if var_4_1:
					return 1
				else
					return 2
			else
				return BuildShipScene.projectName == BuildShipScene.PROJECTS.HEAVY and 2 or 1
	},
	{
		index = 18,_segment = "S003",
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S002",
				12009
			},
			{
				"S002_1",
				12026
			}
		},
		def getSegment:()
			return getProxy(BuildShipProxy).getFinishCount() > 0 and 2 or 1
	},
	{
		index = 19,
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S021",
				12103
			}
		}
	},
	{
		index = 20,
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S022",
				13102
			}
		}
	},
	{
		index = 21,
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S023",
				13104
			}
		}
	},
	{
		index = 22,
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S024",
				13104
			}
		}
	},
	{
		index = 23,
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S025",
				13104
			}
		}
	},
	{
		index = 24,
		interrupt = True,
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S026",
				40002
			}
		}
	},
	{
		index = 25,
		view = {
			"NewMainScene",
			"LevelScene"
		},
		condition = {
			arg = {
				1,
				40004
			},
			def func:(arg_6_0, arg_6_1)
				if arg_6_0 == "NewMainScene":
					return pg.SeriesGuideMgr.CODES.MAINUI, 24
				elif arg_6_0 == "LevelScene":
					if not arg_6_1:
						return pg.SeriesGuideMgr.CODES.CONDITION, 24
					elif arg_6_1:
						if arg_6_1.score > 1:
							return pg.SeriesGuideMgr.CODES.CONDITION, 26
						elif arg_6_1.total_time >= 180:
							return pg.SeriesGuideMgr.CODES.CONDITION, 24
						else
							return pg.SeriesGuideMgr.CODES.CONDITION, 20
		}
	},
	{
		index = 26,
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S027",
				13104
			}
		}
	},
	{
		index = 27,
		interrupt = True,
		view = {
			"NewMainScene"
		},
		segment = {
			{
				"S028",
				40002
			}
		}
	},
	{
		index = 28,_segment = "S029",
		view = {
			"NewMainScene",
			"LevelScene"
		},
		condition = {
			arg = {
				1,
				40004
			},
			def func:(arg_7_0, arg_7_1)
				if arg_7_0 == "NewMainScene":
					return pg.SeriesGuideMgr.CODES.MAINUI, 27
				elif arg_7_0 == "LevelScene":
					if not arg_7_1:
						return pg.SeriesGuideMgr.CODES.CONDITION, 27
					elif arg_7_1:
						if arg_7_1.score > 1:
							return pg.SeriesGuideMgr.CODES.CONDITION, 29
						elif arg_7_1.total_time >= 180:
							return pg.SeriesGuideMgr.CODES.CONDITION, 27
						else
							return pg.SeriesGuideMgr.CODES.CONDITION, 20
		}
	}
}
