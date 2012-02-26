INFILES=*.asm *.inc

default: mg.hex

clean:
	rm *.lst *.hex

melody.asm: twinkle.py
	python twinkle.py
	perl mel2asm.pl < mel_twinkle.txt > melody.asm

mg.hex.mine: mg.hex
	cp mg.hex mg.hex.mine
	flip -d mg.hex.mine
	diff mg.hex.his mg.hex.mine > diff.txt
	cat diff.txt
	echo ---
	diff diff.old diff.txt
	cp diff.txt diff.old

mg.hex: $(INFILES)
	./gavrasm -M -q mg.asm

upload: mg.hex
	avrdude -c usbtiny -p t85 -v -e -U flash:w:mg.hex -C /etc/avrdude.conf

fuses:
	avrdude -c usbtiny -p t85 -v -U lfuse:w:0xF1:m -U hfuse:w:0xDE:m -U efuse:w:0xFF:m -C /etc/avrdude.conf
