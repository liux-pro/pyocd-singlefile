@echo off

REM 获取原图的尺寸（宽度和高度）
for /F "tokens=1,2" %%A in ('magick identify -format "%%w %%h" pyocd_logo.png') do (
    set "width=%%A"
    set "height=%%B"
)

REM 判断长边和短边
if %width% gtr %height% (
    set "long_side=%width%"
    set "short_side=%height%"
) else (
    set "long_side=%height%"
    set "short_side=%width%"
)


REM 将原图的长边作为边长，并生成一个正方形画布
magick convert -size %long_side%x%long_side% xc:transparent -gravity center ( pyocd_logo.png -resize %long_side%x%long_side% ) -composite output.png

magick convert output.png  -define icon:auto-resize=16,48,256 -compress zip pyocd.ico