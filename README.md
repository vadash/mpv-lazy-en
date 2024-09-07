# mpv-lazy-en
English translation for https://github.com/hooke007/MPV_lazy focusing on 2060S (or better) GPU scaling with RIFE

# install
1) Go to https://github.com/hooke007/MPV_lazy/releases/tag/20240406
2) Install `hooke007.mpv-lazy-20240406.exe`
3) Override with `mpv-lazy-20240406-vsMega.7z`
4) Override with [https://github.com/shinchiro/mpv-winbuild-cmake/releases](https://github.com/shinchiro/mpv-winbuild-cmake/releases/download/20240907/mpv-x86_64-v3-20240907-git-0eb5e91.7z)
5) Override with https://github.com/vadash/mpv-lazy-en/archive/refs/heads/main.zip
6) Open video and press. Only Rife: shift + 4. Rife and Nvidia SuperRes: shift + 5
7) Wait few minutes for model to build

# configure
Open `mpv-lazy\portable_config\vs\MEMC_RIFE_NV.vpy` and edit

1080 is good for 2060s+, 1440 is perfect for 3070+
```
H_Pre = 1080 ## Integer, pre-downscale source height (fill in your display height)
```

4151 is 415 lite. Pretty good model imo. 4151 is 20-30% faster than 415
```
Model = 4151 ## <46|415|4151> Model used
```

If you have spare power can try x3 (double computation increase)

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

+Faster updates

+Can use in mpc-hc with nvidia super res (quality 1 or 2)

-Paid(wait for 11.11 deal)
