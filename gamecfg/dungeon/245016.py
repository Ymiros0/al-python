return {
	map_id = 10001,
	id = 245016,
	stages = {
		{
			stageIndex = 1,
			failCondition = 1,
			timeCount = 180,
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
			mainUnitPosition = {
				{
					Vector3(-105, 0, 58),
					Vector3(-105, 0, 78),
					Vector3(-105, 0, 38)
				},
				[-1] = {
					Vector3(15, 0, 58),
					Vector3(15, 0, 78),
					Vector3(15, 0, 38)
				}
			},
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
						timeout = 30
					}
				},
				{
					triggerType = 1,
					waveIndex = 203,
					preWaves = {},
					triggerParams = {
						timeout = 50
					}
				},
				{
					triggerType = 5,
					waveIndex = 204,
					preWaves = {
						102,
						101
					},
					triggerParams = {
						bgm = "battle-2"
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
							monsterTemplateID = 204210,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								10,
								0,
								75
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 204210,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								-15,
								0,
								75
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 242101,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								-5,
								0,
								45
							}
						},
						{
							monsterTemplateID = 242113,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								-5,
								0,
								65
							},
							buffList = {
								8050,
								8051
							}
						},
						{
							monsterTemplateID = 204210,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								-15,
								0,
								35
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 204210,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								10,
								0,
								35
							},
							buffList = {
								8001,
								8007
							}
						}
					},
					airFighter = {
						{
							interval = 10,
							onceNumber = 6,
							totalNumber = 6,
							formation = 10006,
							delay = 0,
							templateID = 2200814,
							score = 1,
							weaponID = {
								2020002
							},
							attr = {
								airPower = 125,
								maxHP = 900,
								attackRating = 23
							}
						}
					}
				},
				{
					triggerType = 0,
					key = True,
					waveIndex = 102,
					conditionType = 1,
					preWaves = {
						101,
						202
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 204209,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								-15,
								0,
								75
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 204209,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								-15,
								0,
								35
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 242214,
							reinforceDelay = 10,
							score = 0,
							delay = 0,
							moveCast = True,
							corrdinate = {
								-5,
								0,
								55
							},
							buffList = {
								8050,
								8051
							}
						},
						{
							monsterTemplateID = 242009,
							reinforceDelay = 10,
							score = 0,
							delay = 0,
							moveCast = True,
							corrdinate = {
								-15,
								0,
								45
							},
							buffList = {
								8050,
								8051
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 209502,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								30,
								0,
								55
							},
							buffList = {
								8001,
								8002
							}
						}
					},
					airFighter = {
						{
							interval = 10,
							onceNumber = 6,
							totalNumber = 6,
							formation = 10006,
							delay = 0,
							templateID = 2200824,
							score = 1,
							weaponID = {
								2020002
							},
							attr = {
								airPower = 125,
								maxHP = 900,
								attackRating = 23
							}
						}
					}
				},
				{
					triggerType = 0,
					key = True,
					waveIndex = 103,
					conditionType = 0,
					preWaves = {
						102,
						101
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 242107,
							reinforceDelay = 6,
							score = 0,
							delay = 0,
							moveCast = True,
							corrdinate = {
								-10,
								0,
								65
							}
						},
						{
							monsterTemplateID = 242108,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								-10,
								0,
								45
							}
						},
						{
							monsterTemplateID = 243018,
							score = 0,
							delay = 0,
							moveCast = True,
							affix = True,
							corrdinate = {
								0,
								0,
								55
							},
							bossData = {
								hpBarNum = 50,
								icon = "qibolin"
							},
							buffList = {
								8050,
								8051
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 204210,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								10,
								0,
								75
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 204210,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								10,
								0,
								35
							},
							buffList = {
								8001,
								8007
							}
						}
					},
					airFighter = {
						{
							interval = 10,
							onceNumber = 6,
							totalNumber = 6,
							formation = 10006,
							delay = 0,
							templateID = 2200824,
							score = 1,
							weaponID = {
								2020002
							},
							attr = {
								airPower = 125,
								maxHP = 900,
								attackRating = 23
							}
						}
					}
				},
				{
					triggerType = 8,
					waveIndex = 900,
					preWaves = {
						103
					},
					triggerParams = {}
				}
			}
		}
	},
	fleet_prefab = {}
}
