import os
import sys
import argparse
import binascii

f = None

def findpos(startpos,val):
	found = False
	vallen = len(val)
	i = startpos
	while not found:
		f.seek(i)
		if(binascii.hexlify(f.read(vallen/2)) == val):
			return i
			break
		i += 1	


def buildval(pos,val):
	i = pos + val
	f.seek(i)
        strs = ""
	done = False
	string_found = False
	c = binascii.hexlify(f.read(1))

	while not done:
		ch = binascii.hexlify(f.read(1))
		if(ch =="00" and string_found):
			break
		elif(ch == "00" or ch == "01"):
			continue
		else:
			string_found = True
			strs += ch.decode("hex")
	
	return strs



def main():
    parser = argparse.ArgumentParser(description="Arguments")
    parser.add_argument("-f","--file",required=True,help="The file name to process")
    parser.add_argument("-r","--rename",action='store_true',help="Flag to rename the file")
    args = parser.parse_args()
	
    global f
    in_file = args.file

    try:
        f = open(in_file,'rb')
    except Exception as e:
	    print "Exception! " + str(e)
	    sys.exit(-1)


    title_pos = findpos(0,'64617461')
    f.seek(title_pos+4)
    title = buildval(title_pos,8)
    print "[*] Title -> " + title
    
    artist_pos = findpos(title_pos,'a9415254')
    f.seek(artist_pos+16)
    artist = buildval(artist_pos,16)
    print "[*] Artist -> " + artist

    album_pos = findpos(0, 'a9616c62')
    f.seek(album_pos+16)
    album = buildval(album_pos,16)
    print "[*] Album -> " + album

    f.close()

    if args.rename :
        new_base_name = "_".join([artist,album,title])
        to_dir = os.path.dirname(in_file) 
        if to_dir == "":
            to_dir = "."
        fname, to_ext = os.path.splitext(in_file)
        out_file = to_dir + "/" + new_base_name + to_ext
        print "[*] Renaming %s to %s" %(in_file,out_file)
        os.rename(in_file, out_file)

	    
main()
