import winsound
from math import log


rate = 5
delta = 120
beat = rate*delta

notes = list(map(int, map(round, [(554.4)*((2**(1./12))**i) for i in range(12)])))
c_sharp = notes[0]
d_sharp = notes[2]
e = notes[3]
f_sharp = notes[5]
b = notes[10]


def play_note(note, length, effect=None):
    '''
    effect is a function recieving note and length
    '''
    if effect is None:
        winsound.Beep(note, length)
    else:
        intervals_num = int(length/delta)
        intervals = [delta for i in range(intervals_num)]
        intervals += [length - intervals_num*delta]
        times = [i*delta for i in range(intervals_num+1)]
        for tim, inter in zip(times, intervals):
            winsound.Beep(effect(note, tim), inter)


ef = lambda n, t: int(n * (2**((1./12)*(2*((1.5)**(-t/delta))))))


rotems_sequence = ((c_sharp, beat, None), (d_sharp, beat, None), (e, int(4./3*beat), None), (b, beat, None), (f_sharp, beat, ef), (f_sharp, beat, None))



if __name__ == '__main__':
    print rotems_sequence
    for note, length, effect in rotems_sequence:
        play_note(note, length, effect)