return {
	id = "CONGLINGKAISHIMOWANG13-3",
	mode = 2,
	fadeOut = 1.5,
	scripts = {
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_545",
			soundeffect = "event./battle/boom2",
			say = "KABOOOM!",
			bgm = "story-mmorpg",
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
			portrait = 403022,
			side = 2,
			bgName = "star_level_bg_545",
			factiontag = "Dragonlord",
			dir = 1,
			nameColor = "#FF9B93",
			actorName = "Blücher",
			say = "Ugh! Seriously?!",
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
			portrait = 403022,
			side = 2,
			bgName = "star_level_bg_545",
			factiontag = "Dragonlord",
			dir = 1,
			nameColor = "#FF9B93",
			actorName = "Blücher",
			say = "Don't assume you've won already!",
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
			portrait = 403022,
			side = 2,
			bgName = "star_level_bg_545",
			factiontag = "Dragonlord",
			dir = 1,
			nameColor = "#FF9B93",
			actorName = "Blücher",
			say = "Revenge WILL be mine!",
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
			portrait = 403022,
			side = 2,
			bgName = "star_level_bg_545",
			factiontag = "Dragonlord",
			dir = 1,
			nameColor = "#FF9B93",
			actorName = "Blücher",
			say = "I'll be back, and:– Whoa, whooooaaaa! Mind the turbulence, dragooooon!",
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
					name = "speed"
				}
			},
			dialogShake = {
				speed = 0.08,
				x = 15,
				number = 2
			}
		},
		{
			side = 2,
			nameColor = "#A9F548FF",
			bgName = "star_level_bg_545",
			say = "Blücher is dragged along helplessly by her dragon. The two disappear like shooting stars among the distant dark clouds.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			effects = {
				{
					active = False,
					name = "speed"
				}
			}
		},
		{
			actor = 501020,
			side = 2,
			bgName = "star_level_bg_545",
			factiontag = "The Hero",
			dir = 1,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Dang. The dragon's scales were too thick and it got away.",
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
			bgName = "star_level_bg_545",
			factiontag = "Saint of the Holy Church",
			dir = 1,
			actor = 802020,
			nameColor = "#A9F548FF",
			say = "Perhaps so, but this is still a major victory for us.",
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
			bgName = "star_level_bg_545",
			factiontag = "Saint of the Holy Church",
			dir = 1,
			actor = 802020,
			nameColor = "#A9F548FF",
			say = "With their general out of the picture, it's only a matter of time before their rank and file collapses.",
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
			actor = 802020,
			side = 2,
			bgName = "star_level_bg_545",
			factiontag = "Saint of the Holy Church",
			dir = 1,
			nameColor = "#A9F548FF",
			say = "And to think you did this by provoking her,: taking her out with flawless teamwork...",
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
			bgName = "star_level_bg_545",
			factiontag = "Saint of the Holy Church",
			dir = 1,
			actor = 802020,
			nameColor = "#A9F548FF",
			say = "You truly are an exceptional strategist, Commander.",
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
			actor = 802020,
			side = 2,
			bgName = "star_level_bg_545",
			factiontag = "Saint of the Holy Church",
			dir = 1,
			nameColor = "#A9F548FF",
			say = "One day, you and your party may just defeat the Demon King and restore peace to the world.",
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
					content = "We will, and that's a promise!",
					flag = 1
				},
				{
					content = "You're flattering me.",
					flag = 2
				}
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "star_level_bg_545",
			factiontag = "Saint of the Holy Church",
			dir = 1,
			optionFlag = 1,
			actor = 802020,
			nameColor = "#A9F548FF",
			say = "Heehee. Your confidence brings me hope.",
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
			actor = 802020,
			side = 2,
			bgName = "star_level_bg_545",
			factiontag = "Saint of the Holy Church",
			dir = 1,
			optionFlag = 1,
			nameColor = "#A9F548FF",
			say = "I look forward to the day I'll hear about how your group took the Demon King out.",
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
			bgName = "star_level_bg_545",
			factiontag = "Commander",
			nameColor = "#A9F548FF",
			optionFlag = 2,
			say = "It's not like we've defeated their whole army yet. Save the praise and medals for when it's warranted.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "star_level_bg_545",
			factiontag = "Saint of the Holy Church",
			dir = 1,
			optionFlag = 2,
			actor = 802020,
			nameColor = "#A9F548FF",
			say = "Yes, I suppose. We mustn't let our guard:wn.",
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
			actor = 802020,
			side = 2,
			bgName = "star_level_bg_545",
			factiontag = "Saint of the Holy Church",
			dir = 1,
			optionFlag = 2,
			nameColor = "#A9F548FF",
			say = "Then let us speak again come the victory celebration.",
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