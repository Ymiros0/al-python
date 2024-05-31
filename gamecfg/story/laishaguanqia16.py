return {
	fadeOut = 1.5,
	mode = 2,
	id = "LAISHAGUANQIA16",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			side = 2,
			nameColor = "#A9F548FF",
			bgName = "bg_ryza_2",
			bgm = "battle-boss-4",
			stopbgm = True,
			say = "KABOOOM!",
			soundeffect = "event./battle/boom2",
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
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			flashN = {
				color = {
					1,
					1,
					1,
					1
				},
				alpha = {
					{
						0,
						1,
						0.2,
						0
					},
					{
						1,
						0,
						0.2,
						0.2
					},
					{
						0,
						1,
						0.2,
						0.4
					},
					{
						1,
						0,
						0.2,
						0.6
					}
				}
			},
			dialogShake = {
				speed = 0.09,
				x = 8.5,
				number = 2
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_ryza_2",
			say = "The girls launched an assault on the island, but hardly made any headway in the face of the Siren defenses.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_ryza_2",
			say = "Even though their goal was within sight, they came under increasingly withering fire with each step they advanced.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_ryza_2",
			say = "A sense of dread filled the air as they realized that they were up against a formation more dangerous than anything they had encountered before.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 7,
			side = 2,
			bgName = "bg_ryza_2",
			actor = 101490,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "What the heck IS this?! I haven't seen an encampment THIS heavily fortified since... ever!",
			soundeffect = "event./battle/boom2",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
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
			},
			flashN = {
				color = {
					1,
					1,
					1,
					1
				},
				alpha = {
					{
						0,
						1,
						0.2,
						0
					},
					{
						1,
						0,
						0.2,
						0.2
					},
					{
						0,
						1,
						0.2,
						0.4
					},
					{
						1,
						0,
						0.2,
						0.6
					}
				}
			},
			dialogShake = {
				speed = 0.09,
				x = 8.5,
				number = 2
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "bg_ryza_2",
			actor = 10900030,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Miss Formidable, Miss Ryza, let's retreat! It would be suicide to keep moving forward.",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "bg_ryza_2",
			actor = 601080,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "She's right. There's no way we'll make it through under fire THIS heavy.",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "bg_ryza_2",
			actor = 10900010,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Yeah, I agree. Knowing when to back off is crucial to surviving an adventure!",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "bg_ryza_2",
			actor = 305140,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Formidable and I will cover the rear. Everyone else, keep shooting while you retreat, and:n't let them see your back!",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "bg_ryza_2",
			stopbgm = True,
			dir = 1,
			actor = 10900010,
			nameColor = "#A9F548FF",
			say = "Got it!",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_ryza_1",
			say = "Having successfully retreated, the girls returned to the Land of Beginnings.",
			bgmDelay = 2,
			bgm = "ryza-az-theme",
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
			expression = 3,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 301290,
			say = "Phew... That was a pretty thrilling attack, wasn't it? Right, Suruga?",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 305140,
			say = "Guess so. But:n't be so reckless next time!",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 301290,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Agreed! I shall make that my motto. By the way, are you alright? You look pretty pale...",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
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
		},
		{
			expression = 3,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 305140,
			say = "Don't worry about me, I'm just tired. If anyone deserves a look at, it's Ryza and her friends.",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 305140,
			say = "Let's not forget they're still learning to use their riggings, and they:n't have the tools to repair them. If they sustain damage, they're in trouble.",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 301290,
			say = "Will:!",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			action = {
				{
					type = "move",
					y = 0,
					delay = 0.6,
					dur = 1,
					x = -2500
				}
			}
		},
		{
			actor = 305140,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "*sigh*... I'll have to find a remote place where I can patch myself up...",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 10900040,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "So you WERE injured after all. Sent her away so you could lick your wounds in private, huh?",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 305140,
			say = "Alright, you caught me. Yes, I got a little scratched up, but please keep it a secret from the others.",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
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
		},
		{
			expression = 3,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 305140,
			say = "It's nothing serious, and I:n't want to make the others worried.",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 6,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 10900040,
			say = "My lips are sealed. But,:n't forget that we're all in this together. There's nothing wrong with occasionally asking for help from your allies.",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 305140,
			say = "Of course I know that. I've always tried to keep my head:wn as much as I can.",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 305140,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "It's just that... as the person with the greatest firepower here, I have to keep morale up. You understand how that feels,:n't you?",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 6,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 10900040,
			say = "Hmm, I suspected you'd say as much. You have a True warrior's spirit. By the way, show me where you got hurt.",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 305140,
			say = "Look, I'll be fine. Your rigging getting scratched up isn't the same as breaking an arm. I can patch myself up.",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 10900040,
			say = "Show me anyway. If I'm to survive our upcoming battles, knowing how to repair riggings is a skill I'm going to need.",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 305140,
			say = "Well, if you insist... You can have my tools and try your hand at it.",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 6,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 10900040,
			say = "Thanks. Now, let's take a look.",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		}
	}
}
