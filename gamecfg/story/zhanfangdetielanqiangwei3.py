return {
	fadeOut = 1.5,
	mode = 2,
	id = "ZHANFANGDETIELANQIANGWEI3",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"The Iron Rose Blooms\n\n<size=45>3 Seydlitz's Friends</size>",
					1
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_103",
			say = "I was walking through the port town along with Seydlitz.",
			bgmDelay = 2,
			bgm = "story-richang-1",
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
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_103",
			say = "Though, it would be more accurate to say that we're on patrol together.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_103",
			say = "(This is the perfect opportunity. I can use this chance to ask about what's been bothering her. Let's start with her relationships...)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 404030,
			side = 2,
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Personal relationships? Oh, that's nothing to worry about. I'm getting along with everyone just as much as ever.",
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
					content = "\"That means you're worried about Lützow,:?\"",
					flag = 1
				},
				{
					content = "\"Is Bismarck worrying you?\"",
					flag = 2
				},
				{
					content = "\"Oh, no. Is it Hipper?\"",
					flag = 3
				}
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "star_level_bg_103",
			dir = 1,
			optionFlag = 1,
			actor = 404030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "W-well... I mean, she can be a little bit of a lazybones, but...",
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
			bgName = "star_level_bg_103",
			dir = 1,
			optionFlag = 1,
			actor = 404030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "But even she hasn't:ne anything worth troubling you over, Commandant!",
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
			bgName = "star_level_bg_103",
			dir = 1,
			optionFlag = 2,
			actor = 404030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Not at all. I have utmost respect for her!",
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
			bgName = "star_level_bg_103",
			dir = 1,
			optionFlag = 3,
			actor = 404030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "While Hipper can be difficult at times, I consider her a very trustworthy ally.",
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
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 404030,
			say = "Commandant, I appreciate your concern. I really:.",
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
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 404030,
			say = "But it's nothing to: with our friends. In fact, I trust them across the board. If there is a problem, I'd say it's myself...",
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
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 404030,
			say = "So I'll: my best to solve it and avoid causing trouble for you, Commandant!",
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
			actor = 404030,
			side = 2,
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Besides, as long as I can faithfully fulfill my duty by your side, I'm more than satisfied!",
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
			bgName = "star_level_bg_103",
			say = "(It:esn't seem like questioning her further will get me answers. I'll just have to keep waiting and watching...)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_103",
			say = "I happen to overhear a conversation as we pass by the outdoor patio of a nearby restaurant.",
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
			expression = 1,
			side = 2,
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601020,
			say = "Wait?! You already have the latest monster-hunting news?!",
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
			actor = 601020,
			side = 2,
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "...Oh, I see. But:esn't that make charge blades useless here?",
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
			actor = 201200,
			side = 2,
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "You'll find that these occasional large targets are more than worth the effort.",
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
			actor = 201200,
			side = 2,
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Aim for its weakness from afar. That giant uses its tail for all of its attacks, so if you cut it off...",
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
			bgName = "star_level_bg_103",
			say = "(Very intriguing. Seydlitz is listening in, too. Might as well ask what she thinks.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "\"Did that pique your interest?\"",
					flag = 1
				}
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 404030,
			say = "Y-yes! A little...",
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
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 404030,
			say = "As far as I can tell, they're discussing a new virtual gaming attraction that recently opened up in the amusement park.",
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
			actor = 404030,
			side = 2,
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "I hear the monster-hunting experience it provides is like the real thing.",
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
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 404030,
			say = "In the simulation, you can even ride horses and gallop through the plains.",
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
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 404030,
			say = "Oh, I'd love to try it...",
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
					content = "\"Do you go horseback riding often?\"",
					flag = 1
				}
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 404030,
			say = "Umm, I occasionally: when I'm on patrol...",
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
			expression = 2,
			side = 2,
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 404030,
			say = "But I've never experienced hunting on horseback.",
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
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 404030,
			say = "Oh! I'm not saying I want to try it right now, though! We haven't even finished our patrols here yet!",
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
			bgName = "star_level_bg_103",
			say = "(I was about to invite her to go horseback riding together, but she shot that:wn before I could say a word.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_103",
			say = "(And she's right. We haven't finished our patrols yet.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_103",
			say = "(I'll have to think of a way to make her open up more...)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		}
	}
}