5.3-影像縮放
5.4-影像翻轉
5.5-影像平移
5.6-影像旋轉
5.7-影像仿射
5.8-影像透視

5.3補充 cv2.resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
其中interpolation:
如果是要縮小圖片的話，通常 INTER_AREA 使用效果較佳。
如果是要放大圖片的話，通常 INTER_CUBIC 使用效果較佳，次等則是 INTER_LINEAR。
如果要追求速度的話，通常使用 INTER_NEAREST。
==========interpolation==========
INTER_NEAREST	最近鄰插值
INTER_LINEAR	雙線性插值（預設）
INTER_AREA	使用像素區域關係進行重採樣。它可能是圖像抽取的首選方法，因為它會產生無雲紋理(波紋)的結果。 但是當圖像縮放時，它類似於INTER_NEAREST方法。
INTER_CUBIC	4x4像素鄰域的雙三次插值
INTER_LANCZOS4	8x8像素鄰域的Lanczos插值
=================================
