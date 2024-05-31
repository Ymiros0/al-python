return {
	fadeOut = 1.5,
	mode = 2,
	id = "PIANRUOFEIXIAN1",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"Like a Soaring Apsaras\n\n<size=45>1 Like a Soaring Apsaras</size>",
					1
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			say = "I was trudging along a stream running through the mountains–",
			bgmDelay = 2,
			bgm = "theme-haitian-soft-loop",
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
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			say = "When suddenly, the melody of a pipa echoes around me. Its soothing tones seem to permeate me, melting away the fatigue of my long trek.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			say = "I continue on towards an open area, eventually reaching the destination Hai Tien and I had agreed upon previously.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 502072,
			side = 2,
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Commander, I appreciate you coming all the way out here.",
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
			expression = 5,
			side = 2,
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502072,
			say = "I've been waiting for you. The tea is ready, so let me get it for you right away.",
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
					content = "\"Thanks a bunch.\"",
					flag = 1
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			say = "\"By the way, I heard the sound of a pipa earlier...\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 9,
			side = 2,
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502072,
			say = "Oh, umm... I was just getting some practice in. I didn't think anyone would be able to hear it...",
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
			expression = 6,
			side = 2,
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502072,
			say = "I originally was planning a surprise performance for you, but you'll have to forgive me for fumbling it.",
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
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502072,
			say = "...Hm? Hearing me play was enough to make your fatigue melt away?",
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
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502072,
			say = "Ahaha... You:n't have to go out of your way to console me...",
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
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502072,
			say = "(Ugh... I was so preoccupied with creating the right atmosphere for our date that I didn't consider how tiring the trek up here would be....)",
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
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502072,
			say = "But, if my music was enough to make you feel better, I am relieved to hear that.",
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
			actor = 502072,
			side = 2,
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "In any case, Commander, I called you here today because I wanted to show you the dance that I've been practicing for quite some time now.",
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
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502072,
			say = "It's called the \"Soaring Apsaras\"– an acrobatic combination of dance and music. I: hope you'll find it to your liking.",
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
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502072,
			say = "...Hmm? Was there something you wanted to ask me, Commander?",
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
					content = "\"What kind of music are you going to perform?\"",
					flag = 1
				},
				{
					content = "\"Can you tell me more about this dance?\"",
					flag = 2
				},
				{
					content = "\"Why did you choose this place?\"",
					flag = 3
				}
			}
		},
		{
			expression = 9,
			side = 2,
			bgName = "star_level_bg_500",
			dir = 1,
			optionFlag = 1,
			actor = 502072,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "It's a bit embarrassing to say this... But it's my original composition.",
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
			bgName = "star_level_bg_500",
			dir = 1,
			optionFlag = 1,
			actor = 502072,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Ever since I first met you, each and every day has been filled with joy and excitement. Before I knew it, you became the first and foremost thing on my mind.",
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
			bgName = "star_level_bg_500",
			dir = 1,
			optionFlag = 1,
			actor = 502072,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I can't: anything about these overflowing feelings, but I at least want to put them:wn in song form... Hopefully, you won't find it strident to your ears...",
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
			bgName = "star_level_bg_500",
			dir = 1,
			optionFlag = 2,
			actor = 502072,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Commander, you should already know that I'm not very athletic.",
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
			bgName = "star_level_bg_500",
			dir = 1,
			optionFlag = 2,
			actor = 502072,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "But this time, I'm going to overcome my limits. Just thinking about performing in front of you makes all the difficult hours of practice feel like a distant memory.",
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
			actor = 502072,
			side = 2,
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			dir = 1,
			optionFlag = 2,
			nameColor = "#A9F548FF",
			say = "Who knows? Maybe I'll be able to capture that same feeling you felt when you heard the sound of the pipa~",
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
			bgName = "star_level_bg_500",
			dir = 1,
			optionFlag = 2,
			actor = 502072,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Heehee. In any case, you're the reason why I'm able to show these things to you today.",
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
			bgName = "star_level_bg_500",
			dir = 1,
			optionFlag = 3,
			actor = 502072,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "In the mountains, the stream burbles beneath the shade of great willows. The flowers are in full bloom, and the wind is refreshing.",
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
			bgName = "star_level_bg_500",
			dir = 1,
			optionFlag = 3,
			actor = 502072,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "When music reverberates, everything becomes more melodious and magnificent. My performance: blends into the scenery all around us, creating a dreamlike, mesmerizing mixture of movement and stillness.",
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
			bgName = "star_level_bg_500",
			dir = 1,
			optionFlag = 3,
			actor = 502072,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "But to be entirely honest, the beautiful scenery around us probably compensates for the inadequacies in my performance. Please bear with me, Commander.",
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
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502072,
			say = "Now:, relax and take a deep breath, and: we'll get started–",
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
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			say = "Sometimes as violent as a sudden hurricane in the summer, at other times as gentle as a newborn's breaths... The sound of the pipa, along with the stream flowing right next to me, seemed like reminders from the heavens to leave behind the material world.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			say = "I can't take my eyes off Hai Tien. It's as if I had stepped into a fairyland depicted in a storybook.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 502072,
			side = 2,
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "How was it, Commander?",
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
			},
			options = {
				{
					content = "\"Simply spectacular...\"",
					flag = 1
				}
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502072,
			say = "I'm so glad to hear that! All my hard work has finally paid off!",
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
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502072,
			say = "Oh, um... Ahem, sorry I got carried away there. Please forget you saw that...",
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
			expression = 6,
			side = 2,
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502072,
			say = "If you:n't mind, would you mind staying here with me a bit longer?",
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
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502072,
			say = "Since you already came all the way up here, why not enjoy a cup of tea while taking in the scenery?",
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
					content = "\"Do you think I could learn that dance?\"",
					flag = 1
				},
				{
					content = "\"Woah, so that's how you play the pipa!\"",
					flag = 2
				}
			}
		},
		{
			expression = 6,
			side = 2,
			bgName = "star_level_bg_500",
			dir = 1,
			optionFlag = 1,
			actor = 502072,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "...Huh? Wh-what did you just say?!",
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
			expression = 5,
			side = 2,
			bgName = "star_level_bg_500",
			dir = 1,
			optionFlag = 1,
			actor = 502072,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I'd be honored to teach you if you really are interested in learning!",
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
			expression = 9,
			side = 2,
			bgName = "star_level_bg_500",
			dir = 1,
			optionFlag = 1,
			actor = 502072,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Though, um, I'm not sure I'd be able to: a good job getting the point across with words alone...",
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
			bgName = "star_level_bg_500",
			hidePaintObj = True,
			optionFlag = 1,
			say = "Hai Tien suddenly shoots up and slides over to my side.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "star_level_bg_500",
			dir = 1,
			optionFlag = 1,
			actor = 502072,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Ah, umm... this is just to teach you the dance moves...",
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
			bgName = "star_level_bg_500",
			dir = 1,
			optionFlag = 1,
			actor = 502072,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Now:, please excuse me–",
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
			bgName = "star_level_bg_500",
			dir = 1,
			optionFlag = 2,
			actor = 502072,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Oh my, you've picked up on it so quickly. As expected of someone as accomplished as you, Commander.",
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
			bgName = "star_level_bg_500",
			dir = 1,
			optionFlag = 2,
			actor = 502072,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "That being the case, allow me to make a suggestion–",
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
			bgName = "star_level_bg_500",
			dir = 1,
			optionFlag = 2,
			actor = 502072,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "How about you improvise a melody, and I'll dance to it? Only if you're up for it, that is.",
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
			bgName = "star_level_bg_500",
			dir = 1,
			optionFlag = 2,
			actor = 502072,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Since you're improvising,:n't worry if you make any minor mistakes. In fact, I... I'd prefer it if you could keep your eyes on me...",
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
			bgName = "star_level_bg_500",
			dir = 1,
			optionFlag = 2,
			actor = 502072,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Oh, but having that said...",
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
			bgName = "star_level_bg_500",
			dir = 1,
			optionFlag = 2,
			actor = 502072,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Umm, if I stumble over my own feet and bump into you because I'm a bit of a klutz... Please:n't hold it against me, okay?",
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
