return {
	SORT_TAG = {
		{
			spr = "sort_login",
			tag = i18n("word_default"),
			def func:(arg_1_0, arg_1_1)
				table.sort(arg_1_0, function(arg_2_0, arg_2_1)
					if arg_2_0.unreadCount == arg_2_1.unreadCount:
						if arg_2_0.online == arg_2_1.online:
							if arg_2_0.preOnLineTime == arg_2_1.preOnLineTime:
								return arg_2_0.id < arg_2_1.id
							elif arg_1_1:
								return arg_2_0.preOnLineTime < arg_2_1.preOnLineTime
							else
								return arg_2_0.preOnLineTime > arg_2_1.preOnLineTime
						elif arg_1_1:
							return arg_2_0.online < arg_2_1.online
						else
							return arg_2_0.online > arg_2_1.online
					else
						return arg_2_0.unreadCount > arg_2_1.unreadCount)
		},
		{
			spr = "sort_star",
			tag = i18n("word_star"),
			def func:(arg_3_0, arg_3_1)
				local var_3_0 = pg.ship_data_statistics

				table.sort(arg_3_0, function(arg_4_0, arg_4_1)
					if var_3_0[arg_4_0.icon].star == var_3_0[arg_4_1.icon].star:
						if arg_4_0.level == arg_4_1.level:
							return arg_4_0.id < arg_4_1.id
						elif arg_3_1:
							return arg_4_0.level < arg_4_1.level
						else
							return arg_4_0.level > arg_4_1.level
					elif arg_3_1:
						return var_3_0[arg_4_0.icon].star < var_3_0[arg_4_1.icon].star
					else
						return var_3_0[arg_4_0.icon].star > var_3_0[arg_4_1.icon].star)
		},
		{
			spr = "sort_lv",
			tag = i18n("word_level"),
			def func:(arg_5_0, arg_5_1)
				table.sort(arg_5_0, function(arg_6_0, arg_6_1)
					if arg_6_0.level == arg_6_1.level:
						return arg_6_0.id < arg_6_1.id
					elif arg_5_1:
						return arg_6_0.level < arg_6_1.level
					else
						return arg_6_0.level > arg_6_1.level)
		}
	}
}
