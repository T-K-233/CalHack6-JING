var pose_old = 0;
var registered = false;
var getX = function(pt) {
  return pt.position.x;
}
var getY = function(pt) {
  return pt.position.y;
}
var process = function(keypoints, t) {
  updateTime();
  if (start_detection) {
    let l_hand_x = getX(keypoints[9]);
    let r_hand_x = getX(keypoints[10]);
    let r_hand_y = getY(keypoints[9]);
    console.log()
    if (r_hand_y<getY(keypoints[0]) && r_hand_y<getY(keypoints[1]) && r_hand_y<getY(keypoints[2])) {
      if (!registered) {
        registered = true;
        console.log("Hands Up!");
        expandEvent();
      }
    } else if (r_hand_y>getY(keypoints[0]) && r_hand_y>getY(keypoints[1]) && r_hand_y>getY(keypoints[2])) {
      if (registered) {
        registered = false;
        console.log("Hands Down!");
        expandEvent();
      }
    }
    if (r_hand_x<getX(keypoints[0]) && r_hand_x<getX(keypoints[1]) && r_hand_x<getX(keypoints[2])) {
      if (!registered) {
        registered = true;
        console.log("Hands Left!");
        toLeft();
      }
    }
    if (l_hand_x>getX(keypoints[0]) && l_hand_x>getX(keypoints[1]) && l_hand_x>getX(keypoints[2])) {
      if (!registered) {
        registered = true;
        console.log("Hands Right!");
        toRight();
      }
    }
    /*
    if (pose_old == 0) {
      console.log("jump")
      pose_old = keypoints;
      return ;
    }
    
    pose_new = keypoints;
    if(pose_old[9] == 0 || pose_old[10]["position"]["x"] == 0){
      console.log('0 Appeared')
    }
    if ((pose_old[9]["position"]["x"] > pose_old[0]["position"]["x"] 
         && pose_new[9]["position"]["x"] <= pose_new[0]["position"]["x"]) ||
      (pose_old[10]["position"]["x"] < pose_old[0]["position"]["x"]
       && pose_new[10]["position"]["x"] >= pose_new[0]["position"]["x"])) {
      console.log('refresh ');
      expandEvent();
    }
    if (((pose_old[10]["position"]["y"] > pose_old[2]["position"]["y"]
        && pose_new[10]["position"]["y"] <= pose_new[2]["position"]["y"]) ||
      (pose_old[9]["position"]["y"] > pose_old[1]["position"]["y"] 
       && pose_new[9]["position"]["y"] <= pose_new[1]["position"]["y"])) && !expanded) {
      console.log('expand ');
      expandEvent();
    } else if (((pose_old[10]["position"]["y"] <= pose_old[2]["position"]["y"]
        && pose_new[10]["position"]["y"] > pose_new[2]["position"]["y"]) || 
      (pose_old[9]["position"]["y"] > pose_old[1]["position"]["y"] 
      && pose_new[9]["position"]["y"] <= pose_new[1]["position"]["y"])) && expanded) {
      expandEvent();
      console.log('close expand');
    }
    pose_old = pose_new;
    */
  }
}