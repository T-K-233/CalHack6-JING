'''
Return the ideal response for input interaction.
All inputs should be tuples.
'''
from datetime import time

def termination():
    if('''when the camera detects person leave'''):
        return True
    return False

def getinteraction():
    '''
    keypoints should be the pose reading from camera.
    '''
    pose_old = keypoints["keypoints"]
    pose_old = pose_old[0:3] + pose_old[9:11]
    assert pose_old[0]["part"] == "nose"
    pose_new = None
    expanded = False
    while (True):
        time.sleep(0.1)
        if pose_new is not None:
            pose_old = pose_new
        '''keypoints should refresh here'''
        pose_new = keypoints["keypoints"]
        pose_new = pose_new[0:3] + pose_new[9:11]

        if (pose_old[4]["position"]["x"] > pose_old[0]["position"]["x"] and pose_new[4]["position"]["x"] <= \
            pose_new[0]["position"]["x"]) or (
                pose_old[3]["position"]["x"] < pose_old[0]["position"]["x"] and pose_new[3]["position"]["x"] >= \
                pose_new[0]["position"]["x"]):
            '''refresh news displaying'''

        if (pose_old[4]["position"]["y"] < pose_old[2]["position"]["y"] and pose_new[4]["position"]["y"] >=
            pose_new[2]["position"]["y"]) or (
                pose_old[3]["position"]["y"] < pose_old[1]["position"]["y"] and pose_new[3]["position"]["y"] >=
                pose_new[1]["position"]["y"]):
            '''expand the events block'''
            expanded = True
        elif ((pose_old[4]["position"]["y"] >= pose_old[2]["position"]["y"] and pose_new[4]["position"]["y"] <
            pose_new[2]["position"]["y"]) or (pose_old[3]["position"]["y"] < pose_old[1]["position"]["y"] and pose_new[3]["position"]["y"] >=
                pose_new[1]["position"]["y"])) and expanded:
            '''close the events block'''

        if(termination()):
            break

