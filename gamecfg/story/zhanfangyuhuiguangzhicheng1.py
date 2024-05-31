return {
	id = "ZHANFANGYUHUIGUANGZHICHENG1",
	mode = 2,
	fadeOut = 1.5,
	scripts = {
		{
			mode = 1,
			asideType = 1,
			bgm = "story-worldα-grief",
			sequence = {
				{
					"\"You know, assistant... I mean, Commander.\"",
					1.5
				},
				{
					"\"I'm pretty scared of death.\"",
					3
				},
				{
					"\"So much so I:n't even wanna think about it.\"",
					4.5
				}
			}
		},
		{
			mode = 1,
			asideType = 1,
			bgm = "story-worldα-grief",
			sequence = {
				{
					"\"The thing that scares me the most is suddenly dropping dead.\"",
					1.5
				},
				{
					"\"Just everything coming to an abrupt end while your mind is still full of thoughts from yesterday and hopes for tomorrow.\"",
					3
				},
				{
					"\"So if I had to die, I'd want to: it on my own terms. I'd want to decide when, where, and how.\"",
					4.5
				},
				{
					"\"...Obviously, I'm nowhere near as brave as you are.\"",
					6
				},
				{
					"\"You:n't come to terms with your own death just like that. It takes time.\"",
					7.5
				}
			}
		},
		{
			mode = 1,
			asideType = 1,
			bgm = "story-worldα-grief",
			sequence = {
				{
					"\"But when death takes me,:n't mourn for me.\"",
					1.5
				},
				{
					"\"Because when death comes, I'll be ready and waiting.\"",
					3
				},
				{
					"\"When my soul passes on, my aspirations also pass on – to you.\"",
					4.5
				}
			}
		},
		{
			mode = 1,
			asideType = 1,
			bgm = "story-worldα-grief",
			sequence = {
				{
					"\"...What? I have too many of those for you to possibly shoulder?\"",
					1.5
				},
				{
					"\"I know you're just trying to lift the mood with a joke, but I'm serious here.\"",
					3
				},
				{
					"\"...You really:n't think you can: it without my help?\"",
					4.5
				},
				{
					"\"You're asking an awful lot from someone who'll be dead.\"",
					6
				},
				{
					"\"But alright. I'll: what I can.\"",
					7.5
				},
				{
					"\"Everything I've worked for, I leave to you. My dreams, my path, and everything I've protected.\"",
					9
				}
			}
		},
		{
			mode = 1,
			blackBg = True,
			effects = {
				{
					active = True,
					name = "zhanfangyuhuiguangzhicheng"
				}
			},
			sequence = {
				{
					"",
					2
				}
			}
		},
		{
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			say = "I step through the:or in that white space. A blinding whiteness appears and fades,: replaced by a soft light.",
			bgm = "story-richang-sooth",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			flashout = {
				black = False,
				dur = 0.5,
				alpha = {
					0,
					1
				}
			},
			flashin = {
				delay = 0.5,
				dur = 0.5,
				black = False,
				alpha = {
					1,
					0
				}
			},
			effects = {
				{
					active = False,
					name = "zhanfangyuhuiguangzhicheng"
				}
			}
		},
		{
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			say = "Next, an overpowering feeling of fatigue hits me, nearly making me fall to the floor.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			say = "I look around. I'm back at the Orthodoxy's conference venue – only now, it is dark outside.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(That's odd. Every other time I've talked to Helena in that space, only an instant would pass in reality, no matter how long we spoke.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(This time, it feels like time has been flowing normally in reality.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Maybe that's why I feel so tired... I must've been standing here for ages.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(I'm still concerned about the source of the jamming... but I won't be able to get anything:ne if I:n't clear my head.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "???",
			bgName = "bg_huiguangzhicheng_cg2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			say = "There you are, mysterious assistant! You're late!",
			bgm = "theme-thedeathXIII",
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
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			dialogShake = {
				speed = 0.08,
				x = 15,
				number = 2
			}
		},
		{
			side = 2,
			actorName = "???",
			bgName = "bg_huiguangzhicheng_cg1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			say = "I've been waiting AGES for you!",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			dialogShake = {
				speed = 0.08,
				x = 15,
				number = 2
			}
		},
		{
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "bg_huiguangzhicheng_cg1",
			hidePaintObj = True,
			say = "I open the:or to the guest room and find a dimly lit room with a hooded girl inside.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "bg_huiguangzhicheng_cg1",
			hidePaintObj = True,
			say = "She is lying on the bed, rhythmically hitting a pillow with an open palm.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "???",
			bgName = "bg_huiguangzhicheng_cg2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			say = "You're the slowest slowpoke who's ever slowed!",
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
			bgName = "bg_huiguangzhicheng_cg1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			say = "What took you so long to leave the venue?!",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			dialogShake = {
				speed = 0.08,
				x = 15,
				number = 2
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_huiguangzhicheng_cg1",
			hidePaintObj = True,
			recallOption = True,
			nameColor = "#5CE6FF",
			say = "(Who in the world...)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "What's going on here?",
					flag = 1
				},
				{
					content = "Uhh... Who might you be?",
					flag = 2
				},
				{
					content = "How'd you get in here?",
					flag = 3
				}
			}
		},
		{
			side = 2,
			actorName = "???",
			bgName = "bg_huiguangzhicheng_cg2",
			hidePaintObj = True,
			dir = 1,
			optionFlag = 1,
			nameColor = "#5CE6FF",
			say = "What:es it look like? I'm WAITING for YOU!",
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
			bgName = "bg_huiguangzhicheng_cg2",
			hidePaintObj = True,
			dir = 1,
			optionFlag = 2,
			nameColor = "#5CE6FF",
			say = "I'm Miss D!",
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
			bgName = "bg_huiguangzhicheng_cg2",
			hidePaintObj = True,
			dir = 1,
			optionFlag = 3,
			nameColor = "#5CE6FF",
			say = "I walked in! Your security is so lax I didn't need to sneak or anything!",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			dialogShake = {
				speed = 0.08,
				x = 15,
				number = 2
			}
		},
		{
			side = 2,
			actorName = "???",
			bgName = "bg_huiguangzhicheng_cg1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			say = "Oh, by the way? I found a security hole of yours and fixed it! You should be thanking me!",
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
			bgName = "bg_huiguangzhicheng_cg2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			say = "Someone was spying on you from extrastellar space! Bet you didn't know that, moron!",
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
					content = "\"Extrastellar space\"? And what: you mean, \"spying on me\"?",
					flag = 1
				}
			},
			dialogShake = {
				speed = 0.08,
				x = 15,
				number = 2
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_huiguangzhicheng_cg2",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Is she talking about that space Helena created with the Tower's power?)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_huiguangzhicheng_cg2",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Speaking of spying, this girl is in the guest room Helena mentioned. She also knows about our communications...)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_huiguangzhicheng_cg2",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Oh boy... Her \"fixing the security hole\" caused the interference that trapped me in the virtual space, didn't it?)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_huiguangzhicheng_cg2",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "......",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "It was all YOUR fault!",
					flag = 1
				},
				{
					content = "Hey, about that \"fixing\" you did...",
					flag = 2
				}
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900430,
			say = "What? You ran late because my fix trapped you in there?",
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
			expression = 6,
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900430,
			say = "I see how it is. You use that as a romantic dating spot. Sorry about that!",
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
					y = 30,
					delay = 0,
					dur = 0.15,
					x = 0,
					number = 2
				}
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(...I did what?)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 0,
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900430,
			say = "But the thing is, I only cut the connection path. I didn't mess with anything local!",
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
			expression = 10,
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900430,
			say = "If you could get in, why didn't you get out?",
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
					content = "......",
					flag = 1
				},
				{
					content = "I didn't know HOW to get out.",
					flag = 2
				}
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900430,
			say = "So you weren't able to...",
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
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900430,
			say = "If you couldn't get out, why did you go in?",
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
					content = "......",
					flag = 1
				},
				{
					content = "I didn't know HOW to get out.",
					flag = 2
				}
			}
		},
		{
			expression = 0,
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900430,
			say = "Wait, did you not go in by your own will?",
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
			expression = 8,
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900430,
			say = "Ugh. This is getting so confusing!",
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
					y = 30,
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
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900430,
			say = "Forget it! You're here, and that's what matters! I've waited long enough, so let's go already!",
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
					content = "Waited for what?",
					flag = 1
				}
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900430,
			say = "To go whale-hunting!",
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
					y = 30,
					delay = 0,
					dur = 0.15,
					x = 0,
					number = 2
				}
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Whales? What: they have to: with anything?)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Wait, I can't let myself be caught up in her flow. I need to get some answers out of her–)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "By the way, who's the \"mysterious assistant\" you mentioned?",
					flag = 1
				},
				{
					content = "Why did you call me \"assistant\"?",
					flag = 2
				}
			}
		},
		{
			actor = 900430,
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			dir = 1,
			optionFlag = 1,
			nameColor = "#5CE6FF",
			say = "You, duh! YOU are Aoste's mysterious assistant!",
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
					y = 30,
					delay = 0,
					dur = 0.15,
					x = 0,
					number = 2
				}
			}
		},
		{
			actor = 900430,
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			dir = 1,
			optionFlag = 2,
			nameColor = "#5CE6FF",
			say = "Because you are! You're Aoste's mysterious assistant!",
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
					y = 30,
					delay = 0,
					dur = 0.15,
					x = 0,
					number = 2
				}
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Wait, so she even knows about my future \"self\"?)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Everyone who knows anything about that has only alluded to it in vague terms... but she just straight-up said it.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Let's play along and see where it gets me.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "How: you remember who I am?",
					flag = 1
				},
				{
					content = "I'm surprised. Everyone else has forgotten who I am.",:
					flag = 2
				}
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "star_level_bg_542",
			dir = 1,
			optionFlag = 1,
			actor = 900430,
			nameColor = "#5CE6FF",
			hidePaintObj = True,
			say = "I just:! What: you want me to say?",
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
					y = 30,
					delay = 0,
					dur = 0.15,
					x = 0,
					number = 2
				}
			}
		},
		{
			expression = 6,
			side = 2,
			bgName = "star_level_bg_542",
			dir = 1,
			optionFlag = 2,
			actor = 900430,
			nameColor = "#5CE6FF",
			hidePaintObj = True,
			say = "That's because they're stupid! They've forgotten me, too!",
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
					y = 30,
					delay = 0,
					dur = 0.15,
					x = 0,
					number = 2
				}
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900430,
			say = "Look, enough Q&A! No more of that until we've caught the whale!",
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
			expression = 10,
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900430,
			say = "I'm not gonna wait one more minute! We're leaving NOW!",
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
					y = 30,
					delay = 0,
					dur = 0.15,
					x = 0,
					number = 2
				}
			}
		},
		{
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			say = "Without any warning, Miss D walks right up to me.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "star_level_bg_542",
			hidePaintObj = True,
			say = "Before I can get a word in, she musters an ungodly strength for her size and drags me outside.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "star_level_bg_523",
			hidePaintObj = True,
			say = "She leads me around the Iris city streets, pulling me by the sleeve of my uniform.",
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
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "star_level_bg_523",
			hidePaintObj = True,
			say = "I'm following her willingly because, despite my first impression, I:n't sense any ill intent from her.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_523",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Also because I have to know who this girl is and what she wants with me.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 10,
			side = 2,
			bgName = "star_level_bg_523",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900430,
			say = "The time has come, the whale has met its match! La-la-la, la-la-laaa!",
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
			bgName = "star_level_bg_523",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900430,
			say = "This time for sure we're bringing home a catch! La-la-la, la-la-laaa!",
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
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "star_level_bg_523",
			hidePaintObj = True,
			say = "She's been in a good mood ever since we left the guest room. She sings a tune, skipping and jumping as she goes:wn the street.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "star_level_bg_523",
			hidePaintObj = True,
			say = "Passersby should be turning their heads at us... but they aren't.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_523",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(It's strange – she's practically screaming for attention, yet nobody seems to notice.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_523",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Sure, it's late, but people are still on the streets. Why isn't anyone looking our way?)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_523",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(It feels like nobody can even see us...)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "Is it just me, or:es nobody else see us?",:
					flag = 1
				},
				{
					content = "Are you cloaking us?",
					flag = 2
				}
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "star_level_bg_523",
			dir = 1,
			optionFlag = 1,
			actor = 900430,
			nameColor = "#5CE6FF",
			hidePaintObj = True,
			say = "I couldn't bring you outside if they did, idiot!",
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
					y = 30,
					delay = 0,
					dur = 0.15,
					x = 0,
					number = 2
				}
			}
		},
		{
			expression = 8,
			side = 2,
			bgName = "star_level_bg_523",
			dir = 1,
			optionFlag = 2,
			actor = 900430,
			nameColor = "#5CE6FF",
			hidePaintObj = True,
			say = "I'll clue you in after we've caught the whale!",
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
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			say = "We keep walking until we arrive at a park, far away from the main venue.",
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
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			say = "The girl is still singing and skipping along without a care.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(I've got to ask...)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "Where are we going?",
					flag = 1
				}
			}
		},
		{
			expression = 8,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900430,
			say = "To the Gate of Avalon!",
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
					y = 30,
					delay = 0,
					dur = 0.15,
					x = 0,
					number = 2
				}
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "Huh? Are you talking about Scapa Flow?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "You're not suggesting we WALK all the way over there, are you?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900430,
			say = "If we have to!",
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
					y = 30,
					delay = 0,
					dur = 0.15,
					x = 0,
					number = 2
				}
			}
		},
		{
			portrait = 805010,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			actorName = "Richelieu",
			nameColor = "#5CE6FF",
			say = "I'm afraid that's not quite practical, Miss D.",
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
			portrait = 805010,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			actorName = "Richelieu",
			nameColor = "#5CE6FF",
			say = "However, Commander, rest assured that there is a better way to get there.",
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
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			say = "Richelieu's sudden appearance leaves me speechless.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 6,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900430,
			say = "Right! The train! Let's take Liz's train!",
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
					y = 30,
					delay = 0,
					dur = 0.15,
					x = 0,
					number = 2
				}
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "...Liz? And what's this \"train\" you're talking about?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "And... why are you here, Richelieu?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "star_level_bg_521",
			dir = 1,
			bgm = "theme-richelieu",
			actor = 805010,
			nameColor = "#5CE6FF",
			hidePaintObj = True,
			say = "I apologize for using such an unorthodox method of extracting you from the venue.",
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
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 805010,
			say = "But, everyone has their eyes on you. Miss D here was the only person capable of sneaking you out undetected.",
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
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Judging from how serious her tone is... This must be a matter of grave importance.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "This must be a highly sensitive topic,:, if you're not even able to discuss it in your own capital.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 805010,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			say = "Yes. No amount of precaution is excessive for what we have to talk about.",
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
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 805010,
			say = "After all, those who would seek to destroy our branch are everywhere, and we:n't even know how many more lurk in the shadows.",
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
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(...I did what?)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 805010,
			say = "Allow me to cut to the chase. The Royal Navy and the Orthodoxy are currently preparing a joint operation.",
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
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 805010,
			say = "Not here, mind you. Our objective lies beyond our own branch.",
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
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 805010,
			say = "If we:n't: something about it, it will one day have tremendous consequences for our world and everything we want to protect.",
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
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "And you want me to help – correct?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 805010,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			say = "Correct. We need to move to a new location before we can tell you more. This place is not safe.",
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
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 805010,
			say = "Please come with me to Camelot's gate at Scapa Flow.",
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
			actor = 805010,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			say = "Queen Elizabeth will give you all the details once we're there.",
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
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 805010,
			say = "I should state upfront that Naval HQ has no idea about this operation and that it is extremely dangerous.",
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
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 805010,
			say = "You can decide whether or not you'd like to help after you've heard what Queen Elizabeth has to say.",
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
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 805010,
			say = "Should you decide to decline our request, I will see to it that you're brought back as soon as possible.",
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
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			say = "I squint at Richelieu and make out two figures standing behind her – Belfast and Sheffield.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Aha. Looks like the operation in Antarctica brought these factions closer than ever.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(I wonder what they've been discussing. I should ask about it later.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 805010,
			say = "Before you speak to Elizabeth, let me introduce you to your escorts. They will also be part of the operation.",
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
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			say = "Richelieu makes a hand gesture, and her Iris comrades step forth out of hiding.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 805030,
			say = "This one is battleship Alsace – Sacrament of the Unified Orthodoxy, an unreachable dream, and guardian of the Holy See.",
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
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 901070,
			say = "I'm Mogador, judge of the Tribunal. I've been dying to show myself to you. Heheh...",
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
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 803020,
			say = "I am Brennus, a cruiser and a Templar Knight. Well met, Swordbearer.",
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
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 901050,
			say = "Name's Fleuret – Le Hardi-class destroyer. Nice meeting you, Commander!",
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
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 901060,
			say = "I-I'm Épée. Like Fleur said, nice to meet you...",
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
			actor = 805010,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			say = "They have all been carefully chosen for their battlefield competence and ability to protect you.",
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
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 805010,
			say = "The Tribunal may have a reputation for working behind the scenes, unlike those present at the venue now...",
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
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 805010,
			say = "But I assure you, these ladies can be relied upon in a fight.",
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
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Templar Knights, members of the Tribunal, and even Alsace... It's a small team, but their skill more than makes up for that.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Clemenceau's cohorts are here, so you'd think she herself would be, too.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(She probably decided to let Richelieu: the talking. Clemenceau would so: that.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			say = "I shoot a look at each member of the team,: turn my eyes back on Richelieu and the Royal Maids.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			say = "Richelieu gives me a solemn look, waiting for an answer from me, while Belfast gives me a small nod.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			say = "Then there's Sheffield. The look in her eyes screams, \"don't ask questions, just come with us.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Elizabeth, Richelieu, and even Clemenceau are all on board with this.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Moreover, their commitment to secrecy speaks volumes to the importance of whatever this is about.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Then there's Miss D who knows what the future has in store. There's so much she could tell me.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Most important of all, they need me. I have to hear what they have to say.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "Show me the way.",
					flag = 1
				}
			}
		},
		{
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			say = "Miss D waves her hands excitedly, and a train appears in the woods.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 9,
			side = 2,
			bgName = "star_level_bg_521",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900430,
			say = "Get in! We're going to Camelot to catch the whale!",
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
					y = 30,
					delay = 0,
					dur = 0.15,
					x = 0,
					number = 2
				}
			}
		}
	}
}
