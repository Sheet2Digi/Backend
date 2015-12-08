import pysynth_b

theList = []

with open('notes.txt') as thefile:

	for line in thefile:
			#line = line[:-2]
			theList.append((line[:-1], 4))

thefile.close()

print theList[0]


song = tuple(theList)
print song

#print isinstance(theList[0], tuple)

pysynth_b.make_wav(song, fn = "GB.wav")


##musicNotes = []

##for line in temp:
	##musicNotes.append(line)
	##print line + "\n"

