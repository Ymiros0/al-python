return {
	id = "XINGHAIZHUGUANG24",
	mode = 2,
	fadeOut = 1.5,
	scripts = {
		{
			actor = 900405,
			side = 2,
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			nameColor = "#FF9B93",
			say = "Targets are acting with hostility. Initiating combat mode.",
			bgm = "battle-warprotocol",
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
			actor = 900405,
			side = 2,
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			nameColor = "#FF9B93",
			say = "Eliminating threats now.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			nameColor = "#A9F548FF",
			bgName = "bg_zhuguang_4",
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
			expression = 3,
			side = 2,
			bgName = "bg_zhuguang_4",
			actor = 9706030,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Stop, Fortress! These girls are not a threat to us!",
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
			bgName = "bg_zhuguang_4",
			factiontag = "Rigging Design Department",
			dir = 1,
			actor = 101510,
			nameColor = "#A9F548FF",
			say = "Did Princeton just... come:wn from the sky?",
			painting = {
				alpha = 0.3,
				time = 1
			},
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
			bgName = "bg_zhuguang_4",
			factiontag = "Special Operations Force",
			dir = 1,
			actor = 118020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Isn't she... META?",
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
			bgName = "bg_zhuguang_4",
			factiontag = "Special Operations Force",
			dir = 1,
			actor = 118020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Why is a META siding with the Sirens? What's the meaning of this?",
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
			bgName = "bg_zhuguang_4",
			factiontag = "Data Retrieval Department",
			dir = 1,
			actor = 104010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Everyone, cease fire and step back for now!",
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
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "We lose contact for just a while, and look what happens...",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			flashout = {
				black = True,
				dur = 0.5,
				alpha = {
					0,
					1
				}
			},
			flashin = {
				delay = 0.5,
				dur = 0.5,
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
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "I TOLD you to stop attacking, Fortress. What's the matter with you?",
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
			actor = 900405,
			side = 2,
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "...They attacked me first.",
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
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "Don't make excuses.",
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
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "Ms. Silver Fox has summoned you. She probably wants you to fix our comms system so things like this won't happen again!",
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
			actor = 900405,
			side = 2,
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "...Fine. Deal with these girls for me,:.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "*sigh*... Hey, you KAN-SEN!",
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
			bgName = "bg_zhuguang_4",
			factiontag = "Special Operations Force",
			dir = 1,
			portrait = 118020,
			actorName = "Guam",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Who? Us?",
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
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "Who: you think? Yes, you.",
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
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "Are you really with the Eagle Union? Why did you attack one of the Council's fleets?",
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
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "And after I expressly asked Ms. Silver Fox to:uble-check that you:n't have any corrosion on you...",
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
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "I can't cover for you if you attack friends and foes indiscriminately, you know.",
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
			actor = 9706030,
			side = 2,
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Which of you is in charge? Who gave the order?",
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
			bgName = "bg_zhuguang_4",
			factiontag = "Rigging Design Department",
			dir = 1,
			portrait = 101510,
			actorName = "Laffey II",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Princeton is fuming...",
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
			bgName = "bg_zhuguang_4",
			factiontag = "Data Retrieval Department",
			dir = 1,
			portrait = 104010,
			actorName = "Constellation",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Guam...",
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
			bgName = "bg_zhuguang_4",
			factiontag = "Special Operations Force",
			dir = 1,
			portrait = 118020,
			actorName = "Guam",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "(Uh-oh, she's got that \"Guam, you better say something\" look!)",
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
			actor = 118020,
			side = 2,
			bgName = "bg_zhuguang_4",
			factiontag = "Special Operations Force",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Ahem. I am Eagle Union large cruiser Guam, hull number CB-2. I'm in charge of this fleet.",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			flashout = {
				black = True,
				dur = 0.5,
				alpha = {
					0,
					1
				}
			},
			flashin = {
				delay = 0.5,
				dur = 0.5,
				black = True,
				alpha = {
					1,
					0
				}
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "*sigh*... No, you aren't, Guam.",
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
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "Constellation is.",
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
			bgName = "bg_zhuguang_4",
			factiontag = "Data Retrieval Department",
			dir = 1,
			actor = 104010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "...How did you know?",
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
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "It's obvious. No sane person would put her in charge of your fleet.",
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
			bgName = "bg_zhuguang_4",
			factiontag = "Special Operations Force",
			dir = 1,
			actor = 118020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Excuse me? Do you even know who I am?",
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
			expression = 7,
			side = 2,
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "I: – all too well, even. I'm from the Union myself, in case you forgot.",
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
			actor = 9706030,
			side = 2,
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "I know all of you. You, Constellation, Laffey, San Jacinto, Louisville, Flasher...",
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
			actor = 9706030,
			side = 2,
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "You know who I am, too. You called me Princeton just a minute ago.",
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
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "And yet, you treat me like a stranger.",
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
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "You:n't recognize the Council or Fortress, and I can't parse your identification signals...",
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
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "So Ms. Silver Fox was right. You ARE from another time and space.",
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
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "Great. Seems we're going to be here for a while.",
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
			actor = 9706030,
			side = 2,
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Fortress, set up a temporary base.",
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
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			say = "Upon receiving Princeton's orders, the floating warships came to life.",
			bgm = "theme-ucnf-image",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			flashout = {
				black = True,
				dur = 0.5,
				alpha = {
					0,
					1
				}
			},
			flashin = {
				delay = 0.5,
				dur = 0.5,
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
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			say = "Starting with the capital ships in the rear of the fleet, the steel giants slowly began descending to the surface.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			say = "After settling in the water, the decks of the warships moved aside, exposing the cannons inside their hulls.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			say = "Looking at the bores of these cannons stirred a sense of security in one's soul.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			say = "Following their larger brethren, the massive repair ship and the vessels damaged in the battle finally touched:wn and began repairs.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 104010,
			side = 2,
			bgName = "bg_zhuguang_4",
			factiontag = "Data Retrieval Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "You're really hunkering:wn, I see.",
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
			actor = 104010,
			side = 2,
			bgName = "bg_zhuguang_4",
			factiontag = "Data Retrieval Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I was wondering what weapons those ships in the back had, since they didn't fight in the battle. Turns out they have large-caliber guns stowed away inside.",
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
			actor = 104010,
			side = 2,
			bgName = "bg_zhuguang_4",
			factiontag = "Data Retrieval Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "They need to be in the water in order to use them,:n't they?",
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
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "Yup. Those are citadel ships, they're our main defense when we set up a temporary base.",
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
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "Now that we have time to talk, let me explain the situation from our perspective.",
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
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "Before arriving here, we got into a space-time anomaly. It appeared without warning, damaging a lot of our equipment to the point of rendering it nonfunctional.",
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
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "As a result, we jumped the gun and attacked you before we knew whether you were corroded or not.",
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
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "For that, I apologize on behalf of all of us.",
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
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "We are not your enemy and we mean no harm to you.",
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
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "I hope that clears the air between us. I'm sure we both have many questions, so let's talk inside.",
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
			expression = 9,
			side = 2,
			bgName = "bg_zhuguang_4",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 9706030,
			say = "Oh, and Guam, no photography is allowed inside the restricted areas. Understood?",
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
			actor = 118020,
			side = 2,
			bgName = "bg_zhuguang_4",
			factiontag = "Special Operations Force",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Ahahaha... Fine, fine!",
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