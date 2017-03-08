
# TimeLapseVideo (timelapseVLCMovieMakerConversion.py)
## Synopsis
This [script] (timelapseVLCMovieMakerConversion.py) was developed to convert .TLV files (time-lapse video) into individual .jpg frames using VLC media player. The frames are then added to a Windows Movie Maker instance for review by the user. 

<a href="http://www.youtube.com/watch?feature=player_embedded&v=BCvdvJ7b_qY
" target="_blank"><img src="http://img.youtube.com/vi/BCvdvJ7b_qY/0.jpg" 
alt="TimeLapseVideo_python" width="240" height="180" border="10" /></a>

## Script Inputs

*For the command line script execution, the following inputs are needed:*
+ Path to the folder where all of the .TLV files are stored
+ Path to a folder where the frames (individual .jpg) will be stored (folder must exist already)
+ Start date for which the cameras were launched
+ End date for when the cameras and files were last picked up

This [time-lapse presentation] (TLV_VLC_MvMkr_script.pdf) is an overview of the script parameters and execution.

## Motivation

The particular cameras that we use are Plotwatcher Pro models made by Day 6 Outdoors. The cameras are set to record and take pictures at 30 minute intervals from sunrise to sunset. Each day is stored on one separate .TLV file (160721AA.TLV, 160722AA.TLV, etc.).

If the SD cards are removed at some point during the day (ex: to swap SD cards), the camera will create a file with an additional file for the particular day with an AB ending (160722AB.TLV). These specific files had to and were addressed during this automated extraction process.

It was necessary to convert from the .TLV files to another format because these file formats are not often used.

Before this script was written I was extracting all of the frames manually using the VLC software, which was very time consuming with two or more months of data from our four different cameras.

I was only able to play one .TLV video file at a time. Once I was in the VLC software I also had to adjust the scene filter to a new folder. It was necessary to change the folder location because the scene filter would overwrite the current frames, instead of appending them after the previous days frames.

Windows Movie Maker did not accept the files as is, so I had to convert them to another format. I used VLC to extract the individual frames from each .TLV file using a scene-filter using command line and save to individual folders, which usually ended up being around 50 photos per day.

Once the frames are extracted, they are imported into a Windows Movie Maker instance using an .XML file and command line.

Windows Movie Maker has a limit of 1000 photos being added at one time so I divided the movie maker files by half-months (MayA, MayB, JuneA, JuneB, etc.). This is the final product from the script.

From here, the user views the movie maker file and removes the super bright or dark photos so the completed video is watchable.

## Installation

Download the [ArcToolbox and script (.zip file)] (CrossSections.zip) to try in ArcGIS.

## Tests

This script was developed and tested with ArcGIS 10.2, Python 2.7

Python modules needed: *acrpy, math, sys, traceback*

## Contributors

Michael Harris is the author of this script.

[StackOverflow] (http://stackoverflow.com/users/4530995/michael-harris)

[LinkedIN] (https://www.linkedin.com/in/michael-harris-366b0060/)

## Acknowledgements

Some code snippets and ideas were obtained from Mark Ellefson 'Classify Stream Type' script and 'Perpendicular Transects' script by Mateus Ferreira.

## License

This code is available under the [MIT License.] (LICENSE.txt)

<img src="XSinputs.png" width="240" height="180" border="10" />
<img src="XSoutput.png" width="240" height="180" border="10" />
<img src="XSwatershed.png" width="240" height="180" border="10" />
