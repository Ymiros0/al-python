return {
	id = "XINGHAIZHUGUANG6",
	mode = 2,
	fadeOut = 1.5,
	scripts = {
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			say = "Sea of Stars - Testing Block",
			bgm = "theme-starsea-core",
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
			bgName = "bg_story_task",
			hidePaintObj = True,
			say = "The shipgirls tripped a motion sensor as they entered a spacious room. It, often used as a conference room, lit up brightly.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 104010,
			side = 2,
			bgName = "bg_story_task",
			factiontag = "Data Retrieval Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Go on. Have a seat.",
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
			bgName = "bg_story_task",
			factiontag = "Special Operations Force",
			dir = 1,
			actor = 118020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Where is everybody? Did we get here way before the others?",
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
			bgName = "bg_story_task",
			factiontag = "Data Retrieval Department",
			dir = 1,
			actor = 104010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "The opposite – we arrived after everyone else. They've all left to focus on their respective missions.",
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
			bgName = "bg_story_task",
			factiontag = "Data Retrieval Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "*sigh*... Now, I summoned you for one specific thing. A salvage mission.",
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
			bgName = "bg_story_task",
			factiontag = "Data Retrieval Department",
			dir = 1,
			actor = 104010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "This is important, so listen closely.",
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
			bgName = "bg_story_task",
			factiontag = "Special Operations Force",
			dir = 1,
			actor = 118020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Uh, what? I thought this was a routine meeting kind of thing.",
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
			bgName = "bg_story_task",
			factiontag = "Special Operations Force",
			dir = 1,
			actor = 118020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Also,:esn't your department deal with salvage? I:n't know the first thing about technology, so I'm not gonna be much help, anyway.",
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
			bgName = "bg_story_task",
			factiontag = "Data Retrieval Department",
			dir = 1,
			actor = 104010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "The thing is... we're short on staff. Furthermore, it's possible that there will be combat during this mission.",
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
			bgName = "bg_story_task",
			factiontag = "Data Retrieval Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Flasher can handle the data salvaging. She's:ne it multiple times before so she'll know how it's:ne.",
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
			bgName = "bg_story_task",
			factiontag = "Data Retrieval Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "While she:es that, you and Louisville just need to keep her safe.",
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
			bgName = "bg_story_task",
			factiontag = "Special Operations Force",
			dir = 1,
			actor = 118020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Ohh, so it's a VIP escort ordeal! In that case, your multitalented girl has you covered!",
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
			bgName = "bg_story_task",
			factiontag = "Special Operations Force",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "So, where and when is the mission?",
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
			bgName = "bg_story_task",
			factiontag = "Data Retrieval Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "The Coral Sea, when the battle took place.",
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
			bgName = "bg_story_task",
			factiontag = "Data Retrieval Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I want to investigate it one more time.",
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
			bgName = "bg_story_task",
			factiontag = "Data Retrieval Department",
			dir = 1,
			actor = 104010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Our previous attempt was a bust, so I've revised the plan. It will work this time.",
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
			bgName = "bg_story_task",
			factiontag = "Special Operations Force",
			dir = 1,
			actor = 118020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Operation \"Chasing Light,\" eh... Nice codename.",
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
			bgName = "bg_story_task",
			hidePaintObj = True,
			say = "Constellation passed Guam the mission briefing. The more she read through it, the more grave her expression turned.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 118020,
			side = 2,
			bgName = "bg_story_task",
			factiontag = "Special Operations Force",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Hang on, this mission is in an area that's always been strictly forbidden for entry.",
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
			bgName = "bg_story_task",
			factiontag = "Special Operations Force",
			dir = 1,
			actor = 118020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Isn't this kind of against regulations?",
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
			bgName = "bg_story_task",
			factiontag = "Data Retrieval Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Don't worry about that. I already got Saratoga to approve everything.",
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
			bgName = "bg_story_task",
			factiontag = "Special Operations Force",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Hmm...",
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
			bgName = "bg_story_task",
			factiontag = "Data Retrieval Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Do you have any other concerns?",
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
			bgName = "bg_story_task",
			factiontag = "Special Operations Force",
			dir = 1,
			actor = 118020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Hmmmmmmm... Nah! I'm in.",
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
			bgName = "bg_story_task",
			factiontag = "Data Retrieval Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "...Thank you.",
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
			bgName = "bg_story_task",
			factiontag = "Data Retrieval Department",
			dir = 1,
			actor = 104010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "San Jacinto, you're in charge of Guam and Louisville. Link up with Flasher: begin the data salvage.",
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
			actor = 107300,
			side = 2,
			bgName = "bg_story_task",
			factiontag = "Data Retrieval Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "You got it. Come with me, folks!",
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
			bgName = "star_level_bg_503",
			hidePaintObj = True,
			say = "Sea of Stars Testing Block - Salvage Preparation Area",
			bgm = "story-richang-11",
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
			bgName = "star_level_bg_503",
			hidePaintObj = True,
			say = "The shipgirls entered an area devoid of actual salvaging equipment. This was no surprise, since their salvage target was not a physical object, but rather data.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_503",
			hidePaintObj = True,
			say = "For that matter, there were no boats or transportation facilities either.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_503",
			hidePaintObj = True,
			say = "At the room's center, encircled by experiment materials, was a massive gateway. The girls' gazes converged upon it.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "star_level_bg_503",
			factiontag = "Special Operations Force",
			dir = 1,
			actor = 118020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Sooo... is this device some kind of portal to access the simulated world?",
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
			bgName = "star_level_bg_503",
			factiontag = "Special Operations Force",
			dir = 1,
			actor = 118020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "No wonder the whole Data Retrieval Department is nowhere to be found during salvages. They all go in there!",
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
			actor = 107300,
			side = 2,
			bgName = "star_level_bg_503",
			factiontag = "Data Retrieval Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Yep. They: make frequent visits to the simulated world.",
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
			bgName = "star_level_bg_503",
			factiontag = "Data Retrieval Department",
			dir = 1,
			actor = 107300,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "This isn't the only gate in the Sea of Stars, though. There are others.",
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
			actor = 107300,
			side = 2,
			bgName = "star_level_bg_503",
			factiontag = "Data Retrieval Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I've heard their functions are all different, too. Maybe it's some sort of technological parallel research.",
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
			actor = 107300,
			side = 2,
			bgName = "star_level_bg_503",
			factiontag = "Data Retrieval Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Hello, Flasher! Everyone is here now.",
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
			bgName = "star_level_bg_503",
			factiontag = "Data Retrieval Department",
			dir = 1,
			actor = 107300,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Let's start off with introductions. This is Guam of the Alaska class, and this is Louisville of the Northampton class.",
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
			actor = 108080,
			side = 2,
			bgName = "star_level_bg_503",
			factiontag = "Data Retrieval Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "N-nice to meet you... I'm Flasher, the submarine. I'll take care of the data salvaging.",
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
			actor = 108080,
			side = 2,
			bgName = "star_level_bg_503",
			factiontag = "Data Retrieval Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I've seen your shows, Guam. I-in fact, I'm a big fan...",
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
			bgName = "star_level_bg_503",
			factiontag = "Data Retrieval Department",
			dir = 1,
			actor = 108080,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "*sniffle*... *sob*... Can I have your autograph, once this is all:ne?",
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
			bgName = "star_level_bg_503",
			factiontag = "Special Operations Force",
			dir = 1,
			actor = 118020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Whoa! Wasn't expecting to run into a fan here of all places! Sure you can have my autograph! I'll write it real big and cute just for you!",
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
			bgName = "star_level_bg_503",
			factiontag = "Data Retrieval Department",
			dir = 1,
			actor = 108080,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Th-thank you.",
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
			bgName = "star_level_bg_503",
			factiontag = "Rigging Design Department",
			dir = 1,
			actor = 103270,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Good girl, good girl. Would you like a cookie?",
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
			bgName = "star_level_bg_503",
			factiontag = "Special Operations Force",
			dir = 1,
			actor = 118020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "...Huh?",
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
			actor = 108080,
			side = 2,
			bgName = "star_level_bg_503",
			factiontag = "Data Retrieval Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "*sniffle*... Yes, please... After the mission.",
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
			bgName = "star_level_bg_503",
			factiontag = "Rigging Design Department",
			dir = 1,
			actor = 103270,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Oh, right. Forgive me. I'd forgotten we're on the job.",
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
			bgName = "star_level_bg_503",
			factiontag = "Special Operations Force",
			dir = 1,
			actor = 118020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Eccentric and forgetful... I see, I see.",
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
			bgName = "star_level_bg_503",
			factiontag = "Special Operations Force",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Heehee, she and I should totally: a show together sometime!",
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
			bgName = "bg_zhuguang_cg2",
			hidePaintObj = True,
			say = "San Jacinto stood before the gate's control panel and entered a command.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_zhuguang_cg2",
			hidePaintObj = True,
			say = "In response, the gate's frame began to rumble as if in an earthquake, buzzing ever so faintly.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_zhuguang_cg2",
			hidePaintObj = True,
			say = "It calmed:wn only a few seconds later, leaving the room silent, save for the stable mechanical whirring of the control panel.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_zhuguang_cg2",
			hidePaintObj = True,
			say = "Then, within the gate's ring, a gently glowing portal manifested.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "Louisville",
			bgName = "bg_zhuguang_cg2",
			factiontag = "Rigging Design Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "If I know my movies, going through this portal will take us somewhere else.",
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
			actorName = "Louisville",
			bgName = "bg_zhuguang_cg2",
			factiontag = "Rigging Design Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Just to make sure here... We ARE going into a simulation, not traveling through time and space, right?",
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
			portrait = 118020,
			side = 2,
			bgName = "bg_zhuguang_cg2",
			factiontag = "Special Operations Force",
			dir = 1,
			nameColor = "#A9F548FF",
			actorName = "Guam",
			hidePaintObj = True,
			say = "Well, yeah. They probably just made this gate thingy look cool for the sake of it.",
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
			bgName = "bg_zhuguang_cg2",
			factiontag = "Special Operations Force",
			dir = 1,
			portrait = 118020,
			actorName = "Guam",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Plus, that's how you know it's reliable. If it didn't look cool, how could you be sure it's going to work?",
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
			actorName = "Louisville",
			bgName = "bg_zhuguang_cg2",
			factiontag = "Rigging Design Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Right... Does anyone know what we're supposed to:, by the way?",
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
			portrait = 118020,
			side = 2,
			bgName = "bg_zhuguang_cg2",
			factiontag = "Special Operations Force",
			dir = 1,
			nameColor = "#A9F548FF",
			actorName = "Guam",
			hidePaintObj = True,
			say = "Aha, now that's a technical question.",
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
			bgName = "bg_zhuguang_cg2",
			factiontag = "Special Operations Force",
			dir = 1,
			portrait = 118020,
			actorName = "Guam",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Which means I, of course,:n't have any clue!",
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
			actorName = "Flasher",
			bgName = "bg_zhuguang_cg2",
			factiontag = "Data Retrieval Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Um... Is this everyone's first salvage mission?",
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
			actorName = "Flasher",
			bgName = "bg_zhuguang_cg2",
			factiontag = "Data Retrieval Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Then:n't worry, I know exactly what to:!",
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
			actorName = "Louisville",
			bgName = "bg_zhuguang_cg2",
			factiontag = "Rigging Design Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Good girl! Thank goodness we have someone so dependable.",
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
			actorName = "Flasher",
			bgName = "bg_zhuguang_cg2",
			factiontag = "Data Retrieval Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I-I'm not THAT dependable, but... Thanks... *sob*... *sniffle*...",
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
			actorName = "San Jacinto",
			bgName = "bg_zhuguang_cg2",
			factiontag = "Data Retrieval Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "If everyone's ready: let's set off, shall we?",
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
			bgName = "bg_zhuguang_cg2",
			factiontag = "Special Operations Force",
			dir = 1,
			portrait = 118020,
			actorName = "Guam",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "For sure! Let's go!",
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
