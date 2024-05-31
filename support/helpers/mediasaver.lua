MediaSaver = {}

local var_0_0 = MediaSaver

function var_0_0.SaveImageWithBytes(arg_1_0, arg_1_1)
	System.IO.File.WriteAllBytes(arg_1_0, arg_1_1)
	YSTool.YSMediaSaver.Inst:SaveImage(arg_1_0)

	if System.IO.File.Exists(arg_1_0) then
		System.IO.File.Delete(arg_1_0)
		warning("del old file path:" .. arg_1_0)
	end
end

function var_0_0.SaveVideoWithPath(arg_2_0)
	YSTool.YSMediaSaver.Inst:SaveVideo(arg_2_0)

	if System.IO.File.Exists(arg_2_0) then
		System.IO.File.Delete(arg_2_0)
		warning("del old file path:" .. arg_2_0)
	end
end
