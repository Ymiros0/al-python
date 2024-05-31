return {
	id = "ZHANFANGYUHUIGUANGZHICHENG20",
	mode = 2,
	fadeOut = 1.5,
	scripts = {
		{
			actor = 0,
			side = 2,
			nameColor = "#5CE6FF",
			hidePaintObj = True,
			say = "Is this... that same space again?",
			blackBg = True,
			bgm = "story-startravel",
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
			effects = {
				{
					active = True,
					name = "juqing_mengjing"
				}
			}
		},
		{
			actor = 0,
			side = 2,
			nameColor = "#5CE6FF",
			blackBg = True,
			say = "Miss D says I got lost when I came in here, but... I think this might be the narrow gap between life and death.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#5CE6FF",
			side = 2,
			blackBg = True,
			say = "(I must've been brought here after I'd died – before the black tornado could corrode me.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#5CE6FF",
			side = 2,
			blackBg = True,
			say = "The foam still covers my mind, protecting my \"self\".",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			nameColor = "#BDBDBD",
			actor = 9705050,
			dir = 1,
			blackBg = True,
			actorName = "???",
			say = "...Back again, \"I\" see.",
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
			nameColor = "#5CE6FF",
			recallOption = True,
			blackBg = True,
			say = "......",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "Who are you?",
					flag = 1
				},
				{
					content = "Where am I?",
					flag = 2
				},
				{
					content = "Am I the only one here?",
					flag = 3
				}
			}
		},
		{
			actor = 9705050,
			nameColor = "#BDBDBD",
			blackBg = True,
			side = 2,
			dir = 1,
			optionFlag = 1,
			actorName = "???",
			say = "A meaningless question.",
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
			actor = 9705050,
			nameColor = "#BDBDBD",
			blackBg = True,
			side = 2,
			dir = 1,
			optionFlag = 2,
			actorName = "???",
			say = "Nowhere.",
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
			actor = 9705050,
			nameColor = "#BDBDBD",
			blackBg = True,
			side = 2,
			dir = 1,
			optionFlag = 3,
			actorName = "???",
			say = "Yes.",
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
			nameColor = "#BDBDBD",
			actor = 9705050,
			dir = 1,
			blackBg = True,
			actorName = "???",
			say = "It's \"my\" turn to ask the questions now.",
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
			nameColor = "#BDBDBD",
			actor = 9705050,
			dir = 1,
			blackBg = True,
			actorName = "???",
			say = "Do you know that what you've been witnessing are mere images?",
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
			nameColor = "#BDBDBD",
			actor = 9705050,
			dir = 1,
			blackBg = True,
			actorName = "???",
			say = "Foregone conclusions, all illusions, all destined to fade away.",
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
			nameColor = "#5CE6FF",
			blackBg = True,
			say = "Yeah. I know that very well.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			nameColor = "#BDBDBD",
			actor = 9705050,
			dir = 1,
			blackBg = True,
			actorName = "???",
			say = "Why struggle? Why resist? Why suffer and face death?",
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
			actor = 9705050,
			nameColor = "#BDBDBD",
			side = 2,
			actorName = "???",
			dir = 1,
			blackBg = True,
			say = "What meaning is there to all of it?",
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
			nameColor = "#5CE6FF",
			blackBg = True,
			say = "Well... It's something only I can:. Doesn't matter if it's real or not.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			nameColor = "#5CE6FF",
			blackBg = True,
			say = "I follow my heart, stick to my sincere beliefs, and: what I must:.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			nameColor = "#5CE6FF",
			blackBg = True,
			say = "What:es the meaning matter, as long as I understand it? If I must, I can share it with someone else.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			nameColor = "#5CE6FF",
			blackBg = True,
			say = "I think there's inherent meaning in treading a path you believe in.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			nameColor = "#5CE6FF",
			blackBg = True,
			say = "Even if it seems meaningless at a glance, nobody knows what effects it might lead to.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 9705050,
			nameColor = "#BDBDBD",
			side = 2,
			actorName = "???",
			dir = 1,
			blackBg = True,
			say = "...Answer received.",
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
			nameColor = "#BDBDBD",
			actor = 9705050,
			dir = 1,
			blackBg = True,
			actorName = "???",
			say = "You're still under the illusion that you can change established reality.",
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
			nameColor = "#5CE6FF",
			blackBg = True,
			say = "Recently, somebody told me, \"Reality and truth are not always one and the same. Reality can only be truth if enough faith goes into it.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			nameColor = "#5CE6FF",
			blackBg = True,
			say = "I've spent a long time trying to figure out what that means...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			nameColor = "#5CE6FF",
			blackBg = True,
			say = "But now, it makes perfect sense.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			nameColor = "#BDBDBD",
			actor = 9705050,
			dir = 1,
			blackBg = True,
			actorName = "???",
			say = "What? That all vain effort will be rewarded?",
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
			nameColor = "#5CE6FF",
			blackBg = True,
			say = "No. It means that you can't always accept reality as the truth.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			nameColor = "#5CE6FF",
			blackBg = True,
			say = "If something:esn't exist in my memory,: it may be truth to others, but it isn't necessarily truth to me.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			nameColor = "#5CE6FF",
			blackBg = True,
			say = "Reality may be set in stone for all I care, but if you:n't accept it as the truth,: it isn't your truth.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			nameColor = "#5CE6FF",
			blackBg = True,
			say = "No matter the situation, no matter the established premise...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			nameColor = "#5CE6FF",
			blackBg = True,
			say = "Until I, as an individual, experience something, make decisions, and see things to their conclusion...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			nameColor = "#5CE6FF",
			blackBg = True,
			say = "I won't accept it as the truth.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			nameColor = "#5CE6FF",
			blackBg = True,
			say = "So I'm going to fight for the sake of my truth.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			nameColor = "#5CE6FF",
			blackBg = True,
			say = "If that sounds like a vain effort to you, well, too bad. That's not enough reason for me to give up.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "star_level_bg_103",
			say = "When the light fades, I see the shadows of trees.",
			bgm = "story-2",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			flashout = {
				black = False,
				dur = 1,
				alpha = {
					0,
					1
				}
			},
			flashin = {
				delay = 1,
				dur = 1,
				black = False,
				alpha = {
					1,
					0
				}
			},
			effects = {
				{
					active = False,
					name = "juqing_mengjing"
				}
			}
		},
		{
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			say = "The warm light shining through the leaves, the scent of flowers, the sounds of baby birds... An incredibly peaceful scene.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			say = "Next to me on this bench is a girl dressed in the style of the Royal Navy. In the space between us sits a small box of sweets.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "star_level_bg_103",
			actorName = "Rodney",
			dir = 1,
			actor = 9705050,
			nameColor = "#BDBDBD",
			hidePaintObj = True,
			say = "Mmm... This is such a nice place.",
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
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "Do you know where we are?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "star_level_bg_103",
			actorName = "Rodney",
			dir = 1,
			actor = 9705050,
			nameColor = "#BDBDBD",
			hidePaintObj = True,
			say = "You're asking \"me\"?",
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
			actor = 9705050,
			nameColor = "#BDBDBD",
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			dir = 1,
			actorName = "Rodney",
			side = 2,
			say = "This is a place that you constructed, that you interpreted, that you wished for.",
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
			actorName = "Rodney",
			dir = 1,
			actor = 9705050,
			nameColor = "#BDBDBD",
			hidePaintObj = True,
			say = "It is your \"end.\"",
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
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "My... end?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "I:n't understand. What happened, and how did I end up here?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 9705050,
			nameColor = "#BDBDBD",
			bgName = "star_level_bg_103",
			hidePaintObj = True,
			dir = 1,
			actorName = "Rodney",
			side = 2,
			say = "You:n't, but \"I\":.",
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
			actorName = "Rodney",
			dir = 1,
			actor = 9705050,
			nameColor = "#BDBDBD",
			hidePaintObj = True,
			say = "You must go.",
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
			actorName = "Rodney",
			dir = 1,
			actor = 9705050,
			nameColor = "#BDBDBD",
			hidePaintObj = True,
			say = "Go back to your battlefield. Continue your vain struggle.",
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
			bgName = "bg_white",
			nameColor = "#BDBDBD",
			dir = 1,
			actor = 9705050,
			actorName = "Rodney",
			say = "\"I'll\" be watching you, Commander.",
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			flashout = {
				black = False,
				dur = 1,
				alpha = {
					0,
					1
				}
			},
			flashin = {
				delay = 1,
				dur = 1,
				black = False,
				alpha = {
					1,
					0
				}
			}
		}
	}
}
