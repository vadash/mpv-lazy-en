# mpv-lazy-en
English translation for https://github.com/hooke007/MPV_lazy plus auto scaling for 4K videos. Made with ChatGPT

# install
1) Go to https://github.com/hooke007/MPV_lazy/releases
2) Install `mpv-lazy-XXX.exe`
3) Override with `mpv-lazy-XXX-rifeCuda.7z`
4) Override with https://github.com/vadash/mpv-lazy-en/archive/refs/heads/main.zip

# configure
Open `portable_config\vs\rife_cuda.vpy` and edit 
```
maxIpps = 80000000    # Max interpolated pixels per second the GPU is capable of. 80kk is solid starting point for 3070ti providing 80% CUDA load
```

Also by default it will use 2x multiplier for 2k+, 3x for 1080p and 6x for 720p so it nicely fits in 144 Hz display without jitter
 
