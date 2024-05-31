return {
	fadeOut = 1.5,
	mode = 2,
	id = "JUFENGYUQINGCHUNZHIQUAN11",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			side = 2,
			stopbgm = True,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "...",
			blackBg = True,
			bgm = "wedding",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			effects = {
				{
					active = True,
					name = "memoryFog"
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			hidePaintObj = True,
			blackBg = True,
			say = "......",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_church",
			factiontag = "The Rising Star",
			dir = 1,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Heheh~♪",
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
				dur = 0.25,
				alpha = {
					0,
					1
				}
			},
			flashin = {
				delay = 0.5,
				dur = 0.25,
				black = True,
				alpha = {
					1,
					0
				}
			}
		},
		{
			actor = 9600010,
			side = 2,
			bgName = "bg_church",
			factiontag = "The Rising Star",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Sooo... you're sure about this?",
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
			bgName = "bg_church",
			factiontag = "The Rising Star",
			dir = 1,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Okay... I feel like the happiest girl alive!",
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
			actor = 9600010,
			side = 2,
			bgName = "bg_church",
			factiontag = "The Rising Star",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "But, living with me's not gonna be easy. You can't just change your mind later, ya hear?",
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
			bgName = "bg_church",
			factiontag = "The Rising Star",
			dir = 1,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Alright,: take my hand...",
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
					content = "(Extend your hand.)",
					flag = 1
				}
			}
		},
		{
			side = 2,
			nameColor = "#A9F548FF",
			bgName = "bg_church",
			hidePaintObj = True,
			say = "SLAM!",
			soundeffect = "event./ui/shuaimen",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			effects = {
				{
					active = False,
					name = "memoryFog"
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
			mode = 1,
			bgName = "bg_jufengv1_cg2",
			bgm = "theme-seaandsun-image",
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
			sequence = {
				{
					"",
					0
				}
			}
		},
		{
			portrait = 9600010,
			side = 2,
			bgName = "bg_jufengv1_cg2",
			factiontag = "The Rising Star",
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Oi! What are ya:ing?!",
			actor = 9600010,
			actorName = "Royal Fortune",
			hidePaintObj = True,
			withoutPainting = True,
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
			bgName = "bg_jufengv1_cg2",
			hidePaintObj = True,
			say = "I open my eyes and see Royal Fortune at the cabin:or, having just thrown it open with force.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 9600030,
			side = 2,
			bgName = "bg_jufengv1_cg2",
			factiontag = "Investor",
			dir = 1,
			nameColor = "#A9F548FF",
			say = "What:es it look like? We're tending to the Commander~",
			actor = 9600030,
			actorName = "Golden Hind",
			hidePaintObj = True,
			withoutPainting = True,
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
			portrait = 9600040,
			side = 2,
			bgName = "bg_jufengv1_cg2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			actorName = "???",
			say = "Shh. Not so loud. The Commander just woke up.",
			withoutPainting = True,
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 9600010,
			side = 2,
			bgName = "bg_jufengv1_cg2",
			factiontag = "The Rising Star",
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Okay, okay...",
			actor = 9600010,
			actorName = "Royal Fortune",
			hidePaintObj = True,
			withoutPainting = True,
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
			portrait = 9600010,
			side = 2,
			bgName = "bg_jufengv1_cg2",
			factiontag = "The Rising Star",
			dir = 1,
			nameColor = "#A9F548FF",
			say = "WAIT, NO! THIS IS NOT OKAY!",
			actor = 9600010,
			actorName = "Royal Fortune",
			hidePaintObj = True,
			withoutPainting = True,
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
			portrait = 9600010,
			side = 2,
			bgName = "bg_jufengv1_cg2",
			factiontag = "The Rising Star",
			dir = 1,
			nameColor = "#A9F548FF",
			say = "The Commander is MY crewmate! Looking after the crew is MY job!",
			actor = 9600010,
			actorName = "Royal Fortune",
			hidePaintObj = True,
			withoutPainting = True,
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
			portrait = 9600010,
			side = 2,
			bgName = "bg_jufengv1_cg2",
			factiontag = "The Rising Star",
			dir = 1,
			nameColor = "#A9F548FF",
			say = "And you! Out of the way!",
			actor = 9600010,
			actorName = "Royal Fortune",
			hidePaintObj = True,
			withoutPainting = True,
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
			portrait = 9600010,
			side = 2,
			bgName = "bg_jufengv1_cg2",
			factiontag = "The Rising Star",
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Famous ghost ship or not, you're in MY seat!",
			actor = 9600010,
			actorName = "Royal Fortune",
			hidePaintObj = True,
			withoutPainting = True,
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
			bgName = "bg_jufengv1_cg3",
			mode = 1,
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
			sequence = {
				{
					"",
					0
				}
			}
		},
		{
			portrait = 9600030,
			side = 2,
			bgName = "bg_jufengv1_cg3",
			factiontag = "Investor",
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Well, well~",
			actor = 9600030,
			actorName = "Golden Hind",
			hidePaintObj = True,
			withoutPainting = True,
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
			portrait = 9600030,
			side = 2,
			bgName = "bg_jufengv1_cg3",
			factiontag = "Investor",
			dir = 1,
			nameColor = "#A9F548FF",
			say = "I thought I heard someone aboard this clipper was dying to meet a ghost ship~",
			actor = 9600030,
			actorName = "Golden Hind",
			hidePaintObj = True,
			withoutPainting = True,
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
			portrait = 9600030,
			side = 2,
			bgName = "bg_jufengv1_cg3",
			factiontag = "Investor",
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Who might that be, hmm~?",
			actor = 9600030,
			actorName = "Golden Hind",
			hidePaintObj = True,
			withoutPainting = True,
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
			portrait = 9600010,
			side = 2,
			bgName = "bg_jufengv1_cg3",
			factiontag = "The Rising Star",
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Ugh! I hate you!",
			actor = 9600010,
			actorName = "Royal Fortune",
			hidePaintObj = True,
			withoutPainting = True,
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
			portrait = 9600010,
			side = 2,
			bgName = "bg_jufengv1_cg3",
			factiontag = "The Rising Star",
			dir = 1,
			nameColor = "#A9F548FF",
			say = "I:n't care about those anymore!",
			actor = 9600010,
			actorName = "Royal Fortune",
			hidePaintObj = True,
			withoutPainting = True,
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
			bgName = "bg_jufengv1_cg3",
			hidePaintObj = True,
			say = "I did not imagine my day would start with a catfight wake-up call...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "Okay, okay. That's enough teasing.",
					flag = 1
				}
			}
		},
		{
			portrait = 9600030,
			side = 2,
			bgName = "bg_jufengv1_cg3",
			factiontag = "Investor",
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Fair enough~ Come sit next to me, Royal Fortune~",
			actor = 9600030,
			actorName = "Golden Hind",
			hidePaintObj = True,
			withoutPainting = True,
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
			actor = 9600010,
			side = 2,
			bgName = "bg_jufengv1_2",
			factiontag = "The Rising Star",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Hmph. \"Thanks.\"",
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
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_jufengv1_2",
			hidePaintObj = True,
			say = "She sits:wn angrily on the bed and grasps my other, unheld hand.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_jufengv1_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "*sigh*... Let's get the important question out of the way.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_jufengv1_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Where's São Martinho? Is she okay?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "???",
			bgName = "bg_jufengv1_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Aye. Safe and sound, thanks to your selfless bravery.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_jufengv1_2",
			factiontag = "The Rising Star",
			dir = 1,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Yeah. She told me she WASN'T after us in particular.",
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
			actor = 9600010,
			side = 2,
			bgName = "bg_jufengv1_2",
			factiontag = "The Rising Star",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Because why would she be? That whole chase only happened because Golden Hind misled us!",
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
			bgName = "bg_jufengv1_2",
			factiontag = "Investor",
			dir = 1,
			actor = 9600030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Well, in my defence, it's only natural to be alarmed in that situation.",
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
			actorName = "???",
			bgName = "bg_jufengv1_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Can't argue with that.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "???",
			bgName = "bg_jufengv1_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "São Martinho feels conflicted about this whole thing. She pursued you all, and you ended up saving her. Must be a hard pill to swallow.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "???",
			bgName = "bg_jufengv1_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Still, I think she'll let you off the hook. Your hand's so warm, anyone would–",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "bg_jufengv1_2",
			factiontag = "The Rising Star",
			dir = 1,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Oi!",
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
			actor = 9600010,
			side = 2,
			bgName = "bg_jufengv1_2",
			factiontag = "The Rising Star",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I see you! Don't you even try!",
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
			actorName = "???",
			bgName = "bg_jufengv1_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Hahahah! You've got a funky crew here, Commander. Hang on to it.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 9600040,
			side = 2,
			bgName = "bg_jufengv1_2",
			factiontag = "A Ghost",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "My name's Mary Celeste, by the way.",
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
			bgName = "bg_jufengv1_2",
			factiontag = "A Ghost",
			dir = 1,
			actor = 9600040,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I'm the True face behind the ghost ship legend of New World.",
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
			actor = 9600010,
			side = 2,
			bgName = "bg_jufengv1_2",
			factiontag = "The Rising Star",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Mhm. She helped by guiding us into the eye of the storm.",
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
			bgName = "bg_jufengv1_2",
			factiontag = "The Rising Star",
			dir = 1,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I figured you should know, since she probably wouldn't tell you herself.",
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
					content = "Thanks for saving us. How can we repay you?",
					flag = 1
				}
			}
		},
		{
			actor = 9600040,
			side = 2,
			bgName = "bg_jufengv1_2",
			factiontag = "A Ghost",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "No need to. You and your crew earned the rescue.",
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
			bgName = "bg_jufengv1_2",
			factiontag = "A Ghost",
			dir = 1,
			actor = 9600040,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Brave people like yourself deserve to see grand voyages to their end. I only did what I thought anyone would have.",
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
			bgName = "bg_jufengv1_2",
			factiontag = "A Ghost",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "As a ghost ship, sailing to the eye of a storm is an instinct imprinted on my hull.",
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
			bgName = "bg_jufengv1_2",
			factiontag = "A Ghost",
			dir = 1,
			actor = 9600040,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Speaking of the storm, it'll abate in a few hours. You can sail away safely after that.",
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
			bgName = "bg_jufengv1_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Will you be coming with us?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 7,
			side = 2,
			bgName = "bg_jufengv1_2",
			factiontag = "A Ghost",
			dir = 1,
			actor = 9600040,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Excuse me?",
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
			bgName = "bg_jufengv1_2",
			factiontag = "A Ghost",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Don't I creep you out? I'm a ghost ship, for god's sake.",
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
					content = "So what?",
					flag = 1
				}
			}
		},
		{
			actor = 9600040,
			side = 2,
			bgName = "bg_jufengv1_2",
			factiontag = "A Ghost",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Come on. You're just saying that.",
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
			actor = 9600010,
			side = 2,
			bgName = "bg_jufengv1_2",
			factiontag = "The Rising Star",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "No, the Commander means it.",
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
			bgName = "bg_jufengv1_2",
			factiontag = "The Rising Star",
			dir = 1,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "The Goddess of Thalasso has nothing against you, so why should we?",
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
			actor = 9600010,
			side = 2,
			bgName = "bg_jufengv1_2",
			factiontag = "The Rising Star",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "You are cordially and sincerely invited to join the crew. We want you with us on this adventure!",
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
			bgName = "bg_jufengv1_2",
			factiontag = "The Rising Star",
			dir = 1,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Isn't that right, Commander?",
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
			actor = 9600010,
			side = 2,
			bgName = "bg_jufengv1_2",
			factiontag = "The Rising Star",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "(Come on, say something!)",
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
					content = "Yeah! You heard her!",
					flag = 1
				},
				{
					content = "Damn right! Took the words right out of my mouth, my queen!",
					flag = 2
				}
			}
		},
		{
			side = 2,
			bgName = "bg_jufengv1_2",
			factiontag = "The Rising Star",
			dir = 1,
			optionFlag = 2,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "O-okay, you:n't need to agree THAT hard...",
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
			bgName = "bg_jufengv1_2",
			factiontag = "A Ghost",
			dir = 1,
			actor = 9600040,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Hmm... Give me a while to think about it.",
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
			bgName = "bg_jufengv1_2",
			factiontag = "A Ghost",
			dir = 1,
			actor = 9600040,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "By the way–",
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
			bgName = "bg_jufengv1_2",
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
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_jufengv1_2",
			hidePaintObj = True,
			say = "Suddenly, the sound of cannon fire rumbles through the cabin window.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "bg_jufengv1_2",
			factiontag = "The Rising Star",
			dir = 1,
			actor = 9600010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "What was that?",
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
			bgName = "bg_jufengv1_2",
			factiontag = "Investor",
			dir = 1,
			actor = 9600030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Oh, dear. It's the Echo Fleet.",
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
			actor = 9600030,
			side = 2,
			bgName = "bg_jufengv1_2",
			factiontag = "Investor",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "And São Martinho is already engaging them. We should back her up~",
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
