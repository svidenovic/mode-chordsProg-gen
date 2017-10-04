
import urllib.request, urllib.parse, re

def download_chord_positions( chord, img_tmp_folder ):
	jguitar_com = "http://jguitar.com";
	url_req = jguitar_com +"/chordsearch/"+ urllib.parse.quote( chord,safe="");

	print(" Accessing the Page... ", end="");
	with urllib.request.urlopen( urllib.request.Request( url_req ) ) as response:
	   page_bytes = response.read();
	print("Done");

	page_html = page_bytes.decode("utf8");

	matches = re.findall( r"[<]img\s+src=\"(/images/chordshape/.*.png)\"", page_html );
	print(" --- Fetching "+str(len(matches))+" images... ");
	for match in matches:
		img_name = urllib.parse.unquote(match).replace( "/images/chordshape/","" );
		with urllib.request.urlopen( jguitar_com + match )\
		as response, open(img_tmp_folder+"/"+img_name, 'wb') as out_img:
			out_img.write( response.read() );
		print(" "+img_name);
	print(" --- Done --- ");
