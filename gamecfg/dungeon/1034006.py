return {
	map_id = 10001,
	id = 1031006,
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
						timeout = 18
					}
				},
				{
					triggerType = 1,
					waveIndex = 203,
					preWaves = {},
					triggerParams = {
						timeout = 33
					}
				},
				{
					triggerType = 1,
					waveIndex = 204,
					preWaves = {},
					triggerParams = {
						timeout = 44
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
							monsterTemplateID = 10042003,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								20,
								0,
								70
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 10042026,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								-15,
								0,
								70
							}
						},
						{
							monsterTemplateID = 10042032,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								-15,
								0,
								40
							}
						},
						{
							monsterTemplateID = 10042003,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								20,
								0,
								40
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
							onceNumber = 3,
							formation = 10006,
							delay = 0,
							templateID = 510007,
							totalNumber = 3,
							weaponID = {
								510505
							},
							attr = {
								airPower = 40,
								maxHP = 15,
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
							monsterTemplateID = 10042048,
							reinforceDelay = 6,
							score = 0,
							delay = 0,
							moveCast = True,
							corrdinate = {
								-10,
								0,
								55
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 10042060,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								30,
								0,
								65
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 10042060,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								30,
								0,
								45
							},
							buffList = {
								8001,
								8002
							}
						}
					}
				},
				{
					triggerType = 0,
					waveIndex = 103,
					conditionType = 1,
					preWaves = {
						102,
						203
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 10042047,
							reinforceDelay = 8,
							score = 0,
							delay = 0,
							moveCast = True,
							corrdinate = {
								-15,
								0,
								30
							}
						},
						{
							monsterTemplateID = 10042033,
							reinforceDelay = 8,
							score = 0,
							delay = 0,
							moveCast = True,
							corrdinate = {
								0,
								0,
								55
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 10042009,
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
							monsterTemplateID = 10042009,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								10,
								0,
								30
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
							onceNumber = 3,
							formation = 10006,
							delay = 0,
							templateID = 510005,
							totalNumber = 3,
							weaponID = {
								510504
							},
							attr = {
								airPower = 40,
								maxHP = 15,
								attackRating = 23
							}
						}
					}
				},
				{
					triggerType = 0,
					key = True,
					waveIndex = 104,
					conditionType = 0,
					preWaves = {
						103,
						102,
						101
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 10042004,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								8,
								0,
								70
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 10042031,
							reinforceDelay = 6,
							score = 0,
							delay = 0,
							moveCast = True,
							corrdinate = {
								-15,
								0,
								55
							}
						},
						{
							monsterTemplateID = 10042038,
							reinforceDelay = 6,
							score = 0,
							delay = 0,
							moveCast = True,
							corrdinate = {
								0,
								0,
								55
							},
							buffList = {
								8027,
								8028
							}
						},
						{
							monsterTemplateID = 10042004,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								8,
								0,
								40
							},
							buffList = {
								8001,
								8007
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 10042060,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								20,
								0,
								55
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 10042008,
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
							monsterTemplateID = 10042008,
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
					}
				},
				{
					triggerType = 8,
					waveIndex = 900,
					preWaves = {
						104
					},
					triggerParams = {}
				}
			}
		}
	},
	fleet_prefab = {}
}
