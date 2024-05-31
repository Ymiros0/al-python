return {
	id = "ZHANFANGYUHUIGUANGZHICHENG17",
	mode = 2,
	fadeOut = 1.5,
	scripts = {
		{
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			say = "We walk to the institute, my memory of the route guiding us.",
			bgm = "theme-aostelab",
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
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			say = "It's the same place I went in the Reality Lens and the same place Kronshtadt and her team described, yet stark differences remain.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			say = "There are no shops, no stalls, and no facilities catering to tourists. They've all been replaced by defensive installations and barricades.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			say = "The mask of peace has come off, revealing the island's True nature as a military base.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			say = "All of a sudden, sirens start to blare.",
			bgm = "airRaidAlarm",
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
			expression = 2,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 803020,
			say = "An alarm. Who carelessly tripped the security system?",
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
			expression = 7,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 805030,
			say = "One's sensors are detecting nothing... They are working, before you ask.",
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
					dur = 0.15,
					x = 0,
					number = 2
				}
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 901070,
			say = "Wasn't me. I'm the one who's been switching off all the systems.",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 901050,
			say = "Since when? I had no idea you were:ing that!",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 901060,
			say = "You Tribunal people scare me...",
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
					dur = 0.15,
					x = 0,
					number = 2
				}
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "I:n't think any of us tripped it. The alarms are going off across the whole island, and I:n't think they activated just to arrest us.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 805030,
			say = "But: who did? One:es not understand.",
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
			bgName = "bg_zhedie_7",
			paintingNoise = True,
			dir = 1,
			actor = 9705040,
			nameColor = "#FFC960",
			hidePaintObj = True,
			say = "An enemy fleet has appeared 50 nautical miles northwest. It seems they're heading your way.",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "A fleet? Can you ID them?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "bg_zhedie_7",
			paintingNoise = True,
			dir = 1,
			actor = 9705040,
			nameColor = "#FFC960",
			hidePaintObj = True,
			say = "They're corrosion entities.",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "You mean those things that the black tornadoes spew out and cannot be analyzed?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "bg_zhedie_7",
			paintingNoise = True,
			dir = 1,
			actor = 9705040,
			nameColor = "#FFC960",
			hidePaintObj = True,
			say = "If you mean corrosion phenomena, yes, but they can manifest through other means.",
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
			bgName = "bg_zhedie_7",
			paintingNoise = True,
			dir = 1,
			actor = 9705040,
			nameColor = "#FFC960",
			hidePaintObj = True,
			say = "Remember, they are literal embodiments of corrosion.",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#FFC960",
			actor = 9705040,
			say = "As you said, they cannot be meaningfully analysed even up-close.",
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
			bgName = "bg_zhedie_7",
			paintingNoise = True,
			dir = 1,
			actor = 9705040,
			nameColor = "#FFC960",
			hidePaintObj = True,
			say = "Or, rather, you CAN, but what you perceive changes slightly each time.",
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
			bgName = "bg_zhedie_7",
			paintingNoise = True,
			dir = 1,
			actor = 9705040,
			nameColor = "#FFC960",
			hidePaintObj = True,
			say = "You also cannot capture them, and they:n't leave wrecks behind when destroyed. It's as though they:n't physically exist.",
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
			bgName = "bg_zhedie_7",
			paintingNoise = True,
			dir = 1,
			actor = 9705040,
			nameColor = "#FFC960",
			hidePaintObj = True,
			say = "In a way, they:n't. They're shadows projected from a different dimension. Imperfectly, at that.",
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
			bgName = "bg_zhedie_7",
			paintingNoise = True,
			dir = 1,
			actor = 9705040,
			nameColor = "#FFC960",
			hidePaintObj = True,
			say = "The data loss caused by the projection process is in fact the reason why they appear as blurs you can't perceive properly.",
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
			bgName = "bg_zhedie_7",
			paintingNoise = True,
			dir = 1,
			actor = 9705040,
			nameColor = "#FFC960",
			hidePaintObj = True,
			say = "Think of them as corrupted data. The fact that they're there means the space you're in is being corroded.",
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
			bgName = "bg_zhedie_7",
			paintingNoise = True,
			dir = 1,
			actor = 9705040,
			nameColor = "#FFC960",
			hidePaintObj = True,
			say = "Now, it looks like we're dealing with... What? The Revolutionary Front?!",
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
			bgName = "bg_zhedie_7",
			paintingNoise = True,
			dir = 1,
			actor = 9705040,
			nameColor = "#FFC960",
			hidePaintObj = True,
			say = "Listen up! Those entities come from the data present in that space!",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "What: you mean?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 6,
			side = 2,
			bgName = "bg_zhedie_7",
			paintingNoise = True,
			dir = 1,
			actor = 9705040,
			nameColor = "#FFC960",
			hidePaintObj = True,
			say = "Just tune in to the frequency we just sent you! Their fleet is broadcasting a message to the island!",
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
			actorName = "Communicator",
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "This is the Revolutionary Front's AO Sector Fleet. We hereby issue an ultimatum to Samos Island.",
			bgm = "battle-hightech",
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
			side = 2,
			actorName = "Communicator",
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "Hand over the individuals behind the attack on the freighter Poltava, disarm your Enforcers, and immediately destroy all artificial intelligence laboratories on the island.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "Communicator",
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "If our demands are not met in three hours, we will achieve these objectives by force.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "Communicator",
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "It is apparent that Samos Island has become a breeding ground for corruption owing to the Oceanic Federation's policy of neglect.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "Communicator",
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "It is home to experiments – especially on weaponized artificial intelligence – that have never received safety assessments nor been held to ethics guidelines, all in the name of \"scientific progress.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "Communicator",
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "These people have put guns in the hands of robots and given the power over life and death to computer programs.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "Communicator",
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "It is exactly that which led to this tragedy. You cannot entrust human lives to machines.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "Communicator",
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "Artificial intelligences armed with weapons are both uncontrollable and extremely dangerous, and the attack on the Poltava proved this.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			actorName = "Communicator",
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "If these evil machines are left to roam free, it will be the end of humanity.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Are they serious? They'll capture the island by force if necessary?)",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(They mentioned artificial intelligences and Enforcers... That means the Antiochus, Dr. Aoste's project.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Then there was that attack on a freighter. They were vague on details...)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Seems safe to assume that the Antiochus struck the Poltava and hurt innocent people.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(In other words, they threatened the safety of the world's oceans, prompting the Revolutionary Front to retaliate.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "Miss D, can you remember what this memory is about?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 4,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900430,
			say = "No, not a thing! But it's obviously bad! Bad and I:n't like it!",
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
					dur = 0.15,
					x = 0,
					number = 2
				}
			}
		},
		{
			expression = 2,
			side = 2,
			bgName = "bg_zhedie_7",
			paintingNoise = True,
			dir = 1,
			actor = 9705040,
			nameColor = "#FFC960",
			hidePaintObj = True,
			say = "...We are in agreement there.",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 901070,
			say = "Sounds like both the Eagle Union and the Royal Navy are involved with this island.",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 901070,
			say = "Those demands were pretty crazy... They want the scientists to hand over those people, disarm their units, and destroy their lab all in three hours.",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 901070,
			say = "You could: maybe two of those in that time, but all three? No way.",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 901050,
			say = "I think they were going to use force anyway all along.",
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
			actorName = "Communicator",
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "BEEP BEEP!",
			soundeffect = "event./ui/noice",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			paintingNoise = True,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900332,
			say = "I see you on the security cams, Commander! What are you:ing on Samos?",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#FFC960",
			actor = 9705040,
			say = "What the–?!",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Shh! I'll handle this!)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "Ahem. Dr. Anzeel?",
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
			paintingNoise = True,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900332,
			say = "Yes, that's my name! Aoste already bailed, so why are you back here?",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "Do you know about the attack on the Poltava? The Revolutionary Front is on the island's:orstep, ready to enact revenge for it.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			paintingNoise = True,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900332,
			say = "Yes, I know about the thing that's filled the world's headlines for days now!",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900332,
			say = "Do you seriously believe that? That the Antiochus would defy protocol and attack a civilian freighter passing by?",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(That sounds just like what the Sirens we know would:...)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Considering everything we've witnessed, that definitely isn't beyond the realm of possibility... as much as it pains me to say that to her.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			paintingNoise = True,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900332,
			say = "\"Revenge,\" my ass... That's just what they want you to think.",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900332,
			say = "The attack was a False flag by the Revolutionary Front. They wanted an excuse to send a fleet to Samos.",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900332,
			say = "Laplace's Demon is nearly finished, and they want to steal it.",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(Laplace's Demon?)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			oldPhoto = True,
			side = 2,
			bgName = "bg_cccpv2_7",
			hideRecordIco = True,
			dir = 1,
			bgm = "battle-executor-type1",
			actor = 900307,
			nameColor = "#FEF15E",
			hidePaintObj = True,
			say = "If we adopt this plan, there may be a chance of success.",
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
				dur = 0.5,
				alpha = {
					0,
					1
				}
			},
			flashin = {
				delay = 0.5,
				dur = 0.5,
				black = False,
				alpha = {
					1,
					0
				}
			}
		},
		{
			side = 2,
			oldPhoto = True,
			bgName = "bg_cccpv2_7",
			dir = 1,
			hideRecordIco = True,
			actor = 900307,
			nameColor = "#FEF15E",
			hidePaintObj = True,
			say = "However, we must ensure that the jamming device remains operational as long as possible. In the meantime, we'll have to hold the line while evacuations are carried out.",
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
			oldPhoto = True,
			bgName = "bg_cccpv2_7",
			dir = 1,
			hideRecordIco = True,
			actor = 900307,
			nameColor = "#FEF15E",
			hidePaintObj = True,
			say = "In other words...",
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
			actorName = "???",
			bgName = "bg_cccpv2_7",
			hidePaintObj = True,
			nameColor = "#FEF15E",
			oldPhoto = True,
			say = "We already know this, Dr. Aoste. We've taken it upon ourselves to build upon this framework.",
			hideRecordIco = True,
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			side = 2,
			oldPhoto = True,
			bgName = "bg_cccpv2_7",
			dir = 1,
			hideRecordIco = True,
			actor = 900307,
			nameColor = "#FEF15E",
			hidePaintObj = True,
			say = "...I understand. But even if that is the case, everyone has already sustained heavy losses. The actual feasibility of the timeframe you provided must still be carefully evaluated...",
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
			oldPhoto = True,
			bgName = "bg_cccpv2_7",
			dir = 1,
			hideRecordIco = True,
			actor = 900307,
			nameColor = "#FEF15E",
			hidePaintObj = True,
			say = "If the \"Light of Dawn\" is ever extinguished,: Laplace's Demon will cease to be. If we have not reached the evacuation threshold at that time, our future operational plans will be impacted.",
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
			oldPhoto = True,
			bgName = "bg_cccpv2_7",
			dir = 1,
			hideRecordIco = True,
			actor = 900308,
			nameColor = "#FEF15E",
			hidePaintObj = True,
			say = "Worry not. I will also help buy time for you.",
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
			oldPhoto = True,
			bgName = "bg_cccpv2_7",
			dir = 1,
			hideRecordIco = True,
			actor = 900307,
			nameColor = "#FEF15E",
			hidePaintObj = True,
			say = "Ahem. Dr. Anzeel?",
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
			oldPhoto = True,
			bgName = "bg_cccpv2_7",
			dir = 1,
			hideRecordIco = True,
			actor = 900308,
			nameColor = "#FEF15E",
			hidePaintObj = True,
			say = "I've already issued too many communications through the process of commanding the operation, and they've likely already identified me for destruction.",
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
			oldPhoto = True,
			bgName = "bg_cccpv2_7",
			dir = 1,
			hideRecordIco = True,
			actor = 900308,
			nameColor = "#FEF15E",
			hidePaintObj = True,
			say = "As long as I can continue to draw their attention, I should be able to alleviate the pressure in other places, giving you more time to implement the plan.",
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
			oldPhoto = True,
			bgName = "bg_cccpv2_7",
			dir = 1,
			hideRecordIco = True,
			actor = 900307,
			nameColor = "#FEF15E",
			hidePaintObj = True,
			say = "But, what will happen to you:?",
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
			oldPhoto = True,
			bgName = "bg_cccpv2_7",
			dir = 1,
			hideRecordIco = True,
			actor = 900308,
			nameColor = "#FEF15E",
			hidePaintObj = True,
			say = "After such a fiasco, someone always has to bear the responsibility. Only now, there aren't many people left who can shoulder that burden.",
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
			oldPhoto = True,
			bgName = "bg_cccpv2_7",
			dir = 1,
			hideRecordIco = True,
			actor = 900307,
			nameColor = "#FEF15E",
			hidePaintObj = True,
			say = "I see... You can bring your KAN-SEN along as well. However, I would like Code G to accompany my Antiochus if possible.",
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
			oldPhoto = True,
			bgName = "bg_cccpv2_7",
			dir = 1,
			hideRecordIco = True,
			actor = 900308,
			nameColor = "#FEF15E",
			hidePaintObj = True,
			say = "Very well. You can have Enterprise, and whoever else manages to survive.",:
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
			oldPhoto = True,
			bgName = "bg_cccpv2_7",
			dir = 1,
			hideRecordIco = True,
			actor = 900308,
			nameColor = "#FEF15E",
			hidePaintObj = True,
			say = "However, take them as far away from NY City as you can. Never let them return here.",
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
			oldPhoto = True,
			bgName = "bg_cccpv2_7",
			dir = 1,
			hideRecordIco = True,
			actor = 900307,
			nameColor = "#FEF15E",
			hidePaintObj = True,
			say = "...Without you here, I'm not sure I'll be able to control them...",
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
			oldPhoto = True,
			bgName = "bg_cccpv2_7",
			dir = 1,
			hideRecordIco = True,
			actor = 900308,
			nameColor = "#FEF15E",
			hidePaintObj = True,
			say = "What happened to the ever-so-wise and stoic Magister? You have no choice but to give those children both a purpose and the responsibility that comes with it, right?",
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
			oldPhoto = True,
			bgName = "bg_cccpv2_7",
			dir = 1,
			hideRecordIco = True,
			actor = 900308,
			nameColor = "#FEF15E",
			hidePaintObj = True,
			say = "...Even after you \"betrayed\" us, I still believe we see things eye-to-eye. And I think what you're:ing is just. I completely understand you, and I trust that in their hearts, they understand you as well...",
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
			oldPhoto = True,
			bgName = "bg_cccpv2_7",
			dir = 1,
			hideRecordIco = True,
			actor = 900308,
			nameColor = "#FEF15E",
			hidePaintObj = True,
			say = "I'm sure they'll need some time to accept it, but they will come to understand you one day...",
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
			oldPhoto = True,
			bgName = "bg_cccpv2_7",
			dir = 1,
			hideRecordIco = True,
			actor = 900308,
			nameColor = "#FEF15E",
			hidePaintObj = True,
			say = "Yes, I'm sure of it...",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(That's what I heard when I was in the Arcana Sanctum. Is this what that conversation referred to?)",
			bgm = "story-commander-up",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			flashout = {
				black = False,
				dur = 0.5,
				alpha = {
					0,
					1
				}
			},
			flashin = {
				delay = 0.5,
				dur = 0.5,
				black = False,
				alpha = {
					1,
					0
				}
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "So the Revolutionary Front wants to steal your time machine – Laplace's Demon. Does the Federation know about this?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			paintingNoise = True,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900332,
			say = "Of course it:es. They got this far in the first place because the RF had the Federation's tactic permission.",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900332,
			say = "The Federation wants the RF to make the first move and escalate tensions. That way, they:n't have to take the blame for starting a war.",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "Wait... Starting a war?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			paintingNoise = True,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900332,
			say = "Yeah. A war that will erase them from time.",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900332,
			say = "Seize the power to control time, and the world shall be yours.",
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
					content = "My god...",
					flag = 1
				},
				{
					content = "They're going to start a World War...",
					flag = 2
				},
				{
					content = "But that's insane!",
					flag = 3
				}
			}
		},
		{
			paintingNoise = True,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900332,
			say = "Don't freak out. Aoste and I already have a plan.",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900332,
			say = "Flare – as in, Enterprise and company – will swoop in unannounced and steal Laplace's Demon and make both sides take a chill pill.",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "Enterprise? You mean... Code G?!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			paintingNoise = True,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900332,
			say = "Look, we've chatted enough and this island is about to become a warzone! You need to get out of here NOW!",
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
			actorName = "Communicator",
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "......",
			soundeffect = "event./ui/noice",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#5CE6FF",
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			say = "The communicator falls silent.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(The tension between the two major players in the alpha timeline is about to boil over into all-out war.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(But, if Anzeel's and Aoste's plan is a success and Laplace's Demon falls into neither side's hands,: this memory won't have anything to: with death.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(So what in the world is going to happen here?)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 901070,
			say = "Commaaander. Who was that? Do you know her?",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "According to the memory we're in, yes. Why: you ask?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 901070,
			say = "Because... she contacted you using the Tribunal's private frequency.",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 901070,
			say = "Everyone on this mission, including Elizabeth, is also using it.",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 901070,
			say = "This frequency is from OUR timeline, so how did that woman know about it and call us on it like it was the most natural thing in the world?",
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
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "(That's a good point... I've grown so used to our frequencies being jammed or intercepted that I've stopped questioning it.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900430,
			say = "How she did it:esn't matter!",
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
			expression = 7,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900430,
			say = "Didn't you hear her? We need to get out of here, and fast!",
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
					dur = 0.15,
					x = 0,
					number = 2
				}
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "It's too late for that. If this memory really is a representation of death, Anzeel's and Aoste's plan is going to fall through.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 10,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#5CE6FF",
			actor = 900430,
			say = "Huh? How: you know that?",
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
					dur = 0.15,
					x = 0,
					number = 2
				}
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "bg_zhedie_7",
			hidePaintObj = True,
			nameColor = "#5CE6FF",
			say = "Because if it had succeeded, this space wouldn't exist in the first place.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		}
	}
}
