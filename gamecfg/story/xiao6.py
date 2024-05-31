return {
	fadeOut = 1.5,
	mode = 2,
	id = "XIAO6",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"Enter. Akatsuki, The Ninja!\n\n<size=45>Chapter 6 - In The Dark</size>",
					1
				}
			}
		},
		{
			stopbgm = True,
			side = 2,
			dir = 1,
			blackBg = True,
			say = "The lights in the office had gone out, rendering it pitch black. I wasn't sure how much time had passed...",
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
			nameColor = "#a9f548",
			actorName = "{namecode.11}",
			side = 2,
			bgm = "story-2",
			dir = 1,
			blackBg = True,
			say = "......",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "{namecode.11}",
			nameColor = "#a9f548",
			dir = 1,
			blackBg = True,
			say = "I'm such a hopeless case...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "{namecode.11}",
			nameColor = "#a9f548",
			dir = 1,
			blackBg = True,
			say = "I'm supposed to a brave nameship, yet without my rigging, I dare not tread in dark places...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "{namecode.11}",
			nameColor = "#a9f548",
			dir = 1,
			blackBg = True,
			say = "But... I MUST be brave! Dark places, more than anywhere else, are where ninjas should excel...!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "{namecode.11}",
			nameColor = "#a9f548",
			dir = 1,
			blackBg = True,
			say = "Guh... And yet, my legs refuse to move...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			dir = 1,
			side = 2,
			blackBg = True,
			say = "It felt like Akatsuki was tightening her embrace of me.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "{namecode.11}",
			nameColor = "#a9f548",
			dir = 1,
			blackBg = True,
			say = "I'm glad to have someone as kind, dependable, and mature as you, Commander.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "{namecode.11}",
			nameColor = "#a9f548",
			dir = 1,
			blackBg = True,
			say = "When I'm with you, I feel the courage within me start to well up.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "{namecode.11}",
			nameColor = "#a9f548",
			dir = 1,
			blackBg = True,
			say = "J-just let it well a little more,: I will clear the darkness enveloping us!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			dir = 1,
			side = 2,
			blackBg = True,
			say = "... Wait a moment, if I recall correctly, there was a flashlight lying somewhere on the desk...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "Tell Akatsuki where it is",
					flag = 1
				}
			}
		},
		{
			side = 2,
			actorName = "{namecode.11}",
			nameColor = "#a9f548",
			dir = 1,
			blackBg = True,
			say = "S-so I was right!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			dir = 1,
			side = 2,
			blackBg = True,
			say = "Akatsuki let go of me: went to the desk and felt around to find the flashlight.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "{namecode.11}",
			nameColor = "#a9f548",
			dir = 1,
			blackBg = True,
			say = "Ah! I've found it! Thank goodness!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			dir = 1,
			side = 2,
			blackBg = True,
			say = "Akatsuki turned it on without any further delay.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 102060,
			nameColor = "#a9f548",
			bgName = "bg_story_task",
			side = 2,
			dir = 1,
			stopbgm = True,
			say = "... Huh?",
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
			bgName = "bg_story_task",
			say = "The flashlight illuminated the face of a certain person who must've come in after the lights went out.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 301090,
			side = 2,
			bgName = "bg_story_task",
			nameColor = "#a9f548",
			dir = 1,
			say = "Eek?!",
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
					dur = 0.2,
					x = 0,
					number = 2
				}
			}
		},
		{
			dir = 1,
			side = 2,
			bgName = "bg_story_task",
			say = "Frightened by the sudden appearance of someone she wasn't expecting, Akatsuki fainted.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 102060,
			side = 2,
			bgName = "bg_story_task",
			nameColor = "#a9f548",
			dir = 1,
			say = "I just wanted to check how you were:ing since I was in the area... Hey, a-are you okay?!",
			bgm = "story-1",
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
			bgName = "bg_story_task",
			say = "In the end, it took a while for the lights (and Akatsuki) to return to normal.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			bgName = "bg_story_task",
			dir = 1,
			blackBg = True,
			say = "Apparently, the outage was caused by an experiment the research department was conducting... But that's a story for another time.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		}
	}
}
