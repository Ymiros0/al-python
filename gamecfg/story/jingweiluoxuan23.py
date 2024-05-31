return {
	fadeOut = 1.5,
	mode = 2,
	id = "JINGWEILUOXUAN23",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			side = 2,
			bgName = "bg_luoxuan_2",
			dir = 1,
			bgmDelay = 1,
			bgm = "hunhe-level",
			actor = 105170,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "Ty, we're getting close to the place where the Sakura Empire Pawns are gathering, right?",
			flashin = {
				delay = 1,
				dur = 1,
				black = True,
				alpha = {
					1,
					0
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
			expression = 1,
			side = 2,
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 107140,
			say = "Yup. If my calculations from the intercepted communications are correct, we'll be at the right coordinates shortly.",
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
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 105170,
			say = "Hmm... It seems strange to me that we haven't even run into any Siren patrols.",
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
			expression = 1,
			side = 2,
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 107140,
			say = "There's a pretty conspicuous absence of mass-produced ships as well.",
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
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 107140,
			say = "If the Reenactment has already ended, the Sirens should be reorganizing their forces accordingly even if the Mirror Sea is still in effect. That's not what we're seeing at all though.",
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
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 107140,
			say = "It's as if...",
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
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 105170,
			say = "They're still trying to lure us in?",
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
			actor = 105170,
			side = 2,
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "(Damnit, we:n't even know if the commander is still here or not...!)",
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
			actor = 105170,
			side = 2,
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "(There's something wrong with this Mirror Sea... I just can't put my finger on it...)",
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
			nameColor = "#ffa500",
			side = 2,
			bgName = "bg_luoxuan_2",
			stopbgm = True,
			dir = 1,
			actor = 900315,
			actorName = "？？？",
			hidePaintObj = True,
			say = "Of course... Most of the normal functionalities of a Mirror Sea have been stripped:wn.",
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
			bgName = "bg_luoxuan_2",
			dir = 1,
			bgmDelay = 1,
			bgm = "deepblue-image",
			actor = 107140,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "Huh? Who are you...?!",
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
			say = "―――！！",
			side = 2,
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			soundeffect = "event./battle/boom2",
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
			bgName = "bg_luoxuan_2",
			dir = 1,
			bgm = "deepblue-image",
			actor = 105170,
			nameColor = "#a9f548",
			hidePaintObj = True,
			say = "That was the only warning shot you'll get. Drop that disguise, or the next shot isn't going to miss.",
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
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 105170,
			say = "You're no Siren at all...",
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
			bgName = "bg_luoxuan_2",
			actorName = "？？？",
			dir = 1,
			actor = 900315,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "Such tremendous firepower... No hesitation at all to aim at your own allies... What is your name...?",
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
			actor = 105170,
			side = 2,
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "New Jersey, Iowa-class battleship of the Eagle Union. Those who try to deceive us by imitating our friends... are no allies of ours!",
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
			bgName = "bg_luoxuan_2",
			actorName = "？？？",
			dir = 1,
			actor = 900315,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "Why are you here... New Jersey?",
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
			actor = 102290,
			side = 2,
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "She... looks just like Helena! I didn't see anything on my radar though!",
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
			actor = 105170,
			side = 2,
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "You're not a Siren, and yet you can't be detected by radar... You're one of the Ashes...",
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
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 105170,
			say = "Boise, help me with manual aiming. We're:ne talking here.",
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
			bgName = "bg_luoxuan_2",
			actorName = "？？？",
			dir = 1,
			actor = 900315,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "Wait, please... I am loyal to the commander...",
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
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 105170,
			say = "How dare you...! What have you:ne with the commander?!",
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
			expression = 6,
			side = 2,
			bgName = "bg_luoxuan_2",
			actorName = "？？？",
			dir = 1,
			actor = 900315,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "Please calm:wn... I am here to guide you to the commander's whereabouts...",
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
			bgName = "bg_luoxuan_2",
			actorName = "？？？",
			dir = 1,
			actor = 900315,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "I would not have exposed myself to you like this if I was intent on attacking you...",
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
			bgName = "bg_luoxuan_2",
			actorName = "？？？",
			dir = 1,
			actor = 900315,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "Please, believe me...",
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
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 105170,
			say = "...Ty, what: you think?",
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
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 107140,
			say = "She has a point. She easily could've utilized this sea fog to ambush us if that was her intent.",
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
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 107140,
			say = "Even if she's one of the Ashes, Commander once said there might be a way to find common ground...",
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
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 105170,
			say = "I:n't trust you, Ashes. But I: trust the commander.",
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
			actor = 105170,
			side = 2,
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "So, where's the commander? You'd better not be trying to trick us.",
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
			bgName = "bg_luoxuan_2",
			actorName = "？？？",
			dir = 1,
			actor = 900315,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "...Thank you. But first, we must defeat our pursuers.",
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
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 105170,
			say = "Pursuers? I didn't see any Sirens following us...",
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
			actor = 105170,
			side = 2,
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			say = "Let me just tell you this - until the commander is back safe and sound,:n't think you've earned an ounce of our trust.",
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
			bgName = "bg_luoxuan_2",
			actorName = "？？？",
			dir = 1,
			actor = 900315,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "There's no use turning around...",
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
			bgName = "bg_luoxuan_2",
			actorName = "？？？",
			dir = 1,
			actor = 900315,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "Our pursuers have already surrounded us.",
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
			bgName = "bg_luoxuan_2",
			actorName = "？？？",
			dir = 1,
			actor = 900315,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "You may not be able to see it on your radar, but they are already all around us.",
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
			bgName = "bg_luoxuan_2",
			actorName = "？？？",
			dir = 1,
			actor = 900315,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "I have hacked into this Mirror Sea, but it is only a matter of time until its automated defenses find us.",
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
			bgName = "bg_luoxuan_2",
			actorName = "？？？",
			dir = 1,
			actor = 900315,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "Just as your eyes can be deceived by the fog, so too can your equipment.",
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
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 105170,
			say = "What are you saying? You did what to the Mirror Sea...?",
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
			expression = 4,
			side = 2,
			bgName = "bg_luoxuan_2",
			actorName = "？？？",
			dir = 1,
			actor = 900315,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "What I make... the Sirens can also unmake.",
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
			bgName = "bg_luoxuan_2",
			actorName = "？？？",
			dir = 1,
			actor = 900315,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "What you see... is only what the Sirens wish for you to see.",
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
			bgName = "bg_luoxuan_2",
			actorName = "？？？",
			dir = 1,
			actor = 900315,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "Mirror hacking protocol - disable stealth system.",
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
			bgName = "bg_luoxuan_2",
			nameColor = "#ffa500",
			dir = 1,
			soundeffect = "event./ui/finger",
			actor = 900315,
			actorName = "？？？",
			hidePaintObj = True,
			say = "Now, look closely at your radars.",
			flashout = {
				dur = 0.15,
				alpha = {
					0,
					1
				}
			},
			flashin = {
				delay = 0.2,
				dur = 0.2,
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
			expression = 5,
			side = 2,
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 105170,
			say = "Are these:ts... all Sirens?! How are there so many of them?!",
			dialogShake = {
				speed = 0.09,
				x = 10,
				number = 2
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
			expression = 5,
			side = 2,
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 105170,
			say = "You led us into this ambush!",
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
			bgName = "bg_luoxuan_2",
			actorName = "？？？",
			dir = 1,
			actor = 900315,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "The protocol I put into place has temporarily increased the sensitivity of your equipment.",
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
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#a9f548",
			actor = 107140,
			say = "Wait, so a lot of these are ghost signals? Are you the reason why Essex, back:...",
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
			actor = 900315,
			nameColor = "#ffa500",
			bgName = "bg_luoxuan_2",
			hidePaintObj = True,
			dir = 1,
			actorName = "？？？",
			side = 2,
			say = "I will deconstruct the Sirens' systems. Please eliminate the real enemies in the vicinity.",
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
			bgName = "bg_luoxuan_2",
			actorName = "？？？",
			dir = 1,
			actor = 900315,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "We will not be able to reach the commander's location with all these Sirens in the way...",
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
			bgName = "bg_luoxuan_6",
			actorName = "？？？",
			dir = 1,
			blackBg = True,
			soundeffect = "event./battle/boom2",
			actor = 900315,
			nameColor = "#ffa500",
			hidePaintObj = True,
			say = "Three, two, one... Shutdown...!",
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
			},
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
