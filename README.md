# mpv-lazy-en
English translation for https://github.com/hooke007/MPV_lazy focusing on Nvidia 2060S (or better) GPU scaling with RIFE + Nvidia SuperRes

# install

1-4) Portable version here https://mega.nz/folder/6rIEFKzY#eo0QBQFR6YLQ8T5CfK1UHQ or https://pixeldrain.com/u/rncgrnVC

Or follow full install

1) Go to https://github.com/hooke007/MPV_lazy/releases/tag/20240406 or https://github.com/vadash/mpv-lazy-en/releases/tag/mpv-lazy-2024V1
2) Extract `hooke007.mpv-lazy-20240406.exe` (mpv-lazy minimal build)
3) Override with `mpv-lazy-20240406-vsMega.7z` (mpv-lazy rife stuff)
4) Override with [https://github.com/shinchiro/mpv-winbuild-cmake/releases](https://github.com/shinchiro/mpv-winbuild-cmake/releases/download/20240920/mpv-x86_64-v3-20240920-git-e3eeaec.7z) (fresh mpv player)

Continue

5) Override with https://github.com/vadash/mpv-lazy-en/archive/refs/heads/main.zip (my repo with translation and tweaks)
6) Open video and press: only Rife: shift + 2/3/4, rife + Nvidia SuperRes shift + 5/6/7
7) Wait few minutes for model to build (one time per resolution)

![image](https://github.com/user-attachments/assets/e466056d-7bd0-4918-b6df-dd42eb29d99b)

# configure
Open `mpv-lazy\portable_config\vs\MEMC_RIFE_NV_`LQ/MQ/HQ`.vpy` and edit

1080 is good for 2060s+, 1440 is perfect for 3070+
```
H_Pre = 1080 ## Integer, pre-downscale source height (fill in your display height)
```

Model used. 450 is rife 4.6, 451 is rife 4.15 lite, 452 is rife 4.18. 450 is fast but artifacts, 451 is good balance and 452 has decent quality
```
Model = 450 ## <450|451|452> 
```

If you have spare power can try x3 (double computation increase)

# update models

Download ONNX models from there https://github.com/AmusementClub/vs-mlrt/releases/tag/external-models

Use v2 models. They are better

Put .onnx file(s) into `mpv-lazy//vs-plugins/models/rife_v2` replacing one of 450 (LQ preset), 451 (MQ preset), 452 (HQ preset) 

# todo

auto switch when open video. Example, 24 fps switches to 48 hz, 25 to 50, 30 to 60. On player close restores default hz

# discuss

!!! DO NOT talk about mpv-lazy there !!!

https://www.svp-team.com/forum/viewtopic.php?id=6281

!!! DO NOT talk about mpv-lazy there !!!

Just good info about models. You can replace 46 model file (onnx) with new one if you need. For example, 4.20 is nice for anime if you have performance

# altenative

[https://www.svp-team.com](https://www.svp-team.com/wiki/RIFE_AI_interpolation)

+GUI

-Paid(wait for 11.11 deal)
