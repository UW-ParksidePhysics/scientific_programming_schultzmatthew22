Final Project Revision Plan

Feedback I received with descending priority:
1. Make sure that the whole stencil can fit onto a standard piece of paper
2. Make sure the minimum size doesn't go below 2mm is diameter
3. Add astronomical symbols to the planets and remove the size numbers + remove secondary graph output
4. Why was turtle chosen for creating the stencil

To accomplish the first task I'll implement a function that calculates the total diameter of all the planets
and the buffer and make sure this number doesn't exceed the standard US Letter length of 279.4mm and height of 215.9mm.

For the next task I will add a simple check to make sure the minimum size of the planets will not be below 2mm is diameter

I will then simply add the astronomical symbols next to the names on the stencil by adding the character next to them
in the script, and then I will remove the displayed converted and actual radii from the stencil. I will also remove the
secondary graphs that are presented as they are not needed.

As for why I chose turtle for this project, when I was looking for a way to create a drawing using python I found turtle
which I saw people saying is good for beginners. One of the main things I liked about it was how I could watch it draw out
what I was having it make so I could see how the changes I made to the numbers would affect how it drew out.
For the completed product I believe it would be best for me to move to matplotlib as when tinkering around with it instead
I realized the stencils made were much cleaner than the turtle one I made. Also, I could not get the astronomical symbols
to show up using turtle.

At this moment there are no changes that I am going to exclude from the finished product. I'm not 100% sure if the minimum
size of 2mm will result in the total size of all the planets to exceed the maximum size limiter of 279.4mm or not. If it does,
I will not be including that change as I feel that making it fit is more important. While I could make it a minimum of 2mm no matter
what the scaling factor is, I feel like that would not accurately accomplish the project as it is supposed to be an accurate scale.
