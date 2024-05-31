return {
	fadeOut = 1.5,
	mode = 2,
	id = "WANSHENGYEDEQIYU4",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"Halloween Hijinks\n\n<size=45>4 The Witch of Hallow's Eve</size>",
					1
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_162",
			say = "I arrived at a witch's fortune-telling shop.",
			bgm = "battle-highseasfleet-reborn",
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
			bgName = "star_level_bg_162",
			say = "Witches might be \"the\" Halloween costume, but there were so many people in our port who fit that descriptor that I couldn't imagine who I'd find inside.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_162",
			say = "\"Guess I might as well just knock.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "Witch?",
			bgName = "star_level_bg_162",
			nameColor = "#A9F548FF",
			say = "Enter, pilgrim of the night.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 102162,
			side = 2,
			bgName = "star_level_bg_162",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "What brings you here at such a late time? Are you a lost soul wandering through the Halloween night?",
			hidePaintEquip = True,
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
			expression = 2,
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			hidePaintEquip = True,
			actor = 102162,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Not surprised, huh? Got a problem with me being the Witch of Hallow's Eve?",
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
			bgName = "star_level_bg_162",
			say = "All I could make out in the smoke-filled shack were a crystal ball placed on a table and Memphis, clad in a witch costume.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_162",
			say = "\"I didn't know you could see the future, Memphis.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			hidePaintEquip = True,
			actor = 102162,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "\"It's not really... Uh, I mean, of course I can! I'm a witch, after all!\"",
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
			bgName = "star_level_bg_162",
			dir = 1,
			hidePaintEquip = True,
			actor = 102162,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Lost pilgrim of the night,: you seek guidance toward your future? Or: you seek time with me?",
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
			bgName = "star_level_bg_162",
			say = "\"Well...\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			hidePaintEquip = True,
			actor = 102162,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "You need not answer. Come and sit. Place your hand on my crystal ball and reveal the future to me. I will predict your future.",
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
			actor = 102162,
			side = 2,
			bgName = "star_level_bg_162",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Oh... I see.",
			hidePaintEquip = True,
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
			bgName = "star_level_bg_162",
			dir = 1,
			hidePaintEquip = True,
			actor = 102162,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "There it is. If the crystal ball says so,: I have no choice but to accept it.",
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
					content = "\"What did the crystal ball show you?\"",
					flag = 1
				},
				{
					content = "\"Is it good or bad?\"",
					flag = 2
				}
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			optionFlag = 1,
			hidePaintEquip = True,
			actor = 102162,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "It reveals a vision of you, Commander, spending Halloween night with a certain shipgirl.",
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
			bgName = "star_level_bg_162",
			dir = 1,
			optionFlag = 2,
			hidePaintEquip = True,
			actor = 102162,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "It's neither, really. Commander, the ball tells me that you'll spend the night with a certain shipgirl.",
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
			bgName = "star_level_bg_162",
			say = "\"Which shipgirl...?\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			hidePaintEquip = True,
			actor = 102162,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Me, of course...is what I'd like to say. But unfortunately, it's not.",
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
			bgName = "star_level_bg_162",
			say = "\"I thought your fortune-telling was just another Halloween attraction.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 102162,
			side = 2,
			bgName = "star_level_bg_162",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "You're not wrong, but to be more precise, it's an attraction with a hint of reality.",
			hidePaintEquip = True,
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
			bgName = "star_level_bg_162",
			dir = 1,
			hidePaintEquip = True,
			actor = 102162,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Here. Take this.",
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
			bgName = "star_level_bg_162",
			say = "Memphis handed me a witch's hat.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 102162,
			side = 2,
			bgName = "star_level_bg_162",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Take a broom with you, too. It'll:uble as a self-defense weapon, which you might just need.",
			hidePaintEquip = True,
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
			bgName = "star_level_bg_162",
			say = "\"I:n't understand. What the heck did you see in my future?\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			hidePaintEquip = True,
			actor = 102162,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "The shipgirl you'll be with can be a little difficult. Trust me, you'll be better off with this.",
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
			bgName = "star_level_bg_162",
			say = "\"A shipgirl you'd call 'difficult'? I can't tell if I know who you're talking about or not...\"",
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
			actor = 102162,
			side = 2,
			bgName = "star_level_bg_162",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "I saw her just a while ago. Beats me how she snuck a real weapon into the party venue.",
			hidePaintEquip = True,
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
			bgName = "star_level_bg_162",
			say = "\"A real weapon...? If she got past the bag check with a weapon,: that's a real emergency. Did the Sirens: this?!\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			hidePaintEquip = True,
			actor = 102162,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "You will need to check on her, but it's hardly an emergency. I wouldn't even call it dangerous. That pirate is just enjoying Halloween in her own way.",
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
			bgName = "star_level_bg_162",
			say = "\"Pirate? A pirate shipgirl? That would be...\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "star_level_bg_162",
			dir = 1,
			hidePaintEquip = True,
			actor = 102162,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Exactly. A pirate shipgirl wearing a red hat. I think you're just the man to deal with her, Commander.",
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
			bgName = "star_level_bg_162",
			say = "\"I'm curious what happened. Instead of just wandering around, I'd better go confront her directly and confirm that she's the one I'm thinking of.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		}
	}
}
