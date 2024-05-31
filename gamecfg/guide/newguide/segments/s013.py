local var_0_0 = {
	"Let's check out your <color=#ff7d36>storage</color>.",
	"Tap <color=#ff7d36>to select tech pack</color>.",
	"Tap <color=#ff7d36>use</color> to open the tech pack."
}

return {
	id = "S013",
	events = {
		{
			alpha = 0.327,
			style = {
				dir = -1,
				mode = 2,
				posY = -50.56,
				posX = -163.2,
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
					posY = -19.78,
					posX = 23.7
				}
			}
		},
		{
			alpha = 0.547,
			waitScene = "StoreHouseScene",
			style = {
				dir = 1,
				mode = 2,
				posY = 65,
				posX = -93.8,
				text = var_0_0[2]
			},
			spriteui = {
				path = "UICamera/Canvas/UIMain/StoreHouseUI(Clone)/item_scrollview/item_grid",
				childPath = "bg/icon_bg/icon",
				pathIndex = "#"
			},
			ui = {
				path = "UICamera/Canvas/UIMain/StoreHouseUI(Clone)/item_scrollview/item_grid",
				pathIndex = "#",
				triggerType = {
					1
				},
				fingerPos = {
					posY = -44.21,
					posX = 50.3
				}
			}
		},
		{
			alpha = 0.298,
			style = {
				dir = 1,
				mode = 2,
				posY = -252,
				posX = -393,
				text = var_0_0[3]
			},
			ui = {
				path = "OverlayCamera/Overlay/UIMain/ItemInfoUI(Clone)/window/actions/use_button",
				pathIndex = -1,
				triggerType = {
					1
				},
				fingerPos = {
					posY = -37.87,
					posX = 49.89
				}
			}
		}
	}
}
