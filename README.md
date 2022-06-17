# streamlit


**Dilation**

This operations consists of convolving an image A with some kernel ( B), which can have any shape or size, usually a square or circle.
The kernel B has a defined anchor point, usually being the center of the kernel.
As the kernel B is scanned over the image, we compute the maximal pixel value overlapped by B and replace the image pixel in the anchor point position with that maximal value. As you can deduce, this maximizing operation causes bright regions within an image to "grow" (therefore the name dilation).
The dilatation operation is: dst(x,y)=max(x′,y′):element(x′,y′)≠0src(x+x′,y+y′)

**Erosion**

This operation is the sister of dilation. It computes a local minimum over the area of given kernel.
As the kernel B is scanned over the image, we compute the minimal pixel value overlapped by B and replace the image pixel under the anchor point with that minimal value.
The erosion operation is: dst(x,y)=min(x′,y′):element(x′,y′)≠0src(x+x′,y+y′)

**Gaussian Blurring**

In this method, instead of a box filter, a Gaussian kernel is used. 
It is done with the function, cv.GaussianBlur(). We should specify the width and height of the kernel which should be positive and odd. 
We also should specify the standard deviation in the X and Y directions, sigmaX and sigmaY respectively. 
If only sigmaX is specified, sigmaY is taken as the same as sigmaX. 
If both are given as zeros, they are calculated from the kernel size. Gaussian blurring is highly effective in removing Gaussian noise from an image.
