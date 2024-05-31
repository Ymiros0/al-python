local var_0_0 = class("AppreciateProxy", import(".NetProxy"))

def var_0_0.register(arg_1_0):
	arg_1_0.initData()
	arg_1_0.checkPicFileState()
	arg_1_0.checkMusicFileState()

def var_0_0.initData(arg_2_0):
	arg_2_0.picManager = BundleWizard.Inst.GetGroupMgr("GALLERY_PIC")
	arg_2_0.musicManager = BundleWizard.Inst.GetGroupMgr("GALLERY_BGM")
	arg_2_0.reForVer = PathMgr.MD5Result
	arg_2_0.galleryPicUnLockIDLIst = {}
	arg_2_0.galleryPicExistStateTable = {}
	arg_2_0.galleryPicLikeIDList = {}
	arg_2_0.musicUnLockIDLIst = {}
	arg_2_0.musicExistStateTable = {}
	arg_2_0.musicLikeIDList = {}
	arg_2_0.mangaReadIDList = {}
	arg_2_0.mangaLikeIDList = {}
	arg_2_0.galleryRunData = {
		middleIndex = 1,
		dateValue = GalleryConst.Data_All_Value,
		sortValue = GalleryConst.Sort_Order_Up,
		likeValue = GalleryConst.Filte_Normal_Value,
		bgFilteValue = GalleryConst.Loading_BG_NO_Filte
	}
	arg_2_0.musicRunData = {
		middleIndex = 1,
		sortValue = MusicCollectionConst.Sort_Order_Up,
		likeValue = MusicCollectionConst.Filte_Normal_Value
	}

def var_0_0.checkPicFileState(arg_3_0):
	local var_3_0
	local var_3_1

	for iter_3_0, iter_3_1 in ipairs(pg.gallery_config.all):
		local var_3_2 = pg.gallery_config[iter_3_1].illustration
		local var_3_3 = GalleryConst.PIC_PATH_PREFIX .. var_3_2
		local var_3_4 = checkABExist(var_3_3)

		arg_3_0.galleryPicExistStateTable[iter_3_1] = var_3_4

def var_0_0.checkMusicFileState(arg_4_0):
	local var_4_0
	local var_4_1

	for iter_4_0, iter_4_1 in ipairs(pg.music_collect_config.all):
		local var_4_2 = pg.music_collect_config[iter_4_1].music
		local var_4_3 = MusicCollectionConst.MUSIC_SONG_PATH_PREFIX .. var_4_2 .. ".b"
		local var_4_4 = checkABExist(var_4_3)

		arg_4_0.musicExistStateTable[iter_4_1] = var_4_4

def var_0_0.updatePicFileExistStateTable(arg_5_0, arg_5_1, arg_5_2):
	arg_5_0.galleryPicExistStateTable[arg_5_1] = arg_5_2

def var_0_0.updateMusicFileExistStateTable(arg_6_0, arg_6_1, arg_6_2):
	arg_6_0.musicExistStateTable[arg_6_1] = arg_6_2

def var_0_0.getPicExistStateByID(arg_7_0, arg_7_1):
	if not arg_7_1:
		assert("不能为空的picID." .. tostring(arg_7_1))

	return arg_7_0.galleryPicExistStateTable[arg_7_1]

def var_0_0.getMusicExistStateByID(arg_8_0, arg_8_1):
	if not arg_8_1:
		assert("不能为空的musicID." .. tostring(arg_8_1))

	return arg_8_0.musicExistStateTable[arg_8_1]

def var_0_0.getSinglePicConfigByID(arg_9_0, arg_9_1):
	local var_9_0 = pg.gallery_config[arg_9_1]

	if var_9_0:
		return var_9_0
	else
		assert(False, "不存在的插画ID." .. tostring(arg_9_1))

def var_0_0.getSingleMusicConfigByID(arg_10_0, arg_10_1):
	local var_10_0 = pg.music_collect_config[arg_10_1]

	if var_10_0:
		return var_10_0
	else
		assert(False, "不存在的音乐ID." .. tostring(arg_10_1))

def var_0_0.updateGalleryRunData(arg_11_0, arg_11_1, arg_11_2, arg_11_3, arg_11_4, arg_11_5):
	arg_11_0.galleryRunData.dateValue = arg_11_1 and arg_11_1 or arg_11_0.galleryRunData.dateValue
	arg_11_0.galleryRunData.sortValue = arg_11_2 and arg_11_2 or arg_11_0.galleryRunData.sortValue
	arg_11_0.galleryRunData.middleIndex = arg_11_3 and arg_11_3 or arg_11_0.galleryRunData.middleIndex
	arg_11_0.galleryRunData.likeValue = arg_11_4 and arg_11_4 or arg_11_0.galleryRunData.likeValue
	arg_11_0.galleryRunData.bgFilteValue = arg_11_5 and arg_11_5 or arg_11_0.galleryRunData.bgFilteValue

def var_0_0.updateMusicRunData(arg_12_0, arg_12_1, arg_12_2, arg_12_3):
	arg_12_0.musicRunData.sortValue = arg_12_1 and arg_12_1 or arg_12_0.musicRunData.sortValue
	arg_12_0.musicRunData.middleIndex = arg_12_2 and arg_12_2 or arg_12_0.musicRunData.middleIndex
	arg_12_0.musicRunData.likeValue = arg_12_3 and arg_12_3 or arg_12_0.musicRunData.likeValue

def var_0_0.getGalleryRunData(arg_13_0, arg_13_1):
	return arg_13_0.galleryRunData

def var_0_0.getMusicRunData(arg_14_0, arg_14_1):
	return arg_14_0.musicRunData

def var_0_0.isPicNeedUnlockByID(arg_15_0, arg_15_1):
	local var_15_0 = arg_15_0.getPicUnlockMaterialByID(arg_15_1)
	local var_15_1 = arg_15_0.getSinglePicConfigByID(arg_15_1)

	if var_15_1:
		local var_15_2 = var_15_1.unlock_level

		if var_15_2[1] == 1 and var_15_2[2] == 0:
			if #var_15_0 == 0:
				return False
			else
				return True
		else
			return True
	else
		assert(False, "不存在的插画ID." .. arg_15_1)

def var_0_0.isMusicNeedUnlockByID(arg_16_0, arg_16_1):
	local var_16_0 = arg_16_0.getMusicUnlockMaterialByID(arg_16_1)
	local var_16_1 = arg_16_0.getSingleMusicConfigByID(arg_16_1)

	if var_16_1:
		local var_16_2 = var_16_1.unlock_level

		if var_16_2[1] == 1 and var_16_2[2] == 0:
			if #var_16_0 == 0:
				return False
			else
				return True
		else
			return True
	else
		assert(False, "不存在的音乐ID." .. arg_16_1)

def var_0_0.getPicUnlockMaterialByID(arg_17_0, arg_17_1):
	local var_17_0 = arg_17_0.getSinglePicConfigByID(arg_17_1)

	if var_17_0:
		local var_17_1 = var_17_0.unlock_cost
		local var_17_2 = {}

		for iter_17_0, iter_17_1 in ipairs(var_17_1):
			local var_17_3 = {
				type = iter_17_1[1],
				id = iter_17_1[2],
				count = iter_17_1[3]
			}

			var_17_2[#var_17_2 + 1] = var_17_3

		return var_17_2
	else
		assert(False, "不存在的插画ID." .. arg_17_1)

def var_0_0.getMusicUnlockMaterialByID(arg_18_0, arg_18_1):
	local var_18_0 = arg_18_0.getSingleMusicConfigByID(arg_18_1)

	if var_18_0:
		local var_18_1 = var_18_0.unlock_cost
		local var_18_2 = {}

		for iter_18_0, iter_18_1 in ipairs(var_18_1):
			local var_18_3 = {
				type = iter_18_1[1],
				id = iter_18_1[2],
				count = iter_18_1[3]
			}

			var_18_2[#var_18_2 + 1] = var_18_3

		return var_18_2
	else
		assert(False, "不存在的音乐ID." .. arg_18_1)

def var_0_0.isPicNeedUnlockMaterialByID(arg_19_0, arg_19_1):
	local var_19_0 = arg_19_0.getPicUnlockMaterialByID(arg_19_1)

	if #var_19_0 == 0:
		return False
	else
		return var_19_0

def var_0_0.isMusicNeedUnlockMaterialByID(arg_20_0, arg_20_1):
	local var_20_0 = arg_20_0.getMusicUnlockMaterialByID(arg_20_1)

	if #var_20_0 == 0:
		return False
	else
		return var_20_0

def var_0_0.getPicUnlockTipTextByID(arg_21_0, arg_21_1):
	local var_21_0 = arg_21_0.getSinglePicConfigByID(arg_21_1)

	if var_21_0:
		return var_21_0.illustrate
	else
		assert(False, "不存在的插画ID." .. arg_21_1)

def var_0_0.getMusicUnlockTipTextByID(arg_22_0, arg_22_1):
	local var_22_0 = arg_22_0.getSingleMusicConfigByID(arg_22_1)

	if var_22_0:
		return var_22_0.illustrate
	else
		assert(False, "不存在的音乐ID." .. arg_22_1)

def var_0_0.getResultForVer(arg_23_0):
	return arg_23_0.reForVer

def var_0_0.clearVer(arg_24_0):
	arg_24_0.reForVer = None

def var_0_0.addPicIDToUnlockList(arg_25_0, arg_25_1):
	if table.contains(arg_25_0.galleryPicUnLockIDLIst, arg_25_1):
		print("already exist picID." .. arg_25_1)
	else
		arg_25_0.galleryPicUnLockIDLIst[#arg_25_0.galleryPicUnLockIDLIst + 1] = arg_25_1

def var_0_0.addMusicIDToUnlockList(arg_26_0, arg_26_1):
	if table.contains(arg_26_0.musicUnLockIDLIst, arg_26_1):
		print("already exist musicID." .. arg_26_1)
	else
		arg_26_0.musicUnLockIDLIst[#arg_26_0.musicUnLockIDLIst + 1] = arg_26_1

def var_0_0.addMangaIDToReadList(arg_27_0, arg_27_1):
	if table.contains(arg_27_0.mangaReadIDList, arg_27_1):
		print("already exist mangaID." .. arg_27_1)
	else
		table.insert(arg_27_0.mangaReadIDList, arg_27_1)

def var_0_0.initMangaReadIDList(arg_28_0, arg_28_1):
	arg_28_0.mangaReadIDList = {}

	for iter_28_0, iter_28_1 in ipairs(arg_28_1):
		for iter_28_2 = 1, 32:
			if bit.band(iter_28_1, bit.lshift(1, iter_28_2 - 1)) != 0:
				local var_28_0 = (iter_28_0 - 1) * 32 + iter_28_2

				arg_28_0.addMangaIDToReadList(var_28_0)

	MangaConst.setVersionAndNewCount()

def var_0_0.getMangaReadIDList(arg_29_0):
	return arg_29_0.mangaReadIDList

def var_0_0.addMangaIDToLikeList(arg_30_0, arg_30_1):
	if table.contains(arg_30_0.mangaLikeIDList, arg_30_1):
		print("already exist mangaID." .. arg_30_1)
	else
		table.insert(arg_30_0.mangaLikeIDList, arg_30_1)

def var_0_0.removeMangaIDFromLikeList(arg_31_0, arg_31_1):
	if table.contains(arg_31_0.mangaLikeIDList, arg_31_1):
		table.removebyvalue(arg_31_0.mangaLikeIDList, arg_31_1, True)
	else
		print("not exist mangaID." .. arg_31_1)

def var_0_0.initMangaLikeIDList(arg_32_0, arg_32_1):
	arg_32_0.mangaLikeIDList = {}

	for iter_32_0, iter_32_1 in ipairs(arg_32_1):
		for iter_32_2 = 1, 32:
			if bit.band(iter_32_1, bit.lshift(1, iter_32_2 - 1)) != 0:
				local var_32_0 = (iter_32_0 - 1) * 32 + iter_32_2

				arg_32_0.addMangaIDToLikeList(var_32_0)

def var_0_0.getMangaLikeIDList(arg_33_0):
	return arg_33_0.mangaLikeIDList

def var_0_0.isPicUnlockedByID(arg_34_0, arg_34_1):
	if table.contains(arg_34_0.galleryPicUnLockIDLIst, arg_34_1):
		return True
	else
		return False

def var_0_0.isMusicUnlockedByID(arg_35_0, arg_35_1):
	if table.contains(arg_35_0.musicUnLockIDLIst, arg_35_1):
		return True
	else
		return False

def var_0_0.isPicUnlockableByID(arg_36_0, arg_36_1):
	local var_36_0 = getProxy(PlayerProxy).getData().level
	local var_36_1 = arg_36_0.getSinglePicConfigByID(arg_36_1)

	if var_36_1:
		local var_36_2 = var_36_1.unlock_level
		local var_36_3 = var_36_2[1]
		local var_36_4 = var_36_2[2]

		if var_36_3 <= var_36_0:
			return True
		elif var_36_4 == GalleryConst.Still_Show_On_Lock:
			return False, True
		else
			return False, False

def var_0_0.isMusicUnlockableByID(arg_37_0, arg_37_1):
	local var_37_0 = getProxy(PlayerProxy).getData().level
	local var_37_1 = arg_37_0.getSingleMusicConfigByID(arg_37_1)

	if var_37_1:
		local var_37_2 = var_37_1.unlock_level
		local var_37_3 = var_37_2[1]
		local var_37_4 = var_37_2[2]

		if var_37_3 <= var_37_0:
			return True
		elif var_37_4 == MusicCollectionConst.Still_Show_On_Lock:
			return False, True
		else
			return False, False

def var_0_0.addPicIDToLikeList(arg_38_0, arg_38_1):
	if table.contains(arg_38_0.galleryPicLikeIDList, arg_38_1):
		print("already exist picID." .. arg_38_1)
	else
		arg_38_0.galleryPicLikeIDList[#arg_38_0.galleryPicLikeIDList + 1] = arg_38_1

def var_0_0.removePicIDFromLikeList(arg_39_0, arg_39_1):
	for iter_39_0, iter_39_1 in ipairs(arg_39_0.galleryPicLikeIDList):
		if iter_39_1 == arg_39_1:
			table.remove(arg_39_0.galleryPicLikeIDList, iter_39_0)

			return

	print("no exist picID." .. arg_39_1)

def var_0_0.isLikedByPicID(arg_40_0, arg_40_1):
	return table.contains(arg_40_0.galleryPicLikeIDList, arg_40_1)

def var_0_0.addMusicIDToLikeList(arg_41_0, arg_41_1):
	if table.contains(arg_41_0.musicLikeIDList, arg_41_1):
		print("already exist picID." .. arg_41_1)
	else
		arg_41_0.musicLikeIDList[#arg_41_0.musicLikeIDList + 1] = arg_41_1

def var_0_0.removeMusicIDFromLikeList(arg_42_0, arg_42_1):
	for iter_42_0, iter_42_1 in ipairs(arg_42_0.musicLikeIDList):
		if iter_42_1 == arg_42_1:
			table.remove(arg_42_0.musicLikeIDList, iter_42_0)

			return

	print("no exist musicID." .. arg_42_1)

def var_0_0.isLikedByMusicID(arg_43_0, arg_43_1):
	return table.contains(arg_43_0.musicLikeIDList, arg_43_1)

def var_0_0.isGalleryHaveNewRes(arg_44_0):
	if PlayerPrefs.GetInt("galleryVersion", 0) < GalleryConst.Version:
		return True
	else
		return False

def var_0_0.isMusicHaveNewRes(arg_45_0):
	if PlayerPrefs.GetInt("musicVersion", 0) < MusicCollectionConst.Version:
		return True
	else
		return False

def var_0_0.isMangaHaveNewRes(arg_46_0):
	if PlayerPrefs.GetInt("mangaVersion", 0) < MangaConst.Version:
		return True
	else
		return False

return var_0_0
