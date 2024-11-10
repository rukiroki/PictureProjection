
<p align="center">
  <a href="./README.md">English</a> |
  <a href="./README_zh.md">简体中文</a>
</p>
PictureProjection is a simple program that can convert images into projections for Minecraft Bedrock Edition, used in conjunction with the Spritecraft map drawing tool: [Spritecraft](https://autosaved.org/Spritecraft). This program generates a Bedrock Edition texture pack file `.mcpack`, based on the projection display of armor stand entities. For more details, see *Quick Start*.

## Features
- The current version only supports the creation of flat map projections of up to 128*128 blocks.
- The image does not need to be perfectly square.
- Armor stand projection.
- Consumes name tags.

## Quick Start && Immersive Tutorial
### First, you need to download the first zip file from the [Release 0.1.0](https://github.com/rukiroki/PictureProjection/releases/tag/0.1.0).
![image](https://github.com/user-attachments/assets/bb6d98ae-4de5-44f3-bf45-35961acb0820)
### Then, unzip the zip file to a directory.
![image](https://github.com/user-attachments/assets/b3defbc4-69d3-4f6f-8dad-1517d21cfd90)
### Double-click to open the program `Picture Projection.exe` and two windows will pop up.
![image](https://github.com/user-attachments/assets/47a554c7-b1bf-488b-a8a9-064e5cdc72a9)
### Generate a map drawing on the web
Copy the link from the command line window [Spritecraft](https://autosaved.org/Spritecraft) to the browser to open and generate your map drawing. Note that the current version supports a maximum of 128*128.
1. Set the maximum width and height to 128, 128.
2. Choose the image you want to convert into a map drawing.
3. Select the blocks you want.
4. Click the "Generate Pixel Art" button.
5. Click the "Download Image" button to download the generated image.

![image](https://github.com/user-attachments/assets/848128fb-8862-4acc-939a-17e470748f39)![image](https://github.com/user-attachments/assets/b5b9f199-1eb2-42f6-9b4c-c39de3ad6bd6)
### Go to the image selection window and choose the image you just generated and downloaded.
![image](https://github.com/user-attachments/assets/1a370688-8aa3-479b-81a0-bc0233a1afba)
### Click OK to start the conversion, and the program will automatically close after the conversion is complete. The generated file will be placed in the root directory of the program.
![image](https://github.com/user-attachments/assets/70346e99-157d-4aa4-8c40-826ea8705005)
### Double-click to open the file `Picture projection.mcpack`, which will automatically import the resource pack and activate the resource pack in the world or globally.
> The resource pack will not change the game behavior and rules, and you can use it on servers by activating it globally.

![image](https://github.com/user-attachments/assets/73152154-e7f2-4014-952e-9dd271a540a6)
![image](https://github.com/user-attachments/assets/c583a6b5-d3e1-462e-aa89-43f68ffd4a50)
### Locate the map drawing construction position
Join the world, take out armor stands, an anvil, name tags, a map, and a conspicuous marker block (such as a redstone block).
Use the anvil to name four name tags as: p01, p02, p03, p04, because the map drawing is divided into four parts; otherwise, due to the Bedrock Edition entity rendering range being only 70 blocks, it will not be displayed if it is too far from the armor stand.
Take out the map and use the conspicuous marker block to find the bottom-left corner of the map, place the armor stand one block to the left and one block down from the bottom-left corner of the map (define the top, bottom, left, and right of the map as top, bottom, left, and right).
![image](https://github.com/user-attachments/assets/2032402f-780e-4d5c-aabd-82c62acf8083)
### Locate the positions for the four armor stands
This texture pack has a small wooden stick at the back 32 blocks, left 32 blocks, and left-rear 32, 32 blocks (which are up and right for the map) for each armor stand, which is used to facilitate finding the positions for the four armor stands.
![image](https://github.com/user-attachments/assets/c10ce13d-ed7e-411b-9e70-3044d85dfd62)
Place an armor stand at the coordinate (customized in the above image) -1, -1 (armor stand -1) on the wooden stick facing the map upwards at 32, 32. Place three armor stands on the three wooden sticks facing the map upwards, then place an armor stand (0) on the upper wooden stick facing down, place an armor stand (1) on the diagonal wooden stick facing down, place an armor stand (2) on the diagonal wooden stick facing down, and place an armor stand (3) on the right wooden stick facing down.
![4775d2fa6433b977efd79a867838775b](https://github.com/user-attachments/assets/3c06c51b-0913-49ad-a8d0-7f807f47adbd)

### Name the armor stands && Display the image
Change the orientation of the (0) armor stand to face downwards. Take out the four prepared name tags and name the (1) armor stand "p01", the (2) armor stand "p02", the (3) armor stand "p04", and the (0) armor stand "p03", and the image projection will be displayed around the armor stands.
![image](https://github.com/user-attachments/assets/a1aa6702-343e-4011-99d0-f16247a43ff1)
### Mission accomplished
Now the map drawing projection is displayed in the world with 80% opacity, and you can start building with the required building materials.
![image](https://github.com/user-attachments/assets/e55d28d2-0fce-46fb-8889-4d81f8f55d88)
In this example, the image is not square. If the imported image is not square, the projection will tend to display towards the upper left.
