local var_0_0 = {
	"HQ is extremely impressed with your performance, Commander. They've given you permission to start working on your second fleet!",
	"Head to the formation menu to put your second fleet, Fleet 2, together. Tap confirm to head directly there.",
	"Tap the button on the right to switch to Fleet 2.",
	"This is where you can begin changing Fleet 2's formation.",
	"The flames of war are raging. Battles will only get harder from here on out. Give 'em hell, Commander!"
}

return {
	id = "SYG006",
	events = {
		{
			alpha = 0.332,
			style = {
				dir = -1,
				mode = 2,
				posY = 0,
				posX = 0,
				text = var_0_0[1]
			}
		},
		{
			alpha = 0.413,
			style = {
				scene = "BIANDUI",
				mode = 2,
				posY = 0,
				dir = -1,
				posX = 0,
				text = var_0_0[2]
			}
		},
		{
			alpha = 0.462,
			style = {
				dir = 1,
				mode = 2,
				posY = 87,
				posX = 228.09,
				text = var_0_0[3]
			},
			ui = {
				hideAnimtor = True,
				path = "/UICamera/Canvas/UIMain/FormationUI(Clone)/nextPage",
				pathIndex = -1,
				triggerType = {
					1
				},
				fingerPos = {
					posY = -45.81,
					posX = 40.2
				}
			}
		},
		{
			alpha = 0.442,
			style = {
				dir = -1,
				mode = 2,
				posY = 121.8,
				posX = 0,
				text = var_0_0[4]
			}
		},
		{
			alpha = 0.44,
			style = {
				dir = -1,
				mode = 2,
				posY = 0,
				posX = 0,
				text = var_0_0[5]
			}
		}
	}
}
