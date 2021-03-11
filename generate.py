import matplotlib.pyplot as plt
import librosa.display
import IPython.display as ipd
import pysrt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--audio_name', type=str, default='test.wav', help='name of audio file')
parser.add_argument('--step_size', type=int, default=3, help='size of steps over audio for sound detection')
parser.add_argument('--frame_size', type=int, default=1024, help='size of frame for rms calculation')
parser.add_argument('--hop_length', type=int, default=512, help='hop length for rms calculation')

opt = parser.parse_args()

audio_name = opt.audio_name
FRAME_SIZE = opt.frame_size
HOP_LENGTH = opt.hop_length
step = opt.step_size

print('Starting...')

ipd.Audio(audio_name)

# load audio files with librosa
aud, sr = librosa.load(audio_name)
rms_aud = librosa.feature.rms(aud, frame_length=FRAME_SIZE, hop_length=HOP_LENGTH)[0]

frames = range(len(rms_aud))
rms_test_1 = rms_aud * 10
t = librosa.frames_to_time(frames, hop_length=HOP_LENGTH)

plt.figure(figsize=(15, 17))

ax = plt.subplot(3, 1, 1)
# librosa.display.waveplot(aud, alpha=0.5)
plt.plot(t, rms_test_1, color="r")
# plt.ylim((-1, 1))
plt.title("Graph sound detection")

fileSub = pysrt.SubRipFile(encoding='utf-8')
fileSub.clear()

frames_have_sound = []
rms_detect = []
soundFlag = False
counter = 1

vowels = []
with open("vowels.txt", "r", encoding='utf-8') as f:
    for line in f:
        for word in line.split():
            vowels.append(word)

print('Making subtitle...')
prev_max_rms = 0
curr_max_rms = 0
for i in range(0, len(t), step):
    if i + step > len(t):
        step = len(t) - i
    curr_max_rms = max(rms_test_1[i:i + step])
    if curr_max_rms > 0.25:
        if len(frames_have_sound) > 0:
            if curr_max_rms - prev_max_rms > 0.3:
                prev_max_rms = curr_max_rms
                continue
        soundFlag = True
        frames_have_sound.append(t[i:i + step + 1])
        key = '%d-%d' % (i, i + step + 1)
        rms_detect.append([i, i + step + 1])
    else:
        if soundFlag:
            soundFlag = False

            startTime = frames_have_sound[0][0]
            endTime = frames_have_sound[-1][-1]

            if endTime - startTime >= 0.2:

                min, sec = divmod(startTime, 60)
                hr, min = divmod(min, 60)
                startTime = "%02d:%02d:%.3f" % (hr, min, sec)

                min, sec = divmod(endTime, 60)
                hr, min = divmod(min, 60)
                endTime = "%02d:%02d:%.3f" % (hr, min, sec)

                word = 'n/a'
                if counter <= len(vowels):
                    word = vowels[counter - 1]
                sub = pysrt.SubRipItem(counter, start=startTime, end=endTime, text=word)

                counter += 1

                fileSub.append(sub)
                fileSub.save('sub.srt')

                # draw detected regions
                startIndex = rms_detect[0]
                endIndex = rms_detect[-1]
                ax.fill_between(t[startIndex[0]:endIndex[-1]], rms_test_1[startIndex[0]:endIndex[-1]], facecolor='b')

            rms_detect = []
            frames_have_sound = []

        prev_max_rms = curr_max_rms

print('Finish!! Check the file `sub.srt`')
plt.show()

