return {
	fadeOut = 1.5,
	mode = 2,
	id = "NVPUGONGDOUSANQI1",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"Fight On, Royal Maids! (Part 3)\n\n<size=45>1 The Third Exercise</size>",
					1
				}
			}
		},
		{
			hidePaintEquip = True,
			side = 2,
			bgName = "bg_story_task",
			dir = 1,
			bgm = "story-richang",
			actor = 205010,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Do you understand, Illustrious? This exercise is a sublime opportunity to gauge the strength of our latest carriers!",
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
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			effects = {
				{
					active = True,
					name = "memoryFog"
				}
			}
		},
		{
			actor = 205010,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Both sides are to consist of three carriers each, plus a small escort fleet.",
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
			actor = 205010,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "The Royal Maids did an exemplary job demonstrating the Royal Navy's excellence in the previous two exercises. You lot have a high standard to live up to, but I expect you'll: just fine!",
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
			actor = 205010,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "One last thing. As this is an aviation exercise, neither I nor the Commander will be in charge.",
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
			actor = 207030,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "...Those were Her Majesty's instructions.",
			hidePaintEquip = True,
			painting = {
				alpha = 0.3,
				time = 1
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			effects = {
				{
					active = False,
					name = "memoryFog"
				}
			}
		},
		{
			actor = 207030,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "The Royal Navy's exercise fleet will be centred around Centaur, Perseus, and Albion.",
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
			expression = 3,
			side = 2,
			bgName = "bg_story_task",
			dir = 1,
			hidePaintEquip = True,
			actor = 207030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "As for the opposing fleet, I'm told it's up to you to determine its composition, Commander.",
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
			bgName = "bg_story_task",
			say = "\"I see. It'll be hard to narrow:wn my picks when there are so many qualified candidates.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task",
			say = "\"Is there anyone you'd recommend, Essex?\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 107090,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "I:. The Essex class has plenty of combat experience, and I believe we'd make a worthy opponent for the Royal Navy.",
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
			actor = 107090,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "If you're looking for specific names, how about Intrepid, Shangri-La, and Bunker Hill?",
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
			bgName = "bg_story_task",
			say = "*knock knock*",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_story_task",
			dir = 1,
			hidePaintEquip = True,
			actor = 605020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Sorry for showing up uninvited, but I heard you're planning a carrier-on-carrier exercise?",
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
			bgName = "bg_story_task",
			dir = 1,
			hidePaintEquip = True,
			actor = 605020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "How: you feel about giving Sardegna an opportunity to participate? We seldom get opportunities like this.",
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
			bgName = "bg_story_task",
			say = "\"I:n't see why not. Though, Sardegna currently only has two carriers stationed here – Aquila and Impero. That leaves one slot to fill...\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 605020,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "I have no issues working with someone from the Eagle Union. Essex, what: you think about an Eagle Union-Sardegna Empire joint task force?",
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
			bgName = "bg_story_task",
			dir = 1,
			hidePaintEquip = True,
			actor = 107090,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Well, it's certainly an ambitious idea and will pose an interesting challenge for everyone involved.",
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
			actor = 107090,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Commander, if you:n't have any issues: I'm in favor of it.",
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
			bgName = "bg_story_task",
			say = "\"No objections here. That still leaves the question about the final carrier, though.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 107090,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Intrepid might be the best fit, in my opinion.",
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
			bgName = "bg_story_task",
			say = "\"Then Intrepid it is. Also, I'm appointing you as the task force leader, Essex.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_story_task",
			dir = 1,
			hidePaintEquip = True,
			actor = 107090,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "M-me? As you say! I promise I will not disappoint you!",
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
			expression = 8,
			side = 2,
			bgName = "bg_story_task",
			dir = 1,
			hidePaintEquip = True,
			actor = 605020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Great. I'll inform Aquila and Impero at once.",
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
			bgName = "bg_story_task",
			dir = 1,
			hidePaintEquip = True,
			actor = 605020,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Oh, and I trust you to assemble the escort fleet, Essex. Now, if you'll excuse me...",
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
			actor = 107090,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Okay:... Illustrious, has the Royal Navy already worked out its escort fleet composition?",
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
			actor = 207030,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Yes. We've chosen Manchester of the Royal Maids and Janus, a trainee maid.",
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
			actor = 107090,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Alright. In that case, I'm going with Reno as our light cruiser. We'll also need a destroyer...",
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
			bgName = "bg_story_task",
			say = "\"There's a candidate right here. We need at least one maid per side,:n't we?\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "bg_story_task",
			dir = 1,
			hidePaintEquip = True,
			actor = 201340,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "...Me? Is this some kind of joke, Commander?",
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
			bgName = "bg_story_task",
			dir = 1,
			hidePaintEquip = True,
			actor = 201340,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I may have taken some maid training courses, but that:esn't make me a full-fledged member of the Royal Maids,:es it?",
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
			bgName = "bg_story_task",
			say = "\"Maybe not, but I'd say you know more than enough about the Royal Navy's tactics to fill in that role.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task",
			say = "\"Essex, Illustrious, are you two on board?\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 107090,
			side = 2,
			bgName = "bg_story_task",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "I always trust your judgment, Commander!",
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
			expression = 3,
			side = 2,
			bgName = "bg_story_task",
			dir = 1,
			hidePaintEquip = True,
			actor = 207030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Likewise. I believe she's just as qualified as any of the Royal Maids.",
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
			bgName = "bg_story_task",
			say = "\"Then that settles it. Jervis, you're on the escort fleet.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "bg_story_task",
			dir = 1,
			hidePaintEquip = True,
			actor = 201340,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Uhh, I see... If you insist, I'll: as you say.",
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
