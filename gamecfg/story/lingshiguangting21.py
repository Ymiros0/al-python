return {
	fadeOut = 1.5,
	mode = 2,
	id = "LINGSHIGUANGTING21",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			actor = 299020,
			side = 2,
			bgName = "bg_camelot_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Yes. This is just after I'd reached the teleporter.",
			bgm = "theme-camelot",
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
			},
			effects = {
				{
					active = True,
					name = "jinguang"
				},
				{
					active = True,
					name = "memoryFog"
				}
			}
		},
		{
			actor = 299020,
			side = 2,
			bgName = "bg_camelot_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "\"So this is Camelot. The Mirror Sea beyond the gate, hidden within Scapa Flow...\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			painting = {
				alpha = 0.3,
				time = 1
			},
			effects = {
				{
					active = False,
					name = "jinguang"
				}
			}
		},
		{
			actor = 299020,
			side = 2,
			bgName = "bg_camelot_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "\"And this seems to be the device that 'links it to other areas.' Must be a teleporter of some kind.\"",
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
			bgName = "bg_camelot_1",
			say = "She paid no mind to the gorgeous greenery around her and instead went straight into the castle hall, as if led by an invisible hand.",
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
			actor = 299020,
			side = 2,
			bgName = "bg_camelot_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "\"Coordinates? Did Her Majesty leave these? ...No, I know where these will take me.\"",
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
			actor = 299020,
			side = 2,
			bgName = "bg_camelot_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "\"Somewhere in this place is a lead on a cure. And I'm going to find it...\"",
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
			actor = 299020,
			side = 2,
			bgName = "bg_camelot_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "I'm never making the same mistake again. Your visions will not lead me astray.",
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
			actor = 299020,
			side = 2,
			bgName = "bg_camelot_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "I am Monarch! I am excellence given form!",
			effects = {
				{
					active = True,
					name = "speed"
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
			stopbgm = True,
			mode = 1,
			blackBg = True,
			effects = {
				{
					active = False,
					name = "speed"
				}
			},
			effects = {
				{
					active = False,
					name = "memoryFog"
				}
			},
			effects = {
				{
					active = True,
					name = "jinguang"
				}
			},
			sequence = {
				{
					"",
					2
				}
			}
		}
	}
}
