# mpv-lazy-en
English translation for https://github.com/hooke007/MPV_lazy plus auto scaling for 4K videos

# install
1) Go to https://github.com/hooke007/MPV_lazy/releases
2) Install `mpv-lazy-XXX.exe`
3) Override with `mpv-lazy-XXX-rifeCuda.7z`
4) Override with https://github.com/vadash/mpv-lazy-en/archive/refs/heads/main.zip
5) Open video and press shift + 3(#)

# configure
Open `portable_config\vs\rife_cuda.vpy` and edit 
```
maxIpps = 80000000    # Max interpolated pixels per second the GPU is capable of. 80kk is solid starting point for 3070ti providing 80% CUDA load
```
Get your value here https://browser.geekbench.com/cuda-benchmarks For example, 3050 value will be 72998/165866 * 80000000 = 35000000

Also by default it will use 2x multiplier for 2k+, 3x for 1080p and 6x for 720p so it nicely fits in 144 Hz display without jitter
 
If your 720/1080p content starts lagging reduce these multipliers (1.2 and 1.4) a bit
```
if interpMulti == 3: maxIpps = 1.2 * maxIpps # approximation fix
elif interpMulti == 6: maxIpps = 1.4 * maxIpps # approximation fix
```

