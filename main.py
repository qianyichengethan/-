#out
import numpy as np
import time
import random
import serial

freqtable = dict((
				(np.log(130.8),"c"),(np.log(261.6),"c"),(np.log(523.3),"c"),(np.log(1047),"c"),
				(np.log(138.6),"#c"),(np.log(277.2),"#c"),(np.log(554.4),"#c"),(np.log(1109),"#c"),
				(np.log(146.8),"d"),(np.log(293.7),"d"),(np.log(587.3),"d"),(np.log(1175),"d"),
				(np.log(155.6),"#d"),(np.log(311.1),"#d"),(np.log(622.3),"#d"),(np.log(1245),"#d"),
				(np.log(164.8),"e"),(np.log(329.6),"e"),(np.log(659.3),"e"),(np.log(1319),"e"),
				(np.log(174.6),"f"),(np.log(349.2),"f"),(np.log(698.5),"f"),(np.log(1397),"f"),
				(np.log(185),"#f"),(np.log(370),"#f"),(np.log(740),"#f"),(np.log(1480),"#f"),
				(np.log(196),"g"),(np.log(392),"g"),(np.log(784),"g"),(np.log(1568),"g"),
				(np.log(207.7),"#g"),(np.log(415),"#g"),(np.log(830.6),"#g"),(np.log(1661),"#g"),
				(np.log(220),"a"),(np.log(440),"a"),(np.log(880),"a"),(np.log(1760),"a"),
				(np.log(233.1),"#a"),(np.log(466.2),"#a"),(np.log(932.3),"#a"),(np.log(1865),"#a"),
				(np.log(246.9),"b"),(np.log(493.9),"b"),(np.log(987.8),"b"),(np.log(1976),"b"),
				))
table1 = [np.log(130.8),np.log(261.6),np.log(523.3),np.log(1047),
			np.log(138.6),np.log(277.2),np.log(554.4),np.log(1109),
			np.log(146.8),np.log(293.7),np.log(587.3),np.log(1175),
			np.log(155.6),np.log(311.1),np.log(622.3),np.log(1245),
			np.log(164.8),np.log(329.6),np.log(659.3),np.log(1319),
			np.log(174.6),np.log(349.2),np.log(698.5),np.log(1397),
			np.log(185),np.log(370),np.log(740),np.log(1480),
			np.log(196),np.log(392),np.log(784),np.log(1568),
			np.log(207.7),np.log(415),np.log(830.6),np.log(1661),
			np.log(220),np.log(440),np.log(880),np.log(1760),
			np.log(233.1),np.log(466.2),np.log(932.3),np.log(1865),
			np.log(246.9),np.log(493.9),np.log(987.8),np.log(1976)]
table11 = sorted(table1)

ser = serial.Serial("COM4",230400)
frate = 10000
if __name__ == '__main__':
    #ser.write("test\n")
    #print ser.readline()
    
    data = ser.read(200)
    start = time.clock()
    data = list(bytearray(data))
    print data
    #print int(data[0])
    data = np.array(data)


    w = np.fft.fft(data)
    freqs = np.fft.fftfreq(200)
    idx = np.argmax(np.abs(w))

    freq = freqs[idx]
    freq_in_hertz = abs(freq * frate)

    hertz = freq_in_hertz
    print freq_in_hertz
    lg = np.log(hertz)
    target = min((abs(test-lg), test, lg-test) for test in table11)
    #Find the closest tune
    print target
    tunefreq = target[1]
    tune = freqtable[tunefreq]
    print tune
    dist = target[2]

    if abs(dist)<=0.02885:
    	light = "mid"   
    elif dist>0.02885 and dist <= 0.08655:
    	light = "right1"
    elif dist > 0.08655:
    	light = "right2"
    elif dist < (-0.02885) and dist >=(-0.08655):
    	light = "left1"
    else:
    	light = "left2"
    end=time.clock()
    print light
    print end - start

