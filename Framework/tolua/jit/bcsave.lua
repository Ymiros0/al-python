﻿local var_0_0 = require("jit")

assert(var_0_0.version_num == 20100, "LuaJIT core/library version mismatch")

local var_0_1 = require("bit")
local var_0_2 = "luaJIT_BC_"

local function var_0_3()
	io.stderr:write("Save LuaJIT bytecode: luajit -b[options] input output\n  -l        Only list bytecode.\n  -s        Strip debug info (default).\n  -g        Keep debug info.\n  -n name   Set module name (default: auto-detect from input name).\n  -t type   Set output file type (default: auto-detect from output name).\n  -a arch   Override architecture for object files (default: native).\n  -o os     Override OS for object files (default: native).\n  -e chunk  Use chunk string as input.\n  --        Stop handling options.\n  -         Use stdin as input and/or stdout as output.\n\nFile types: c h obj o raw (default)\n")
	os.exit(1)
end

local function var_0_4(arg_2_0, ...)
	if arg_2_0 then
		return arg_2_0, ...
	end

	io.stderr:write("luajit: ", ...)
	io.stderr:write("\n")
	os.exit(1)
end

local function var_0_5(arg_3_0)
	if type(arg_3_0) == "function" then
		return arg_3_0
	end

	if arg_3_0 == "-" then
		arg_3_0 = nil
	end

	return var_0_4(loadfile(arg_3_0))
end

local function var_0_6(arg_4_0, arg_4_1)
	if arg_4_0 == "-" then
		return io.stdout
	end

	return var_0_4(io.open(arg_4_0, arg_4_1))
end

local var_0_7 = {
	obj = "obj",
	c = "c",
	h = "h",
	o = "obj",
	raw = "raw"
}
local var_0_8 = {
	arm64 = true,
	arm = true,
	mips = true,
	arm64be = true,
	x64 = true,
	x86 = true,
	ppc = true,
	mipsel = true
}
local var_0_9 = {
	dragonfly = true,
	osx = true,
	openbsd = true,
	netbsd = true,
	freebsd = true,
	solaris = true,
	windows = true,
	linux = true
}

local function var_0_10(arg_5_0, arg_5_1, arg_5_2)
	arg_5_0 = string.lower(arg_5_0)

	local var_5_0 = var_0_4(arg_5_1[arg_5_0], "unknown ", arg_5_2)

	return var_5_0 == true and arg_5_0 or var_5_0
end

local function var_0_11(arg_6_0)
	local var_6_0 = string.match(string.lower(arg_6_0), "%.(%a+)$")

	return var_0_7[var_6_0] or "raw"
end

local function var_0_12(arg_7_0)
	var_0_4(string.match(arg_7_0, "^[%w_.%-]+$"), "bad module name")

	return string.gsub(arg_7_0, "[%.%-]", "_")
end

local function var_0_13(arg_8_0)
	if type(arg_8_0) == "string" then
		local var_8_0 = string.match(arg_8_0, "[^/\\]+$")

		if var_8_0 then
			arg_8_0 = var_8_0
		end

		local var_8_1 = string.match(arg_8_0, "^(.*)%.[^.]*$")

		if var_8_1 then
			arg_8_0 = var_8_1
		end

		arg_8_0 = string.match(arg_8_0, "^[%w_.%-]+")
	else
		arg_8_0 = nil
	end

	var_0_4(arg_8_0, "cannot derive module name, use -n name")

	return string.gsub(arg_8_0, "[%.%-]", "_")
end

local function var_0_14(arg_9_0, arg_9_1, arg_9_2)
	local var_9_0, var_9_1 = arg_9_0:write(arg_9_2)

	if var_9_0 and arg_9_1 ~= "-" then
		var_9_0, var_9_1 = arg_9_0:close()
	end

	var_0_4(var_9_0, "cannot write ", arg_9_1, ": ", var_9_1)
end

local function var_0_15(arg_10_0, arg_10_1)
	local var_10_0 = var_0_6(arg_10_0, "wb")

	var_0_14(var_10_0, arg_10_0, arg_10_1)
end

local function var_0_16(arg_11_0, arg_11_1, arg_11_2)
	local var_11_0 = var_0_6(arg_11_1, "w")

	if arg_11_0.type == "c" then
		var_11_0:write(string.format("#ifdef _cplusplus\nextern \"C\"\n#endif\n#ifdef _WIN32\n__declspec(dllexport)\n#endif\nconst unsigned char %s%s[] = {\n", var_0_2, arg_11_0.modname))
	else
		var_11_0:write(string.format("#define %s%s_SIZE %d\nstatic const unsigned char %s%s[] = {\n", var_0_2, arg_11_0.modname, #arg_11_2, var_0_2, arg_11_0.modname))
	end

	local var_11_1 = {}
	local var_11_2 = 0
	local var_11_3 = 0

	for iter_11_0 = 1, #arg_11_2 do
		local var_11_4 = tostring(string.byte(arg_11_2, iter_11_0))

		var_11_3 = var_11_3 + #var_11_4 + 1

		if var_11_3 > 78 then
			var_11_0:write(table.concat(var_11_1, ",", 1, var_11_2), ",\n")

			var_11_2, var_11_3 = 0, #var_11_4 + 1
		end

		var_11_2 = var_11_2 + 1
		var_11_1[var_11_2] = var_11_4
	end

	var_0_14(var_11_0, arg_11_1, table.concat(var_11_1, ",", 1, var_11_2) .. "\n};\n")
end

local function var_0_17(arg_12_0, arg_12_1, arg_12_2, arg_12_3)
	arg_12_3.cdef("typedef struct {\n  uint8_t emagic[4], eclass, eendian, eversion, eosabi, eabiversion, epad[7];\n  uint16_t type, machine;\n  uint32_t version;\n  uint32_t entry, phofs, shofs;\n  uint32_t flags;\n  uint16_t ehsize, phentsize, phnum, shentsize, shnum, shstridx;\n} ELF32header;\ntypedef struct {\n  uint8_t emagic[4], eclass, eendian, eversion, eosabi, eabiversion, epad[7];\n  uint16_t type, machine;\n  uint32_t version;\n  uint64_t entry, phofs, shofs;\n  uint32_t flags;\n  uint16_t ehsize, phentsize, phnum, shentsize, shnum, shstridx;\n} ELF64header;\ntypedef struct {\n  uint32_t name, type, flags, addr, ofs, size, link, info, align, entsize;\n} ELF32sectheader;\ntypedef struct {\n  uint32_t name, type;\n  uint64_t flags, addr, ofs, size;\n  uint32_t link, info;\n  uint64_t align, entsize;\n} ELF64sectheader;\ntypedef struct {\n  uint32_t name, value, size;\n  uint8_t info, other;\n  uint16_t sectidx;\n} ELF32symbol;\ntypedef struct {\n  uint32_t name;\n  uint8_t info, other;\n  uint16_t sectidx;\n  uint64_t value, size;\n} ELF64symbol;\ntypedef struct {\n  ELF32header hdr;\n  ELF32sectheader sect[6];\n  ELF32symbol sym[2];\n  uint8_t space[4096];\n} ELF32obj;\ntypedef struct {\n  ELF64header hdr;\n  ELF64sectheader sect[6];\n  ELF64symbol sym[2];\n  uint8_t space[4096];\n} ELF64obj;\n")

	local var_12_0 = var_0_2 .. arg_12_0.modname
	local var_12_1 = false
	local var_12_2 = false

	if arg_12_0.arch == "x64" or arg_12_0.arch == "arm64" or arg_12_0.arch == "arm64be" then
		var_12_1 = true
	elseif arg_12_0.arch == "ppc" or arg_12_0.arch == "mips" then
		var_12_2 = true
	end

	local function var_12_3(arg_13_0)
		return arg_13_0
	end

	local var_12_4 = var_12_3
	local var_12_5 = var_12_3

	if arg_12_3.abi("be") ~= var_12_2 then
		var_12_3 = var_0_1.bswap

		function var_12_4(arg_14_0)
			return var_0_1.rshift(var_0_1.bswap(arg_14_0), 16)
		end

		if var_12_1 then
			local var_12_6 = arg_12_3.cast("int64_t", 4294967296)

			function var_12_5(arg_15_0)
				return var_0_1.bswap(arg_15_0) * var_12_6
			end
		else
			var_12_5 = var_12_3
		end
	end

	local var_12_7 = arg_12_3.new(var_12_1 and "ELF64obj" or "ELF32obj")
	local var_12_8 = var_12_7.hdr

	if arg_12_0.os == "bsd" or arg_12_0.os == "other" then
		local var_12_9 = assert(io.open("/bin/ls", "rb"))
		local var_12_10 = var_12_9:read(9)

		var_12_9:close()
		arg_12_3.copy(var_12_7, var_12_10, 9)
		var_0_4(var_12_8.emagic[0] == 127, "no support for writing native object files")
	else
		var_12_8.emagic = "\x7FELF"
		var_12_8.eosabi = ({
			freebsd = 9,
			openbsd = 12,
			solaris = 6,
			netbsd = 2
		})[arg_12_0.os] or 0
	end

	var_12_8.eclass = var_12_1 and 2 or 1
	var_12_8.eendian = var_12_2 and 2 or 1
	var_12_8.eversion = 1
	var_12_8.type = var_12_4(1)
	var_12_8.machine = var_12_4(({
		arm64 = 183,
		arm = 40,
		mips = 8,
		arm64be = 183,
		x64 = 62,
		x86 = 3,
		ppc = 20,
		mipsel = 8
	})[arg_12_0.arch])

	if arg_12_0.arch == "mips" or arg_12_0.arch == "mipsel" then
		var_12_8.flags = var_12_3(1342181382)
	end

	var_12_8.version = var_12_3(1)
	var_12_8.shofs = var_12_5(arg_12_3.offsetof(var_12_7, "sect"))
	var_12_8.ehsize = var_12_4(arg_12_3.sizeof(var_12_8))
	var_12_8.shentsize = var_12_4(arg_12_3.sizeof(var_12_7.sect[0]))
	var_12_8.shnum = var_12_4(6)
	var_12_8.shstridx = var_12_4(2)

	local var_12_11 = arg_12_3.offsetof(var_12_7, "space")
	local var_12_12 = 1

	for iter_12_0, iter_12_1 in ipairs({
		".symtab",
		".shstrtab",
		".strtab",
		".rodata",
		".note.GNU-stack"
	}) do
		local var_12_13 = var_12_7.sect[iter_12_0]

		var_12_13.align = var_12_5(1)
		var_12_13.name = var_12_3(var_12_12)

		arg_12_3.copy(var_12_7.space + var_12_12, iter_12_1)

		var_12_12 = var_12_12 + #iter_12_1 + 1
	end

	var_12_7.sect[1].type = var_12_3(2)
	var_12_7.sect[1].link = var_12_3(3)
	var_12_7.sect[1].info = var_12_3(1)
	var_12_7.sect[1].align = var_12_5(8)
	var_12_7.sect[1].ofs = var_12_5(arg_12_3.offsetof(var_12_7, "sym"))
	var_12_7.sect[1].entsize = var_12_5(arg_12_3.sizeof(var_12_7.sym[0]))
	var_12_7.sect[1].size = var_12_5(arg_12_3.sizeof(var_12_7.sym))
	var_12_7.sym[1].name = var_12_3(1)
	var_12_7.sym[1].sectidx = var_12_4(4)
	var_12_7.sym[1].size = var_12_5(#arg_12_2)
	var_12_7.sym[1].info = 17
	var_12_7.sect[2].type = var_12_3(3)
	var_12_7.sect[2].ofs = var_12_5(var_12_11)
	var_12_7.sect[2].size = var_12_5(var_12_12)
	var_12_7.sect[3].type = var_12_3(3)
	var_12_7.sect[3].ofs = var_12_5(var_12_11 + var_12_12)
	var_12_7.sect[3].size = var_12_5(#var_12_0 + 1)

	arg_12_3.copy(var_12_7.space + var_12_12 + 1, var_12_0)

	local var_12_14 = var_12_12 + #var_12_0 + 2

	var_12_7.sect[4].type = var_12_3(1)
	var_12_7.sect[4].flags = var_12_5(2)
	var_12_7.sect[4].ofs = var_12_5(var_12_11 + var_12_14)
	var_12_7.sect[4].size = var_12_5(#arg_12_2)
	var_12_7.sect[5].type = var_12_3(1)
	var_12_7.sect[5].ofs = var_12_5(var_12_11 + var_12_14 + #arg_12_2)

	local var_12_15 = var_0_6(arg_12_1, "wb")

	var_12_15:write(arg_12_3.string(var_12_7, arg_12_3.sizeof(var_12_7) - 4096 + var_12_14))
	var_0_14(var_12_15, arg_12_1, arg_12_2)
end

local function var_0_18(arg_16_0, arg_16_1, arg_16_2, arg_16_3)
	arg_16_3.cdef("typedef struct {\n  uint16_t arch, nsects;\n  uint32_t time, symtabofs, nsyms;\n  uint16_t opthdrsz, flags;\n} PEheader;\ntypedef struct {\n  char name[8];\n  uint32_t vsize, vaddr, size, ofs, relocofs, lineofs;\n  uint16_t nreloc, nline;\n  uint32_t flags;\n} PEsection;\ntypedef struct __attribute((packed)) {\n  union {\n    char name[8];\n    uint32_t nameref[2];\n  };\n  uint32_t value;\n  int16_t sect;\n  uint16_t type;\n  uint8_t scl, naux;\n} PEsym;\ntypedef struct __attribute((packed)) {\n  uint32_t size;\n  uint16_t nreloc, nline;\n  uint32_t cksum;\n  uint16_t assoc;\n  uint8_t comdatsel, unused[3];\n} PEsymaux;\ntypedef struct {\n  PEheader hdr;\n  PEsection sect[2];\n  // Must be an even number of symbol structs.\n  PEsym sym0;\n  PEsymaux sym0aux;\n  PEsym sym1;\n  PEsymaux sym1aux;\n  PEsym sym2;\n  PEsym sym3;\n  uint32_t strtabsize;\n  uint8_t space[4096];\n} PEobj;\n")

	local var_16_0 = var_0_2 .. arg_16_0.modname
	local var_16_1 = false

	if arg_16_0.arch == "x86" then
		var_16_0 = "_" .. var_16_0
	elseif arg_16_0.arch == "x64" then
		local var_16_2 = true
	end

	local var_16_3 = "   /EXPORT:" .. var_16_0 .. ",DATA "

	local function var_16_4(arg_17_0)
		return arg_17_0
	end

	local var_16_5 = var_16_4

	if arg_16_3.abi("be") then
		var_16_4 = var_0_1.bswap

		function var_16_5(arg_18_0)
			return var_0_1.rshift(var_0_1.bswap(arg_18_0), 16)
		end
	end

	local var_16_6 = arg_16_3.new("PEobj")
	local var_16_7 = var_16_6.hdr

	var_16_7.arch = var_16_5(({
		ppc = 498,
		arm = 448,
		mips = 870,
		mipsel = 870,
		x64 = 34404,
		x86 = 332
	})[arg_16_0.arch])
	var_16_7.nsects = var_16_5(2)
	var_16_7.symtabofs = var_16_4(arg_16_3.offsetof(var_16_6, "sym0"))
	var_16_7.nsyms = var_16_4(6)
	var_16_6.sect[0].name = ".drectve"
	var_16_6.sect[0].size = var_16_4(#var_16_3)
	var_16_6.sect[0].flags = var_16_4(1051136)
	var_16_6.sym0.sect = var_16_5(1)
	var_16_6.sym0.scl = 3
	var_16_6.sym0.name = ".drectve"
	var_16_6.sym0.naux = 1
	var_16_6.sym0aux.size = var_16_4(#var_16_3)
	var_16_6.sect[1].name = ".rdata"
	var_16_6.sect[1].size = var_16_4(#arg_16_2)
	var_16_6.sect[1].flags = var_16_4(1076887616)
	var_16_6.sym1.sect = var_16_5(2)
	var_16_6.sym1.scl = 3
	var_16_6.sym1.name = ".rdata"
	var_16_6.sym1.naux = 1
	var_16_6.sym1aux.size = var_16_4(#arg_16_2)
	var_16_6.sym2.sect = var_16_5(2)
	var_16_6.sym2.scl = 2
	var_16_6.sym2.nameref[1] = var_16_4(4)
	var_16_6.sym3.sect = var_16_5(-1)
	var_16_6.sym3.scl = 2
	var_16_6.sym3.value = var_16_4(1)
	var_16_6.sym3.name = "@feat.00"

	arg_16_3.copy(var_16_6.space, var_16_0)

	local var_16_8 = #var_16_0 + 1

	var_16_6.strtabsize = var_16_4(var_16_8 + 4)
	var_16_6.sect[0].ofs = var_16_4(arg_16_3.offsetof(var_16_6, "space") + var_16_8)

	arg_16_3.copy(var_16_6.space + var_16_8, var_16_3)

	local var_16_9 = var_16_8 + #var_16_3

	var_16_6.sect[1].ofs = var_16_4(arg_16_3.offsetof(var_16_6, "space") + var_16_9)

	local var_16_10 = var_0_6(arg_16_1, "wb")

	var_16_10:write(arg_16_3.string(var_16_6, arg_16_3.sizeof(var_16_6) - 4096 + var_16_9))
	var_0_14(var_16_10, arg_16_1, arg_16_2)
end

local function var_0_19(arg_19_0, arg_19_1, arg_19_2, arg_19_3)
	arg_19_3.cdef("typedef struct\n{\n  uint32_t magic, cputype, cpusubtype, filetype, ncmds, sizeofcmds, flags;\n} mach_header;\ntypedef struct\n{\n  mach_header; uint32_t reserved;\n} mach_header_64;\ntypedef struct {\n  uint32_t cmd, cmdsize;\n  char segname[16];\n  uint32_t vmaddr, vmsize, fileoff, filesize;\n  uint32_t maxprot, initprot, nsects, flags;\n} mach_segment_command;\ntypedef struct {\n  uint32_t cmd, cmdsize;\n  char segname[16];\n  uint64_t vmaddr, vmsize, fileoff, filesize;\n  uint32_t maxprot, initprot, nsects, flags;\n} mach_segment_command_64;\ntypedef struct {\n  char sectname[16], segname[16];\n  uint32_t addr, size;\n  uint32_t offset, align, reloff, nreloc, flags;\n  uint32_t reserved1, reserved2;\n} mach_section;\ntypedef struct {\n  char sectname[16], segname[16];\n  uint64_t addr, size;\n  uint32_t offset, align, reloff, nreloc, flags;\n  uint32_t reserved1, reserved2, reserved3;\n} mach_section_64;\ntypedef struct {\n  uint32_t cmd, cmdsize, symoff, nsyms, stroff, strsize;\n} mach_symtab_command;\ntypedef struct {\n  int32_t strx;\n  uint8_t type, sect;\n  int16_t desc;\n  uint32_t value;\n} mach_nlist;\ntypedef struct {\n  uint32_t strx;\n  uint8_t type, sect;\n  uint16_t desc;\n  uint64_t value;\n} mach_nlist_64;\ntypedef struct\n{\n  uint32_t magic, nfat_arch;\n} mach_fat_header;\ntypedef struct\n{\n  uint32_t cputype, cpusubtype, offset, size, align;\n} mach_fat_arch;\ntypedef struct {\n  struct {\n    mach_header hdr;\n    mach_segment_command seg;\n    mach_section sec;\n    mach_symtab_command sym;\n  } arch[1];\n  mach_nlist sym_entry;\n  uint8_t space[4096];\n} mach_obj;\ntypedef struct {\n  struct {\n    mach_header_64 hdr;\n    mach_segment_command_64 seg;\n    mach_section_64 sec;\n    mach_symtab_command sym;\n  } arch[1];\n  mach_nlist_64 sym_entry;\n  uint8_t space[4096];\n} mach_obj_64;\ntypedef struct {\n  mach_fat_header fat;\n  mach_fat_arch fat_arch[2];\n  struct {\n    mach_header hdr;\n    mach_segment_command seg;\n    mach_section sec;\n    mach_symtab_command sym;\n  } arch[2];\n  mach_nlist sym_entry;\n  uint8_t space[4096];\n} mach_fat_obj;\n")

	local var_19_0 = "_" .. var_0_2 .. arg_19_0.modname
	local var_19_1 = false
	local var_19_2 = false
	local var_19_3 = 4
	local var_19_4 = "mach_obj"

	if arg_19_0.arch == "x64" then
		var_19_2, var_19_3, var_19_4 = true, 8, "mach_obj_64"
	elseif arg_19_0.arch == "arm" then
		var_19_1, var_19_4 = true, "mach_fat_obj"
	elseif arg_19_0.arch == "arm64" then
		var_19_2, var_19_3, var_19_1, var_19_4 = true, 8, true, "mach_fat_obj"
	else
		var_0_4(arg_19_0.arch == "x86", "unsupported architecture for OSX")
	end

	local function var_19_5(arg_20_0, arg_20_1)
		return var_0_1.band(arg_20_0 + arg_20_1 - 1, -arg_20_1)
	end

	local var_19_6 = var_0_1.bswap
	local var_19_7 = arg_19_3.new(var_19_4)
	local var_19_8 = var_19_5(arg_19_3.offsetof(var_19_7, "space") + #var_19_0 + 2, var_19_3)
	local var_19_9 = ({
		x86 = {
			7
		},
		x64 = {
			16777223
		},
		arm = {
			7,
			12
		},
		arm64 = {
			16777223,
			16777228
		}
	})[arg_19_0.arch]
	local var_19_10 = ({
		x86 = {
			3
		},
		x64 = {
			3
		},
		arm = {
			3,
			9
		},
		arm64 = {
			3,
			0
		}
	})[arg_19_0.arch]

	if var_19_1 then
		var_19_7.fat.magic = var_19_6(3405691582)
		var_19_7.fat.nfat_arch = var_19_6(#var_19_10)
	end

	for iter_19_0 = 0, #var_19_10 - 1 do
		local var_19_11 = 0

		if var_19_1 then
			local var_19_12 = var_19_7.fat_arch[iter_19_0]

			var_19_12.cputype = var_19_6(var_19_9[iter_19_0 + 1])
			var_19_12.cpusubtype = var_19_6(var_19_10[iter_19_0 + 1])
			var_19_11 = arg_19_3.offsetof(var_19_7, "arch") + iter_19_0 * arg_19_3.sizeof(var_19_7.arch[0])
			var_19_12.offset = var_19_6(var_19_11)
			var_19_12.size = var_19_6(var_19_8 - var_19_11 + #arg_19_2)
		end

		local var_19_13 = var_19_7.arch[iter_19_0]

		var_19_13.hdr.magic = var_19_2 and 4277009103 or 4277009102
		var_19_13.hdr.cputype = var_19_9[iter_19_0 + 1]
		var_19_13.hdr.cpusubtype = var_19_10[iter_19_0 + 1]
		var_19_13.hdr.filetype = 1
		var_19_13.hdr.ncmds = 2
		var_19_13.hdr.sizeofcmds = arg_19_3.sizeof(var_19_13.seg) + arg_19_3.sizeof(var_19_13.sec) + arg_19_3.sizeof(var_19_13.sym)
		var_19_13.seg.cmd = var_19_2 and 25 or 1
		var_19_13.seg.cmdsize = arg_19_3.sizeof(var_19_13.seg) + arg_19_3.sizeof(var_19_13.sec)
		var_19_13.seg.vmsize = #arg_19_2
		var_19_13.seg.fileoff = var_19_8 - var_19_11
		var_19_13.seg.filesize = #arg_19_2
		var_19_13.seg.maxprot = 1
		var_19_13.seg.initprot = 1
		var_19_13.seg.nsects = 1

		arg_19_3.copy(var_19_13.sec.sectname, "__data")
		arg_19_3.copy(var_19_13.sec.segname, "__DATA")

		var_19_13.sec.size = #arg_19_2
		var_19_13.sec.offset = var_19_8 - var_19_11
		var_19_13.sym.cmd = 2
		var_19_13.sym.cmdsize = arg_19_3.sizeof(var_19_13.sym)
		var_19_13.sym.symoff = arg_19_3.offsetof(var_19_7, "sym_entry") - var_19_11
		var_19_13.sym.nsyms = 1
		var_19_13.sym.stroff = arg_19_3.offsetof(var_19_7, "sym_entry") + arg_19_3.sizeof(var_19_7.sym_entry) - var_19_11
		var_19_13.sym.strsize = var_19_5(#var_19_0 + 2, var_19_3)
	end

	var_19_7.sym_entry.type = 15
	var_19_7.sym_entry.sect = 1
	var_19_7.sym_entry.strx = 1

	arg_19_3.copy(var_19_7.space + 1, var_19_0)

	local var_19_14 = var_0_6(arg_19_1, "wb")

	var_19_14:write(arg_19_3.string(var_19_7, var_19_8))
	var_0_14(var_19_14, arg_19_1, arg_19_2)
end

local function var_0_20(arg_21_0, arg_21_1, arg_21_2)
	local var_21_0, var_21_1 = pcall(require, "ffi")

	var_0_4(var_21_0, "FFI library required to write this file type")

	if arg_21_0.os == "windows" then
		return var_0_18(arg_21_0, arg_21_1, arg_21_2, var_21_1)
	elseif arg_21_0.os == "osx" then
		return var_0_19(arg_21_0, arg_21_1, arg_21_2, var_21_1)
	else
		return var_0_17(arg_21_0, arg_21_1, arg_21_2, var_21_1)
	end
end

local function var_0_21(arg_22_0, arg_22_1)
	local var_22_0 = var_0_5(arg_22_0)

	require("jit.bc").dump(var_22_0, var_0_6(arg_22_1, "w"), true)
end

local function var_0_22(arg_23_0, arg_23_1, arg_23_2)
	local var_23_0 = var_0_5(arg_23_1)
	local var_23_1 = string.dump(var_23_0, arg_23_0.strip)
	local var_23_2 = arg_23_0.type

	if not var_23_2 then
		var_23_2 = var_0_11(arg_23_2)
		arg_23_0.type = var_23_2
	end

	if var_23_2 == "raw" then
		var_0_15(arg_23_2, var_23_1)
	else
		if not arg_23_0.modname then
			arg_23_0.modname = var_0_13(arg_23_1)
		end

		if var_23_2 == "obj" then
			var_0_20(arg_23_0, arg_23_2, var_23_1)
		else
			var_0_16(arg_23_0, arg_23_2, var_23_1)
		end
	end
end

local function var_0_23(...)
	local var_24_0 = {
		...
	}
	local var_24_1 = 1
	local var_24_2 = false
	local var_24_3 = {
		type = false,
		strip = true,
		modname = false,
		arch = var_0_0.arch,
		os = string.lower(var_0_0.os)
	}

	while var_24_1 <= #var_24_0 do
		local var_24_4 = var_24_0[var_24_1]

		if type(var_24_4) == "string" and string.sub(var_24_4, 1, 1) == "-" and var_24_4 ~= "-" then
			table.remove(var_24_0, var_24_1)

			if var_24_4 == "--" then
				break
			end

			for iter_24_0 = 2, #var_24_4 do
				local var_24_5 = string.sub(var_24_4, iter_24_0, iter_24_0)

				if var_24_5 == "l" then
					var_24_2 = true
				elseif var_24_5 == "s" then
					var_24_3.strip = true
				elseif var_24_5 == "g" then
					var_24_3.strip = false
				else
					if var_24_0[var_24_1] == nil or iter_24_0 ~= #var_24_4 then
						var_0_3()
					end

					if var_24_5 == "e" then
						if var_24_1 ~= 1 then
							var_0_3()
						end

						var_24_0[1] = var_0_4(loadstring(var_24_0[1]))
					elseif var_24_5 == "n" then
						var_24_3.modname = var_0_12(table.remove(var_24_0, var_24_1))
					elseif var_24_5 == "t" then
						var_24_3.type = var_0_10(table.remove(var_24_0, var_24_1), var_0_7, "file type")
					elseif var_24_5 == "a" then
						var_24_3.arch = var_0_10(table.remove(var_24_0, var_24_1), var_0_8, "architecture")
					elseif var_24_5 == "o" then
						var_24_3.os = var_0_10(table.remove(var_24_0, var_24_1), var_0_9, "OS name")
					else
						var_0_3()
					end
				end
			end
		else
			var_24_1 = var_24_1 + 1
		end
	end

	if var_24_2 then
		if #var_24_0 == 0 or #var_24_0 > 2 then
			var_0_3()
		end

		var_0_21(var_24_0[1], var_24_0[2] or "-")
	else
		if #var_24_0 ~= 2 then
			var_0_3()
		end

		var_0_22(var_24_3, var_24_0[1], var_24_0[2])
	end
end

return {
	start = var_0_23
}
