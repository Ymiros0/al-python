﻿return {
	fadeOut = 1.5,
	mode = 2,
	id = "HEYAZHIYAN1",
	once = true,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			stopbgm = true,
			mode = 1,
			blackBg = true,
			effects = {
				{
					active = true,
					name = "heyazhiyan"
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
			mode = 1,
			effects = {
				{
					active = false,
					name = "heyazhiyan"
				}
			},
			sequence = {
				{
					"The Graceful Banquet\n\n<size=45>1 The Teahouse</size>",
					1
				}
			}
		},
		{
			side = 2,
			bgName = "star_level_bg_157",
			dir = 1,
			bgmDelay = 2,
			bgm = "story-china",
			actor = 502071,
			nameColor = "#a9f548",
			hidePaintObj = true,
			say = "\"The moon shines on streams among swaying pines – rising mist flanks the dew-rich apricot trees.\"",
			flashout = {
				black = true,
				dur = 1,
				alpha = {
					0,
					1
				}
			},
			flashin = {
				delay = 1,
				dur = 1,
				black = true,
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
			expression = 1,
			side = 2,
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			actor = 502071,
			say = "Mmh... This tea is so fragrant.",
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
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			actor = 205093,
			say = "Is this the place? It matches the description...",
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
			actor = 205093,
			side = 2,
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			say = "Oh, seems someone left the door open.",
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
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			actor = 502081,
			say = "Welcome to the Dragon Empery Teahouse! Are you visiting alone?",
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
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			actor = 205093,
			say = "Yep, it's just me.",
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
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			actor = 502081,
			say = "Right this way then, please!",
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
			dir = 1,
			side = 2,
			bgName = "star_level_bg_157",
			say = "Howe entered the old-fashioned teahouse and Hai Chi showed her to a seat.",
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
			expression = 8,
			side = 2,
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			actor = 502071,
			say = "Welcome, Howe.",
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
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			actor = 205093,
			say = "Thanks. I hope you don't mind having me here.",
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
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			actor = 502071,
			say = "Not at all, we're honored to. Hai Chi, would you get her some tea?",
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
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			actor = 502081,
			say = "Sure! Here you go.",
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
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			actor = 205093,
			say = "Thanks. I've brought homemade cookies. Would you like some?",
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
			expression = 8,
			side = 2,
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			actor = 502071,
			say = "My, Howe, you're too generous for a guest.",
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
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			actor = 205093,
			say = "Don't be shy. We're all friends here.",
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
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			actor = 502081,
			say = "Look, sis! This cookie's shape spells out \"good fortune!\"",
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
			expression = 1,
			side = 2,
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			actor = 502081,
			say = "And this one looks like a garden lantern! These are so cool, Howe!",
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
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			actor = 205093,
			say = "Yes, I went for some Dragon Empery design elements, since I'm visiting you all today. I hope you like them.",
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
			actor = 501020,
			side = 2,
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			say = "Hey, did someone say cookies? Save some for us!",
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
			dir = 1,
			side = 2,
			bgName = "star_level_bg_157",
			say = "Fu Shun entered the teahouse with Grozny in tow, the scent of cookies seemingly having attracted them.",
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
			actor = 501020,
			side = 2,
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			say = "Wow! These are almost too pretty to eat... I mean, right, Grozny?",
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
			actor = 701024,
			side = 2,
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			say = "Yeah. But I still wanna eat.",
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
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			actor = 205093,
			say = "Then by all means, eat. I've made lots in preparation for this evening's banquet.",
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
			actor = 501020,
			side = 2,
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			say = "Hehehe. So, the reason I brought Grozny along is she said she wants to try Dragon Empery tea. I'm not stepping on anyone's toes here, am I?",
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
			expression = 8,
			side = 2,
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			actor = 502071,
			say = "Not at all. In fact, that's very kind of you. Hai Chi, please get some tea for Grozny as well.",
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
			actor = 701024,
			side = 2,
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			say = "Is this a teapot? Then I can pour for myself.",
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
			bgName = "star_level_bg_157",
			say = "Grozny poured the contents of the teapot into her trusty canteen, then chugged the hot tea all in one go.",
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
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			actor = 502071,
			say = "Goodness gracious...! Didn't that burn?",
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
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			actor = 701024,
			say = "...*burp*. Nope, I'm good.",
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
			actor = 501020,
			side = 2,
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			say = "You can't do that, Grozny! You're supposed to take your time with tea, you know? Also, you should be drinking from a teacup instead!",
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
			bgName = "star_level_bg_157",
			say = "Fu Shun snatched the canteen from Grozny and put a teacup on the table in its place.",
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
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			actor = 701024,
			say = "That's tiny. What's the point if I can't chug?",
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
			actor = 501020,
			side = 2,
			bgName = "star_level_bg_157",
			hidePaintObj = true,
			dir = 1,
			nameColor = "#a9f548",
			say = "It's the prime experience! Watch, I'll show you how to drink it like An Shan taught me.",
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
			expression = 8,
			side = 2,
			bgName = "star_level_bg_157",
			dir = 1,
			blackBg = true,
			actor = 502071,
			nameColor = "#a9f548",
			hidePaintObj = true,
			say = "Heehee, how lovely. Hosting a tea party was the right decision indeed.",
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
