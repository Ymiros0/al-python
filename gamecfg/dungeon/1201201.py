return {
	id = 1201201,
	bgm = "story-masazhusai",
	stages = {
		{
			stageIndex = 1,
			failCondition = 1,
			timeCount = 60,
			passCondition = 1,
			backGroundStageID = 1,
			totalArea = {
				-75,
				20,
				90,
				70
			},
			playerArea = {
				-75,
				20,
				42,
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
					waveIndex = 201,
					conditionType = 1,
					preWaves = {
						100
					},
					triggerParams = {},
					spawn = {
						{
							monsterTemplateID = 11900101,
							moveCast = True,
							delay = 1,
							score = 0,
							corrdinate = {
								0,
								0,
								55
							},
							bossData = {
								hpBarNum = 100,
								icon = "aisaikesi"
							},
							buffList = {
								8607,
								8610
							},
							phase = {
								{
									switchParam = 1,
									switchTo = 1,
									index = 0,
									switchType = 1,
									setAI = 10001
								},
								{
									index = 1,
									switchType = 1,
									switchTo = 2,
									switchParam = 3,
									addWeapon = {
										607002,
										607003,
										607004
									}
								},
								{
									index = 2,
									switchParam = 3,
									switchTo = 3,
									switchType = 1,
									removeWeapon = {},
									addWeapon = {
										607008,
										607009
									}
								},
								{
									index = 3,
									switchParam = 3,
									switchTo = 4,
									switchType = 1,
									removeWeapon = {},
									addWeapon = {
										607001
									},
									addBuff = {}
								},
								{
									index = 4,
									switchType = 1,
									switchTo = 5,
									switchParam = 3,
									removeWeapon = {
										607001
									},
									addWeapon = {
										607005,
										607006
									},
									removeBuff = {},
									addBuff = {}
								},
								{
									index = 5,
									switchType = 1,
									switchTo = 6,
									switchParam = 3,
									addWeapon = {
										607005
									}
								},
								{
									index = 6,
									switchType = 1,
									switchTo = 7,
									switchParam = 1
								},
								{
									index = 7,
									switchType = 1,
									switchTo = 8,
									switchParam = 5,
									addWeapon = {}
								},
								{
									index = 8,
									switchParam = 4,
									switchTo = 9,
									switchType = 1,
									removeWeapon = {
										607005
									},
									addWeapon = {
										607001
									}
								},
								{
									index = 9,
									switchType = 1,
									switchTo = 202,
									switchParam = 3,
									addWeapon = {
										607005
									}
								},
								{
									index = 202,
									switchType = 1,
									switchTo = 1,
									switchParam = 3,
									removeWeapon = {
										607001
									}
								}
							}
						}
					}
				},
				{
					triggerType = 8,
					key = True,
					waveIndex = 900,
					preWaves = {
						201
					},
					triggerParams = {}
				}
			}
		}
	},
	fleet_prefab = {}
}
