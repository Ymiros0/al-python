return {
	fadeOut = 1.5,
	mode = 2,
	id = "SHISHANGTEKANHEDINGJIER2",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"Port Fashion Collection! Part 2\n\n<size=45>2 Sojourn Through Clear Seas</size>",
					1
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_106",
			hidePaintObj = True,
			say = "On Unzen's invitation, I've come to the beach. We gaze at the calm seas together, enjoying the tranquility.",
			bgm = "story-richang-7",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 303191,
			side = 2,
			bgName = "star_level_bg_106",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			live2d = "main1",
			say = "Here, Commander, have some tea.",
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
			actor = 303191,
			side = 2,
			bgName = "star_level_bg_106",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			live2d = True,
			say = "...Oh, you find its taste lacking? I thought the leaves had sufficiently infused the water, so I strained them in advance...",
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
			actor = 303191,
			side = 2,
			bgName = "star_level_bg_106",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			live2d = "headtouch",
			say = "It seems this had the opposite effect of what I intended...",
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
			actor = 303191,
			side = 2,
			bgName = "star_level_bg_106",
			live2d = True,
			withoutActorName = True,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "That's not strictly True. I tell her that the aftertaste definitely makes me think of her.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 303191,
			side = 2,
			bgName = "star_level_bg_106",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			live2d = True,
			say = "Heehee. That makes me feel better. Thank you.",
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
			actor = 303191,
			side = 2,
			bgName = "star_level_bg_106",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			live2d = "mission_complete",
			say = "Now, why:n't you come and lie:wn beside me? The view is quite different here.",
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
					content = "But what if I fall into the water?",
					flag = 1
				},
				{
					content = "Wouldn't it be pretty cramped, though?",
					flag = 2
				}
			}
		},
		{
			live2d = "main2",
			side = 2,
			bgName = "star_level_bg_106",
			dir = 1,
			optionFlag = 1,
			actor = 303191,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "You need not worry about that. I promise you it won't happen.",
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
			live2d = True,
			side = 2,
			bgName = "star_level_bg_106",
			dir = 1,
			optionFlag = 1,
			actor = 303191,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Oh, but if you: wish to swim in the deep blue, I will gladly join you.",
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
			live2d = True,
			side = 2,
			bgName = "star_level_bg_106",
			dir = 1,
			optionFlag = 1,
			actor = 303191,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "That sounds like it could be fun. Unless you'd prefer to swim alone, that is?",
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
			live2d = "main2",
			side = 2,
			bgName = "star_level_bg_106",
			dir = 1,
			optionFlag = 2,
			actor = 303191,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "You think so? I think there's plenty of space for both of us if you:n't mind our skins touching.",
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
			live2d = True,
			side = 2,
			bgName = "star_level_bg_106",
			dir = 1,
			optionFlag = 2,
			actor = 303191,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Granted, that is a big if... Maybe that IS something you'd prefer to avoid?",
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
			actor = 303191,
			side = 2,
			bgName = "star_level_bg_106",
			live2d = True,
			withoutActorName = True,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I:n't want her to jump to any more conclusions, so I shrug and sit:wn in the hammock. Immediately, my nose picks up a saline breeze and a pure scent coming from Unzen.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 303191,
			side = 2,
			bgName = "star_level_bg_106",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			live2d = "mission",
			say = "Thank you, truly, for indulging this wanderer today, Commander.",
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
			actor = 303191,
			side = 2,
			bgName = "star_level_bg_106",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			live2d = True,
			say = "You know, I've known you for a while now, and thoughts of you always come to mind whenever I go wandering.",
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
			actor = 303191,
			side = 2,
			bgName = "star_level_bg_106",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			live2d = "main2",
			say = "If the fates permitted it, I would freely walk the lands for years with only you by my side... Of course, that's not going to happen.",
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
			actor = 303191,
			side = 2,
			bgName = "star_level_bg_106",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			live2d = True,
			say = "But, even being with you for a few hours still makes me feel unbelievably fulfilled.",
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
			actor = 303191,
			side = 2,
			bgName = "star_level_bg_106",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			live2d = True,
			say = "...Oh, please, there's no need to be sorry.",
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
			actor = 303191,
			side = 2,
			bgName = "star_level_bg_106",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			live2d = True,
			say = "It's just a pipe dream of mine. I know you cannot abscond your role in protecting the world's lanes.",
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
			actor = 303191,
			side = 2,
			bgName = "star_level_bg_106",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			live2d = True,
			say = "I ask only that you stay True to your duty until we can enjoy True, lasting peace.",
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
					content = "One day, I'll make your dream come True.",
					flag = 1
				}
			}
		},
		{
			actor = 303191,
			side = 2,
			bgName = "star_level_bg_106",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			live2d = "main3",
			say = "Oh, Commander...",
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
			actor = 303191,
			side = 2,
			bgName = "star_level_bg_106",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			live2d = True,
			say = "All those days I languished over what my dream is... You are the only one who can bring such a tempest to my calm heart.",
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
			actor = 303191,
			side = 2,
			bgName = "star_level_bg_106",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			live2d = True,
			say = "I will remember that promise until the end of my days.",
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
			actor = 303191,
			side = 2,
			bgName = "star_level_bg_106",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			live2d = True,
			say = "But for now, let's just enjoy this moment to ourselves...",
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
