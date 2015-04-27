Instructions for usage of VoxelStitch.exe

Read all of these before starting!
This program is dumb - if it doesn't find what it wants, it'll throw a tantrum and collapse on the floor with an error.

Step 1:
	As per http://www.curse.com/mc-mods/minecraft/225179-voxelmap you need to enable image output by editing your VoxelMap config.
	You may also want to disable dynamic lighting.
	You can find your config at C:\Users\[Your user account]\AppData\Roaming\.minecraft\mods\VoxelMods\
	Clarification: You simply need to add "Output Images:true" on a new line at the bottom of the Voxelmap config - it'll be overwritten at Minecraft boot, so every time you want to save actual images you'll need to set that option again.
	Don't close this Explorer window down yet - you'll need to get there again later.

Step 2:
	Get those images!
	Start up Minecraft with  everything installed and ready to go. It'll be best to make sure that it's daytime in A'therys before starting.
	Open up the world map, and thoroughly pan around all the areas you want mapping.
	Disconnect from the server and quit the game before a wild SpiderVorske attacks you.

Step 3:
	Find those images!
	These will usually be in C:\Users\[Your user account]\AppData\Roaming\.minecraft\mods\VoxelMods\voxelMap\cache\rp.gazamo.com\Overworld\images\z1
	Can't find them? Make sure you set that config option every time you start up the game!
	(V2 only!) Using the directory selection screen automagically opens up the right folder in your AppData if it exists. Scroll down a bit and you should be able to go through and find your image folder.

Step 4:
	Put the images in the right place. (V1 only!)
	Simply copy and paste all the images into the images folder WITHIN the dist folder in the VoxelStitch folder, which you should have unzipped or whatever by now.

Step 5:
	Want to see the image just before it's saved for whatever reason? You can! (V1 Only for now!)
	In the top bar of your Control Panel, paste in "Control Panel\Programs\Default Programs\Set Associations"
	Find the .bmp file association, and click change program on it and switch it over to mspaint.exe
	This is because the default windows image viewer thing is terrible, and refuses to accept a /wait command so the temporary image is automatically deleted before it can load it.

Step 6:
	When you have ensured that everything is in the right place, run VoxelStitch.exe!
	You'll see plenty of numbers fly by, trying to inform you as to which files it's processing right then.
	If you want to understand these, have a look at the VOxelStitch.py file in the main directory - it should be clear enough as to what is what.

Step 7:
	Your image should now be complete!
	It will be saved as "compiledMap.png" in the same folder as VoxelStitch.exe.
