### https://github.com/hooke007/MPV_lazy/wiki/3_K7sfunc
### RIFE (v4+) Frame interpolation, high performance requirement, NVIDIA exclusive

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

############
# User options #
############

H_Pre = 1080 ## Integer, pre-downscale source height (fill in your display height)
Lt_D2k = False ## <True|False> Whether to interpolate frames for sources exceeding DCI2K resolution
Model = 4151 ## <46|415|4151> Model used
Ext_Proc = False ## <True|False> Whether to use external padding/cropping processing
T_Tta = False ## <True|False> Whether to use ensemble model
Fps_Num = 2 ## Integer, Fps_Num/Fps_Den value, i.e., frame rate multiplier
Fps_Den = 1 ## Integer
Sc_Mode = 1 ## <0|1|2> Scene change detection mode, 0 to disable
Gpu = 0 ## GPU index used, 0 is the first in order
Gpu_T = 2 ## <1|2|3> Number of GPU threads
St_Eng = False ## <True|False> Whether to use static engine (requires preprocessing for different resolutions); dynamic engine adapts to different resolutions (QVGA→DCI4K)
Ws_Size = 0 ## Integer, constrain VRAM (MiB), minimum for static engine is 128 (dynamic engine automatically doubles), set below this value to maximize utilization
Lk_Fmt = False ## <True|False> Lock pixel format to yuv420p8

ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
clip = k7f.RIFE_NV(clip, lt_d2k=Lt_D2k, model=Model, ext_proc=Ext_Proc, t_tta=T_Tta, fps_in=container_fps, fps_num=Fps_Num, fps_den=Fps_Den, sc_mode=Sc_Mode, gpu=Gpu, gpu_t=Gpu_T, st_eng=St_Eng, ws_size=Ws_Size)

clip.set_output()
