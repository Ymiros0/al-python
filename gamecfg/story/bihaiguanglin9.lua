﻿return {
	id = "BIHAIGUANGLIN9",
	mode = 2,
	once = true,
	fadeType = 1,
	fadein = 1.5,
	scripts = {
		{
			side = 2,
			nameColor = "#a9f548",
			bgm = "battle-boss-longgong",
			hidePaintObj = true,
			dir = 1,
			say = "Shimakaze darted between the enemy mass-produced ships, skillfully avoiding the increasingly tumultuous waves as she made her way to the Heart of the Dragon Palace.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			expression = 2,
			side = 2,
			actor = 301290,
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			say = "Gotta jump over that next huge wave and duck under that mass-produced ship up ahead...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			expression = 4,
			side = 2,
			actor = 301290,
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			say = "Woooah! It almost feels like I'm surfing!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			paintingNoise = true,
			nameColor = "#a9f548",
			side = 2,
			actor = 307120,
			dir = 1,
			say = "Shimakaze, do you see that weird-looking structure in front of you?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			actor = 301290,
			nameColor = "#a9f548",
			side = 2,
			hidePaintObj = true,
			dir = 1,
			say = "Uhhh... Oh yeah, I do! There's some kind of energy reading coming from it!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			expression = 5,
			side = 2,
			paintingNoise = true,
			actor = 307120,
			dir = 1,
			nameColor = "#a9f548",
			say = "I think that's the mechanism causing all this! We'll need to hurry up and destroy it–",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			actor = 301290,
			nameColor = "#a9f548",
			side = 2,
			hidePaintObj = true,
			dir = 1,
			say = "Right-o! Ready, steady... Wait, huh?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			expression = 2,
			side = 2,
			paintingNoise = true,
			actor = 307120,
			dir = 1,
			nameColor = "#a9f548",
			say = "Don't you know you have to bring the right class for the job? Now this... is where a full-fledged carrier gets to shine!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			expression = 1,
			side = 2,
			paintingNoise = true,
			actor = 307120,
			dir = 1,
			nameColor = "#a9f548",
			say = "Shimakaze, stand back! It's time for some aircraft-delivered fireworks!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			actor = 301290,
			side = 2,
			nameColor = "#a9f548",
			hidePaintObj = true,
			dir = 1,
			say = "Oh, of course. You're up, Katsuragi!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			},
			action = {
				{
					type = "shake",
					y = 45,
					delay = 0,
					dur = 0.15,
					x = 0,
					number = 2
				}
			}
		}
	}
}
