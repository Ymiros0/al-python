return {
	fadeOut = 1.5,
	mode = 2,
	id = "KONGXIANGJIAOHUIDIAN17",
	once = True,
	fadeType = 2,
	scripts = {
		{
			side = 2,
			nameColor = "#A9F548FF",
			bgName = "bg_bsmre_cg15",
			hidePaintObj = True,
			stopbgm = True,
			bgmDelay = 2,
			say = "Mirror Sea - α phase, control center",
			bgm = "story-midgard",
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
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "bg_bsmre_cg15",
			actorName = "U-556 META?",
			dir = 1,
			actor = 9708010,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "So this is where you found Ulrich, trapped in a nightmare...",
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
			actor = 9708010,
			nameColor = "#ffa500",
			bgName = "bg_bsmre_cg15",
			hidePaintObj = True,
			dir = 1,
			actorName = "U-556 META?",
			side = 2,
			say = "Are you sure it's a good idea to use the:me projector, Lord Bismarck?",
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
			bgName = "bg_bsmre_cg15",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 405050,
			say = "It's the quickest way to get a grasp on what this place really is.",
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
			actor = 405050,
			side = 2,
			bgName = "bg_bsmre_cg15",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "All you need to: is keep an eye on me. If something happens to me, hit me with a dummy round.",
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
			bgName = "bg_bsmre_cg15",
			actorName = "U-556 META?",
			dir = 1,
			actor = 9708010,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "O-okay! I'll try my best not to hurt you with it!",
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
			expression = 1,
			side = 2,
			bgName = "bg_bsmre_cg15",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 405050,
			say = "Heh. That would be preferable, yes.",
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
			bgName = "bg_bsmre_cg15",
			hidePaintObj = True,
			say = "Bismarck deployed her rigging and started to divert resources into anti-corruption measures as before, getting ready to place her hand on the:me's surface.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_bsmre_cg15",
			hidePaintObj = True,
			say = "Instantly, her vision distorted like ripples moving across a lake's surface.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			stopbgm = True,
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			bgmDelay = 2,
			say = "When she opened her eyes again, she once more found herself in that burning graveyard, with Friedrich collapsed on the ground next to her.",
			bgm = "theme-bismark-reborn",
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
			actor = 405050,
			side = 2,
			bgName = "bg_zhuiluo_2",
			nameColor = "#A9F548FF",
			dir = 1,
			say = "This was Ulrich's deepest fear, the root of her nightmares.",
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
			expression = 3,
			side = 2,
			bgName = "bg_zhuiluo_2",
			actor = 405050,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "But I was the one to touch the:me this time, not her.",
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
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			say = "She rose to her feet, called her rigging, and looked around the area.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			say = "The metallic dragon slowly rose into the sky, conveying large amounts of information to Bismarck in real time.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			say = "It did not take long for her to locate the \"edge\" of the nightmare.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			say = "Beyond the edge of the burning graveyard was a thick wall of inscrutable black fog. Even one glance at it was enough to make one's stomach turn.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			say = "Through Geryon's eyes, however, she could catch a glimpse beyond the fog – of something moving, stirring.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_zhuiluo_2",
			actor = 405050,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "What is that...?! Geryon, get closer! Blow away that fog!",
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
			side = 2,
			nameColor = "#ffa500",
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			actorName = "Geryon",
			say = "ROOOAAAR!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			dialogShake = {
				speed = 0.08,
				x = 15,
				number = 2
			},
			effects = {
				{
					active = True,
					name = "speed"
				}
			}
		},
		{
			side = 2,
			nameColor = "#A9F548FF",
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			say = "Geryon let loose a piercing roar, the shockwave blowing away the black fog just enough to expose what lay below – a jet-black aircraft, with a red core that glistened like a sinister eye.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			effects = {
				{
					active = False,
					name = "speed"
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			say = "At the exact same moment the fog parted, a flash of light appeared on the horizon for just a moment.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 405050,
			side = 2,
			bgName = "bg_zhuiluo_2",
			nameColor = "#A9F548FF",
			dir = 1,
			say = "Is it... beckoning me closer?",
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
			expression = 3,
			side = 2,
			bgName = "bg_zhuiluo_2",
			actor = 405050,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "No, that light wasn't meant for me... It's what led Ulrich to this Mirror Sea!",
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
			side = 2,
			nameColor = "#A9F548FF",
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			say = "KABOOOM!",
			soundeffect = "event./battle/boom2",
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
			side = 2,
			nameColor = "#ffa500",
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			actorName = "Geryon",
			say = "ROOOAAAR!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			dialogShake = {
				speed = 0.08,
				x = 15,
				number = 2
			},
			effects = {
				{
					active = True,
					name = "speed"
				}
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_zhuiluo_2",
			actor = 405050,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "An ambush?! Geryon, come back! Defensive position!",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			effects = {
				{
					active = False,
					name = "speed"
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			say = "The red eye fixed on her seemed to glare harshly, and patterns of light soon appeared one after another across the mangled wreckages of the mass-produced ships.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			say = "They lurched to life, aiming their weapons at Bismarck.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_zhuiluo_2",
			actor = 405050,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Is that strange plane... controlling these Siren husks?",
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
			actor = 405050,
			side = 2,
			bgName = "bg_zhuiluo_2",
			nameColor = "#A9F548FF",
			dir = 1,
			say = "Setting secondary guns to automatic fire. Geryon, use your main battery to take out that command unit!",
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
			side = 2,
			nameColor = "#ffa500",
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			actorName = "Geryon",
			say = "ROOOAAAR!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			dialogShake = {
				speed = 0.08,
				x = 15,
				number = 2
			},
			effects = {
				{
					active = True,
					name = "speed"
				}
			}
		},
		{
			side = 2,
			nameColor = "#A9F548FF",
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			say = "The steel dragon flapped its wings and set sights on the Siren aircraft.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			effects = {
				{
					active = False,
					name = "speed"
				}
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "bg_zhuiluo_2",
			actor = 405050,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Let's see what's behind that mask of yours!",
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
			bgName = "bg_bsmre_5",
			hidePaintObj = True,
			say = "The instant her cannons fired, Bismarck was abruptly whisked away back to reality.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "bg_bsmre_5",
			actorName = "U-556 META?",
			dir = 1,
			actor = 9708010,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "Lord Bismarck! Wake up!",
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
			actor = 405050,
			side = 2,
			bgName = "bg_bsmre_5",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "What happened? Did I start acting up?",
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
			bgName = "bg_bsmre_5",
			actorName = "U-556 META?",
			dir = 1,
			actor = 9708010,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "No, you were fine! Jade warned us that a humanoid Siren is coming this way, and fast!",
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
			expression = 5,
			side = 2,
			bgName = "bg_bsmre_5",
			actorName = "U-556 META?",
			dir = 1,
			actor = 9708010,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "She scrambled her aircraft to intercept, but they were all shot:wn immediately!",
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
			bgName = "bg_bsmre_5",
			actorName = "U-556 META?",
			dir = 1,
			actor = 9708010,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "And that's not the worst part! Zuikaku said the enemy is The Hermit herself!",
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
			expression = 5,
			side = 2,
			bgName = "bg_bsmre_5",
			actorName = "U-556 META?",
			dir = 1,
			actor = 9708010,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "...Sorry for waking you up, but I had to, or else everyone would be in danger!",:
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
			bgName = "bg_bsmre_5",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 405050,
			say = "(I was this close to finding something out, too... But, we'll need to deal with this threat before I can try again.)",
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
			bgName = "bg_bsmre_5",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 405050,
			say = "Thanks, U-556. Come with me, but:n't attack unless I order you to.",
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
			bgName = "bg_bsmre_5",
			actorName = "U-556 META?",
			dir = 1,
			actor = 9708010,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "Okay! I promise I won't!",
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
		}
	}
}
