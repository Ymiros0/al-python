return {
	map_id = 10005,
	id = 6000,
	stages = {
		{
			stageIndex = 1,
			failCondition = 1,
			timeCount = 90,
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
					triggerType = 0,
					waveIndex = 101,
					conditionType = 1,
					preWaves = {
						100
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 753,
							score = 0,
							pilotAITemplateID = 20005,
							delay = 1,
							moveCast = True,
							corrdinate = {
								0,
								0,
								60
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 753,
							score = 0,
							pilotAITemplateID = 20005,
							delay = 1,
							moveCast = True,
							corrdinate = {
								0,
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
							onceNumber = 2,
							formation = 10006,
							delay = 0,
							templateID = 300501,
							totalNumber = 2,
							weaponID = {
								300523
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
					waveIndex = 102,
					conditionType = 1,
					preWaves = {
						101
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 753,
							score = 0,
							pilotAITemplateID = 20005,
							delay = 1,
							moveCast = True,
							corrdinate = {
								-5,
								0,
								60
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 754,
							moveCast = True,
							delay = 1,
							score = 0,
							corrdinate = {
								10,
								0,
								45
							}
						},
						{
							monsterTemplateID = 753,
							score = 0,
							pilotAITemplateID = 20005,
							delay = 1,
							moveCast = True,
							corrdinate = {
								-5,
								0,
								30
							},
							buffList = {
								8001,
								8007
							}
						},
						airFighter = {
							{
								interval = 10,
								onceNumber = 2,
								formation = 10006,
								delay = 0,
								templateID = 300501,
								totalNumber = 2,
								weaponID = {
									300523
								},
								attr = {
									airPower = 40,
									maxHP = 15,
									attackRating = 23
								}
							}
						}
					}
				},
				{
					triggerType = 0,
					waveIndex = 103,
					conditionType = 1,
					preWaves = {
						102
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 750,
							reinforceDelay = 10,
							pilotAITemplateID = 40001,
							delay = 1,
							moveCast = True,
							corrdinate = {
								-3,
								0,
								55
							},
							bossData = {
								hpBarNum = 145,
								icon = "ligen"
							},
							buffList = {
								8601,
								8045,
								8046
							}
						}
					},
					reinforcement = {
						{
							monsterTemplateID = 753,
							score = 0,
							pilotAITemplateID = 20005,
							delay = 0,
							moveCast = True,
							corrdinate = {
								-12,
								0,
								65
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 753,
							score = 0,
							pilotAITemplateID = 20005,
							delay = 0,
							moveCast = True,
							corrdinate = {
								-12,
								0,
								30
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							monsterTemplateID = 754,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								10,
								0,
								75
							}
						},
						{
							monsterTemplateID = 754,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								10,
								0,
								20
							}
						},
						{
							monsterTemplateID = 755,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								30,
								0,
								75
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 755,
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
						},
						{
							monsterTemplateID = 755,
							moveCast = True,
							delay = 0,
							score = 0,
							corrdinate = {
								30,
								0,
								25
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
							onceNumber = 3,
							formation = 10006,
							delay = 0,
							templateID = 300502,
							totalNumber = 6,
							weaponID = {
								300524
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
					triggerType = 8,
					key = True,
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
