import pysynth

marioSong = (
	('e5', 8), ('e5', 8), ('e5', 8), ('c5', 8), ('e5', 8),
	('g5', 4), ('g4', 4),
	('c5', 4), ('g4', 4), ('e4', 4), 
	('a4', 4), ('b4', 4), ('bb4', 8), ('a4', 4),
	('g4', 4), ('e5', 4), ('g5', 4), ('a5', 4), ('f5', 8), ('g5', 8),
	('e5', 8), ('c5', 8), ('d5', 8), ('b4', 8) 
)
##test = (('c5', 8), ('c5', 8), ('c5', 8), ('g5', 8), ('e5', 4), ('d5', 8), ('c5', 4) )
##pysynth.make_wav(test, fn = "test.wav")
pysynth.make_wav(marioSong, bpm = 200, fn = "marioSong.wav")