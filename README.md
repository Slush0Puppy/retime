# ![Logo](https://i.imgur.com/FohZNXF.png)  Slush Puppy's Retime Tool

Hello, user!
This is **S**lush **P**uppy's **R**etime **T**ool, designed for precisely retiming speedruns down to the millisecond. You can enter the input times manually or use the method described for YouTube videos:

![GUI](https://i.imgur.com/tVRJLtI.png)

To use this, first of all find the framerate of the YouTube video you want to retime. Right click the video and click "Stats for nerds", and at the start of the 3rd line (titled "Current / Optimal Res") there will be a resolution followed by @xx, where xx is the framerate of the video. Enter this into the Video FPS box.

Next, find the first frame of the run. By using the , and . keys, you can advance one frame at a time to find the exact point. When you have found it, right click and select "Copy debug info", then paste it into the "Start frame" box or click the arrow next to it.
Do the same for the end frame.

When you are done, the exact time of the run will be displayed in the box, where it can be copied with the clipboard button or entered into speedrun.com.


The "Modifier" box will add a certain amount of time to the result. This is especially useful for games with unusual timing methods like Super Mario 64, where the timer is always at exactly 1.33 seconds on the first frame the logo appears. Moderators could set the Start frame to this point and set the Modifier to 1.33.

The message icon will copy custom mod note to the user's clipboard. This can be used to show the start and end times to ensure that the timing is clear. This message can be edited in source\mod message\message.txt, with phrases <start>, <end>, <result>, <framerate>, and <modifier> being replaced with their respective variables.


### CREDITS:
- <a href="https://www.speedrun.com/SlushPuppy"><img src="https://www.speedrun.com/themes/user/SlushPuppy/image.png" width=20 height=20> SlushPuppy</a>: Developer
- <a href="https://www.speedrun.com/Oxknifer"><img src="https://www.speedrun.com/themes/user/Oxknifer/image.png" width=20 height=20> Oxknifer</a>: Lead beta tester
- <a href="https://www.speedrun.com/g0goTBC"><img src="http://www.cityrider.com/fixed/43aspect.png" width=20 height=20> g0goTBC</a>: Beta tester
- <a href="https://www.speedrun.com/AprilSR"><img src="https://www.speedrun.com/themes/user/AprilSR/image.png" width=20 height=20> AprilSR</a>: Beta tester
