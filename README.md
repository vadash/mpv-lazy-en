# MPV Lazy EN

English translation for [MPV_lazy](https://github.com/hooke007/MPV_lazy) focused on NVIDIA RTX video enhancement features (RTX 2060 Super or better).
Only tested for windows.

![MPV Lazy Interface](https://i.imgur.com/BXDBdwI.png)

## Features

- RIFE frame interpolation with NVIDIA GPU acceleration
- NVIDIA DLSS Super Resolution (auto-scaling)
- Automatic display refresh rate switching
- Multiple quality presets (LQ/MQ/HQ)

## Full Installation

1. **Base Installation**
   - Download from [MPV Lazy Releases](https://github.com/hooke007/MPV_lazy/releases/tag/20240406):
     - `hooke007.mpv-lazy-20240406.exe`
     - `mpv-lazy-20240406-vsMega.7z`

2. **MPV Update**
   - Replace files with latest [MPV WinBuild](https://github.com/shinchiro/mpv-winbuild-cmake/releases) (`mpv-x86_64-v3-xxx.7z`)

3. **English Translation and tweaks**
   - Override with files from [MPV Lazy EN](https://github.com/vadash/mpv-lazy-en/archive/refs/heads/main.zip)

To update for new mpv-lazy just repeat step 3.

## Quick Start

1. Install
2. Open any video file and press `Shift + 2/3/4` for RIFE + NVIDIA SuperRes (LQ/MQ/HQ)
3. Wait for the model to build (first time only)

## Configuration

### RIFE Settings
File: `portable_config/vs/MEMC_RIFE_NV_{LQ|MQ|HQ}.vpy`

```python
# Pre-downscale height (adjust for your GPU)
H_Pre = 1080  # RTX 2060 Super
# H_Pre = 1440  # RTX 3070 or better

# Model Selection
Model = 450  # Fast
#Model = 451  # Balanced
#Model = 452  # Quality
```

### Auto Features

#### RIFE Interpolation
Add to `mpv.conf`:
```
vf=vapoursynth="~~/vs/MEMC_RIFE_NV_HQ.vpy"
```

#### Display Refresh Rate
Edit values in `portable_config/scripts/Set-refresh-rate.lua`:
- START_HZ (default: 48)
- EXIT_HZ (default: 75)

Requires [NirCmd](https://www.nirsoft.net/utils/nircmd.zip) (included as `nircmd_portable.exe`)

## Model Performance

Benchmarked FPS (fastest to slowest):
1. RIFE 4.6 - 112 fps (oldest)
2. RIFE 4.15 lite - 100 fps (recommended)
3. RIFE 4.26 - 86 fps
4. RIFE 4.25 - 84 fps
5. RIFE 4.18 - 75 fps

Recommended: RIFE 4.25, 4.18, or 4.15 lite

## Updating Models

1. Download V2 `.onnx` files from [AMUSEMENT Club Models](https://github.com/AmusementClub/vs-mlrt/releases/tag/external-models)
2. Place in `mpv-lazy\vs-plugins\models\rife_v2\`:
   - `450.onnx` - LQ preset (4.9)
   - `451.onnx` - MQ preset (4.15 lite)
   - `452.onnx` - HQ preset (4.25)

## Support

Discussions: [SVP Team Forum](https://www.svp-team.com/forum/viewtopic.php?id=6281)

**Note:** Please do not discuss MPV Lazy in official MPV forums.
