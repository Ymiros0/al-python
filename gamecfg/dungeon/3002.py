return {
	map_id = 10005,
	id = 3002,
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
					key = True,
					waveIndex = 101,
					conditionType = 1,
					preWaves = {
						100
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 0,
							corrdinate = {
								0,
								0,
								70
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 0,
							corrdinate = {
								0,
								0,
								55
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 0,
							corrdinate = {
								0,
								0,
								40
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 2,
							corrdinate = {
								11,
								0,
								80
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 2,
							corrdinate = {
								11,
								0,
								70
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 2,
							corrdinate = {
								11,
								0,
								60
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 4,
							corrdinate = {
								11,
								0,
								60
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 4,
							corrdinate = {
								11,
								0,
								50
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 4,
							corrdinate = {
								11,
								0,
								40
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 6,
							corrdinate = {
								19,
								0,
								75
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 6,
							corrdinate = {
								19,
								0,
								65
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 8,
							corrdinate = {
								19,
								0,
								55
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 8,
							corrdinate = {
								19,
								0,
								35
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 10,
							corrdinate = {
								25,
								0,
								80
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 10,
							corrdinate = {
								25,
								0,
								65
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 10,
							corrdinate = {
								30,
								0,
								50
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 12,
							corrdinate = {
								35,
								0,
								55
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 12,
							corrdinate = {
								25,
								0,
								45
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 12,
							corrdinate = {
								15,
								0,
								35
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 14,
							corrdinate = {
								15,
								0,
								75
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 14,
							corrdinate = {
								25,
								0,
								65
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 16,
							corrdinate = {
								30,
								0,
								50
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 16,
							corrdinate = {
								30,
								0,
								35
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 18,
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
							monsterTemplateID = 712,
							moveCast = True,
							delay = 18,
							corrdinate = {
								30,
								0,
								50
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 20,
							corrdinate = {
								30,
								0,
								80
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 20,
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
							monsterTemplateID = 712,
							moveCast = True,
							delay = 22,
							corrdinate = {
								30,
								0,
								55
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 22,
							corrdinate = {
								30,
								0,
								40
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 24,
							corrdinate = {
								30,
								0,
								70
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 24,
							corrdinate = {
								30,
								0,
								55
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 26,
							corrdinate = {
								30,
								0,
								80
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 26,
							corrdinate = {
								30,
								0,
								60
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 28,
							corrdinate = {
								30,
								0,
								60
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 28,
							corrdinate = {
								30,
								0,
								40
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 30,
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
							monsterTemplateID = 712,
							moveCast = True,
							delay = 30,
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
							monsterTemplateID = 712,
							moveCast = True,
							delay = 32,
							corrdinate = {
								30,
								0,
								55
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 32,
							corrdinate = {
								30,
								0,
								35
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 34,
							corrdinate = {
								30,
								0,
								80
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 34,
							corrdinate = {
								30,
								0,
								50
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 36,
							corrdinate = {
								35,
								0,
								55
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 36,
							corrdinate = {
								25,
								0,
								45
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 36,
							corrdinate = {
								15,
								0,
								35
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 38,
							corrdinate = {
								25,
								0,
								65
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 38,
							corrdinate = {
								35,
								0,
								55
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 40,
							corrdinate = {
								30,
								0,
								80
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 40,
							corrdinate = {
								30,
								0,
								35
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 42,
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
							monsterTemplateID = 712,
							moveCast = True,
							delay = 42,
							corrdinate = {
								30,
								0,
								50
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 44,
							corrdinate = {
								30,
								0,
								80
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 44,
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
							monsterTemplateID = 712,
							moveCast = True,
							delay = 46,
							corrdinate = {
								30,
								0,
								40
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 49,
							corrdinate = {
								30,
								0,
								55
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 49,
							corrdinate = {
								30,
								0,
								40
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 52,
							corrdinate = {
								30,
								0,
								80
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 52,
							corrdinate = {
								30,
								0,
								70
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 55,
							corrdinate = {
								30,
								0,
								50
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 55,
							corrdinate = {
								30,
								0,
								40
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 57,
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
							monsterTemplateID = 712,
							moveCast = True,
							delay = 57,
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
							monsterTemplateID = 712,
							moveCast = True,
							delay = 59,
							corrdinate = {
								30,
								0,
								55
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 59,
							corrdinate = {
								30,
								0,
								35
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 61,
							corrdinate = {
								25,
								0,
								80
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 61,
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
							monsterTemplateID = 712,
							moveCast = True,
							delay = 63,
							corrdinate = {
								25,
								0,
								75
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 63,
							corrdinate = {
								45,
								0,
								65
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 63,
							corrdinate = {
								35,
								0,
								55
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 65,
							corrdinate = {
								30,
								0,
								85
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 65,
							corrdinate = {
								30,
								0,
								55
							},
							buffList = {
								8001,
								8002
							}
						},
						{
							monsterTemplateID = 712,
							moveCast = True,
							delay = 65,
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
					}
				}
			}
		}
	},
	fleet_prefab = {}
}
