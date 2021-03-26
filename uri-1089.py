while True:
    n = int (input ())
    if n == 0:
        break
    waveform = list(map(int,input().split()))
    waveform.append (waveform [0])
    waveform.append (waveform [1])
    peaks = 0
    for i in range (1, n + 1):
        if waveform [i] <waveform [i-1] and waveform [i] <waveform [i + 1]:
            peaks += 1
        elif waveform [i]> waveform [i-1] and waveform [i]> waveform [i + 1]:
            peaks += 1
    print (peaks)