# mpv-lazy-en
English translation for https://github.com/hooke007/MPV_lazy focusing on 2060S (or better) GPU scaling with RIFE

# install
1) Go to https://github.com/hooke007/MPV_lazy/releases/tag/20240406
2) Install `hooke007.mpv-lazy-20240406.exe`
3) Override with `mpv-lazy-20240406-vsMega.7z`
4) Override with https://github.com/vadash/mpv-lazy-en/archive/refs/heads/main.zip
5) Open video and press shift + 4($)

# configure
Open `mpv-lazy\portable_config\vs\MEMC_RIFE_NV.vpy` and edit

1080 is good for 2060s, 1440 can do 3070
```
H_Pre = 1080 ## Integer, pre-downscale source height (fill in your display height)
```

4151 is 415 lite. Pretty good model imo. 4151 is 29-30% faster than 415
```
Model = 4151 ## <46|415|4151> Model used
```

If you have spare power can try x3 (double computation increase)
