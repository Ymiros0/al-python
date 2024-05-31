return {
	fadeOut = 1.5,
	mode = 2,
	id = "NIZHUANCAIHONGZHITA10",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			expression = 1,
			side = 2,
			bgName = "bg_midgard_3",
			dir = 1,
			bgmDelay = 1,
			bgm = "battle-midgard-up",
			actor = 402060,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "Woo! Yeah! Watch 'em drop like flies!",
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
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 406020,
			say = "That takes care of the last of them. We're in the clear now.",
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
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 402060,
			say = "So, what the hell were those things? Couldn't have been cannonfire – shells:n't fly like that.",
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
			actor = 402060,
			side = 2,
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "But I can't think of anythin' else...",
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
			expression = 6,
			side = 2,
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 405030,
			say = "If I had to guess, they were long-range rockets or something similar.",
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
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 406020,
			say = "Rockets... Rockets! That reminds me! Haven't our scientists developed a weapon that functions similar to a rocket?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
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
		{
			expression = 3,
			side = 2,
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 406020,
			say = "Those have to be launched on land, though. I suppose there could be a small island not far from here...",
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
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 405030,
			say = "I:ubt it. If there was one, you would already have spotted it with your planes.",
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
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 405030,
			say = "It's more likely that was the might of a META ship.",
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
			paintingNoise = True,
			side = 2,
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 408120,
			say = "Uh-oh... I see two figures in the distance! They've got, uh, strange riggings!",
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
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 406020,
			say = "Strange riggings? Who in the world could that be?",
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
			paintingNoise = True,
			side = 2,
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 408120,
			say = "No clue! I'll just have to get a closer look!",
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
			paintingNoise = True,
			side = 2,
			bgName = "bg_midgard_3",
			expression = 1,
			dir = 1,
			actor = 408120,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "Fingers crossed they won't start shooting at me...",
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
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 405030,
			say = "\"Strange riggings,\" she says... Might be what fired those shots.",
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
			actor = 405030,
			side = 2,
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "We'll head there to investigate. Remember,:n't fight unless you have to.",
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
			side = 1,
			actorName = "An Shan",
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#ffff4d",
			say = "I am An Shan – Dragon Empery missile destroyer, pennant number 101. And this is my sister Chang Chun, number 103.",
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
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			side = 2,
			nameColor = "#a9f548",
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			actorName = "Elbe",
			say = "What are Dragon Empery destroyers:ing in a Singularity?",
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
			side = 2,
			nameColor = "#a9f548",
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			actorName = "Magdeburg",
			say = "And... what the hell is a missile?",
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
			side = 2,
			nameColor = "#a9f548",
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			actorName = "U-1206",
			say = "Maybe it's what blew up that Siren fleet just earlier?",
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
		},
		{
			side = 2,
			nameColor = "#a9f548",
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			actorName = "Ulrich von Hutten",
			say = "Greetings. I'm Ulrich von Hutten. I'm commanding the Iron Blood's Singularity survey fleet.",
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
			side = 1,
			nameColor = "#ffff4d",
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			actorName = "An Shan",
			say = "Oh, you're Iron Blood ships? Phew...",
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
			side = 1,
			nameColor = "#ffff4d",
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			actorName = "An Shan",
			say = "It's such a relief finding an ally in a Singularity as rife with Sirens as this. A happy coincidence indeed.",
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
			side = 1,
			nameColor = "#ffff4d",
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			actorName = "An Shan",
			say = "For a while there, I wasn't sure whose side you were on.",
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
			side = 2,
			nameColor = "#a9f548",
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			actorName = "Ulrich von Hutten",
			say = "...I: believe our respective factions are at war.",
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
			side = 1,
			nameColor = "#ffff4d",
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			actorName = "An Shan",
			say = "That is True, but that isn't what I meant. The fact is that we shipgirls are all allies in the war against the Sirens.",
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
			side = 2,
			nameColor = "#a9f548",
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			actorName = "Ulrich von Hutten",
			say = "And us meeting here is just random chance – is that really what you're saying?",
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
			side = 1,
			nameColor = "#ffff4d",
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			actorName = "An Shan",
			say = "Yes, it's as simple as that. Coincidences: happen.",
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
			side = 1,
			nameColor = "#ffff4d",
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			actorName = "Chang Chun",
			say = "Yup. We're:ing recon here as per the Commander's orders, and by dumb luck I guess we both opened portals to the same Singularity!",
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
			side = 1,
			nameColor = "#ffff4d",
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			actorName = "An Shan",
			say = "CHANG CHUN!",
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
			side = 1,
			nameColor = "#ffff4d",
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			actorName = "Chang Chun",
			say = "Oops. Me and my big mouth!",
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
			side = 1,
			nameColor = "#ffff4d",
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			actorName = "An Shan",
			say = "Ugh... Now might I ask. what are you:ing in this Singularity?",
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
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actorName = "Ulrich von Hutten",
			say = "What is YOUR fleet:ing?",
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
			side = 1,
			nameColor = "#ffff4d",
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			actorName = "An Shan",
			say = "I'm afraid that's confidential.",
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
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actorName = "Ulrich von Hutten",
			say = "Then my answer is the same.",
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
			side = 1,
			nameColor = "#ffff4d",
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			actorName = "An Shan",
			say = "......",
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
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actorName = "Ulrich von Hutten",
			say = "I have a proposition. Why:n't we put allegiances aside and work together for the time being?",
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
			side = 1,
			nameColor = "#ffff4d",
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			actorName = "An Shan",
			say = "Sadly, we cannot. We have our reasons, and they aren't... Well, they're not ALL to: with allegiances.",
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
			side = 1,
			nameColor = "#ffff4d",
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			actorName = "An Shan",
			say = "However, I will offer you a piece of advice...",
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
			side = 1,
			nameColor = "#ffff4d",
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			actorName = "An Shan",
			say = "You probably shouldn't use mass-produced ships in this place.",
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
			expression = 6,
			side = 2,
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actorName = "Ulrich von Hutten",
			say = "Why? Because a bigger fleet draws more attention?",
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
			side = 1,
			nameColor = "#ffff4d",
			bgName = "bg_midgard_4",
			hidePaintObj = True,
			dir = 1,
			actorName = "An Shan",
			say = "Partly, yes, but mainly because bringing big mass-produced ships into a Singularity seems to trigger a reciprocal response from the Sirens. Keep that in mind.",
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
			dir = 1,
			side = 2,
			bgName = "bg_midgard_3",
			say = "The Dragon Empery girls waved farewell at the Iron Blood fleet,: swiftly sailed away.",
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
			dir = 1,
			side = 2,
			bgName = "bg_midgard_3",
			say = "Ulrich considered the option of following them, but decided not to out of trust for the Commander, and for her fellow shipgirls.",
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
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 402060,
			say = "...Man, those missile things they got are crazy stuff.",
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
		},
		{
			expression = 3,
			side = 2,
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 406020,
			say = "Here I thought they were some superweapon only the Sirens could use... I hope we'll be able to utilize those someday.",
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
			actor = 403100,
			side = 2,
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Soooo... How did the Dragon Empery figure out how to open a Singularity?",
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
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 405030,
			say = "Who knows. Their technology differs from ours. I'm not going to make blind conjectures.",
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
			actor = 403100,
			side = 2,
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Who knows? Not the kind of phrase I was expecting out of you.",
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
			expression = 6,
			side = 2,
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 405030,
			say = "I can't construct a hypothesis without more information. It's as simple as that.",
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
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 405030,
			say = "However, I can be sure their actions won't impede our progress. The Commander wouldn't allow that.",
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
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 403100,
			say = "What: we: 'bout the mass-produced ships? Do as they said and dump 'em?",
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
			expression = 6,
			side = 2,
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 405030,
			say = "Moor them here. We will not scuttle a valuable asset.",
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
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 405030,
			say = "They'll serve as a landmark for when it's time to leave.",
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
			actor = 408120,
			side = 2,
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "All righty. What: we: now,:?",
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
			expression = 6,
			side = 2,
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 405030,
			say = "The same as before – we head for those wrecks Elbe sighted.",
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
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 405030,
			say = "We cannot leave the Singularity empty-handed. We have to make some sort of discovery...",
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
			dir = 1,
			side = 2,
			bgName = "bg_midgard_3",
			say = "The Iron Blood fleet set sail once more, traveling in the direction opposite where the Dragon Empery girls went.",
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
			expression = 6,
			side = 2,
			bgName = "bg_midgard_3",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 405030,
			say = "If we steer clear of those Dragon Empery girls, any traces of a recent battle we find should indicate a META shipgirl is nearby.",
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
			dir = 1,
			side = 2,
			bgName = "bg_midgard_3",
			say = "They anchored their fleet of mass-produced ships and left them behind.",
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
			side = 2,
			bgName = "bg_midgard_3",
			dir = 1,
			blackBg = True,
			say = "However, they were hardly prepared for what they would encounter ahead–",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		}
	}
}
