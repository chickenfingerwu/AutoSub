# AutoSub
AutoSub - auto generate SubRip file for audio because I'm lazy

For class INT3411_20 of 2021 UET-VNU.

This is not a ML tool, don't expect it to auto generate subtitles for audio. It can only automatically generate markups in the SubRip file for wherever it detects a 
sound.

Sound detection is based on RMS level so record with as little noise as possible.

Vowels should be as seperate as possible for best result.

# Installation
cd to AutoSub and run:
```bash
pip install -r requirements.txt
```

# Usage
To generate a srt file. Run:
```bash
python generate.py --audio_name your_audio_file.wav
```
Mess with other parameters in the generate.py file to find the best settings for your file.

To shift the time of srt file, run (this is an example):
```bash
python shift.py --srt_file your_srt_file.srt --start_time_after 00:00:01.881 --shift_time 00:00:02.000
```
Specify start_time_after for where to start shifting, shift_time specifies how much to shift.

# Acknowledgment 
Library for editing srt file used in this project is pysrt by byroot: https://github.com/byroot/pysrt
