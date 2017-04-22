#include <iostream>
#include <unistd.h>
#include <sys/types.h>
#include <errno.h>
#include <stdio.h>
#include <sys/wait.h>
#include <stdlib.h>
using namespace std;

int main()
{
  system("gnome-terminal -x sh -c 'cd /home/GR/catkin_ws/wandrian ; roslaunch gscam gscam_nodelet.launch'");
  system("gnome-terminal -x sh -c 'cd /home/GR/catkin_ws/wandrian ; rosrun mjpeg_server mjpeg_server'");
  system("gnome-terminal -x sh -c 'cd /home/GR/catkin_ws/wandrian ; roslaunch kobuki_node minimal.launch'");
  cout << "Done\n";
  return 0;
}
