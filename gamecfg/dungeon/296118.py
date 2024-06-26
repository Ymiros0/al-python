return {
	id = 296118,
	map_id = 10001,
	bgm = "story-6",
	stages = {
		{
			stageIndex = 1,
			failCondition = 1,
			timeCount = 80,
			passCondition = 1,
			backGroundStageID = 1,
			totalArea = {
				-70,
				20,
				90,
				70
			},
			playerArea = {
				-70,
				20,
				37,
				68
			},
			enemyArea = {},
			fleetCorrdinate = {
				-80,
				0,
				75
			},
			waves = {
				{
					triggerType = 1,
					waveIndex = 100,
					preWaves = {},
					triggerParams = {
						timeout = 0.5
					}
				},
				{
					triggerType = 1,
					waveIndex = 202,
					preWaves = {},
					triggerParams = {
						timeout = 7
					}
				},
				{
					triggerType = 1,
					key = True,
					waveIndex = 203,
					preWaves = {
						101
					},
					triggerParams = {
						timeout = 0.5
					}
				},
				{
					triggerType = 0,
					key = True,
					waveIndex = 101,
					conditionType = 1,
					preWaves = {
						100
					},
					triggerParam = {},
					spawn = {
						{
							score = 0,
							monsterTemplateID = 295118,
							delay = 0,
							moveCast = True,
							affix = True,
							corrdinate = {
								-5,
								0,
								55
							},
							buffList = {
								200041,
								200042
							},
							bossData = {
								hpBarNum = 100,
								icon = "shengwang_alter"
							},
							phase = {
								{
									switchParam = 1.5,
									switchTo = 1,
									index = 0,
									switchType = 1,
									setAI = 20006,
									addWeapon = {}
								},
								{
									switchParam = 4.4,
									switchTo = 2,
									index = 1,
									switchType = 1,
									setAI = 75019,
									addWeapon = {
										2970029
									},
									removeWeapon = {},
									addBuff = {
										200043
									}
								},
								{
									switchParam = 1.5,
									switchTo = 3,
									index = 2,
									switchType = 1,
									setAI = 70093,
									addWeapon = {
										2970034
									},
									removeWeapon = {
										2970029
									},
									removeBuff = {
										200043
									}
								},
								{
									index = 3,
									switchType = 1,
									switchTo = 4,
									switchParam = 8,
									addWeapon = {
										2970022,
										2970039
									},
									removeWeapon = {
										2970034
									},
									addBuff = {
										200036
									}
								},
								{
									switchType = 1,
									switchTo = 5,
									index = 4,
									switchParam = 14,
									setAI = 10001,
									addWeapon = {
										2970044,
										2970049
									},
									removeWeapon = {
										2970022,
										2970039
									}
								},
								{
									switchParam = 8,
									switchTo = 6,
									index = 5,
									switchType = 1,
									setAI = 70093,
									addWeapon = {
										2970022,
										2970039
									},
									removeWeapon = {
										2970044,
										2970049
									},
									addBuff = {
										200036
									}
								},
								{
									switchType = 1,
									switchTo = 7,
									index = 6,
									switchParam = 12,
									setAI = 10001,
									addWeapon = {
										2970054,
										2970059
									},
									removeWeapon = {
										2970022,
										2970039
									}
								},
								{
									switchParam = 200,
									switchTo = 1,
									index = 7,
									switchType = 1,
									setAI = 70093,
									addWeapon = {
										2970022,
										2970039
									},
									removeWeapon = {
										2970054,
										2970059
									},
									addBuff = {
										200036
									}
								},
								{
									index = 21,
									switchParam = 3,
									switchTo = 22,
									switchType = 1,
									addWeapon = {
										2970064
									},
									removeWeapon = {}
								},
								{
									index = 22,
									switchType = 1,
									switchTo = 23,
									switchParam = 3,
									addWeapon = {
										2970069
									},
									addBuff = {
										200051
									},
									removeWeapon = {}
								},
								{
									index = 23,
									switchParam = 3,
									switchTo = 24,
									switchType = 1,
									addWeapon = {
										2970079,
										2970094,
										2970099
									},
									removeWeapon = {
										2970069
									}
								},
								{
									index = 24,
									switchParam = 3,
									switchTo = 25,
									switchType = 1,
									addWeapon = {
										2970084
									},
									removeWeapon = {}
								},
								{
									index = 25,
									switchParam = 1,
									switchTo = 26,
									switchType = 1,
									addWeapon = {},
									removeWeapon = {
										2970089
									}
								},
								{
									index = 26,
									switchParam = 3,
									switchTo = 27,
									switchType = 1,
									addWeapon = {
										2970089
									},
									removeWeapon = {}
								},
								{
									index = 27,
									switchParam = 1,
									switchTo = 24,
									switchType = 1,
									addWeapon = {},
									removeWeapon = {
										2970084
									}
								},
								{
									index = 41,
									switchParam = 2,
									switchTo = 42,
									switchType = 1,
									addWeapon = {},
									removeWeapon = {}
								},
								{
									index = 42,
									switchParam = 10,
									switchTo = 43,
									switchType = 1,
									addWeapon = {
										2970104
									},
									removeWeapon = {}
								},
								{
									index = 43,
									switchType = 1,
									switchTo = 44,
									switchParam = 5,
									addWeapon = {
										2970109,
										2970114
									},
									removeWeapon = {
										2970104
									},
									addBuff = {
										8789
									}
								},
								{
									index = 44,
									switchParam = 4,
									switchTo = 45,
									switchType = 1,
									addWeapon = {
										2970119
									},
									removeWeapon = {}
								},
								{
									index = 45,
									switchParam = 1,
									switchTo = 46,
									switchType = 1,
									addWeapon = {},
									removeWeapon = {
										2970124
									}
								},
								{
									index = 46,
									switchParam = 4,
									switchTo = 47,
									switchType = 1,
									addWeapon = {
										2970124
									},
									removeWeapon = {}
								},
								{
									index = 47,
									switchParam = 1,
									switchTo = 44,
									switchType = 1,
									addWeapon = {},
									removeWeapon = {
										2970119
									}
								}
							}
						}
					}
				},
				{
					triggerType = 0,
					waveIndex = 2001,
					conditionType = 1,
					preWaves = {
						202
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 295973,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								0,
								0,
								35
							},
							buffList = {
								8001,
								8053
							}
						},
						{
							monsterTemplateID = 295973,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								0,
								0,
								85
							},
							buffList = {
								8001,
								8053
							}
						}
					}
				},
				{
					triggerType = 0,
					waveIndex = 2002,
					conditionType = 1,
					preWaves = {
						202
					},
					triggerParam = {},
					spawn = {},
					reinforcement = {
						{
							monsterTemplateID = 295973,
							moveCast = True,
							delay = 14,
							score = 0,
							corrdinate = {
								0,
								0,
								35
							},
							buffList = {
								8001,
								8053
							}
						},
						{
							monsterTemplateID = 295973,
							moveCast = True,
							delay = 14,
							score = 0,
							corrdinate = {
								0,
								0,
								85
							},
							buffList = {
								8001,
								8053
							}
						},
						reinforceDuration = 180
					}
				},
				{
					triggerType = 8,
					waveIndex = 900,
					preWaves = {
						203
					},
					triggerParams = {}
				}
			}
		}
	},
	fleet_prefab = {}
}
