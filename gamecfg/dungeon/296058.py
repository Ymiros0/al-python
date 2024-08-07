return {
	id = 296058,
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
						timeout = 3
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
							monsterTemplateID = 295058,
							score = 0,
							delay = 0,
							moveCast = True,
							affix = True,
							corrdinate = {
								-10,
								0,
								55
							},
							bossData = {
								hpBarNum = 100,
								icon = "canglong_alter"
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
									switchParam = 12,
									addWeapon = {
										2967004,
										2967014,
										2967024
									}
								},
								{
									index = 2,
									switchParam = 3,
									switchTo = 3,
									switchType = 1,
									addWeapon = {
										2967034,
										2967044
									},
									removeWeapon = {
										2967014,
										2967024
									}
								},
								{
									index = 3,
									switchParam = 4,
									switchTo = 4,
									switchType = 1,
									addWeapon = {
										2967074
									},
									removeWeapon = {
										2967044
									}
								},
								{
									index = 4,
									switchType = 1,
									switchTo = 5,
									switchParam = 3,
									addWeapon = {
										2967044
									}
								},
								{
									index = 5,
									switchType = 1,
									switchTo = 6,
									switchParam = 9,
									removeWeapon = {
										2967044
									}
								},
								{
									index = 6,
									switchParam = 6,
									switchTo = 7,
									switchType = 1,
									addWeapon = {
										2967084,
										2967094,
										2967104
									},
									removeWeapon = {
										2967004,
										2967034,
										2967074
									}
								},
								{
									switchParam = 9,
									switchTo = 8,
									index = 7,
									switchType = 1,
									setAI = 70058
								},
								{
									switchType = 1,
									switchTo = 9,
									index = 8,
									switchParam = 8,
									setAI = 10001,
									addWeapon = {
										2967114,
										2967124,
										2967134
									},
									removeWeapon = {
										2967084,
										2967094,
										2967104
									}
								},
								{
									index = 9,
									switchType = 1,
									switchTo = 10,
									switchParam = 3,
									addWeapon = {
										2967044
									}
								},
								{
									index = 10,
									switchType = 1,
									switchTo = 11,
									switchParam = 6,
									removeWeapon = {
										2967044
									}
								},
								{
									switchType = 1,
									switchTo = 12,
									index = 11,
									switchParam = 8,
									setAI = 70058,
									addWeapon = {
										2967144,
										2967154,
										2967164,
										2967174
									},
									removeWeapon = {
										2967124,
										2967134
									}
								},
								{
									switchType = 1,
									switchTo = 13,
									index = 12,
									switchParam = 8,
									setAI = 10001,
									addWeapon = {
										2967184
									},
									removeWeapon = {
										2967114,
										2967144,
										2967154,
										2967164,
										2967174
									}
								},
								{
									index = 13,
									switchType = 0,
									switchTo = -1,
									addWeapon = {},
									removeWeapon = {
										2967184
									}
								}
							}
						}
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
