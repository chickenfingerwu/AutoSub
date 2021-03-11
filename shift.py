import pysrt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--srt_name', type=str, default='sub.srt', help='name of srt file to edit')
parser.add_argument('--start_time_after', type=str, default='00:00:00.000',
                    help='{hh:mm:ss.ms} where to start shift entire sub file')
parser.add_argument('--shift_time', type=str, default='00:00:00.000', help='{hh:mm:ss.ms} shift how much time')

opt = parser.parse_args()

srtName = opt.srt_name
startTimeAfter = [value for value in opt.start_time_after.split(':')]
hour = int(startTimeAfter[0])
min = int(startTimeAfter[1])
sec, milisec = startTimeAfter[2].split('.')
sec = int(sec)
milisec = int(milisec)

shiftTime = [value for value in opt.shift_time.split(':')]
sHour = int(shiftTime[0])
sMin = int(shiftTime[1])
sSec, sMilisec = shiftTime[2].split('.')
sSec = int(sSec)
sMilisec = int(sMilisec)

fileSub = pysrt.open(srtName)
fileSub.slice(starts_after=[hour, min, sec, milisec]).shift(sHour, sMin, sSec, sMilisec)
fileSub.save()
