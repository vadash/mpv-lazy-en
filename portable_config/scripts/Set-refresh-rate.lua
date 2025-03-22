-- mpv Lua script to set display refresh rate
-- version 1.0
-- by vadash
local mp = require "mp"
local utils = require "mp.utils"

-- Constants
local NIRCMD_PATH = "nircmd_portable.exe" -- Specify the full executable name if needed
local RESOLUTION_WIDTH = 2560 -- Hardcoded resolution width
local RESOLUTION_HEIGHT = 1440 -- Hardcoded resolution height
local BITS_PER_PIXEL = 32 -- Hardcoded bits per pixel
local START_HZ = 48 -- Refresh rate when MPV starts
local EXIT_HZ = 75 -- Refresh rate when MPV exits

-- Function to set the hardcoded resolution and refresh rate
local function set_display_hz(hz)
-- Build a table of arguments rather than a single string
local args = {
NIRCMD_PATH,
"setdisplay",
tostring(RESOLUTION_WIDTH),
tostring(RESOLUTION_HEIGHT),
tostring(BITS_PER_PIXEL),
tostring(hz)
}
local result = utils.subprocess({ args = args, cancellable = false })
if result.status ~= 0 then
mp.msg.error("Failed to set refresh rate to " .. hz)
else
mp.msg.info(string.format("Display set to %dx%d@%dHz", RESOLUTION_WIDTH, RESOLUTION_HEIGHT, hz))
end
end

-- Set to START_HZ when the player starts
set_display_hz(START_HZ)

-- Set to EXIT_HZ when the player exits
mp.register_event("shutdown", function()
set_display_hz(EXIT_HZ)
end)
