#include<ros/ros.h>
#include<sensor_msgs/LaserScan.h>
#include<geometry_msgs/Twist.h>
#include<iostream>
#include <fstream>

using namespace std;

class Stopper{
public:
    const static double FORWARD_SPEED_MPS=0.05;  //运动速度
    const static double MIN_SCAN_ANGLE_RAD=-30.0/180*M_PI; //最小角度
    const static double MAX_SCAN_ANGLE_RAD=30.0/180*M_PI;  //最大角度
    const static float MIN_PROXIMITY_RANGE_M=1.5;  //期望的最近距离
    Stopper();  //构造函数
    void startMoving();
    ofstream file;

private:
    ros::NodeHandle node;     //私有成员
    ros::Publisher commandPub;
    ros::Subscriber laserSub;
    bool keepMoving;       //指示器
    void moveForward();
    void moveBackward();
    void scanCallback(const sensor_msgs::LaserScan::ConstPtr& scan);  //回调函数
}; 
//构造函数
Stopper::Stopper() {
    keepMoving=true;
    commandPub=node.advertise<geometry_msgs::Twist>("/cmd_vel_mux/input/teleop", 10);
    laserSub=node.subscribe("/turtlebot/laser/scan", 1, &Stopper::scanCallback, this);
}
//发布向前移动消息
void Stopper::moveForward(){
    geometry_msgs::Twist msg;
    msg.linear.x= FORWARD_SPEED_MPS;
//    msg.linear.y=FORWARD_SPEED_MPS;
    commandPub.publish(msg);
}


//回调函数，若最近距离小于指定值，更改keepMoving标志为False
void Stopper::scanCallback(const sensor_msgs::LaserScan::ConstPtr &scan) {
    int minIndex=ceil(MIN_SCAN_ANGLE_RAD-scan->angle_min)/scan->angle_increment;
    int maxIndex=floor(MAX_SCAN_ANGLE_RAD-scan->angle_min)/scan->angle_increment;
    float closestRange=scan->ranges[minIndex];
    for(int currIndex=minIndex+1; currIndex<=maxIndex; currIndex++) {
        if(scan->ranges[currIndex] < closestRange) {
            closestRange=scan->ranges[currIndex];
        }
    }
    ROS_INFO_STREAM("Closest_range: " << closestRange);
    if(closestRange<MIN_PROXIMITY_RANGE_M){
        ROS_INFO("Stop!");
        keepMoving=false;
    }
}
//开始移动，一直循环发送moveForward()直到keepMoving标志变为False
void Stopper::startMoving(){
    ros::Rate rate(10);
    ROS_INFO("start moving");

    while(ros::ok()&&keepMoving){
        moveForward();
        ros::spinOnce();
        rate.sleep();
        file<<"Moving_"<<keepMoving<<endl;
    }

    file<<"Moving_end_"<<keepMoving<<endl;
    usleep(1000*1000*10);
    keepMoving = true;
    startMoving();
}

int main(int argc, char** argv){

    ros::init(argc, argv, "mystage");
    Stopper stopper;
    stopper.file.open("//home//admini//Desktop//log");
    stopper.startMoving();
    return 0;
}
