return {
	id = "HAITIAN3",
	mode = 2,
	fadeOut = 1.5,
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"Set Sail! An Inspiration-Seeking Journey\n\n<size=45>3 Set Sail! An Inspiration-Seeking Journey!</size>",
					1
				}
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "I brought all our freshly-purchased wares back to the office and spread them out on the floor to organize them–",
			bgm = "story-richang-6",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "A tent, a tarp, two camping chairs, a foldable sunbed... Insect spray, wet wipes, sunscreen...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Wait, what? Why is there an axe here?!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 502070,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Um, well, just in case we need firewood or encounter a ferocious beast... It's better to come prepared, right?",
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
					content = "There shouldn't be any wild beasts around the port, I think...",
					flag = 1
				},
				{
					content = "I'm not sure how much of a threat wild beasts pose to cannon-toting shipgirls, but...",
					flag = 2
				}
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502070,
			say = "Y-yes, you're right...! We can leave the axe behind, and the crowbar as well...",
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
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "After returning a whole bunch of items we didn't plan on using such as walkie-talkies, a folding clothesrack, and a chainsaw...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
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
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_story_task_2",
			hidePaintObj = True,
			say = "Hai Tien and I finally set out on our camping trip in search of inspiration.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			say = "A bit later, in the woods behind the port...",
			bgm = "story-richang-5",
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
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502070,
			say = "Phew... The air here is so crisp and refreshing. My mind already feels totally refreshed.",
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
			actor = 502070,
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "I haven't had any flashes of inspiration yet, but at least my body feels lighter than before.",
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
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			say = "Hai Tien has a smile on her face as she speaks. A squirrel hops:wn from the tree trunk, circles around her, and: darts off deeper into the woods.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Want to try following the squirrel?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 7,
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502070,
			say = "That sounds like an excellent idea! Thank you!",
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
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			say = "The two of us head deeper into the woods as well, following the direction of the squirrel.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			say = "It seems that we happened to go on our camping trip during the flowering season. A kaleidoscope of flowers are in full bloom everywhere we look, and I inadvertently slow:wn to admire them.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502070,
			say = "Have these flowers piqued your interest, Commander? I happen to know a thing or two about them, if you'd like to learn more about them.",
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
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			say = "Hai Tien's eyes are shimmering with anticipation. She clearly wants to demonstrate her knowledge to me.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "\"I'd be glad to learn more.\"",
					flag = 1
				},
				{
					content = "\"Actually, I'm not too sure...\"",
					flag = 2
				}
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			optionFlag = 1,
			say = "You're my teacher today, Miss Hai Tien!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			optionFlag = 2,
			say = "The scenery here is certainly beautiful, but...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 9,
			side = 2,
			bgName = "star_level_bg_520",
			dir = 1,
			optionFlag = 2,
			actor = 502070,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "...But?",
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
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			optionFlag = 2,
			say = "It pales in comparison to your beauty.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502070,
			say = "*cough*, *cough*... Geez, Commander, please:n't tease me like that...",
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
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			say = "But, she is unable to hide the faint blush on her cheeks.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 8,
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502070,
			say = "Now that I think about it, you didn't come here just to hear me yap about flowers...",
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
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502070,
			say = "Oh, right! Commander, have you ever heard of the Flying Flower Game? It's a game where we take turns reciting poetry verses around a particular word or theme, and the loser has to play a punishment round.",
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
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Sounds interesting. Definitely a good way to spruce up our stroll.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Alright, let's: this!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502070,
			say = "Heehee. Allow me to begin,:. \"Before the Calyx Tower, spring is in full bloom.\"",
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
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "(According to the rules, I have to respond with a poetry verse that includes a flower-themed word)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "\"Beneath the swirling petals, glasses clink and feelings deepen.\"",
					flag = 1
				},
				{
					content = "\"Flowers and spring showers? Naw, we gon' make it rain!\"",
					flag = 2
				}
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "star_level_bg_520",
			dir = 1,
			optionFlag = 1,
			actor = 502070,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Wow, that's a great response, Commander, I'm surprised.",
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
			actor = 502070,
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			dir = 1,
			optionFlag = 1,
			nameColor = "#A9F548FF",
			say = "I shall continue:.",
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
			bgName = "star_level_bg_520",
			dir = 1,
			optionFlag = 2,
			actor = 502070,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Um, Commander... I believe we might be going a bit off-topic...",
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
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			optionFlag = 2,
			say = "Ahem... Oh, is that so? It, uhh, might just be... yeah, a poem you've never heard before!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 502070,
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			dir = 1,
			optionFlag = 2,
			nameColor = "#A9F548FF",
			say = "Hrmm... Really now? Well, it matters not. I shall continue:.",
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
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Bring it! Let's see what you've got!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502070,
			say = "\"As moon waxes, floral shadows fall before the window.\"",
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
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "\"There rests a beauty, like a flower wreathed in clouds.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502070,
			say = "\"Clothes like dancing clouds, cheeks like a rosy blossom.\"",
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
					content = "\"The spring breeze gently caresses the steps, peonies even more beautiful in the rich dew.\"",
					flag = 1
				},
				{
					content = "\"And upon the branches bloom countless pear flowers.\"",
					flag = 2
				}
			}
		},
		{
			expression = 9,
			side = 2,
			bgName = "star_level_bg_520",
			dir = 1,
			optionFlag = 1,
			actor = 502070,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Hmm... Commander, are you sure this verse connects with the previous one?",
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
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			optionFlag = 1,
			say = "I guess not, but... When I look at you, it feels like everything wants to connect back to the starting verse...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			optionFlag = 1,
			say = "\"If not a fairy descended the mountains, she must be a goddess bathed in moonlight\" ...I think those words describe you perfectly, Hai Tien.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "star_level_bg_520",
			dir = 1,
			optionFlag = 1,
			actor = 502070,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Um... I, I guess I can overlook this and not count this as your loss...",
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
			bgName = "star_level_bg_520",
			dir = 1,
			optionFlag = 2,
			actor = 502070,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Well:ne! Let's keep it up–",
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
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502070,
			say = "\"As song comes from boats, flowers line the shore.'",
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
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Let me think... Urgh, I:n't think I can come up with anything else...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502070,
			say = "Heehee. It appears that I'm the victor. Now:... 'A flower must be harvested when the time is right. Wait not until the branches are empty.\"",
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
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502070,
			say = "Commander, would you mind making me a flower crown?",
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
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "(A flower crown? That shouldn't be a very difficult request...)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			say = "I nod my head and agree to go along with Hai Tien's request.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			say = "Just as I am hard at work scavenging for flowers and branches, weaving them together into a circlet large enough to rest atop her head...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			say = "I feel a slender, soft hand slide into my own, gently dropping a carefully-crafted ring of grass into my palm.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			say = "My eyes turn towards the hand's owner. It is not just her cheeks that are bright red this time – even the tips of her ears are dyed an adorable pink.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 502070,
			say = "This is... my way of thanking you for the flower crown.",
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
			bgName = "star_level_bg_520",
			hidePaintObj = True,
			say = "Her voice sounds tender, almost wavering.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		}
	}
}
