return {
	id = "JIARIXINTIAODAYOULUN30",
	mode = 2,
	fadeOut = 1.5,
	scripts = {
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			say = "I've come to the ship's cargo unloading station. For some reason, there's a huge fish tank sitting here.",
			bgm = "story-niceship-soft",
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
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "(You could fit a whale in there. Odd that it's empty.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			say = "As I start to wonder how it got here, I suddenly hear Huan Ch'ang speaking.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 504010,
			say = "Th-this can't be right! Or my divination would be wrong...",
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
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 504010,
			say = "Harbin got me such a large tank, and yet...",
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
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			say = "Her eyes are on the floor as she walks toward me, muttering something under her breath.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 5,
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 504010,
			say = "C-Commander?!",
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
			},
			options = {
				{
					content = "(Offer her your condolences.)",
					flag = 1
				},
				{
					content = "(Give her your sympathy.)",
					flag = 2
				}
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 504010,
			say = "No, I can't accept this...",
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
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 108020,
			say = "What's up, Huan? Why can't you catch any fish?",
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
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			say = "Albacore happens to pass by and overhear our conversation. She waltzes over to us with marked interest.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 504010,
			say = "*sigh*...",
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
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 108020,
			say = "Don't fret! I'll give you a hand! Start up the fish catchamatron!",
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
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "The what now?",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 108020,
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "You:n't know? This has been on the ship the whole time! You just put a submarine in there and send 'er:wn to catch some fish.",
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
					content = "Why a submarine?",
					flag = 1
				},
				{
					content = "Who came up with this?",
					flag = 2
				},
				{
					content = "When did they add that?",
					flag = 3
				}
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 108020,
			say = "Tsk, tsk, always so concerned with the details. It:esn't matter!",
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
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			say = "Gears and chains start to rattle,: Albacore boards the \"fish catchamatron.\"",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 108020,
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Oh, I forgot to mention – someone needs to steer it from up here. Otherwise you can't determine the angle to plunge it into the sea.",
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
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 108020,
			say = "That someone will be you, Commander!",
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
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "Alright:.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			say = "Doing as she asks, I get in front of the control panel and operate the chain swing.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			say = "All I need to: is decide on the angle and the device will send Albacore:wn into the sea.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			say = "After fiddling with the controls a few times, we get a bite.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 108020,
			say = "I got one! Now pull me back up!",
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
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			say = "The winch fires up and reels in the chain. The catch comes into view, and it's revealed that Albacore caught... a blobfish.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "(I'll be damned. She caught a blobfish at–)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "(Hang on! Blobfish:n't even swim up to these depths!)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 504010,
			say = "......",
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
			actor = 301050,
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "I was passing by and noticed how Huan Ch'ang looked upset that there are no fish to put in the tank.",
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
			actor = 301050,
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "I can help with that. Yes, as long as any kind of fish will:.",
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
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 504010,
			say = "That's very kind of you, but you see...",
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
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			say = "Before Huan Ch'ang can even finish, Ayanami takes a few steps forward and blows a whistle.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			say = "Moments later, a seagull flies over from the garden and squawks a couple of times. It and Ayanami must have some sort of deal.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			},
			options = {
				{
					content = "What's the deal with that bird?",
					flag = 1
				},
				{
					content = "That's old Squawkey, isn't it?",
					flag = 2
				}
			}
		},
		{
			actor = 301050,
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			dir = 1,
			optionFlag = 1,
			nameColor = "#A9F548FF",
			say = "He's a friend I made long ago on Seabreeze Island. He came to meet us as soon as we anchored.",
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
			actor = 301050,
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			dir = 1,
			optionFlag = 2,
			nameColor = "#A9F548FF",
			say = "Yes! I'm surprised you remembered his name. He came flying to meet us as soon as we made landfall.",
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
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "(Ahh. So that's why I didn't see Ayanami or any birds when I went to check on the roosting spot on the island. They'd already gone back to the ship.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			say = "Right:, some things fall from the sky and land on the deck with a flop.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			say = "It's a couple of fish. Squawkey:ve:wn from the skies and caught them underwater with his beak.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 301050,
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Don't feel sad, Huan. Now you have lots of fish.",
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
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 504010,
			say = "I can't believe this... I'm losing to a bird!",
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
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			say = "Huan Ch'ang makes a sad expression and mumbles something.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 1,
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 504010,
			say = "No, actually... Thanks... I need to go and be alone for a bit...",
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
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			say = "With a wave of her hand, she leaves the scene.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 0,
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			say = "(She looked pretty shocked about that.)",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			say = "Afterward, I, Ayanami, and Albacore put the fish inside the tank.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "star_level_bg_179",
			hidePaintObj = True,
			say = "I'll quickly clean up the place a bit: go have a look somewhere else.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		}
	}
}
