return {
	id = 296104,
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
							monsterTemplateID = 295104,
							delay = 0,
							moveCast = True,
							affix = True,
							corrdinate = {
								-5,
								0,
								55
							},
							buffList = {
								8981
							},
							bossData = {
								hpBarNum = 100,
								icon = "fanji_alter"
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
									switchType = 1,
									switchTo = 2,
									index = 1,
									switchParam = 4.5,
									setAI = 20006,
									addWeapon = {
										2969004,
										2969009
									}
								},
								{
									switchType = 1,
									switchTo = 3,
									index = 2,
									switchParam = 2,
									setAI = 10001,
									addWeapon = {
										2969019
									}
								},
								{
									index = 3,
									switchParam = 4,
									switchTo = 4,
									switchType = 1,
									addWeapon = {
										2969014
									},
									removeWeapon = {
										2969004,
										2969009,
										2969019
									}
								},
								{
									switchType = 1,
									switchTo = 5,
									index = 4,
									switchParam = 1.5,
									setAI = 70093,
									addWeapon = {
										2969019
									},
									removeWeapon = {
										2969014
									}
								},
								{
									switchType = 1,
									switchTo = 1,
									index = 5,
									switchParam = 1,
									setAI = 70093,
									addWeapon = {},
									removeWeapon = {
										2969019
									}
								},
								{
									switchType = 1,
									switchTo = 12,
									index = 11,
									switchParam = 2,
									setAI = 70093,
									addWeapon = {},
									removeWeapon = {}
								},
								{
									switchType = 1,
									switchTo = 13,
									index = 12,
									switchParam = 4,
									setAI = 10001,
									addWeapon = {
										2969024,
										2969029
									},
									removeWeapon = {
										2969014
									}
								},
								{
									switchType = 1,
									switchTo = 14,
									index = 13,
									switchParam = 4,
									setAI = 70093,
									addWeapon = {
										2969039
									},
									removeWeapon = {
										2969024,
										2969029
									}
								},
								{
									index = 14,
									switchParam = 5,
									switchTo = 15,
									switchType = 1,
									addWeapon = {
										2969004,
										2969034
									},
									removeWeapon = {
										2969039
									}
								},
								{
									switchType = 1,
									switchTo = 12,
									index = 15,
									switchParam = 4,
									setAI = 10001,
									addWeapon = {
										2969014
									},
									removeWeapon = {
										2969004,
										2969034
									}
								},
								{
									switchType = 1,
									switchTo = 22,
									index = 21,
									switchParam = 1,
									setAI = 70093,
									addWeapon = {},
									removeWeapon = {}
								},
								{
									index = 22,
									switchParam = 2,
									switchTo = 23,
									switchType = 1,
									addWeapon = {
										2969044
									},
									removeWeapon = {}
								},
								{
									index = 23,
									switchParam = 5,
									switchTo = 24,
									switchType = 1,
									addWeapon = {
										2969034,
										2969039
									},
									removeWeapon = {}
								},
								{
									switchType = 1,
									switchTo = 25,
									index = 24,
									switchParam = 9,
									setAI = 10001,
									addWeapon = {
										2969049,
										2969054
									},
									removeWeapon = {
										2969034,
										2969039
									}
								},
								{
									index = 25,
									switchParam = 3.5,
									switchTo = 23,
									switchType = 1,
									addWeapon = {},
									removeWeapon = {
										2969049,
										2969054
									}
								},
								{
									switchType = 1,
									switchTo = 32,
									index = 31,
									switchParam = 1,
									setAI = 70093,
									addWeapon = {
										2969044
									},
									removeWeapon = {}
								},
								{
									index = 32,
									switchParam = 2,
									switchTo = 33,
									switchType = 1,
									addWeapon = {
										2969059,
										2969064
									},
									removeWeapon = {}
								},
								{
									index = 33,
									switchParam = 3,
									switchTo = 34,
									switchType = 1,
									addWeapon = {
										2969004
									},
									removeWeapon = {}
								},
								{
									index = 34,
									switchParam = 3,
									switchTo = 35,
									switchType = 1,
									addWeapon = {
										2969034
									},
									removeWeapon = {}
								},
								{
									index = 35,
									switchParam = 3,
									switchTo = 36,
									switchType = 1,
									addWeapon = {
										2969069,
										2969084,
										2969089
									},
									removeWeapon = {
										2969004,
										2969059,
										2969064
									}
								},
								{
									index = 36,
									switchParam = 3,
									switchTo = 37,
									switchType = 1,
									addWeapon = {
										2969074
									},
									removeWeapon = {
										2969034
									}
								},
								{
									index = 37,
									switchParam = 1,
									switchTo = 38,
									switchType = 1,
									addWeapon = {},
									removeWeapon = {
										2969079
									}
								},
								{
									index = 38,
									switchParam = 3,
									switchTo = 39,
									switchType = 1,
									addWeapon = {
										2969079
									},
									removeWeapon = {}
								},
								{
									index = 39,
									switchParam = 1,
									switchTo = 36,
									switchType = 1,
									addWeapon = {},
									removeWeapon = {
										2969074
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
							monsterTemplateID = 295959,
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
							monsterTemplateID = 295959,
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
							monsterTemplateID = 295959,
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
							monsterTemplateID = 295959,
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
