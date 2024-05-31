return {
	fadeOut = 1.5,
	mode = 2,
	id = "SHENDUHUIYIN10",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			expression = 2,
			side = 2,
			bgName = "bg_underwater",
			dir = 1,
			bgm = "battle-deepecho",
			actor = 701090,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "Good day my fellow crewmates, this is Captain Soobrazitelny speaking. We're now at a depth of 500 meters and will arrive at the objective shortly!",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 705060,
			say = "500 meters... That's crazy when you think about it.",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 705060,
			say = "Speaking of crazy, did our favorite genius mechanic really get promoted to captain by piloting it for a short while?",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 718010,
			say = "Let her have her fun. You know how she is – when she finds a shiny new toy to play with, she becomes fixated on it.",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 718010,
			say = "Captain Soobrazitelny,: you have a read on the meteorite's exact location yet?",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 701090,
			say = "I'm picking up some sort of reading, but I can't tell you where it's coming from with all our sensors going haywire!",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "It seems we're not making much progress...",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 718010,
			say = "I anticipated our sensors would start acting up the deeper:wn we went, but not to THIS extent.",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "And with our radio connection to the base severed, we're as good as dead if disaster strikes.",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "...Wait a moment. Comms not working, sensors malfunctioning... You've gotta be kidding me.",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 718010,
			say = "Soobrazitelny! Switch the sub over to soundless mode right now! Bash any sound-producing equipment into silence if you must, just: it!",
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
			actor = 701090,
			side = 2,
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Why would I:... Oh! We're in a Mirror Sea?! I'm on it!",
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
			bgName = "bg_underwater",
			say = "A few hectic moments later...",
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
			},
			painting = {
				alpha = 0.3,
				time = 1
			}
		},
		{
			expression = 6,
			side = 2,
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 701090,
			say = "There are submarine-type Sirens straight above us... Have they always been able to operate at depths this great?!",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 718010,
			say = "It's possible, but: we couldn't have known since nobody's gone this deep in a vessel before.",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Think about that – that's invaluable intel. Even if we turn back right now, we won't be leaving empty-handed.",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Even so, what are the implications of a Siren presence:wn here? Did they finally decide to retrieve the meteorite?",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 705060,
			say = "They could be, which would be really bad news.",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "With no armaments on this sub to speak of, there's not much we can: about it either.",
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
			actor = 701100,
			side = 2,
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Won't we be fine if we just go back up and fight them on the surface?",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 718010,
			say = "Not happening. If they spot us while we're resurfacing, it's all over.",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Hmm... Soobrazitelny, what equipment did we lose in the process of you breaking them?",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 718010,
			say = "Choose something that's fragile and buoyant. I'm thinking we can eject something through the sub's stern,: make our escape while the Sirens are distracted by it.",
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
			bgName = "bg_underwater",
			say = "Kronshtadt looked at Soobrazitelny and proposed to her a desperate, daring plan.",
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
			bgName = "bg_underwater",
			say = "Caught 500 meters beneath the surface with enemies all around, the pressure was bearing:wn on the girls...",
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
			bgName = "bg_underwater",
			say = "A few hectic moments later...",
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
			expression = 3,
			side = 2,
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 718010,
			say = "Do you think they've gone away yet?",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Who can say? Our equipment's only quiet because it's broken.",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 718010,
			say = "We can't stall our engines forever at this depth, and we're going to run out of oxygen eventually if we:n't get away from those damn Sirens.",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 718010,
			say = "My decoy plan is by no means foolproof, but all we can: is pray that it works...",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 701090,
			say = "Picking up Siren movements! I think... Yes, those submarines from before are resurfacing!",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Do you think they took the bait? Phew...",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 707010,
			say = "Thank goodness... I was so sure we were:ne for...!",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "You did well by staying calm, Volga. And by keeping Kiev's and our Captain's spirits up.",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 718010,
			say = "The crisis is over now, but we can't simply resurface here or we'll run right into Sirens again.",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 718010,
			say = "So here's what we're going to: - continue the search. They'll be hesitant to fire torpedoes at us as long as we stay close to the meteorite survey site.",
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
			actor = 701090,
			side = 2,
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Ooh, clever! And if they try it anyway, we'll just ram them into oblivion!",
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
			bgName = "bg_underwater",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 701100,
			say = "Did you hit yourself on the head? Heck no, we're not:ing that.",
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
			bgName = "bg_underwater",
			dir = 1,
			blackBg = True,
			actor = 701090,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "Hey, I'm just messing with you! I'm not dumb! Anyway, let's get this mission back on track!",
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
