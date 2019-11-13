'''
Credit entirely to 
    SCOTT RALSTON for this code
'''



from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from math import log2, pow
from collections import OrderedDict
from scipy.io import wavfile
plt.style.use('ggplot')
import cv2
import os
from IPython.display import clear_output
import shutil

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=False)
from bisect import bisect_left

def takeClosest(myList, myNumber):
    """
    Assumes myList is sorted. Returns closest value to myNumber.

    If two numbers are equally close, return the smallest number.
    """
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
       return(after)
    else:
       return(before)

def pitch(freq):
        h = round(12*log2(freq/C0))
        octave = h // 12
        n = h % 12
        return name[n] + str(octave)



#=================================Parameters====================================

#audio = "overtone_singing.wav"
audio = "ah-ee-ooh.wav"
snippet = 0.1
fps = 28
#filename = "overtone_7"
filename = "ah-ee-ooh"

testing = True #displays graphs for testing (set False when creating video)
is_it_stereo = True
ymax = 7000
fmax = 5000
fmin = 0
showpitches = False
only_fundamental = False


A4 = 440
C0 = A4*pow(2, -4.75)
name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
threshold = 1500
note_frequencies = []
for h in range(88):
    note_frequencies.append(C0*pow(2,h/12))


Fs,y1 = wavfile.read(audio)
T = 1/Fs # sampling period
N = len(y1) # total points in signal
duration = N/Fs  # seconds in clip

#==================================Check File Path==================================


vidpath= "Videos/"+filename+".avi"
exists = os.path.isfile(vidpath)
if exists:
    ok = str(input("A file called "+filename+ " already exists. Would you like to overwrite it? (y/n)"))
    if ok != "y":
        raise ValueError("Please start over with a new filename.")

#==================================Clear Frames Folder==================================

folder = 'frames'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)


def Analyze_Spectrum(t_start,audio,snippet,ymax,fmax,fmin=0,list_pitches=False,fft_plot = True,stereo = False):
    
    t_end = t_start + snippet
    Fs,y1 = wavfile.read(audio)

    if stereo:
        y=[]
        for i in range(int(Fs*t_start),int(Fs*t_end)):
            y.append(y1[i][1])
    else:
        y = y1[int(Fs*t_start):int(Fs*t_end)]

    T = 1/Fs # sampling period
    N = len(y) # total points in signal
    t = N/Fs  # seconds of sampling


    t_vec = np.arange(N)*T # time vector for plotting


    Y_k = np.fft.fft(y)[0:int(N/2)]/N # FFT function from numpy
    Y_k[1:] = 2*Y_k[1:] # need to take the single-sided spectrum only
    Pxx = np.abs(Y_k) # be sure to get rid of imaginary part

    f = Fs*np.arange((N/2))/N; # frequency vector
    #f = np.delete(f,-1,0)
    f_per_index = f[10]/10
    a = int(fmin/f_per_index)
    b = int(fmax/f_per_index)
    
    def pitch(freq):
        h = round(12*log2(freq/C0))
        octave = h // 12
        n = h % 12
        return name[n] + str(octave)
    
    class Pitch(object):
        def __init__(self, f, pitch):
            self.f = f
            self.pitch = pitch

    
    
    pitches = []
   
    thresh = []
    
    i = 1
    while i < len(Pxx):     
        n = 0
        freqs = []
        #print(Pxx, Pxx[i])
        if Pxx[i]>threshold:
            while Pxx[i+n]>threshold:
                freqs.append(f[i+n])
                n +=1
              
            i+=n
            frequency = mean(freqs)
            if frequency < fmax:
                pitches.append(Pitch(takeClosest(note_frequencies, frequency),pitch(frequency)))
        else:
            i+=1
    if only_fundamental:
        pitches = pitches[:1]
    pitches = dict([ (p.pitch, p.f) for p in pitches ])
    
      
    #pitches = OrderedDict.fromkeys(pitches)
    
    
    for i in range(len(Pxx[a:b])):
        thresh.append(threshold)

    thresh = np.array(thresh)
    
     # plotting
    if fft_plot:
        fig,ax = plt.subplots(figsize = None)
        plt.plot(f[a:b],Pxx[a:b])
        
        #ax.set_xscale('log')
        ax.set_yscale('log')
        ticks = []
        labels = []
        if showpitches:
            for i in range(len(pitches)):
                labels.append(list(pitches)[i])
                ticks.append(pitches[list(pitches)[i]])
            plt.plot(f[a:b],thresh,label='Threshold')
            plt.xticks(ticks,labels)
            plt.xlabel('Note Names')
            plt.legend(shadow=True,edgecolor = "white")
        else:
            plt.xlabel('Frequency [Hz]')

        plt.ylabel('Amplitude')
        
        
        plt.ylim(1,ymax)
        if testing:
            plt.show()
        

        path = "frames/" + str(int(t_start*fps)) + ".png"

        plt.savefig(path,bbox_inches='tight')
        plt.close()
        


    
    




def y_max(t_start,audio,snippet,ymax,fmax,fmin=0,list_pitches=False,fft_plot = True,stereo = False):   
    t_end = t_start + snippet
    Fs,y1 = wavfile.read(audio)

    if stereo:
        y=[]
        for i in range(int(Fs*t_start),int(Fs*t_end)):
            y.append(y1[i][1])
    else:
        y = y1[int(Fs*t_start):int(Fs*t_end)]

    T = 1/Fs # sampling period
    N = len(y) # total points in signal
    t = N/Fs  # seconds of sampling


    t_vec = np.arange(N)*T # time vector for plotting


    Y_k = np.fft.fft(y)[0:int(N/2)]/N # FFT function from numpy
    Y_k[1:] = 2*Y_k[1:] # need to take the single-sided spectrum only
    Pxx = np.abs(Y_k) # be sure to get rid of imaginary part

    f = Fs*np.arange((N/2))/N; # frequency vector
    #f = np.delete(f,-1,0)
    
    return(np.amax(f))



   
maxima = []
for n in range(int(fps*(duration-snippet))):
    t_start = n/fps
    maxima.append(y_max(t_start,audio,snippet,ymax,fmax))
    print(n)
ymax = max(maxima) + 100

    
    
for n in range(15):#(int(fps*(duration-snippet))):
    t_start = n/fps
    Analyze_Spectrum(t_start,audio,snippet,ymax,fmax,stereo=is_it_stereo)
    if not testing:
        clear_output()
    print(n,"/",int(fps*(duration-snippet))-1)



image_folder = 'frames'
video_name = vidpath

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

images = [int(x[:-4]) for x in images]
images.sort()
images = [str(x) for x in images]
images = [x + ".png" for x in images]
#print(images)
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, fps, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()


    
    
    
    
print("Done")






