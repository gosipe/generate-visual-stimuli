# -*- coding: utf-8 -*-
"""
Created on Wed May  7 15:43:29 2025
Edited on Wed May 7 16:40:29 2025
@author: jgronemeyer
Adapted from: https://discourse.psychopy.org/t/save-stimulus-as-a-video-file-e-g-mp4/17523

Run this script from within a psychopy environment. 
It will create a video of a drifting grating stimulus and save it as an mp4 file.

In VSCode, select the interpreter in the bottom corner of the window.
    Psychopy should show up as a Global Environment; select it.

"""

from psychopy import visual, core, event
import time
import imageio
import numpy as np

def main():
    image_flag=1
    video_flag=1
    image_flag=1
    video_flag=1
    # create window
    win0 = visual.Window([800, 600], screen = 0, monitor = 'testMonitor',
                        fullscr=False, color=[0, 0, 0], units='pix')

    gratingStimulus = visual.GratingStim(win=win0, tex='sin', units='pix', pos=(
        0.0, 0.0), size=800, sf=0.01, ori=0.0, phase=(0.0, 0.0))

    win0.getMovieFrame(buffer='back')
    start_time = time.time()
    run_time = 5 # run stimulus time in seconds

    frames = []

    while(time.time() - start_time < run_time):
        # 1st parameter is for speed of drifting
        # 2nd parameter is for direction of drifint ('+': left to right)
        gratingStimulus.setPhase(0.02, '+')
        gratingStimulus.draw()
        win0.flip()
        frames.append(win0.getMovieFrame())

        if len(event.getKeys()) > 0:
            break
        event.clearEvents()
    print("Play time: ", time.time()-start_time)    
    win0.close()

    ## FILE SAVING ##
    # the original forum post used the win0.saveMovieFrames function,
    # but this requires movieio as an external dependency. 
    # Instead, we will use imageio to save the frames (win0.getMovieFrame() return PIL image frames).
    
    fps = 30
    video_file = "output_video.avi"
    if video_flag:
        # write frames to mp4
        with imageio.get_writer(video_file, fps=fps) as writer:
            for img in frames:
                # if img is a PIL Image, convert to numpy array
                frame = np.array(img)
                writer.append_data(frame)

        print(f"Saved video to {video_file}")
    image_file = "output_image.tiff"
    if image_flag:
        imageio.imwrite(image_file,frames[0])
        print(f"Saved video to {image_file}")

if __name__ == "__main__":
    main()