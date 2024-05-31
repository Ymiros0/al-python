return {
	fadeOut = 1.5,
	mode = 2,
	id = "BULISITUOERBOSS2",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"An Exercise Gone Slightly Wrong\n\n<size=45>2. The Investigator Arrives</size>",
					1
				}
			}
		},
		{
			bgm = "battle-boss-4",
			oldPhoto = True,
			bgName = "bg_story_nepu2",
			side = 2,
			dir = 1,
			bgmDelay = 2,
			soundeffect = "event./battle/boom2",
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "KABOOOM!",
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
			oldPhoto = True,
			bgName = "bg_story_nepu2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Bristol came under heavy fire from afar the moment she arrived in the area with the ruined naval base.",
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
			oldPhoto = True,
			bgName = "bg_story_nepu2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Her attackers were the opposing exercise team. It's only natural they would target her.",
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
			bgName = "bg_story_nepu2",
			oldPhoto = True,
			dir = 1,
			actor = 101490,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "S-someone's shooting at me?!",
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
			expression = 4,
			side = 2,
			bgName = "bg_story_nepu2",
			oldPhoto = True,
			dir = 1,
			actor = 101490,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "Aw crap! I can't believe this place has fallen too!",
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
			bgName = "bg_story_nepu2",
			oldPhoto = True,
			dir = 1,
			actor = 101490,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "What's my damage... Huh? No damage?! Seems they aren't a real threat in that case.",
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
			oldPhoto = True,
			bgName = "bg_story_nepu2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "She was hit numerous times, but suffered not as much as a scratch.",
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
			oldPhoto = True,
			bgName = "bg_story_nepu2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Which is no surprise, given the fleet was firing blanks as part of the exercise. Bristol, however, had no way of knowing this at the time.",
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
			bgName = "bg_story_nepu2",
			oldPhoto = True,
			dir = 1,
			actor = 101490,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "I've got to stay calm! First thing's first, I have to find something to hide behind!",
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
			oldPhoto = True,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "She took a quick look around and spotted an abandoned base. She sailed towards it while firing back at the opponents.",
			bgm = "xinnong-3",
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
			oldPhoto = True,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "The base was barren and lonesome. Despite the daytime sun's glow, it inspired a melancholic mood.",
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
			actor = 101490,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			oldPhoto = True,
			say = "Lights... on!",
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
			bgName = "star_level_bg_148",
			oldPhoto = True,
			dir = 1,
			actor = 101490,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "Whew... Helps calm my nerves.",
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
			actor = 101490,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			oldPhoto = True,
			say = "If the enemy's advanced all the way out here, our hopes of turning the tables look pretty bleak...",
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
			bgName = "star_level_bg_148",
			oldPhoto = True,
			dir = 1,
			actor = 101490,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "But if things are this bad, why did Ingraham radio me just earlier...?",
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
			bgName = "star_level_bg_148",
			oldPhoto = True,
			dir = 1,
			actor = 101490,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "I can't even investigate what's going on here when I:n't have any leads...",
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
			oldPhoto = True,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Bristol began thinking. Just:, a cold wind blew against her body, sending a shiver through it. She listened close, and seemed to hear a voice carried by the wind.",
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
			actor = 900321,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			oldPhoto = True,
			say = "...stol...",
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
			actor = 900321,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			oldPhoto = True,
			say = "Bris...tol... I've been looking for you...",
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
			oldPhoto = True,
			bgName = "star_level_bg_148",
			side = 2,
			dir = 1,
			actor = 101490,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "EEK!",
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
			expression = 4,
			side = 2,
			bgName = "star_level_bg_148",
			oldPhoto = True,
			dir = 1,
			actor = 101490,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "...Wh-whoever you are, I'm not scared of you! But I know better than to talk to strangers, so go away!",
			effects = {
				{
					active = False,
					name = "speed"
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
			actor = 900321,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			oldPhoto = True,
			say = "Bristol... c'mon...",
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
			oldPhoto = True,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "The voice got closer and clearer until eventually, its source came into view.",
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
			bgName = "star_level_bg_148",
			oldPhoto = True,
			dir = 1,
			actor = 101490,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "Wh-who's there?!",
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
			bgName = "star_level_bg_148",
			oldPhoto = True,
			dir = 1,
			actor = 101450,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "It's me, dummy! Allen! What's the matter? Didya get hit on the head with a blank or something?",
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
			actor = 101450,
			side = 2,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			oldPhoto = True,
			say = "Also, didn't you get the memo? The attackers have moved to a new location, so we should reposition too.",
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
			bgName = "star_level_bg_148",
			oldPhoto = True,
			dir = 1,
			actor = 101490,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "Oh yeah? Out of all the stickers on your rigging, which one represents the Commander?",
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
			bgName = "star_level_bg_148",
			oldPhoto = True,
			dir = 1,
			actor = 101450,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "...What?",
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
			bgName = "star_level_bg_148",
			oldPhoto = True,
			dir = 1,
			actor = 101490,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "I knew it! You're not Allen, you're just an impostor!",
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
			expression = 2,
			side = 2,
			bgName = "star_level_bg_148",
			oldPhoto = True,
			dir = 1,
			actor = 101450,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "What are you talking about?! I:n't under–",
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
			bgName = "star_level_bg_148",
			oldPhoto = True,
			dir = 1,
			actor = 101490,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "Begone,:ppelganger! You:n't belong in this world! Leave me and my friends alone!",
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
			oldPhoto = True,
			bgName = "star_level_bg_148",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Bristol chanted a series of incoherent spells at the top of her lungs,: ran inside the base, shrouded in darkness.",
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
			say = "Some time later, Ingraham received a status update from the fleet participating in the exercise.",
			side = 2,
			bgName = "bg_main_day",
			dir = 1,
			bgm = "level",
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
			expression = 2,
			side = 2,
			bgName = "bg_main_day",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 101480,
			say = "...An unidentified ship came into the area and fired warning shots at you?",
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
			actor = 101480,
			side = 2,
			bgName = "bg_main_day",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "There's no way an enemy could appear out of the blue this close to port... Unless... Yeah, that's got to be Bristol.",
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
			bgName = "bg_main_day",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 101480,
			say = "She just got back from an excursion and needs some time to adjust, I reckon.",
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
			bgName = "bg_main_day",
			paintingNoise = True,
			dir = 1,
			actor = 101450,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "Thing is, I met her at the old ruins earlier. I tried to talk to her, but she yelled weird stuff back at me: ran off.",
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
			bgName = "bg_main_day",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 101480,
			say = "What did she say, exactly?",
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
			bgName = "bg_main_day",
			paintingNoise = True,
			dir = 1,
			actor = 101450,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "Uhh... The gist of it was, \"leave me alone.\"",
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
			actor = 101480,
			side = 2,
			bgName = "bg_main_day",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Geesh... She must be really bummed out. Maybe she wants us to suspend the exercise for her sake.",
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
			bgName = "bg_main_day",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 101450,
			say = "She could've just said it if so... I'll go ask the Commander about that.",
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
			actor = 101480,
			side = 2,
			bgName = "bg_main_day",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "...",
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
			bgName = "bg_main_day",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 101480,
			say = "(What the heck's up with Bristol? I told her to link up with the attackers, but instead she's acting independently.)",
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
			actor = 101480,
			side = 2,
			bgName = "bg_main_day",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
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
			expression = 1,
			side = 2,
			bgName = "bg_main_day",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 101480,
			say = "(Wait... What if she didn't get those orders because of the radio static?)",
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
			actor = 101480,
			side = 2,
			bgName = "bg_main_day",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = ".........",
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
			bgName = "bg_main_day",
			dir = 1,
			blackBg = True,
			actor = 101480,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "(Then I've gotta find her and make:ubly sure she gets them this time!)",
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
