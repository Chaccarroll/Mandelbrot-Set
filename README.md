# Mandelbrot Set

Here is my attempt at creating the Mandelbrot Set in python, implementing Numpy, Matplotlib, and Numba to complete it. 

I was looking for a project to practise pyhton, and specifically to introduce me to a few of the popular and useful libraries like Numpy and Matplotlib. Around the same time I became interested in the Mandelbrot Set, a fractal created using the recursive function Z = Z^2 + C in the complex plane (instead of X and Y coordinates, its the Real and Imaginary coordinates). 

Through this project, I was able to practise and familiarize myself with the packages Numpy and Matplotlib. But using just these two packages wasnt enough. The main issue I ran into was the fact that the image was just taking too long to generate. I researched on how to bring this time down and thats when I learned of the package Numba. Numba is able to translate your python code to machine code so that It can run much faster. It works very well combined with NumPy and when used on code that is computation heavy. The addition of numba was night and day for the image generation in this project. 

This project is not perfect and there are some areas I would like to fix one day (namely Id like to add moore colors and Id love to make a zoom program that will create a video of a mandelbrot zoom) but for now it was a perfect introduction to some widely used python packages.  
