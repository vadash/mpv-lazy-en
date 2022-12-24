### rife v4 frame filler, high performance requirements, Nvidia card only

import vapoursynth as vs
from vapoursynth import core
import math
from vsmlrt import RIFE, RIFEModel, Backend

input = video_in
colorlv = input.get_frame(0).props._ColorRange
fmt_fin = input.format.id

interpMulti = 2 			# frame rate (integer)
if video_in_dh <= 1080: interpMulti = 3
if video_in_dh <= 720: interpMulti = 6
GPU = 0 							# The serial number of the graphics card used, 0 is sorted number one
GPU_t = 3 						# Number of graphics card threads used
WS_size = 2048        # Constrained video memory size
maxIpps = 80000000    # Max interpolated pixels per second the GPU is capable of. 80kk is solid starting point for 3070ti providing 80% CUDA load

if container_fps > 59 :
	raise Exception("The source frame rate exceeds the limit and the script has been temporarily disabled")

dsWidth = video_in_dw
dsHeight = video_in_dh
clipIpps = container_fps * video_in_dw * video_in_dh * (interpMulti - 1)
dsPercent = 1.00
while clipIpps > maxIpps:
  dsPercent -= 0.01
  dsWidth = int(video_in_dw * dsPercent)
  dsHeight = int(video_in_dh * dsPercent)
  clipIpps = container_fps * dsWidth * dsHeight * (interpMulti - 1)

dsWidth = math.ceil(dsWidth / 16) * 16
dsHeight = math.ceil(dsHeight / 16) * 16
cut0 = core.resize.Bilinear(clip=input, width=dsWidth, height=dsHeight, format=vs.RGBS, matrix_in_s="709")
w_tmp = math.ceil(cut0.width / 32) * 32 - cut0.width
h_tmp = math.ceil(cut0.height / 32) * 32 - cut0.height
cut1 = core.misc.SCDetect(clip=cut0, threshold=0.2)
cut2 = cut1.std.AddBorders(right=w_tmp, bottom=h_tmp)
cut3 = RIFE(clip=cut2, multi=interpMulti, model=RIFEModel.v4_6, backend=Backend.TRT(fp16=True, device_id=GPU, workspace=WS_size, use_cuda_graph=True, num_streams=GPU_t))
fin = cut3.std.Crop(right=w_tmp, bottom=h_tmp)
output = fin.resize.Bilinear(format=fmt_fin, matrix_s="709", range=1 if colorlv==0 else None)
#output = core.text.Text(output, text=(str(clipIpps) + "x " + str(dsWidth) + "x" + str(dsHeight)), alignment=7, scale=2)
output.set_output()

