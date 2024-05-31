return {
	id = "XINGHAIZHUGUANG16",
	mode = 2,
	fadeOut = 1.5,
	scripts = {
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_starsea_core_3",
			hidePaintObj = True,
			say = "In the Sea of Stars control room, TB's battle with the hostile data raged on.",
			bgm = "theme-ucnf-beacon",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Advanced KAN-SEN Research and Planning Department",
			dir = 1,
			actor = 199030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "TB, it glowed again...",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Advanced KAN-SEN Research and Planning Department",
			dir = 1,
			actor = 199030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I'll break the glass!",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Main Terminal",
			dir = 1,
			actor = 900284,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Don't worry, Anchorage.",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Main Terminal",
			dir = 1,
			actor = 900284,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "In crisis mode, I have full control of all resources within the Sea of Stars.",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Advanced KAN-SEN Research and Planning Department",
			dir = 1,
			actor = 199030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "...Hm?",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Main Terminal",
			dir = 1,
			actor = 900284,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "In other words, there's no need for you to break the glass.",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Main Terminal",
			dir = 1,
			actor = 900284,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Status report. I've successfully isolated the hostile data within a sandbox.",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Main Terminal",
			dir = 1,
			actor = 900284,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "At this time, it is impossible to delete the data.",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Main Terminal",
			dir = 1,
			actor = 900284,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Due to the hostile data's attack on our communications system, I've taken the system offline to physically isolate it from said data.",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Main Terminal",
			dir = 1,
			actor = 900284,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "It will be impossible to leave the control room or communicate with the outside. I'm sorry.",
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
			actor = 199030,
			side = 2,
			bgName = "bg_starsea_core_3",
			factiontag = "Advanced KAN-SEN Research and Planning Department",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "It's okay. I'm right here...",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Advanced KAN-SEN Research and Planning Department",
			dir = 1,
			actor = 199030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "TB, go!",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Advanced KAN-SEN Research and Planning Department",
			dir = 1,
			actor = 199030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Fight that data!",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Advanced KAN-SEN Research and Planning Department",
			dir = 1,
			actor = 199030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I'll draw you a picture!",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Main Terminal",
			dir = 1,
			actor = 900284,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Thank you for that.",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Main Terminal",
			dir = 1,
			actor = 900284,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Question. why have you mentioned the act of drawing?",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Advanced KAN-SEN Research and Planning Department",
			dir = 1,
			actor = 199030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Huh? Don't you draw, too?",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Advanced KAN-SEN Research and Planning Department",
			dir = 1,
			actor = 199030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "You drew that on the screen. It's cute.",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Main Terminal",
			dir = 1,
			actor = 900284,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "On the screen?",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Main Terminal",
			dir = 1,
			actor = 900284,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "That is no drawing. It's simply a visual display of the affected area.",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Advanced KAN-SEN Research and Planning Department",
			dir = 1,
			actor = 199030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "But it looks like a drawing...",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Advanced KAN-SEN Research and Planning Department",
			dir = 1,
			actor = 199030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Umm... Like a beacon?",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Advanced KAN-SEN Research and Planning Department",
			dir = 1,
			actor = 199030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "And letters... U, C...",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Main Terminal",
			dir = 1,
			actor = 900284,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Beacons, letters... Synchronizing analysis module.",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Main Terminal",
			dir = 1,
			actor = 900284,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Performing visual data verification. No similar patterns found.",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Advanced KAN-SEN Research and Planning Department",
			dir = 1,
			actor = 199030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "TB... You:n't see it?",
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
			bgName = "bg_starsea_core_3",
			factiontag = "Advanced KAN-SEN Research and Planning Department",
			dir = 1,
			actor = 199030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "It's okay... I'll draw it!",
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
