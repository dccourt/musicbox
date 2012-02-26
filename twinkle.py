notes_treble  = "CCGGAAG-FFEEDDC-GGFFEED-GGFFEEEDCCGGAAG-FFEEDDC-"
notes_bass    = "C E F E D C FGE E D C G E D C CGC E F E D C FIC "
#notes_bass   = "C E F E D C FGE E D C GGE D C CGC E F E D C FIC "

# Note 'I' in bass line: using > G implies a note in the next octave.
# In this case, 'I' means B(higher).

f = open('mel_twinkle.txt', 'w')

f.write("; Twinkle twinkle\n")

time = 120
delta_time = 60
key_treb = 5    # which octave
key_bass = 3

for (ch_treb, ch_bass) in zip(notes_treble, notes_bass):
	if ch_treb == ',':
		# Rest.  Skip n time.
		time += delta_time
	elif ch_treb == '-':
		# I changed my mind - sounds better without a pause here.
		pass
		# half rest.
		# time += (delta_time / 2)
	else:
		f.write("%d %s%d" % (time, ch_treb, key_treb))

	if ch_bass != ' ':
		# might not have written the time if we had no treble note
		if ch_treb in ('-', ','):
			f.write("%d" % time);

		# Maybe allow for note above this octave.
		key = key_bass
		if ch_bass > 'G':
			key = key_bass + 1
			ch_bass = chr(ord(ch_bass) - 7)

		f.write(" %s%d" % (ch_bass, key))
	
	f.write("\n")

	time += delta_time

f.write("%d EoS\n" % (time + (delta_time * 5)))

f.close()
