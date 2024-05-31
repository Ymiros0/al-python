return {
	fadeOut = 1.5,
	mode = 2,
	id = "XINANFENG7",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"A Gust of Motivation!\n\n<size=45>7 You Can Do It, Libeccio!</size>",
					1
				}
			}
		},
		{
			bgm = "story-1",
			side = 2,
			bgName = "star_level_bg_113",
			bgmDelay = 2,
			say = "Port - Main Plaza",
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
			side = 2,
			bgName = "star_level_bg_113",
			say = "Today is Libeccio's last day as secretary, and I was making my way back to the office from the piers, when suddenly––",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "star_level_bg_113",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601050,
			say = "I guess I made it, huh... It'll be nice to sleep in tomorrow~",
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
			bgName = "star_level_bg_113",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601050,
			say = "Ehehe~ Commander, getting to spend so much time with you was an absolute blast, but being the secretary is really tough after all.",
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
			bgName = "star_level_bg_113",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601050,
			say = "Working so much all the time makes you want to take it easy from time to time,:esn't it? Have you ever wanted to just stay home, Commander?",
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
			bgName = "star_level_bg_113",
			say = "Well, uh...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "\"Of course.\"",
					flag = 1
				},
				{
					content = "\"Of course not.\"",
					flag = 2
				}
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "star_level_bg_113",
			dir = 1,
			optionFlag = 1,
			actor = 601050,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Riiiight? In that case, come play with me!",
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
			bgName = "star_level_bg_113",
			dir = 1,
			optionFlag = 2,
			actor = 601050,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Woahhh... That's super crazy!",
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
			bgName = "star_level_bg_113",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601050,
			say = "Oh, look, isn't that Maestrale over there...?",
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
			bgName = "star_level_bg_113",
			say = "My eyes follow in the direction Libeccio is pointing, and there I see Maestrale, walking alongside Laffey, Ayanami, and Z23.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "star_level_bg_113",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601050,
			say = "Good afternoon, everyone~!",
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
			bgName = "star_level_bg_113",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601040,
			say = "Oh, it's Libeccio and the Commander! G-good afternoon!",
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
			actor = 301050,
			side = 2,
			bgName = "star_level_bg_113",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Good afternoon, yes.",
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
			actor = 401230,
			side = 2,
			bgName = "star_level_bg_113",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Hello, you two.",
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
			actor = 101170,
			side = 2,
			bgName = "star_level_bg_113",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "'ello... Would you like to join our tea party as well?",
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
			actor = 401230,
			side = 2,
			bgName = "star_level_bg_113",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Stop that, Laffey! The Commander is still working!",
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
			actor = 101170,
			side = 2,
			bgName = "star_level_bg_113",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Mm... Maybe next time:...",
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
			bgName = "star_level_bg_113",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601050,
			say = "Were you going to throw a tea party?",
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
			actor = 401230,
			side = 2,
			bgName = "star_level_bg_113",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Not quite. Javelin invited us to attend the Royal Navy's tea party.",
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
			bgName = "star_level_bg_113",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601050,
			say = "I see, I see! That sounds fun! Have a good time over there, Maestrale!",
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
			bgName = "star_level_bg_113",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601040,
			say = "Th-thank you...",
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
			bgName = "bg_story_task",
			say = "Office - Soon afterwards",
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
			}
		},
		{
			expression = 6,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601050,
			say = "Heh heh, Libeccio's secretary operation was a huge success!",
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
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601050,
			say = "I did a good job with my work, and I even got to help Maestrale make friends! Libeccio is super awesome!",
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
					content = "\"You sure are, Libeccio~\"",
					flag = 1
				},
				{
					content = "\"Brava, Libeccio!\"",
					flag = 2
				}
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601050,
			say = "Ehehe... I'll go make some tea for you, Commander~",
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
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601050,
			say = "Here you go, your very last cup of Secretary Libeccio's tea!",
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
			bgName = "bg_story_task",
			say = "Seeing Libeccio's time as secretary come to an end was a little bittersweet, but I was proud of how much she had grown during this short time.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			bgName = "bg_story_task",
			say = "I bring the cup of tea that was just served to me to my lips...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "Cold. The tea bag had been steeped in cold water...",
					flag = 1
				}
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601050,
			say = "Ehh? Did I mess up?! I'm so sorry!",
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
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601050,
			say = "Wh-wh-what should I:? We're out of tea bags... I'm sorry–!",
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
			blackBg = True,
			side = 2,
			bgName = "bg_story_task",
			say = "Having that said, she still has a lot more growing to:––",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		}
	}
}
