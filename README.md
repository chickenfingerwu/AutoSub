# AutoSub
AutoSub - auto generate SubRip file for audio because I'm lazy

For class INT3411_20 of 2021 UET-VNU.

This is not a ML tool, don't expect it to auto generate subtitles for audio. It can only automatically generate markups in the SubRip file for wherever it detects a 
sound.

Sound detection is based on RMS level so record with as little noise as possible.

Read slow for best results, vowels should be as separate as possible. Refer to the test.wav file as example.

# Installation
cd to AutoSub and run:
```bash
pip install -r requirements.txt
```

# vowels.txt file
This file will be what the tool uses for subbing. Writes all your vowels in the article here, for example: 
"TpHCM năm 2020 có xe ô tô bay" writes to vowels.txt -> "Thành phố Hồ Chí Minh năm hai không hai mươi có xe ô tô bay"

# Usage
To test example:
```bash
python generate.py
```
Will generate sub.srt file for the test.wav file.

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
