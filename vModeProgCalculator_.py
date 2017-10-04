
#~ To implement more modes, edit JUST this file

import re;
chromatic_scale = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#'];
intervals = [2,2,1,2,2,2,1];
modes = [
	"ionian","dorian","phrygian","lydian","mixolydian","aeolian","locrian"
];

def extract_keyNmode( key_mode ):
	re_pattern = r"^(";
	for note in chromatic_scale[:-1]:
		re_pattern += r""+note+r"|"+note.lower()+r"|";
	re_pattern += r""+chromatic_scale[-1]+r"|"+chromatic_scale[-1].lower()+r")\s+(";
	# mode part:
	for mode in modes[:-1]:
		re_pattern += r""+gen_re_pattern_(mode) +r"|"
	re_pattern += r""+gen_re_pattern_(modes[-1])+r")$";
	
	key = ""; mode = "";
	matches = re.findall( re_pattern, key_mode );
	for match in matches: # should be only 1 match
		key = match[0].upper();
		for m in modes:
			if re.match( match[1], m ):
				mode = m; break;
	
	return [key,mode];
	

def gen_re_pattern_( mode_name ):
	re_pattern = r"";
	for ln in range(2, len(mode_name)+1):
		mode_name_part = r"";
		for i in range(0,ln):
			mode_name_part += r""+mode_name[i];
		re_pattern += mode_name_part;
		if ln < len(mode_name):
			re_pattern += "|";
	return re_pattern;
	
def gen_prog_arr_( start_note, key ):
	chord_triad = ["","m","m","","","m","dim"];
	prog_arr = [];
	start_note_idx = 0;
	while 1:
		if chromatic_scale[start_note_idx] == start_note:
			break;
		else:
			start_note_idx += 1;
	csi = start_note_idx;
	for i in range(0,len(intervals)):
		prog_arr.append( chromatic_scale[csi]+chord_triad[i]+"/"+key );
		csi += intervals[i];
		if csi >= len(chromatic_scale):
			csi -= len(chromatic_scale);
	return prog_arr;
	
def gen_start_note_(key, mode_num):
	start_note = key;
	if mode_num == 1:
		return start_note;
	start_note_idx = 0;
	while 1:
		if chromatic_scale[start_note_idx] == start_note:
			break;
		else:
			start_note_idx += 1;
	for i in range(0,mode_num-1):
		start_note_idx -= intervals[i];
	if start_note_idx < 0:
		start_note_idx += len(chromatic_scale);
	start_note = chromatic_scale [start_note_idx];
	return start_note;

def get_mode_prog( key, mode ):
	key = key.strip().upper();
	mode = mode.strip().lower();
	mode_prog = [];
	
	for i in range(0,len(modes)):
		#~ if re.match( r"^"+gen_re_pattern_(modes[i])+r"$", mode ):
		if re.match( r"^"+modes[i]+r"$", mode ):
			print(" --- {} {} --- ".format(
				key, modes[i][0].upper()+modes[i][1:] )
			);
			start_note = gen_start_note_(key, i+1);
			mode_prog = gen_prog_arr_( start_note, key );
			break;
	
	return mode_prog;
