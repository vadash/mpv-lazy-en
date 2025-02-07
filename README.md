# MPV Lazy EN

English translation for [MPV_lazy](https://github.com/hooke007/MPV_lazy) focusing on NVIDIA RTX 2060 Super (or better) GPU scaling with RIFE and NVIDIA Super Resolution.

![image](https://github.com/user-attachments/assets/2cb3e22c-e60f-461a-ad5a-51a78a52af4b)

## Table of Contents

- [Installation](#installation)
  - [Portable Version](#portable-version)
  - [Full Installation](#full-installation)
- [Configuration](#configuration)
- [Updating Models](#updating-models)
- [Discussion](#discussion)

## Installation

### Portable Version

You can download the portable version directly from the links below:

- https://github.com/vadash/mpv-lazy-en/releases/tag/mpv-lazy-2024V1

### Full Installation

Follow these steps for a complete installation:

1. **Mpv-lazy orifinal**
   - Visit the [MPV Lazy EN Releases](https://github.com/hooke007/MPV_lazy/releases/tag/20240406).
   - Download `hooke007.mpv-lazy-20240406.exe`, `mpv-lazy-20240406-vsMega.7z`.

2. **Update mpv**
   - Download and override with the `mpv-x86_64-v3-xxx.7z` [MPV WinBuild CMake Release](https://github.com/shinchiro/mpv-winbuild-cmake/releases).

3. **Install translation and tweaks**
   - Override with the [MPV Lazy EN Main Branch](https://github.com/vadash/mpv-lazy-en/archive/refs/heads/main.zip).
   - Open a video file and press the following keys:
     - **Only RIFE:** `Shift + 2/3/4`
     - **RIFE + NVIDIA SuperRes:** `Shift + 5/6/7`
   - Wait a few minutes for the model to build.

## Configuration

To configure the settings:

1. Open the configuration file located at:
   ```
   mpv-lazy\portable_config\vs\MEMC_RIFE_NV_{LQ|MQ|HQ}.vpy
   ```

2. Edit the following parameters based on your GPU:

   - **Pre-downscale Source Height:**
     ```python
     H_Pre = 1080  # Integer, pre-downscale source height (fill in your display height)
     ```
     - `1080` is recommended for NVIDIA RTX 2060 Super and above.
     - `1440` is ideal for NVIDIA RTX 3070 and higher.

   - **Model Selection:**
     ```python
     Model = 450  # <450|451|452>
     ```
     - `450`: RIFE 4.6 – Fast but may have artifacts.
     - `451`: RIFE 4.15 lite – Good balance between speed and quality.
     - `452`: RIFE 4.25 – Decent quality with slow performance.

3. **Performance Optimization:**
   - If you have additional computational power, you can try using `x3` for double the computation, which increases processing speed.

## Model speed

From fastest to most slow

1. RIFE 4.6 (very old model, fastest) - 112 fps
2. RIFE 4.15 lite (decent progress, exploring lite models) - 100 fps
3. RIFE 4.26 (not worth) - 86 fps
4. RIFE 4.25 (breakthrough after 4.18) - 84 fps
5. RIFE 4.18 (another good model) - 75 fps

Try to use 425, 418 or 415lite if you can

## Updating Models

To update the RIFE models:

1. **Download ONNX Models:**
   - Visit the [AMUSEMENT Club Models](https://github.com/AmusementClub/vs-mlrt/releases/tag/external-models) and download the desired `.onnx` V2 model files.

2. **Replace Existing Models:**
   - Place the downloaded `.onnx` files into the following directory:
     ```
     mpv-lazy\vs-plugins\models\rife_v2
     ```
   - Replace one of the existing models:
     - `450.onnx` for LQ preset
     - `451.onnx` for MQ preset
     - `452.onnx` for HQ preset

## Auto start RTX

Add to the end of `mpv.conf`

`vf=vapoursynth="~~/vs/MEMC_RIFE_NV_HQ.vpy",d3d11vpp=scale=2:scaling-mode=nvidia`

## Discussion

**Important:** Do not discuss MPV Lazy in the official forums.

- Visit the [SVP Team Forum](https://www.svp-team.com/forum/viewtopic.php?id=6281) for discussions related to models and other relevant topics.
