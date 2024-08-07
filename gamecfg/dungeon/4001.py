return {
	map_id = 10005,
	id = 4001,
	stages = {
		{
			stageIndex = 1,
			failCondition = 1,
			timeCount = 300,
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
							monsterTemplateID = 621,
							moveCast = True,
							delay = 0,
							corrdinate = {
								11,
								0,
								55
							},
							bossData = {
								hpBarNum = 10,
								icon = "qingye"
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
						101
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 622,
							reinforceDelay = 5,
							delay = 2,
							moveCast = True,
							corrdinate = {
								8,
								0,
								55
							},
							bossData = {
								hpBarNum = 12,
								icon = "ruihe"
							}
						}
					}
				},
				{
					triggerType = 0,
					key = True,
					waveIndex = 103,
					conditionType = 1,
					preWaves = {
						102
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 623,
							reinforceDelay = 5,
							delay = 2,
							moveCast = True,
							corrdinate = {
								15,
								0,
								55
							},
							bossData = {
								hpBarNum = 8,
								icon = "xiangfeng"
							}
						},
						{
							monsterTemplateID = 624,
							reinforceDelay = 5,
							delay = 2,
							moveCast = True,
							corrdinate = {
								8,
								0,
								40
							},
							bossData = {
								hpBarNum = 8,
								icon = "xianghe"
							}
						}
					}
				}
			}
		}
	},
	fleet_prefab = {}
}
