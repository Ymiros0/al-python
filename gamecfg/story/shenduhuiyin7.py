return {
	fadeOut = 1.5,
	mode = 2,
	id = "SHENDUHUIYIN7",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			bgm = "bgm-cccp3",
			side = 2,
			bgName = "bg_deepecho_2",
			say = "The sudden blaring of sirens interrupted the banter between the two ships.",
			dir = 1,
			bgmDelay = 1,
			soundeffect = "event./ui/alarm",
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
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			actor = 718010,
			side = 2,
			bgName = "bg_deepecho_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "What's happening?!",
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
			expression = 6,
			side = 2,
			bgName = "bg_deepecho_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 701090,
			say = "Kronshtadt! We're picking up Siren signatures! They're headed our way!",
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
					y = 0,
					delay = 0,
					dur = 0.4,
					x = 30,
					number = 2
				}
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "bg_deepecho_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 718010,
			say = "How many? Volga, have you sent out any recons yet?",
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
			actor = 707010,
			side = 2,
			bgName = "bg_deepecho_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "I have! I'll try to get some more out in a moment–",
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
			actor = 707010,
			side = 2,
			bgName = "bg_deepecho_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "It seems there's only a handful of them. What's more, they:n't appear to have their course set on us – we just happen to be in their path.",
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
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "bg_deepecho_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 707010,
			say = "I believe our mass-produced ships stationed at the research base will be enough to deal with them.",
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
			bgName = "bg_deepecho_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 718010,
			say = "Most likely. Still, we ought to eliminate them ourselves. Think of it as a warmup.",
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
			actor = 705060,
			side = 2,
			bgName = "bg_deepecho_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Warmup for what?",
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
			bgName = "bg_deepecho_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 718010,
			say = "Our objective – that Siren relic – is bound to have more than a handful of Sirens guarding it, so why not test our tactics in a comparatively safe environment?",
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
			bgName = "bg_deepecho_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 701090,
			say = "She's right, you know! We need to get into the swing of fighting while defending the Suliko!",
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
			bgName = "bg_deepecho_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 707010,
			say = "Kiev and I agree wholeheartedly! I'll keep my planes on them so we:n't lose track of–",
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
			side = 2,
			nameColor = "#a9f548",
			bgName = "bg_deepecho_3",
			hidePaintObj = True,
			dir = 1,
			actorName = "Volga",
			say = "Hey... Everyone, look at the sky!",
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
			bgName = "bg_deepecho_3",
			say = "The girls gathered on the deck looked up and saw a night sky with curtains of silver-blue light slowly fluttering high above.",
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
			side = 2,
			nameColor = "#a9f548",
			bgName = "bg_deepecho_3",
			hidePaintObj = True,
			dir = 1,
			actorName = "Soobrazitelny",
			say = "An aurora! What a spectacular and rare sight!",
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
			side = 2,
			nameColor = "#a9f548",
			bgName = "bg_deepecho_3",
			hidePaintObj = True,
			dir = 1,
			actorName = "Kiev",
			say = "Agreed...",
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
			side = 2,
			nameColor = "#a9f548",
			bgName = "bg_deepecho_3",
			hidePaintObj = True,
			dir = 1,
			actorName = "Soobrazitelny",
			say = "Say, Kiev, believe it or not, but I have a question for you! Do you know how auroras are formed?",
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
			side = 2,
			nameColor = "#a9f548",
			bgName = "bg_deepecho_3",
			hidePaintObj = True,
			dir = 1,
			actorName = "Soobrazitelny",
			say = "This is admittedly a gap in my knowledge and I thought, \"Hey, Kiev is the quiet type, so she likely knows more than she lets on!\"",
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
			side = 2,
			nameColor = "#a9f548",
			bgName = "bg_deepecho_3",
			hidePaintObj = True,
			dir = 1,
			actorName = "Kiev",
			say = "...That's a stereotype about introverts. Quiet people aren't always smart.",
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
			side = 2,
			nameColor = "#a9f548",
			bgName = "bg_deepecho_3",
			hidePaintObj = True,
			dir = 1,
			actorName = "Soobrazitelny",
			say = "Shh! The genius mechanic asked you a question! What you just gave me is not an answer, but a sidenote!",
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
			side = 2,
			nameColor = "#a9f548",
			bgName = "bg_deepecho_3",
			hidePaintObj = True,
			dir = 1,
			actorName = "Kiev",
			say = "...It so happens I: know. Auroras are the result of fast-moving charged particles from the sun colliding with air particulars in the planet's magnetic field. Does that make sense to you?",
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
			side = 2,
			nameColor = "#a9f548",
			bgName = "bg_deepecho_3",
			hidePaintObj = True,
			dir = 1,
			actorName = "Volga",
			say = "The explanation is lost on me, I'm afraid. All I know is these lights are gorgeous~ I should make a wish to the aurora!",
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
			bgName = "bg_deepecho_3",
			say = "Volga put her hands together and whispered a wish to the sky.",
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
			side = 2,
			nameColor = "#a9f548",
			bgName = "bg_deepecho_3",
			hidePaintObj = True,
			dir = 1,
			actorName = "Volga",
			say = "(Please, watch over my friends and let our mission here go without a hitch.)",
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
			side = 2,
			bgName = "bg_deepecho_3",
			dir = 1,
			blackBg = True,
			say = "At that exact moment, the Suliko's sensors picked up a distress signal from an unknown source...",
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
