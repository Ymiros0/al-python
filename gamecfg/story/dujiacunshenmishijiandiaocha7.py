return {
	fadeOut = 1.5,
	mode = 2,
	id = "DUJIACUNSHENMISHIJIANDIAOCHA7",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			stopbgm = True,
			mode = 1,
			sequence = {
				{
					"The Spiriting-Away Incident?\n\n<size=45>Assemble the Fleet!</size>",
					1
				}
			}
		},
		{
			side = 2,
			actorName = "Tengu",
			bgName = "bg_village_in",
			factiontag = "Wants You to Respect Your Elders",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Well, it's time for the intermission.",
			bgm = "map-longgong",
			icon = {
				scale = 8,
				image = "Props/story_yatiangou",
				pos = {
					0,
					0
				}
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "Tengu",
			bgName = "bg_village_in",
			factiontag = "Wants You to Respect Your Elders",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Travelers, was our play to your liking?",
			icon = {
				scale = 8,
				image = "Props/story_yatiangou",
				pos = {
					0,
					0
				}
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 301810,
			side = 0,
			bgName = "bg_village_in",
			nameColor = "#A9F548FF",
			dir = 1,
			hideOther = True,
			actorName = "Kasumi & Hatsuzuki",
			hidePaintObj = True,
			say = "- It was great. - I'll have nightmares about this!",
			subActors = {
				{
					actor = 301890,
					hidePaintObj = True,
					pos = {
						x = 1100
					}
				}
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 101490,
			side = 0,
			bgName = "bg_village_in",
			nameColor = "#A9F548FF",
			dir = 1,
			hideOther = True,
			actorName = "Bristol & Fu Shun",
			hidePaintObj = True,
			say = "- I can't wait for more! - Show us the next act already!",
			subActors = {
				{
					actor = 501020,
					hidePaintObj = True,
					pos = {
						x = 1185
					}
				}
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "bg_village_in",
			factiontag = "Little Miss Possessive Demon",
			dir = 1,
			actor = 301890,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Wait, there's more?! God, have mercy on me...",
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
			side = 2,
			actorName = "Tengu",
			bgName = "bg_village_in",
			factiontag = "Wants You to Respect Your Elders",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Ah. That's great to hear.",
			icon = {
				scale = 8,
				image = "Props/story_yatiangou",
				pos = {
					0,
					0
				}
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "Tengu",
			bgName = "bg_village_in",
			factiontag = "Wants You to Respect Your Elders",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Now, let us continue to the–",
			icon = {
				scale = 8,
				image = "Props/story_yatiangou",
				pos = {
					0,
					0
				}
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			nameColor = "#A9F548FF",
			bgName = "bg_village_in",
			hidePaintObj = True,
			say = "BOOOM!",
			soundeffect = "event./battle/boom2",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			flashN = {
				color = {
					1,
					1,
					1,
					1
				},
				alpha = {
					{
						0,
						1,
						0.2,
						0
					},
					{
						1,
						0,
						0.2,
						0.2
					},
					{
						0,
						1,
						0.2,
						0.4
					},
					{
						1,
						0,
						0.2,
						0.6
					}
				}
			},
			dialogShake = {
				speed = 0.09,
				x = 8.5,
				number = 2
			}
		},
		{
			actor = 301810,
			side = 2,
			bgName = "bg_village_in",
			factiontag = "Foo is Here Too",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "...What was that?",
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
			side = 2,
			nameColor = "#A9F548FF",
			bgName = "bg_village_in",
			hidePaintObj = True,
			say = "BOOOM!",
			soundeffect = "event./battle/boom2",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			flashN = {
				color = {
					1,
					1,
					1,
					1
				},
				alpha = {
					{
						0,
						1,
						0.2,
						0
					},
					{
						1,
						0,
						0.2,
						0.2
					},
					{
						0,
						1,
						0.2,
						0.4
					},
					{
						1,
						0,
						0.2,
						0.6
					}
				}
			},
			dialogShake = {
				speed = 0.09,
				x = 8.5,
				number = 2
			}
		},
		{
			actor = 501020,
			side = 2,
			bgName = "bg_village_in",
			factiontag = "Thrillseeker and Daredevil",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Zoinks! Is that an earthquake?!",
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
					dur = 0.1,
					x = 0,
					number = 2
				}
			}
		},
		{
			side = 2,
			actorName = "Chouchinobake",
			bgName = "bg_village_in",
			factiontag = "Party at the Onsen!",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Naw, girl, that's definitely no earthquake!",
			icon = {
				scale = 8,
				image = "Props/story_denglonggui",
				pos = {
					0,
					0
				}
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "Chouchinobake",
			bgName = "bg_village_in",
			factiontag = "Party at the Onsen!",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "This ain't good, folks! Someone's attacking the barrier!",
			icon = {
				scale = 8,
				image = "Props/story_denglonggui",
				pos = {
					0,
					0
				}
			},
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "bg_village_in",
			factiontag = "Nice and Simple Kind of Gal",
			dir = 1,
			actor = 305130,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Attacking it?",
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
			bgName = "bg_village_in",
			factiontag = "Nice and Simple Kind of Gal",
			dir = 1,
			actor = 305130,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Oh boy... Lemme guess, y'all forgot to tell the Commander you were goin' here, didn'tcha?",
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
			bgName = "bg_village_in",
			factiontag = "100-Rolling Investigator",
			dir = 1,
			actor = 101490,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Oh! Right! I knew we'd forgotten something!",
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
					dur = 0.1,
					x = 0,
					number = 2
				}
			}
		},
		{
			actor = 501020,
			side = 2,
			bgName = "bg_village_in",
			factiontag = "Thrillseeker and Daredevil",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Uh-oh! We need to stop the attack immediately!",
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
			bgName = "bg_village_in",
			factiontag = "Nice and Simple Kind of Gal",
			dir = 1,
			actor = 305130,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "*sigh*... Just what we needed...",
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
			bgName = "bg_village_in",
			factiontag = "Nice and Simple Kind of Gal",
			dir = 1,
			actor = 305130,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Shimakaze, you're the quickest – scoot over there 'n tell the Commander to stop! We'll take things from here!",
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
			bgName = "bg_village_in",
			factiontag = "Hippity Hoppity!",
			dir = 1,
			actor = 301290,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Roger-dodger! I'm on my way!",
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
			bgName = "bg_village_out",
			hidePaintObj = True,
			say = "Meanwhile, outside the strange torii gate...",
			bgm = "nagato-map",
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
			paintingNoise = True,
			side = 2,
			bgName = "bg_village_out",
			factiontag = "Surprisingly Good with Disguises",
			dir = 1,
			actor = 702040,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Comrade Commander, we've finished blockading the waters around the island. Entry will be possible once the barrier has been destroyed.",
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
			paintingNoise = True,
			side = 2,
			bgName = "bg_village_out",
			factiontag = "Plays the Teacher a Lot",
			dir = 1,
			actor = 107030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I've got the skies under complete lockdown, too. Not a single bird or ghost is getting out!",
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
			bgName = "bg_village_out",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Excellent. Nagato, how are things on your end?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 305050,
			side = 2,
			bgName = "bg_village_out",
			factiontag = "The Guardian Fox",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Expected to finish in ten minutes.",
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
			bgName = "bg_village_out",
			factiontag = "The Guardian Fox",
			dir = 1,
			actor = 305050,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Yamashiro, Musashi, focus fire. Coordinate your attacks on the talisman with me.",
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
			actor = 305020,
			side = 2,
			bgName = "bg_village_out",
			factiontag = "Bad Luck Won't Stop Her",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Understood, Lady Nagato!",
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
			bgName = "bg_village_out",
			factiontag = "Protector of the Weak",
			dir = 1,
			actor = 305100,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Shinano and the girls' safety hinges on us. I will hold nothing back.",
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
			bgName = "bg_village_out",
			hidePaintObj = True,
			say = "Nagato, Yamashiro, and Musashi are bombarding the barrier. A group of shipgirls from all factions stood just behind them, ready to run in.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_village_out",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "The talisman will be destroyed in ten minutes. All ships, prepare for battle!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "Everyone",
			bgName = "bg_village_out",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Roger!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "???",
			bgName = "bg_village_out",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Wait, wait! Please wait, Commander!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_village_out",
			hidePaintObj = True,
			say = "A familiar voice calls out to me from nowhere. Then, Shimakaze appears seemingly out of thin air from beyond the torii gate.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_village_out",
			hidePaintObj = True,
			say = "More follow a few moments later. Owari, Hatsuzuki, and Bristol with the rest of her team.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 501020,
			side = 2,
			bgName = "bg_village_out",
			factiontag = "Thrillseeker and Daredevil",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Geesh, you guys gathered a small army here...",
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
			actor = 301890,
			side = 2,
			bgName = "bg_village_out",
			factiontag = "Little Miss Possessive Demon",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "See? I TOLD you we should've called the Commander before we went in!",
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
			bgName = "bg_village_out",
			factiontag = "Hippity Hoppity!",
			dir = 1,
			actor = 301290,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "This is all a big misunderstanding, Commander! Please allow me a minute to explain!",
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
			bgName = "bg_village_out",
			hidePaintObj = True,
			say = "Shimakaze, in her panic, blew way past a summary and:ve into a convoluted explanation...",
			bgm = "cw-level",
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
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_village_out",
			hidePaintObj = True,
			say = "Fortunately, Shinano had come along, and she provided me with a brief overview of what had happened.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 307080,
			side = 2,
			bgName = "bg_village_out",
			factiontag = "Habitual Sleepwalker",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "All we intended for was an unforgettable summer experience... We are truly sorry...",
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
			bgName = "bg_village_out",
			factiontag = "Habitual Sleepwalker",
			dir = 1,
			actor = 307080,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "This one suspected the invitation of poor messaging... A mistake most unfortunate...",
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
			bgName = "bg_village_out",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "I understand now. You wanted to make it look like a spiriting-away case as part of the play.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_village_out",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Instead, it made your intentions all the more fuzzy.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "bg_village_out",
			factiontag = "The Guardian Fox",
			dir = 1,
			actor = 305050,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Such a misunderstanding is nobody's fault. Let it not bother you.",
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
			actor = 702040,
			side = 2,
			bgName = "bg_village_out",
			factiontag = "Surprisingly Good with Disguises",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I'll admit, it DID result in an unforgettable experience.",
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
			bgName = "bg_village_out",
			factiontag = "Surprisingly Good with Disguises",
			dir = 1,
			actor = 702040,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "It was certainly the last way I expected that flyer to keep its word.",
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
			actor = 702040,
			side = 2,
			bgName = "bg_village_out",
			factiontag = "Surprisingly Good with Disguises",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I wondered what form this Youkai Troupe would take, and I was not disappointed.",
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
			actor = 107030,
			side = 2,
			bgName = "bg_village_out",
			factiontag = "Plays the Teacher a Lot",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Speaking of them, is that where we'll meet the troupe? Just past the barrier under the torii gate?",
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
			actor = 307080,
			side = 2,
			bgName = "bg_village_out",
			factiontag = "Habitual Sleepwalker",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Yes... They cannot leave the barrier in their current forms...",
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
			bgName = "bg_village_out",
			factiontag = "Plays the Teacher a Lot",
			dir = 1,
			actor = 107030,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Did you hear that? We'll get to see some real youkai! Let's go!",
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
			bgName = "bg_village_out",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "(Well... I suppose the crisis is over now.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_village_out",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "(Everyone's safe, and I:n't want to undermine the efforts Shinano and the Youkai Troupe put into all this.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_village_out",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "(Let's head in and see what this play is like.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		}
	}
}