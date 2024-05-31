return {
	fadeOut = 1.5,
	mode = 2,
	id = "YUYEJINGHUN17",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_600",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Whydah, and something about a collection room?",
			bgm = "qe-ova-15",
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
			actor = 0,
			side = 2,
			bgName = "star_level_bg_600",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "That's on the second floor, I think. I should head up there.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_600",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Those two will probably still be in the corridor, though. I can't sneak past them like this. What to:...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "Time to use my gun.",
					flag = 1
				},
				{
					content = "I could make a loud noise...",
					flag = 2
				}
			}
		},
		{
			portrait = 401020,
			side = 2,
			bgName = "star_level_bg_600",
			factiontag = "Impromptu Replacement GM",
			nameColor = "#A9F548FF",
			optionFlag = 1,
			actorName = "Z2",
			hidePaintObj = True,
			say = "You ready your firearm... but: you think about it. You:n't want to take them out, you just want to sneak past without being seen.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 401020,
			side = 2,
			bgName = "star_level_bg_600",
			factiontag = "Impromptu Replacement GM",
			nameColor = "#A9F548FF",
			optionFlag = 1,
			actorName = "Z2",
			hidePaintObj = True,
			say = "So never mind the gun – what you need is a distraction.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 107090,
			side = 2,
			bgName = "star_level_bg_600",
			factiontag = "Serious Protégé GM",
			actorName = "Essex",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "With your mind set, you start looking around the room for something you can use.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 107090,
			side = 2,
			bgName = "star_level_bg_600",
			factiontag = "Serious Protégé GM",
			actorName = "Essex",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Faced with all these objects, your brain kicks into full drive.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 107060,
			side = 2,
			bgName = "star_level_bg_600",
			factiontag = "Serious GM",
			actorName = "Enterprise",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Roll a D100... 43, a success. You have a flash of inspiration, and another piece of your mind puzzle falls into place.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 107060,
			side = 2,
			bgName = "star_level_bg_600",
			factiontag = "Serious GM",
			actorName = "Enterprise",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Being an excellent investigator, you have practiced a skill all by yourself to raise your odds of surviving any given case... making traps.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 107060,
			side = 2,
			bgName = "star_level_bg_600",
			factiontag = "Serious GM",
			actorName = "Enterprise",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "You've remembered the skill Trap-Making. Your proficiency is novice-level.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "Huh? Trap-Making?",
					flag = 1
				},
				{
					content = "It's not called Survival?",
					flag = 2
				},
				{
					content = "Who came up with this one?",
					flag = 3
				}
			},
			location = {
				"Investigator Stat Revealed",
				3
			}
		},
		{
			portrait = 401020,
			side = 2,
			bgName = "star_level_bg_600",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			optionFlag = 3,
			actorName = "Z2",
			say = "Let's just say it was a sweet pirate who loves pacts.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 101490,
			side = 2,
			bgName = "star_level_bg_600",
			factiontag = "(Self-Proclaimed) Great Detective GM",
			actorName = "Bristol",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "\"Trap\" is kind of an umbrella term. You can craft surprising things if you just get creative.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 101490,
			side = 2,
			bgName = "star_level_bg_600",
			factiontag = "(Self-Proclaimed) Great Detective GM",
			actorName = "Bristol",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Also, all skills that get you out of tight spots matter! Especially since traps can also inflict damage to your opponent!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_600",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Damage isn't really the point, but this:es seem like a versatile skill.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_600",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "The components I've got are... Tables and chairs, planks, fireworks, and paper towels. I think I can craft a noisemaker.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 502070,
			side = 2,
			bgName = "star_level_bg_600",
			factiontag = "Bookworm GM",
			actorName = "Hai Tien",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "You start making a bomb right away. While your proficiency could be better, this skill has gotten you out of sticky situations many times before.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 301160,
			side = 2,
			bgName = "star_level_bg_600",
			factiontag = "LCK-Maxed GM",
			actorName = "Yukikaze",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Roll a D100! 1! Hahahaha! Another critical success from Yukikaze the Great!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			dialogShake = {
				speed = 0.08,
				x = 15,
				number = 2
			}
		},
		{
			portrait = 502070,
			side = 2,
			bgName = "star_level_bg_600",
			factiontag = "Bookworm GM",
			actorName = "Hai Tien",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Good lord... Ahem. Your skill pulls through for you once again.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 502070,
			side = 2,
			bgName = "star_level_bg_600",
			factiontag = "Bookworm GM",
			actorName = "Hai Tien",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "You have successfully crafted a shiny bomb. However, you: not yet know how powerful it is.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_600",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Between a bomb and a gun, I've got plenty to distract them.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 502070,
			side = 2,
			bgName = "star_level_bg_600",
			factiontag = "Bookworm GM",
			actorName = "Hai Tien",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "You crack a satisfied smile and set your plan into motion...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_156",
			hidePaintObj = True,
			say = "Sometime later...",
			bgm = "theme-highseasfleet-reborn",
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
			portrait = 502070,
			side = 2,
			bgName = "star_level_bg_156",
			factiontag = "Bookworm GM",
			actorName = "Hai Tien",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "The plan is very simple. Setting off a bomb is sure to make a loud noise and distract people in the vicinity.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 502070,
			side = 2,
			bgName = "star_level_bg_156",
			factiontag = "Bookworm GM",
			actorName = "Hai Tien",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "While they go to investigate, you can head up to the second floor and continue your investigation.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 502070,
			side = 2,
			bgName = "star_level_bg_156",
			factiontag = "Bookworm GM",
			actorName = "Hai Tien",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "After laying:wn a fuse and lighting it, you return to the observation deck and wait for the explosion.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 107090,
			side = 2,
			bgName = "star_level_bg_156",
			factiontag = "Serious Protégé GM",
			actorName = "Essex",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Roll a D100... 71, a failure. You wait and wait, but the explosion never comes.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_156",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Was it because I didn't set up the fuse right? Time for plan B.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 502070,
			side = 2,
			bgName = "star_level_bg_156",
			factiontag = "Bookworm GM",
			actorName = "Hai Tien",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "You find a great spot to fire from the observation deck. You aim your gun at the bomb and pull the trigger...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 107090,
			side = 2,
			bgName = "star_level_bg_156",
			factiontag = "Serious Protégé GM",
			actorName = "Essex",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Roll a D100... 98, a critical failure this time. Your accuracy is so poor, the shot hits a marble pillar way off from the target, causing major damage to it.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 502070,
			side = 2,
			bgName = "star_level_bg_156",
			factiontag = "Bookworm GM",
			actorName = "Hai Tien",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Not just that, the recoil makes you fall flat on your butt. A stinging pain shoots up from your tailbone.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_156",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "How many bullets: I have left?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 502070,
			side = 2,
			bgName = "star_level_bg_156",
			factiontag = "Bookworm GM",
			actorName = "Hai Tien",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Two.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_156",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Then I'll give it another shot.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 107090,
			side = 2,
			bgName = "star_level_bg_156",
			factiontag = "Serious Protégé GM",
			actorName = "Essex",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Roll a D100... 53. Your poorly aimed shot goes through a board covering up a fireplace.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_156",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "One more! Just let me shoot one more time! And have Yukikaze throw the dice!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 301160,
			side = 2,
			bgName = "star_level_bg_156",
			factiontag = "LCK-Maxed GM",
			actorName = "Yukikaze",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "You missed twice in a row, and now you need Yukikaze the Great to save you. You're hopeless~",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 107090,
			side = 2,
			bgName = "star_level_bg_156",
			factiontag = "Serious Protégé GM",
			actorName = "Essex",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "But wait! If she makes the roll, it's going to–",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 301160,
			side = 2,
			bgName = "star_level_bg_156",
			factiontag = "LCK-Maxed GM",
			actorName = "Yukikaze",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Yukikaze the Great rolls a, you guessed it, 1! Critical success! The shot hits the bomb and sets it off!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "Bam! Get in there!",
					flag = 1
				},
				{
					content = "You're the best, Yukikaze the Great!",
					flag = 2
				}
			}
		},
		{
			portrait = 301160,
			side = 2,
			bgName = "star_level_bg_156",
			factiontag = "LCK-Maxed GM",
			actorName = "Yukikaze",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Heheh. Now to roll for how big the blast is.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 301160,
			side = 2,
			bgName = "star_level_bg_156",
			factiontag = "LCK-Maxed GM",
			actorName = "Yukikaze",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Yukikaze the Great rolls a... Look at that! 1! Critical success!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 502070,
			side = 2,
			bgName = "star_level_bg_156",
			factiontag = "Bookworm GM",
			actorName = "Hai Tien",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I-I can't believe this... My goodness, it's actually happening...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_156",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "What?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 107090,
			side = 2,
			bgName = "star_level_bg_156",
			factiontag = "Serious Protégé GM",
			actorName = "Essex",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Oh boy... Hai Tien, please continue.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 502070,
			side = 2,
			bgName = "star_level_bg_156",
			factiontag = "Bookworm GM",
			actorName = "Hai Tien",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Right... The blast is so, so much bigger than you anticipated. Not only:es it cause further damage to the pillar and fireplace...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 502070,
			side = 2,
			bgName = "star_level_bg_156",
			factiontag = "Bookworm GM",
			nameColor = "#A9F548FF",
			soundeffect = "event./battle/boom2",
			actorName = "Hai Tien",
			hidePaintObj = True,
			say = "It detonates with a massive \"KABOOM!\" and all but cracks the land beneath your feet, making the tiny little castle tremble in fear.",
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
			portrait = 502070,
			side = 2,
			bgName = "star_level_bg_156",
			factiontag = "Bookworm GM",
			actorName = "Hai Tien",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Next, you hear the sound of trees falling, rocks crumbling, and the world shaking...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 502070,
			side = 2,
			bgName = "star_level_bg_156",
			factiontag = "Bookworm GM",
			actorName = "Hai Tien",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Rattle... Clack-clack... Rumble...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 502070,
			side = 2,
			bgName = "star_level_bg_156",
			factiontag = "Bookworm GM",
			actorName = "Hai Tien",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Your vision goes black.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 502070,
			side = 2,
			nameColor = "#FF9B93",
			factiontag = "Bookworm GM",
			blackBg = True,
			bgm = "story-oldcastle-carnival",
			actorName = "Hai Tien",
			hidePaintObj = True,
			say = "This is your morning news.",
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
			portrait = 502070,
			side = 2,
			actorName = "Hai Tien",
			factiontag = "Bookworm GM",
			nameColor = "#FF9B93",
			blackBg = True,
			hidePaintObj = True,
			say = "At 1 AM yesterday, there was an explosion at the old castle on the outskirts of Arkham.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 502070,
			side = 2,
			actorName = "Hai Tien",
			factiontag = "Bookworm GM",
			nameColor = "#FF9B93",
			blackBg = True,
			hidePaintObj = True,
			say = "Police and ambulances rushed to the scene, where they found the bodies of several victims.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 502070,
			side = 2,
			actorName = "Hai Tien",
			factiontag = "Bookworm GM",
			nameColor = "#FF9B93",
			blackBg = True,
			hidePaintObj = True,
			say = "Among them were Lord Manjuu's two daughters, the castle's three servants, and one unidentified person.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 502070,
			side = 2,
			actorName = "Hai Tien",
			factiontag = "Bookworm GM",
			nameColor = "#FF9B93",
			blackBg = True,
			hidePaintObj = True,
			say = "The police have found traces of a homemade bomb where the building suffered a structural collapse, and speculate that it was the cause of the explosion.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 502070,
			side = 2,
			actorName = "Hai Tien",
			factiontag = "Bookworm GM",
			nameColor = "#FF9B93",
			blackBg = True,
			hidePaintObj = True,
			say = "They believe it's likely that this was a crime perpetrated by the unidentified person. The on-scene investigation is ongoing.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			stopbgm = True,
			mode = 1,
			bgm = "story-oldcastle-carnival",
			sequence = {
				{
					"BE-05 - No Survivors Tonight",
					1
				}
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_159",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Are you serious? That was the setup for a bad ending?",
			bgm = "theme-ijndailymeeting",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_159",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Essex, did you realize something bad was going to happen partway through?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 107090,
			side = 2,
			bgName = "star_level_bg_159",
			factiontag = "Serious Protégé GM",
			actorName = "Essex",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Yes... From the moment you let Yukikaze roll the dice.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 101490,
			side = 2,
			bgName = "star_level_bg_159",
			factiontag = "(Self-Proclaimed) Great Detective GM",
			actorName = "Bristol",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Amazing, Commander! You even got to THIS special ending!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 101490,
			side = 2,
			bgName = "star_level_bg_159",
			factiontag = "(Self-Proclaimed) Great Detective GM",
			actorName = "Bristol",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Not only: you have to make the most powerful bomb, you also have to try to hit it with your gun.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 101490,
			side = 2,
			bgName = "star_level_bg_159",
			factiontag = "(Self-Proclaimed) Great Detective GM",
			actorName = "Bristol",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "After missing two shots, at least one has to hit the pillar and cause enough damage to it.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 101490,
			side = 2,
			bgName = "star_level_bg_159",
			factiontag = "(Self-Proclaimed) Great Detective GM",
			actorName = "Bristol",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Then, and only if the final shot hits and is a critical success, it sets off a chain reaction and triggers this ultra-rare ending!",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_159",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "So, I had to not only make the \"right\" choices, but also get the \"right\" dice rolls?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 107090,
			side = 2,
			bgName = "star_level_bg_159",
			factiontag = "Serious Protégé GM",
			actorName = "Essex",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Mhm. Nobody should be able to meet such specific conditions under normal circumstances.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			portrait = 107090,
			side = 2,
			bgName = "star_level_bg_159",
			factiontag = "Serious Protégé GM",
			actorName = "Essex",
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "I was so sure you'd never see that ending. I:n't know whether to call you very lucky or very UNlucky.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_159",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "It took you by complete surprise, so I guess I'm lucky, in a way?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		}
	}
}
