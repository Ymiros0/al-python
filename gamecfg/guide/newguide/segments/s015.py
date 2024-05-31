local var_0_0 = {
	"Let's check out your <color=#ff7d36>storage</color>.",
	"Let's see what <color=#ff7d36>designs</color> you currently have!",
	"Tap here to start <color=#ff7d36>making gear</color>!",
	"I knew it'd be you! Tap here to confirm."
}

return {
	id = "S015",
	events = {
		{
			alpha = 0.271,
			style = {
				dir = -1,
				mode = 2,
				posY = -102.56,
				posX = 0,
				text = var_0_0[1]
			},
			ui = {
				pathIndex = -1,
				def dynamicPath:()
					if getProxy(SettingsProxy).IsMellowStyle():
						return "/OverlayCamera/Overlay/UIMain/NewMainMellowTheme(Clone)/frame/bottom/frame/storage"
					else
						return "/OverlayCamera/Overlay/UIMain/NewMainClassicTheme(Clone)/frame/bottom/equipButton",
				triggerType = {
					1
				},
				fingerPos = {
					posY = -38.49,
					posX = 42.4
				}
			}
		},
		{
			alpha = 0.207,
			style = {
				dir = -1,
				mode = 2,
				posY = 0,
				posX = 0,
				text = var_0_0[2]
			},
			ui = {
				path = "OverlayCamera/Overlay/UIMain/topItems/adapt/bottom_back/types/design",
				pathIndex = -1,
				triggerType = {
					2
				},
				fingerPos = {
					posY = -36.2,
					posX = 61.6
				}
			}
		},
		{
			alpha = 0,
			waitScene = "EquipmentDesignLayer",
			style = {
				dir = -1,
				mode = 2,
				posY = 0,
				posX = 210.07,
				text = var_0_0[3]
			},
			ui = {
				path = "UICamera/Canvas/UIMain/StoreHouseUI(Clone)/EquipmentDesignUI(Clone)/equipment_scrollview/equipment_grid/0/info/make_btn",
				pathIndex = -1,
				triggerType = {
					1
				},
				fingerPos = {
					posY = -50.32,
					posX = 23.88
				}
			}
		},
		{
			alpha = 0.342,
			style = {
				dir = -1,
				mode = 2,
				posY = -2.69,
				posX = 202.1,
				text = var_0_0[4]
			},
			ui = {
				path = "/OverlayCamera/Overlay/UIMain/msg_panel/bg/confirm_btn",
				pathIndex = -1,
				triggerType = {
					1
				},
				fingerPos = {
					posY = -34.24,
					posX = 36.62
				}
			}
		}
	}
}
