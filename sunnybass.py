import bs4
import re

exfile = open('MrSunnyBass.html')
# exfile = open('typicalbass.html')
exsoup = bs4.BeautifulSoup(exfile,'html.parser')

# Find the span with class "c6 c7"
entries = exsoup.find_all("span", {"class": "c6 c7"})

songlist = []

for entry in entries:
    anchor = entry.contents[0]
    song_title = anchor.contents[0].replace(" Bass Line Play Along Backing Track","")
    song_vcode = re.search(r'.*?%3D(.*)%26list.*', anchor['href']).group(1)
    if song_title[0].isnumeric():
        song_alphcat = 'A'
    else:
        song_alphcat = song_title[0].upper()
        
    song = (song_title,song_vcode,song_alphcat)
    songlist.append(song)

songlist.sort()
# print(songlist)
fout = open('output.html','w')
fout.write('<table>\n')
prev_alphcat = 'A'

for song in songlist:
    curr_alphcat = song[2]
    print('prev',prev_alphcat,'curr', curr_alphcat)
    if prev_alphcat == curr_alphcat:
        newline = '<tr><td><a target="_new" href="http://youtube.com/watch?v=' \
              + song[1] + '">' + song[0] \
              + '</a></td></tr>\n'
    else:
        newline = '<tr><td id="' + curr_alphcat + '"><a target="_new" href="http://youtube.com/watch?v=' \
              + song[1] + '">' + song[0] \
              + '</a></td></tr>\n'
    fout.write(newline)
    prev_alphcat = curr_alphcat

fout.write('</table>\n')
fout.close()

# Inside that span, there will be one <a>

# Extract the href attribute

# From there, find the first occurence of text between the '=' (%3D) and '&' (%26)

# Also extract the anchor text

# https://learnpython.com/blog/sort-tuples-in-python/

# https://www.w3schools.com/python/python_tuples_access.asp

# https://stackoverflow.com/questions/9889635/regular-expression-to-return-all-characters-between-two-special-characters
