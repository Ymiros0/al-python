return {
	fadeOut = 1.5,
	mode = 2,
	id = "LAISHAGUANQIA3",
	once = True,
	fadeType = 2,
	fadein = 1.5,
	scripts = {
		{
			side = 2,
			nameColor = "#A9F548FF",
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			stopbgm = True,
			say = "Mirror Sea - In the past",
			bgm = "story-6",
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
			}
		},
		{
			nameColor = "#A9F548FF",
			side = 2,
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			say = "Inside Purity's temporary command post...",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			actor = 900233,
			nameColor = "#A9F548FF",
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			dir = 1,
			actorName = "Purity",
			side = 2,
			say = "Heh heh! So whaddya think? This baby oughta raise your combat capabilities by at least 300%!",
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
			actor = 10900060,
			side = 2,
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "So this is a \"rigging,\" as you called it... Yes, I: feel stronger.",
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
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 10900060,
			say = "Hrm... How:es one attack with it? Do I simply aim straight ahead of me and fire?",
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
			bgName = "bg_zhuiluo_2",
			actorName = "Purity",
			dir = 1,
			actor = 900233,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Yeah, that's the– Whoa, you trying to kill me?! Point that thing AWAY from me!",
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
			expression = 2,
			side = 2,
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			actor = 900233,
			actorName = "Purity",
			nameColor = "#A9F548FF",
			say = "If you want some target practice, shoot at Tester's mass-produced mooks outside instead.",
			typewriter = {
				speed = 0.05,
				speedUp = 0.01
			}
		},
		{
			expression = 3,
			side = 2,
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 10900060,
			say = "Refine my skills through live combat, you say? A wise suggestion. And you? What will you be:ing in the meanwhile?",
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
			bgName = "bg_zhuiluo_2",
			actorName = "Purity",
			dir = 1,
			actor = 900233,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Me? I just pinpointed the location of the Mirror Sea's control center. That's where I'm gonna find Tester.",
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
			actor = 900233,
			nameColor = "#A9F548FF",
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			dir = 1,
			actorName = "Purity",
			side = 2,
			say = "Take my fleet and attack head-on. While she's distracted, I'll sneak in behind the lines and end her sorry existence with one blow!",
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
			bgName = "bg_zhuiluo_2",
			actorName = "Purity",
			dir = 1,
			actor = 900233,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "...But if we fail, it's gonna come:wn to a war of attrition, and we ain't winning one of those.",
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
			actor = 10900060,
			side = 2,
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Oho. And you're sure that you'll be able to defeat her in a one-on-one?",
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
			bgName = "bg_zhuiluo_2",
			actorName = "Purity",
			dir = 1,
			actor = 900233,
			nameColor = "#A9F548FF",
			hidePaintObj = True,
			say = "Hell yeah I will! One-on-one fights are my specialty!",
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
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 10900060,
			say = "I see. You Sirens: remind me of the Philuscha somewhat, your kind having both clearly defined roles and unique abilities.",
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
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 10900060,
			say = "Knowing that, I leave Tester to your capable hands. In the meantime, I shall lead your fleet.",
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
			bgName = "bg_zhuiluo_2",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 10900060,
			say = "Heheh... It will be interesting to see what destruction I can cause with this rigging in tandem with my natural powers.",
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
			stopbgm = True,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			nameColor = "#A9F548FF",
			bgmDelay = 2,
			say = "Mirror Sea Ruins - Land of Beginnings",
			bgm = "ryza-az-battle",
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
			bgName = "bg_ryza_1",
			say = "KABOOOM!",
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
			expression = 2,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 305140,
			say = "That ought to be the last one! Are you two okay?!",
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
			actor = 10900050,
			side = 2,
			bgName = "bg_ryza_1",
			nameColor = "#A9F548FF",
			dir = 1,
			say = "We're fine... Thank you.",
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
			expression = 6,
			side = 2,
			bgName = "bg_ryza_1",
			actor = 10900040,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "No problems here. Suruga, you're one tough fighter. I've felled my fair share of behemoths, but it's as if the sea is your playground...",
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
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 301290,
			say = "Suruga, I've come to your aid—h-hey, is it just me, or is the fight already over?!",
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
			expression = 1,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 207050,
			say = "That is our Suruga for you, ever at home on the battlefield. I presume your acquaintances here are more of Ryza's friends?",
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
			actor = 10900010,
			side = 2,
			bgName = "bg_ryza_1",
			nameColor = "#A9F548FF",
			dir = 1,
			say = "Lila, Serri! You ended up here, too?!",
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
			bgName = "bg_ryza_1",
			actor = 10900020,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "It has been so long, Miss Lila and Miss Serri.",
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
			expression = 1,
			side = 2,
			bgName = "bg_ryza_1",
			actor = 10900030,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Have you two been well?",
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
			expression = 6,
			side = 2,
			bgName = "bg_ryza_1",
			actor = 10900040,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Ryza, Claudia, even Patricia... What a place to run into you girls.",
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
			expression = 7,
			side = 2,
			bgName = "bg_ryza_1",
			actor = 10900050,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Hey, Ryza... It's been a while. Are we in another world, or something?",
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
			expression = 1,
			side = 2,
			bgName = "bg_ryza_1",
			actor = 10900010,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Seems like it. So you've already figured things out, Serri?",
			hidePaintEquip = True,
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
			expression = 2,
			side = 2,
			bgName = "bg_ryza_1",
			actor = 10900050,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "No... I just sensed that the flow of the air here is nothing like what I'm used to.",
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
			expression = 1,
			side = 2,
			bgName = "bg_ryza_1",
			actor = 10900050,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Guess that means I'm right.",
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
			bgName = "bg_ryza_1",
			actor = 10900010,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "We just learned about it a little while ago, but basically...",
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
			expression = 1,
			side = 2,
			bgName = "bg_ryza_1",
			actor = 10900040,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Azur Lane, shipgirls, the Mirror Sea, Sirens... I've never heard of any of this.",
			hidePaintEquip = True,
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
			expression = 5,
			side = 2,
			bgName = "bg_ryza_1",
			actor = 10900040,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "But thanks. I'm starting to understand the mess we've gotten into now.",
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
			bgName = "bg_ryza_1",
			actor = 10900050,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "If this really is another land...: Formidable, you'd better be careful. Those enemies had the aura of Philuscha on them...",
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
			bgName = "bg_ryza_1",
			actor = 10900050,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "The Philuscha may have been brought here alongside us.",
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
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 207050,
			say = "These so-called \"Philuscha,\" I presume, are lifelong enemies you've fought in your own world?",
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
			bgName = "bg_ryza_1",
			actor = 10900050,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "I:n't know about lifelong... but sure, kind of.",
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
			actor = 207050,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Then the Philuscha you know are not machines, but living beings?",
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
			bgName = "bg_ryza_1",
			actor = 10900040,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Yeah. They hate water by nature, and... Huh. Come to think of it, those enemies were off.",
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
			expression = 6,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 207050,
			say = "Interesting that you should mention that. While everyone was talking, I took the liberty of searching the enemies' remains.",
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
			actor = 207050,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Based on my investigation, I believe that those were mass-produced models made from Sirens' knowledge of the Philuscha you know.",
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
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 207050,
			say = "I base this off of the fact that our enemies' remains were all mechanical. It seems that the Philuscha of your world were not truly brought here.",
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
			bgName = "bg_ryza_1",
			actor = 10900050,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Guess not... Well, at least that's some good news.",
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
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601080,
			say = "Welp, we've finally got a moment of peace. Say, everyone! It's all dark out, and I:n't wanna stay in such a messy place...",
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
			actor = 601080,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Most of all, you've all gotta be tired. How about we eat and rest at my mass-produced ship?",
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
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601080,
			say = "Trading scoops is a lot more efficient when you've got a full belly and a rested body!",
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
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 301290,
			say = "I concur with Alfredo! Honestly, I'm famished...",
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
			bgName = "bg_ryza_1",
			actor = 10900010,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Oh boy, otherworldly delicious foods?! I'm so in! C'mon, let's go! I'm hungry for both food and knowledge!",
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
			expression = 1,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 101490,
			say = "Hehehe! I've been taking notes this whole time. Let's solve some mysteries over a big meal!",
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
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 207050,
			say = "There you have it. Please lead the way, Alfredo.",
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
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			actor = 601080,
			say = "Roger that! Come, everyone. to the mass-produced model of Sardegna's own Oriani-class destroyer!",
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
			actor = 601080,
			side = 2,
			bgName = "bg_ryza_1",
			hidePaintObj = True,
			dir = 1,
			nameColor = "#A9F548FF",
			say = "Our Sardegnian cuisine is so good, it'll make you forget you're smack-dab in the middle of a battlefield! Now get those butts into gear and follow my lead!",
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
