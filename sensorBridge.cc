/*
 * Copyright 2016 The Cartographer Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "cartographer_ros/sensor_bridge.h"

#include "cartographer/kalman_filter/pose_tracker.h"
#include "cartographer_ros/msg_conversion.h"
#include "cartographer_ros/time_conversion.h"

#include <iostream>
#include <fstream>
#include <typeinfo>
#include "Eigen/Core"
#include "Eigen/Geometry"
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <termios.h>
#include "sensor_msgs/Imu.h"

struct SAngle
{
    short Angle[3];
    short T;
};

struct SAcc
{
    short a[3];
    short T;
};

struct SAngle stcAngle;
struct SAcc  stcAcc;
enum Datatype{Angle_velocity, Acce};

sensor_msgs::Imu::_angular_velocity_type angular_veloModi;
sensor_msgs::Imu::_linear_acceleration_type linear_acceModi;



//using Quaternion = Eigen::Quaternion<FloatType>;

namespace cartographer_ros {

namespace carto = ::cartographer;

using carto::transform::Rigid3d;

namespace {

const string& CheckNoLeadingSlash(const string& frame_id) {
  if (frame_id.size() > 0) {
    CHECK_NE(frame_id[0], '/');
  }
  return frame_id;
}

}  // namespace

SensorBridge::SensorBridge(
    const string& tracking_frame, const double lookup_transform_timeout_sec,
    tf2_ros::Buffer* const tf_buffer,
    carto::mapping::TrajectoryBuilder* const trajectory_builder)
    : tf_bridge_(tracking_frame, lookup_transform_timeout_sec, tf_buffer),
      trajectory_builder_(trajectory_builder) {}

void SensorBridge::HandleOdometryMessage(
    const string& sensor_id, const nav_msgs::Odometry::ConstPtr& msg) {
  const carto::common::Time time = FromRos(msg->header.stamp);
  const auto sensor_to_tracking = tf_bridge_.LookupToTracking(
      time, CheckNoLeadingSlash(msg->child_frame_id));
  if (sensor_to_tracking != nullptr) {
    trajectory_builder_->AddOdometerData(
        sensor_id, time,
        ToRigid3d(msg->pose.pose) * sensor_to_tracking->inverse());
  }
}
    std::ofstream out("/home/admini/Documents/file");

///////Convert to EulerAngle
void toEulerAngle(const Eigen::Quaterniond& q, double& pitch, double& roll, double& yaw)
{
  double ysqr = q.y() * q.y();
  double t0 = -2.0f * (ysqr + q.z() * q.z()) + 1.0f;
  double t1 = +2.0f * (q.x() * q.y() - q.w() * q.z());
  double t2 = -2.0f * (q.x() * q.z() + q.w() * q.y());
  double t3 = +2.0f * (q.y() * q.z() - q.w() * q.x());
  double t4 = -2.0f * (q.x() * q.x() + ysqr) + 1.0f;

  t2 = t2 > 1.0f ? 1.0f : t2;
  t2 = t2 < -1.0f ? -1.0f : t2;

  pitch = std::asin(t2);
  roll = std::atan2(t3, t4);
  yaw = std::atan2(t1, t0);

  std::cout<<"pitch "<<pitch<<" roll "<<roll<<" yaw "<<yaw<<std::endl;
}

/////converted info out _mulitied
void covInfout(const Eigen::Vector3d& linear_acceleration, const Eigen::Vector3d& angular_velocity)
{
    //
    std::cout<<"cov_acc"<<linear_acceleration<<std::endl;
    std::cout<<"cov_ang"<<angular_velocity<<std::endl;
}
/////



////set spped
void set_speed(int fd, int speed)
{
    int speed_arr[] = {B115200,B38400, B19200, B9600, B4800, B2400, B1200, B300 };
    int name_arr[] = {115200,38400, 19200, 9600, 4800, 2400, 1200, 300 };

    int   i;
    int   status;
    struct termios   Opt;    //
    tcgetattr(fd, &Opt);    //
    for ( i= 0; i < sizeof(speed_arr) / sizeof(int); i++)
    {

        if (speed == name_arr[i])
        {
            tcflush(fd, TCIOFLUSH);  //
            //cfsetispeed(&Opt, speed_arr[i]);//
            cfsetospeed(&Opt, speed_arr[i]);//
            status = tcsetattr(fd, TCSANOW, &Opt);//

            if (status != 0)
            {
                perror("tcsetattr fd1 error");
                return;
            }
            else
            {
                // printf("set fd1 ok \n");
            }

            tcflush(fd,TCIOFLUSH); //
        }
    }
}
//


///get IMU data
void getImuData(Datatype dt, float &val1, float &val2, float &val3)
{
    int fd,flag,rd_num=0;
    struct termios term;//
    speed_t baud_rate_i,baud_rate_o,baud_rate_a,baud_rate_b;    //
    char recv_buf[20];//
    //fd=open("/dev/ttyUSB0",O_RDWR|O_NONBLOCK|O_NOCTTY | O_NDELAY);     //
    fd=open("/dev/ttyUSB0",O_RDWR|O_NONBLOCK);
    if(fd==-1)    //error
        printf("can not open the ttyUSB0!\n");
    else    //ok
        // printf("open USB-Serial ttyUSB0 ok!\n");

    flag=tcgetattr(fd,&term);
    baud_rate_i=cfgetispeed(&term);
    baud_rate_o=cfgetospeed(&term);
    //printf("baudrate of in is:%d,baudrate of out is%d,fd=%d\n",baud_rate_i,baud_rate_o,fd);

    set_speed(fd,9600);

    flag=tcgetattr(fd,&term);
    baud_rate_a=cfgetispeed(&term);
    baud_rate_b=cfgetospeed(&term);
    // printf("baudrate of in is:%d,baudrate of out is%d,fd=%d,flag=%d\n,",baud_rate_a,baud_rate_b,fd,flag);

    while(1)
    {
        read(fd,recv_buf,11);
        if(recv_buf[0] == 0x55)
        {
            //    printf("get data\n");

            break;
        }
        //  printf("cur %x\n", recv_buf[0]);
    }

    while(1)
    {
        rd_num=read(fd,recv_buf,11);

//        printf("%x_%x_%d\n", recv_buf[0], recv_buf[1], rd_num);
        if(rd_num>0)
        {
            if(recv_buf[1] == 0x52 && dt==Angle_velocity)
            {
                stcAngle.Angle[0] = (recv_buf[3]<<8)|(recv_buf[2] & 0xff);
                stcAngle.Angle[1] = (recv_buf[5]<<8)|(recv_buf[4] & 0xff);
                stcAngle.Angle[2] = (recv_buf[7]<<8)|(recv_buf[6] & 0xff);

                //printf("Angle_Acce:%.3f %.3f %.3f\r\n",(float)stcAngle.Angle[0]/32768*2000,(float)stcAngle.Angle[1]/32768*2000,(float)stcAngle.Angle[2]/32768*2000);
                val1 = (float)stcAngle.Angle[0]/32768*2000;
                val2 = (float)stcAngle.Angle[1]/32768*2000;
                val3 = (float)stcAngle.Angle[2]/32768*2000;
                return;
            }

            if(recv_buf[1] == 0x51 && dt==Acce)
            {
                stcAngle.Angle[0] = (recv_buf[3]<<8)|(recv_buf[2] & 0xff);
                stcAngle.Angle[1] = (recv_buf[5]<<8)|(recv_buf[4] & 0xff);
                stcAngle.Angle[2] = (recv_buf[7]<<8)|(recv_buf[6] & 0xff);

                //printf("Acce:%.3f %.3f %.3f\r\n",(float)stcAngle.Angle[0]/32768*16,(float)stcAngle.Angle[1]/32768*16,(float)stcAngle.Angle[2]/32768*16);

                val1 = (float)stcAngle.Angle[0]/32768*16;
                val2 = (float)stcAngle.Angle[1]/32768*16;
                val3 = (float)stcAngle.Angle[2]/32768*16;

                return;
            }

        }

//            printf("read ttyUSB0 fail!\n");
        usleep(20000); //1000us = 1ms
    }
}
///End get IMU data




void SensorBridge::HandleImuMessage(const string& sensor_id,
                                    const sensor_msgs::Imu::ConstPtr& msg) {
  CHECK_NE(msg->linear_acceleration_covariance[0], -1);
  CHECK_NE(msg->angular_velocity_covariance[0], -1);
  const carto::common::Time time = FromRos(msg->header.stamp);
  const auto sensor_to_tracking = tf_bridge_.LookupToTracking(
      time, CheckNoLeadingSlash(msg->header.frame_id));
  if (sensor_to_tracking != nullptr) {

      float ax, ay, az;  //linear_acceleration
      float avx, avy, avz; //angular_velocity
      //get Angle_velocity and replace
      getImuData(Angle_velocity, avx, avy, avz);
      std::cout<<"Angle_velocity: "<<avx<<" "<<avy<<" "<<avz<<std::endl;
      angular_veloModi.x = avx;
      angular_veloModi.y = avy;
      angular_veloModi.z = avz;
      //get Accelorate and replace
      getImuData(Acce,ax,ay,az);
      std::cout<<"Accerate: "<<ax<<" "<<ay<<" "<<az<<std::endl;
      linear_acceModi.x = ax;
      linear_acceModi.y = ay;
      linear_acceModi.z = az;

      CHECK(sensor_to_tracking->translation().norm() < 1e-5)
        << "The IMU frame must be colocated with the tracking frame. "
           "Transforming linear acceleration into the tracking frame will "
           "otherwise be imprecise.";
    trajectory_builder_->AddImuData(
        sensor_id, time,
//        sensor_to_tracking->rotation() * ToEigen(msg->linear_acceleration),
//        sensor_to_tracking->rotation() * ToEigen(msg->angular_velocity));

        sensor_to_tracking->rotation() * ToEigen(linear_acceModi),
            sensor_to_tracking->rotation() * ToEigen(angular_veloModi));


//    sensor_to_tracking->rotation();
      std::cout<<"Cur_accele "<<msg->linear_acceleration<<std::endl;
      out<<"msg_acce "<<msg->linear_acceleration<<std::endl;
      std::cout<<"Cur_velo "<<msg->angular_velocity<<std::endl;
      out<<"mag_velo "<<msg->angular_velocity<<std::endl;
      covInfout(sensor_to_tracking->rotation() * ToEigen(angular_veloModi),
                sensor_to_tracking->rotation() * ToEigen(angular_veloModi));
//      covInfout(sensor_to_tracking->rotation() * ToEigen(msg->linear_acceleration),
//                sensor_to_tracking->rotation() * ToEigen(msg->angular_velocity));
//
//      std::cout<<sensor_to_tracking->rotation();
//        std::cout<<typeid(sensor_to_tracking->rotation()).name()<<std::endl;
//        std::cout<<typeid(msg->angular_velocity).name()<<std::endl;
//        std::cout<<typeid(ToEigen(msg->angular_velocity)).name()<<std::endl;
//        std::cout<<typeid(sensor_to_tracking->rotation()* ToEigen(msg->linear_acceleration)).name()<<std::endl;
//
//        out<<typeid(sensor_to_tracking->rotation()).name()<<std::endl;
//        out<<typeid(msg->angular_velocity).name()<<std::endl;
//        out<<typeid(ToEigen(msg->angular_velocity)).name()<<std::endl;
//        out<<typeid(sensor_to_tracking->rotation() * ToEigen(msg->linear_acceleration)).name()<<std::endl;

        double pitch, roll,  yaw;
        toEulerAngle(sensor_to_tracking->rotation(),pitch,roll,yaw);
//        toEulerAngle(sensor_to_tracking->rotation() * ToEigen(msg->linear_acceleration),pitch,roll,yaw);
//        toEulerAngle(sensor_to_tracking->rotation() * ToEigen(msg->angular_velocity),pitch,roll,yaw);
//        std::cout<<"pitch "<<pitch<<"roll "<<roll<<"yaw "<<yaw<<std::endl;
        std::cout<<"x"<<sensor_to_tracking->rotation().x()<<std::endl;
        std::cout<<"y"<<sensor_to_tracking->rotation().y()<<std::endl;
        std::cout<<"z"<<sensor_to_tracking->rotation().z()<<std::endl;
        std::cout<<"w"<<sensor_to_tracking->rotation().w()<<std::endl;
        out<<"pitch "<<pitch<<"roll "<<roll<<"yaw "<<yaw<<std::endl;
//      std::cout<<"Cur_rotation"<<sensor_to_tracking->rotation()<<std::endl;
//      out<<"rotation"<<sensor_to_tracking->rotation()<<std::endl;
//      out<<target<<std::endl;
      //getIMUData
//      float val1, val2, val3;
//
////      for(int i=0; i<10;i++)
////      {
//          getImuData(Angle_acce, val1, val2, val3);
//          std::cout<<"Angle_acce: "<<val1<<" "<<val2<<" "<<val3<<std::endl;
//          getImuData(Acce, val1, val2, val3);
//          std::cout<<"Acce: "<<val1<<" "<<val2<<" "<<val3<<std::endl;
//
//          std::cout<<std::endl;
////      }
  }
}



void SensorBridge::HandleLaserScanMessage(
    const string& sensor_id, const sensor_msgs::LaserScan::ConstPtr& msg) {
  HandleRangefinder(sensor_id, FromRos(msg->header.stamp), msg->header.frame_id,
                    carto::sensor::ToPointCloud(ToCartographer(*msg)));
}

void SensorBridge::HandleMultiEchoLaserScanMessage(
    const string& sensor_id,
    const sensor_msgs::MultiEchoLaserScan::ConstPtr& msg) {
  HandleRangefinder(sensor_id, FromRos(msg->header.stamp), msg->header.frame_id,
                    carto::sensor::ToPointCloud(ToCartographer(*msg)));
}

void SensorBridge::HandlePointCloud2Message(
    const string& sensor_id, const sensor_msgs::PointCloud2::ConstPtr& msg) {
  pcl::PointCloud<pcl::PointXYZ> pcl_point_cloud;
  pcl::fromROSMsg(*msg, pcl_point_cloud);
  carto::sensor::PointCloud point_cloud;
  for (const auto& point : pcl_point_cloud) {
    point_cloud.emplace_back(point.x, point.y, point.z);
  }
  HandleRangefinder(sensor_id, FromRos(msg->header.stamp), msg->header.frame_id,
                    point_cloud);
}

const TfBridge& SensorBridge::tf_bridge() const { return tf_bridge_; }

void SensorBridge::HandleRangefinder(const string& sensor_id,
                                     const carto::common::Time time,
                                     const string& frame_id,
                                     const carto::sensor::PointCloud& ranges) {
  const auto sensor_to_tracking =
      tf_bridge_.LookupToTracking(time, CheckNoLeadingSlash(frame_id));
  if (sensor_to_tracking != nullptr) {
    trajectory_builder_->AddRangefinderData(
        sensor_id, time, sensor_to_tracking->translation().cast<float>(),
        carto::sensor::TransformPointCloud(ranges,
                                           sensor_to_tracking->cast<float>()));
  }
}

}  // namespace cartographer_ros
