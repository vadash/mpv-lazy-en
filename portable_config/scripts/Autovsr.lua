-- Description: This script enables or disables NVIDIA's DLSS Super Resolution (VSR) in MPV.
-- Credits: https://gist.github.com/azumukupoe/a56a78d71cf26a8f682dc06407e615db
local mp = require 'mp'
local autovsr_enabled = false

local function autovsr()
    local display_width = mp.get_property_native("display-width")
    local video_width = mp.get_property_native("width")
    local display_height = mp.get_property_native("display-height")
    local video_height = mp.get_property_native("height")

    if video_width and display_width and video_height and display_height then
        local scale = math.max(display_width, display_height) / math.max(video_width, video_height)
        scale = scale - scale % 0.1 --

        local vf = mp.get_property("vf") or ""
        if string.match(vf, "@vsr") then
            mp.command("vf remove @vsr")
        end

        if scale > 1 then
            mp.command("vf append @vsr:d3d11vpp:scaling-mode=nvidia:scale=" .. scale)
        end
    end
end

local function activate()
    autovsr_enabled = not autovsr_enabled

    if autovsr_enabled then
        autovsr()
        mp.observe_property("video-params/pixelformat", "native", autovsr)
        mp.observe_property("vf", "native", autovsr)
        mp.osd_message("RTX ON")
    else
        mp.command("vf remove @vsr")
        mp.unobserve_property(autovsr)
        mp.osd_message("RTX OFF")
    end
end

-- Automatically activate VSR on startup
activate()

mp.add_key_binding("ctrl+shift+u", "autovsr", activate)
