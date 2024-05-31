local var_0_0 = {
	"Let's head to the <color=#ff7d36>Dock</color>.",
	"Select one of your girls and tap to view her details.",
	"Tap <color=#ff7d36>gear</color> to see what gear she currently has equipped.",
	"Let's <color=#ff7d36>enhance this gear</color> one time!",
	"Tap to confirm.",
	"This is where you'll see <color=#ff7d36>the gear's stats after it's been enhanced!</color>",
	"Tap <color=#ff7d36>enhance</color> to start enhancing."
}

return {
	id = "S018",
	events = {
		{
			alpha = 0.274,
			style = {
				dir = -1,
				mode = 2,
				posY = 0,
				posX = 0,
				text = var_0_0[1]
			},
			ui = {
				pathIndex = -1,
				def dynamicPath:()
					if getProxy(SettingsProxy).IsMellowStyle():
						return "/OverlayCamera/Overlay/UIMain/NewMainMellowTheme(Clone)/frame/bottom/frame/dock"
					else
						return "/OverlayCamera/Overlay/UIMain/NewMainClassicTheme(Clone)/frame/bottom/dockBtn",
				triggerType = {
					1
				},
				fingerPos = {
					posY = -19.37,
					posX = 35.15
				}
			},
			code = {
				2
			}
		},
		{
			alpha = 0.306,
			waitScene = "DockyardScene",
			style = {
				dir = -1,
				mode = 2,
				posY = 0,
				posX = -5.18,
				text = var_0_0[2]
			},
			ui = {
				path = "/UICamera/Canvas/UIMain/DockyardUI(Clone)/main/ship_container/ships",
				pathIndex = 0,
				image = {
					isChild = True,
					source = "content/ship_icon",
					target = "content/ship_icon",
					isRelative = True
				},
				triggerType = {
					1
				},
				fingerPos = {
					posY = -74.58,
					posX = 48.4
				}
			},
			code = {
				2
			}
		},
		{
			alpha = 0.294,
			waitScene = "ShipMainScene",
			style = {
				dir = -1,
				mode = 2,
				posY = 0,
				posX = 0,
				text = var_0_0[3]
			},
			ui = {
				path = "/OverlayCamera/Overlay/UIMain/blur_panel/adapt/left_length/frame/root/equpiment_toggle",
				pathIndex = -1,
				triggerType = {
					2
				}
			},
			code = {
				2
			}
		},
		{
			alpha = 0.364,
			style = {
				dir = 1,
				mode = 2,
				posY = -140,
				posX = 6,
				text = var_0_0[4]
			},
			ui = {
				path = "OverlayCamera/Overlay/UIMain/equipment_r_container(Adapt)/equipment_r_container/equipment_r/equipment/equipment_r2",
				pathIndex = -1,
				triggerType = {
					1
				}
			}
		},
		{
			alpha = 0.152,
			waitScene = "EquipmentInfoLayer",
			style = {
				dir = -1,
				mode = 2,
				posY = 0,
				posX = 265.7,
				text = var_0_0[5]
			},
			ui = {
				path = "OverlayCamera/Overlay/UIMain/EquipmentInfoUI(Clone)/default/actions/action_button_2",
				pathIndex = -1,
				triggerType = {
					1
				},
				fingerPos = {
					posY = -29.38,
					posX = 44.9
				}
			}
		},
		{
			alpha = 0.405,
			style = {
				dir = -1,
				mode = 2,
				posY = 226,
				posX = 479,
				text = var_0_0[6]
			}
		},
		{
			alpha = 0.366,
			style = {
				dir = 1,
				mode = 2,
				posY = 0,
				posX = 0,
				text = var_0_0[7]
			},
			ui = {
				path = "OverlayCamera/Overlay/UIMain/EquipUpgradeUI(Clone)/main/panel/material_panel/start_btn",
				pathIndex = -1,
				triggerType = {
					1
				},
				fingerPos = {
					posY = -19.78,
					posX = 30.24
				}
			}
		}
	}
}
