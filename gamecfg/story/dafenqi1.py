return {
	fadeOut = 1.5,
	mode = 2,
	id = "DAFENQI1",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"Your Dear Inventor\n\n<size=45>1 Wellspring of Inspiration</size>",
					1
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "At noon on a clear and sunny day...",
			bgmDelay = 2,
			bgm = "story-richang-6",
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
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 608020,
			say = "Commander, you've got to test out my latest invention!",
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
					dur = 0.2,
					x = 0,
					number = 2
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
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "Leonardo da Vinci, the inventor with seemingly endless vitality, comes through my office:ors carrying some strange contraption.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 608020,
			say = "Check it out! I call it the Stiffy Shoulder Massaginator! It'll make your shoulder stiffness go away faster than you can say \"ow, that's smart!\"",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 608020,
			say = "I figure you'll benefit from it a lot since you're strapped to your desk all the time. Come on, try it!",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "It's True – I've had to file a lot of paperwork lately, and that has taken its toll on me. It can't hurt to try.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "\"Well...\"",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "\"On one hand, it:es its job exactly as advertised. On the other...\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "\"It's really loud. Can't you make it quieter somehow?\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 6,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 608020,
			say = "WHAT? DID YOU SAY SOMETHING? I CAN'T HEAR YOU!",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "\"I said it's too loud!\"",
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
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "*click*",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "It's impossible to have a conversation over the noise from her invention, so I decide to switch it off.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 608020,
			say = "I see. So the noise is a problem.",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 608020,
			say = "To be fair, I only designed it to give you a great shoulder massage, not to be quiet or anything!",
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
					y = 0,
					delay = 0,
					dur = 0.4,
					x = 30,
					number = 2
				}
			}
		},
		{
			expression = 8,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 608020,
			say = "So if it makes a little noise, that's fine!",
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
					content = "\"It's much more than 'a little' noise.\"",
					flag = 1
				},
				{
					content = "\"It negatively affects the user experience.\"",
					flag = 2
				}
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 608020,
			say = "It's a minor detail,:n't worry about it! It works, that's what matters. By the way,: you have any more problems other than stiff shoulders?",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 608020,
			say = "Big or small, I wanna know! Heck, the more the better!",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "\"Let me guess – you came to my office expressly to find inspiration again, didn't you?\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 608020,
			say = "Uh... Ahahah... Guilty as charged.",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 608020,
			say = "Yeah, my idea well has been pretty dry for a while now.",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 608020,
			say = "So I thought, \"hey, you have a vast range of knowledge, so you must have a good idea or two I can work with.\"",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "\"I'm happy to give you that. After I finish my work.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 608020,
			say = "Awesome! Thanks, Commander!",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 608020,
			say = "In fact, let me help you with the work! It'll be quicker that way, plus I want to make up for dropping in unannounced!",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "Since da Vinci wants this work:ne and over as quickly as possible, I thought she'd prioritize efficiency above all else.",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "However, that presumption proved wrong – she reads through the request forms, sent in by shipgirls, meticulously and slowly.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 6,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 608020,
			say = "Geesh... All these needs I never knew about...",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 608020,
			say = "This gives me loads of ideas for new inventions, actually...",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "She smacks the table with both her hands and stands up, as if she just figured something out.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 8,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 608020,
			say = "I've got it!",
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
					active = True,
					name = "speed"
				}
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 608020,
			say = "Commander, I'm going to be your secretary starting tomorrow!",
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
			},
			action = {
				{
					type = "shake",
					y = 30,
					delay = 0,
					dur = 0.2,
					x = 0,
					number = 2
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
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 608020,
			say = "These request forms provide excellent inspo! And working as your secretary, I'll get to read them all day!",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "\"If you want to, be my guest. Just:n't forget to perform the actual duties of a secretary.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 608020,
			say = "Well, of course! I'll chew through those papers while savoring the sweet taste of inspiration.",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 608020,
			say = "Heck, I can get the job:ne in a flash if I really want to!",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 608020,
			say = "Let me: this and I promise you won't be disappointed♪",
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
					y = 0,
					delay = 0,
					dur = 0.4,
					x = 30,
					number = 2
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "And so, I welcomed da Vinci aboard as my secretary.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		}
	}
}
