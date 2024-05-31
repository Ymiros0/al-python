return {
	id = 1784303,
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
						timeout = 20
					}
				},
				{
					triggerType = 1,
					waveIndex = 203,
					preWaves = {},
					triggerParams = {
						timeout = 40
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
							deadFX = "udf_shanshuo",
							reinforceDelay = 6,
							monsterTemplateID = 16584203,
							sickness = 0.1,
							delay = 1.5,
							corrdinate = {
								-5,
								0,
								50
							},
							bossData = {
								hpBarNum = 10,
								icon = ""
							},
							buffList = {}
						}
					},
					reinforcement = {
						{
							deadFX = "udf_shanshuo",
							delay = 0.5,
							monsterTemplateID = 16584003,
							sickness = 0.3,
							corrdinate = {
								-5,
								0,
								75
							},
							buffList = {
								8001,
								8007,
								200720,
								200721
							}
						},
						{
							deadFX = "udf_shanshuo",
							delay = 0.5,
							monsterTemplateID = 16584003,
							sickness = 0.3,
							corrdinate = {
								-5,
								0,
								25
							},
							buffList = {
								8001,
								8007,
								200720,
								200721
							}
						},
						{
							deadFX = "udf_shanshuo",
							delay = 0,
							monsterTemplateID = 16584002,
							sickness = 0.3,
							corrdinate = {
								-8,
								0,
								65
							},
							buffList = {
								8001,
								8007,
								200720,
								200721
							}
						},
						{
							deadFX = "udf_shanshuo",
							delay = 0,
							monsterTemplateID = 16584002,
							sickness = 0.3,
							corrdinate = {
								-8,
								0,
								35
							},
							buffList = {
								8001,
								8007,
								200720,
								200721
							}
						},
						{
							deadFX = "udf_shanshuo",
							delay = 0,
							monsterTemplateID = 16584001,
							sickness = 0.3,
							corrdinate = {
								-16,
								0,
								42
							},
							buffList = {
								8001,
								8007,
								200720,
								200721
							}
						},
						{
							deadFX = "udf_shanshuo",
							delay = 0,
							monsterTemplateID = 16584001,
							sickness = 0.3,
							corrdinate = {
								-16,
								0,
								58
							},
							buffList = {
								8001,
								8007,
								200720,
								200721
							}
						}
					},
					airFighter = {
						{
							interval = 5,
							onceNumber = 4,
							formation = 10006,
							delay = 0,
							templateID = 1007084,
							totalNumber = 20,
							weaponID = {
								1007094,
								1007099
							},
							attr = {
								airPower = 40,
								maxHP = 15,
								attackRating = 23
							}
						},
						{
							interval = 5,
							onceNumber = 2,
							formation = 10006,
							delay = 0,
							templateID = 1007089,
							totalNumber = 10,
							weaponID = {
								1007104,
								1007109
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
					waveIndex = 900,
					preWaves = {
						101
					},
					triggerParams = {}
				}
			}
		}
	},
	fleet_prefab = {}
}
