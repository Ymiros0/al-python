return {
	id = "HAIDAOSUIJI9-1",
	mode = 2,
	scripts = {
		{
			nameColor = "#A9F548FF",
			side = 2,
			say = "These mushrooms look as poisonous as it gets, but they should be safe to lie:wn on.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			say = "You sit:wn on the cap of a mushroom and rest. Its surface is velvety soft, and gently beckons you to dreamland.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			say = "When you open your eyes again, you find yourself inside a cave packed with treasures.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			flashout = {
				black = True,
				dur = 1,
				alpha = {
					0,
					1
				}
			},
			flashin = {
				delay = 1,
				dur = 1,
				black = True,
				alpha = {
					1,
					0
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			say = "Among them, an old-fashioned but ornate treasure chest atop a tall pedestal in the cave's center catches your eye.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "Claim the treasure for yourself.",
					flag = 1
				},
				{
					content = "This is a dream. Snap out of it.",
					flag = 2
				}
			}
		}
	}
}
