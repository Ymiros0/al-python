return {
	map_id = 10001,
	id = 1801013,
	stages = {
		{
			stageIndex = 1,
			failCondition = 1,
			timeCount = 180,
			passCondition = 1,
			backGroundStageID = 1,
			totalArea = {
				-80,
				20,
				90,
				70
			},
			playerArea = {
				-80,
				20,
				45,
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
							deadFX = "idol_bomb_stg",
							reinforceDelay = 6,
							score = 0,
							monsterTemplateID = 16601101,
							delay = 0,
							moveCast = True,
							corrdinate = {
								-5,
								0,
								55
							}
						}
					},
					reinforcement = {
						{
							deadFX = "idol_bomb_stg",
							score = 0,
							monsterTemplateID = 16601001,
							delay = 0,
							moveCast = True,
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
							deadFX = "idol_bomb_stg",
							score = 0,
							monsterTemplateID = 16601001,
							delay = 0,
							moveCast = True,
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
							deadFX = "idol_bomb_stg",
							reinforceDelay = 6,
							score = 0,
							monsterTemplateID = 16601102,
							delay = 0,
							moveCast = True,
							corrdinate = {
								-5,
								0,
								55
							}
						}
					},
					reinforcement = {
						{
							deadFX = "idol_bomb_stg",
							score = 0,
							monsterTemplateID = 16601002,
							delay = 0,
							moveCast = True,
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
							deadFX = "idol_bomb_stg",
							score = 0,
							monsterTemplateID = 16601002,
							delay = 0,
							moveCast = True,
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
					triggerType = 0,
					key = True,
					waveIndex = 104,
					conditionType = 0,
					preWaves = {
						500,
						102,
						101
					},
					triggerParam = {},
					spawn = {
						{
							monsterTemplateID = 16601301,
							reinforceDelay = 6,
							delay = 0,
							moveCast = True,
							corrdinate = {
								-5,
								0,
								50
							},
							bossData = {
								hpBarNum = 30,
								icon = ""
							},
							phase = {
								{
									switchParam = 1.5,
									switchTo = 1,
									index = 0,
									switchType = 1,
									setAI = 20006
								},
								{
									index = 1,
									switchType = 1,
									switchTo = 2,
									switchParam = 5,
									addWeapon = {
										3141001
									}
								},
								{
									index = 2,
									switchParam = 12.5,
									switchTo = 3,
									switchType = 1,
									addWeapon = {
										3141002,
										3141003
									},
									removeWeapon = {
										3141001
									}
								},
								{
									index = 3,
									switchParam = 15,
									switchTo = 4,
									switchType = 1,
									addWeapon = {
										3141004,
										3141005
									},
									removeWeapon = {
										3141002,
										3141003
									}
								},
								{
									index = 4,
									switchType = 1,
									switchTo = 1,
									switchParam = 0.5,
									removeWeapon = {
										3141004,
										3141005
									}
								}
							}
						}
					},
					reinforcement = {
						{
							deadFX = "idol_bomb_stg",
							score = 0,
							monsterTemplateID = 16601001,
							delay = 0,
							moveCast = True,
							corrdinate = {
								2,
								0,
								75
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							deadFX = "idol_bomb_stg",
							score = 0,
							monsterTemplateID = 16601002,
							delay = 0,
							moveCast = True,
							corrdinate = {
								10,
								0,
								65
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							deadFX = "idol_bomb_stg",
							score = 0,
							monsterTemplateID = 16601002,
							delay = 0,
							moveCast = True,
							corrdinate = {
								10,
								0,
								35
							},
							buffList = {
								8001,
								8007
							}
						},
						{
							deadFX = "idol_bomb_stg",
							score = 0,
							monsterTemplateID = 16601001,
							delay = 0,
							moveCast = True,
							corrdinate = {
								2,
								0,
								25
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