sourapples
=========

About
--
If you own an iPod and have dug around in its filesystem (maybe to back up your music) there's a good chance you were suprised to find that your favorite tunes were renamed to cryptic four character strings. I know I was a little aggravated when I had no way to know what track any file actually was without having to open it in a music player.  Sourapples was written to quickly extract title, artist, and album information from these strangely named files and automatically rename them to a relevant name.


Version
----

1.0

Installation
-----

```sh
git clone git@github.com:NickMich/sourapples.git sourapples
cd sourapples
python setup.py install

```

Usage
-----
Version 1.0 of sourapples is very straightfoward to use. After installing you should have sourapples.py added to your system $PATH, probably at /usr/local/bin/sourapples.py, but you can check with 

```sh
$ which sourapples.py
/usr/local/bin/sourapples.py
$
```


##### Command line options

* [-f|--file] - Required - The input .m4a file to read information from
* [-r|--rename] - Optional - A flag indicating if you want to rename the file from the four-character format to Artist_Album_Tile.m4a

##### Example
```sh
$ sourapples.py -f EZUE.m4a -r
[*] Title -> Factory
[*] Artist -> Bruce Springsteen
[*] Album -> Darkness on the Edge of Town
[*] Renaming EZUE.m4a to ./Bruce Springsteen_Darkness on the Edge of Town_Factory.m4a

```

Issues/Limitations
=====
* Sourapples currently only parses .m4a files
* Output file format during renaming will become more flexible

License
----

MIT



