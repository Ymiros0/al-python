return {
	id = "JIARIXINTIAODAYOULUN14",
	mode = 2,
	fadeOut = 1.5,
	scripts = {
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			say = "Cruise Ship - Warehouse",
			bgm = "login_us_0401",
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
			expression = 4,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 101490,
			say = "Commander, Fu Shun, Essex, Alfredo, Ema, Alsace... and me, Bristol. Yep, the gang's all here.",
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
			actor = 501020,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Yeah! So? Out with it! What: we: now, Captain?",
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
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 101490,
			say = "Naturally... it's time to review our third mystery!",
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
			actor = 0,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Then why did we gather here in the warehouse instead of the mystery room?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 107094,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "I think we'll have a freer range of motion here. Don't worry, Commander. I'll explain everything.",
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
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 107094,
			say = "We still have time before we get started, so let's review the third case. the ghost of the cabin quarter.",
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
			actor = 107094,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Once again, we have exactly three clues.",
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
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 107094,
			say = "Clue the first. footsteps in the night. Mysterious footsteps can be heard from a corridor near the cabins late at night.",
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
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 107094,
			say = "Clue the second. spirit photography. Alfredo Oriani got a picture of a ghost in one corridor.",
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
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 107094,
			say = "Clue the third. the inescapable corridor. In one corridor, a thick fog appears and disorients people passing through.",
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
			actor = 107094,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "As usual, Commander, I'd like to hear your thoughts.",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "All of these have logical explanations.",
					flag = 1
				},
				{
					content = "I have an idea who the culprit is.",
					flag = 2
				},
				{
					content = "Okay, bear with me here. No – SQUID with me here.",
					flag = 3
				}
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			optionFlag = 1,
			say = "Well, all of this can be explained with science. There isn't even a mystery here. It's all just dumb rumors.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "star_level_bg_148",
			dir = 1,
			optionFlag = 1,
			actor = 101490,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Yeah! And that means that this series of events was all artificially set up!",
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
			actor = 501020,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			optionFlag = 1,
			nameColor = "#A9F548FF",
			say = "We've already identified the suspect, too!",
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
			actor = 0,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			optionFlag = 2,
			say = "Water vapor, sea fog, ghosts... Tempesta has to be behind this.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			optionFlag = 2,
			actor = 601090,
			say = "Incredible, Commander... You reached that conclusion this quickly? It took us hours of discussion to figure it out.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			optionFlag = 3,
			say = "Because the ghost might just be a giant squid monster that can disappear and spew sea fog at will.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 7,
			side = 2,
			bgName = "star_level_bg_148",
			dir = 1,
			optionFlag = 3,
			actor = 805030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "*sigh*... Commander, now isn't the time for jokes.",
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
			actor = 107094,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "I think we can all agree that Tempesta must be the culprits behind this series of events.",
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
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 107094,
			say = "I've found it strange ever since the ship was attacked.",
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
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 107094,
			say = "Tempesta has to pass through a storm to come to our world. Don't you find it a little convenient that they'd appear at the perfect place and time to get in our way?",
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
			actor = 107094,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "This leads us naturally to one answer. Tempesta sent informants onto the cruise ship ahead of time. They coordinated the ambush.",
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
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 107094,
			say = "The sounds of dragging things, strange noises, disappearing food, water vapor, and sea fog... All of it is evidence that someone with Tempesta is on board.",
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
			actor = 107094,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "The clue we found while investigating the ghost is the most damning of all. Tempesta just happens to have one shipgirl who can turn invisible,:es it not?",
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
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 107094,
			say = "And what: you know, that same girl didn't appear during the attack today!",
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
			actor = 0,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "It's Mary Celeste!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 107094,
			say = "Exactly! She's the culprit behind everything that's been happening!",
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
			actor = 0,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Mary definitely:es seem to be the likely culprit.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "So, we know who the mastermind is. I still:n't understand why we assembled in the warehouse today.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 101490,
			say = "To catch her red-handed, of course! Heheh, Essex set a brilliant trap. Our prey should take the bait any minute now!",
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
			actor = 0,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "A trap?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 107094,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Earlier, feigning small talk, I told Mary Celeste at the wharf that you would be coming to take inventory in the warehouse tonight. Alone.",
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
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 107094,
			say = "She was visibly disturbed. By:, I already knew that I had her in my grasp.",
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
			actor = 107094,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Shh. Everyone but the Commander, hide. The pressure sensor I set up just went off – someone's coming.",
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
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			say = "The sound of footsteps suddenly becomes audible in the seemingly empty warehouse.",
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
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			say = "When the sound stops, suddenly, something soft presses against my back.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "star_level_bg_148",
			paintingNoise = True,
			dir = 1,
			actor = 9600040,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "(Phew... I can finally be alone with the Commander...)",
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
			bgName = "star_level_bg_148",
			paintingNoise = True,
			dir = 1,
			actor = 9600040,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "(Something's really wrong with this cruise ship. I can go invisible, and it's still so darn hard to get close to you!)",
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
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9600040,
			say = "Ahem. Don't move! Yarrr, I be a pirate!",
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
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			say = "A silhouette emerges out of thin air. It's Mary Celeste.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			say = "Our hypothesis from before was right on the money. Mary Celeste and her pet, the giant squid(?) monster Argo, are the ones behind all of these mysteries.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			actor = 601080,
			say = "*snap!*",
			soundeffect = "event./ui/kuaimen",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			flashout = {
				dur = 0.15,
				alpha = {
					0,
					1
				}
			},
			flashin = {
				delay = 0.2,
				dur = 0.2,
				alpha = {
					1,
					0
				}
			}
		},
		{
			expression = 1,
			nameColor = "#A9F548FF",
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			side = 2,
			actor = 601080,
			say = "Heheh, got my evidence!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 501020,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Finally, the adventure reaches its climax!",
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
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 101490,
			say = "The truth of the seven mysteries will now be unveiled!",
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
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 107094,
			say = "There can only be one truth. Mary Celeste, you are the culprit!",
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
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 805030,
			say = "Cold-Hearted Killing Machine, entering extermination mode!",
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
			expression = 7,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9600040,
			say = "W-wait, wait, wait! You:n't have to go that far!",
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
			expression = 4,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9600040,
			say = "Hahaha... I can't believe you got me that fast. And you even set a trap... Not bad, not bad at all.",
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
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9600040,
			say = "I admit defeat. You got me. What are you gonna: to me, Commander?",
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
			actor = 0,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Hmm... Illegal boarding, food theft, attempted kidnapping...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 7,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9600040,
			say = "H-huh? You're actually planning to punish me?!",
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
			actor = 0,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "I'm kidding. But it is True that your flippant actions have caused trouble for everyone else on the cruise. How: you plan to make up for that?",:
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9600040,
			say = "Heheh, easy! I've already got a plan.",
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
			actor = 9600040,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "A late-night bonfire party at Tempesta HQ. All are invited! How's that sound?",
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
