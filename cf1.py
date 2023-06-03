#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty

x = 0
y = 0
z = 0
theta = 0

def poseCallback(pose_message):
    global x
    global y
    global z
    global theta
    global cf1lin
    global cf1ang
    
    x = pose_message.x
    y = pose_message.y
    theta = pose_message.theta
    cf1lin = pose_message.linear_velocity
    cf1ang = pose_message.angular_velocity

def cf2Callback(pose_message):
    global cf2x
    global cf2y
    global cf2z
    global cf2theta
    global cf2lin
    global cf2ang
    
    cf2x = pose_message.x
    cf2y = pose_message.y
    cf2theta = pose_message.theta
    cf2lin = pose_message.linear_velocity
    cf2ang = pose_message.angular_velocity

def cf3Callback(pose_message):
    global cf3x
    global cf3y
    global cf3z
    global cf3theta
    global cf3lin
    global cf3ang
    
    cf3x = pose_message.x
    cf3y = pose_message.y
    cf3theta = pose_message.theta
    cf3lin = pose_message.linear_velocity
    cf3ang = pose_message.angular_velocity

def cf4Callback(pose_message):
    global cf4x
    global cf4y
    global cf4z
    global cf4theta
    global cf4lin
    global cf4ang
    
    cf4x = pose_message.x
    cf4y = pose_message.y
    cf4theta = pose_message.theta
    cf4lin = pose_message.linear_velocity
    cf4ang = pose_message.angular_velocity

def direction_vector(menace):
    linear_vel = cf1lin
    angular_vel = cf1ang
    turtle_heading = theta #heading angle
    
    if angular_vel != 0 :
        dt=0.3
        turtle_heading = theta+angular_vel * dt
        direction_vec = [math.cos(turtle_heading)+x, math.sin(turtle_heading)+y]#direction vector
        new_vect = [menace[0]*-1 + direction_vec[0], menace[1]*-1 + direction_vec[1]]
        #deviate =[math.cos(new_vect), math.sin(new_vect)]
        #avoide_crash(direction_vec[0], direction_vec[1])
        print("direction:",direction_vec)
        print("menace:", menace)
        print("new_vect:",new_vect)
        avoide_crash(new_vect[0], new_vect[1])

def avoide_crash (xgoal, ygoal):
    global x
    global y
    global theta

    velocity_message = Twist()
    # cmd_vel_topic = '/turtle0/cmd_vel'

    while(True):
        kv =0.6			
        distance = abs(math.sqrt(((xgoal-x)**2)+((ygoal-y)**2)))
        linear_speed = kv * distance

        ka = 8.0
        desired_angle_goal = math.atan2(ygoal-y, xgoal-x)
        dtheta = desired_angle_goal-theta 

        if dtheta > math.pi:
            #angular_speed = ka * (dtheta)
            dtheta = dtheta - 2*math.pi
        elif dtheta < -math.pi:
            #angular_speed = ka * (aux)
            dtheta = 2*math.pi
        angular_speed = ka * (dtheta)


        velocity_message.linear.x = linear_speed
        velocity_message.angular.z = angular_speed
        velocity_publisher.publish(velocity_message)
        #print ('x=', x, 'y=', y)
        # print(dtheta)
        if (distance < 0.1):
            break



def rotate (angle):
    global x
    global y
    global theta

    velocity_message = Twist()
    # cmd_vel_topic = '/turtle0/cmd_vel'

    while(True):
        ka = 6.0
        desired_angle_goal = math.radians(angle)
        dtheta = desired_angle_goal-theta        
        aux = 2*math.pi-dtheta
        if dtheta > math.pi:
            #angular_speed = ka * (dtheta)
            dtheta = dtheta - 2*math.pi
        elif dtheta < -math.pi:
            #angular_speed = ka * (aux)
            dtheta = dtheta + 2*math.pi
            
        angular_speed = ka * (dtheta)

        velocity_message.angular.z = angular_speed
        velocity_message.linear.x = 0.0	
        velocity_publisher.publish(velocity_message)
        #print ('x=', x, 'y=', y)
        # print(dtheta)
        if (dtheta < 0.03):
            break

def orientate (xgoal, ygoal):
    global x
    global y
    global theta

    velocity_message = Twist()
    # cmd_vel_topic = '/turtle0/cmd_vel'

    while(True):
        ka = 6.0
        desired_angle_goal = math.atan2(ygoal-y, xgoal-x)
        dtheta = desired_angle_goal-theta        
        aux = 2*math.pi-dtheta
        if dtheta > math.pi:
            #angular_speed = ka * (dtheta)
            dtheta = dtheta - 2*math.pi
        elif dtheta < -math.pi:
            #angular_speed = ka * (aux)
            dtheta = 2*math.pi
        angular_speed = ka * (dtheta)
        velocity_message.angular.z = angular_speed
        velocity_message.linear.x = 0.0	
        velocity_publisher.publish(velocity_message)
        #print ('x=', x, 'y=', y)
        # print(dtheta)
        if (dtheta < 0.03):
            break

def go_to_goal (xgoal, ygoal):
    global x
    global y
    global theta

    velocity_message = Twist()
    # cmd_vel_topic = '/turtle0/cmd_vel'

    while(True):
        kv = 0.8				
        distance = abs(math.sqrt(((xgoal-x)**2)+((ygoal-y)**2)))
        linear_speed = kv * distance

        ka = 6.0
        desired_angle_goal = math.atan2(ygoal-y, xgoal-x)
        dtheta = desired_angle_goal-theta 
        if dtheta > math.pi:
            #angular_speed = ka * (dtheta)
            dtheta = dtheta - 2*math.pi
        elif dtheta < -math.pi:
            #angular_speed = ka * (aux)
            dtheta = 2*math.pi
        angular_speed = ka * (dtheta)

        cf2dist = math.sqrt(((cf2x- x)**2)+((cf2y-y)**2))
        cf3dist = math.sqrt(((cf3x- x)**2)+((cf3y-y)**2))
        cf4dist = math.sqrt(((cf4x- x)**2)+((cf4y-y)**2))
        down_wall = math.sqrt(((x-x)**2) + ((0.5-y)**2))
        print("down:",down_wall)
        up_wall = math.sqrt(((x-x)**2) + ((10.5-y)**2))
        print("up:",up_wall)
        r_wall = math.sqrt(((10.5-x)**2) + ((y-y)**2))
        print("right:",r_wall)
        l_wall = math.sqrt(((0.5-x)**2) + ((y-y)**2))
        print("left:",l_wall,"\n")

        print("cf3dist:", cf3dist)


        if  (cf2dist < 2):

            heading = cf2theta
            t_h = heading + cf2ang * 0.1
            menace = [(math.cos(t_h))/cf2lin,(math.sin(t_h))/cf2lin]
            direction_vector(menace)

        elif (cf3dist < 2):
            if cf3lin != 0:
                heading = cf3theta
                t_h = heading + cf3ang * 0.1
                menace = [(math.cos(t_h))/cf3lin,(math.sin(t_h))/cf3lin]
                direction_vector(menace)
                print("cf3dist:", cf3dist)
            else:
                heading = cf3theta
                t_h = heading + cf3ang * 0.1
                menace = [(math.cos(t_h)),(math.sin(t_h))]
                direction_vector(menace)
                print("cf3dist:", cf3dist)
                pass

        elif (cf4dist < 2):

            heading = cf4theta
            t_h = heading + cf4ang * 0.1
            menace = [(math.cos(t_h))/cf4lin,(math.sin(t_h))/cf4lin]
            direction_vector(menace)
        elif (down_wall < 0.5):

            menace=[(x,1)]
            direction_vector(menace)

        elif (up_wall < 0.5):

            menace=[x,1.5]
            #velocity_message.linear.x = linear_speed*0.5
            direction_vector(menace)

        elif (r_wall < 0.5):
            print("alv vas a CCHOCAR")
            time.sleep(1)
            menace=[10.5,y]
            direction_vector(menace)

        elif (l_wall < 0.5):

            menace=[-10,y]
            direction_vector(menace)

        else:

            velocity_message.linear.x = linear_speed
            velocity_message.angular.z = angular_speed
            velocity_publisher.publish(velocity_message)
        #print ('x=', x, 'y=', y)
        # print(dtheta)
        if (distance < 0.01):
            break

if __name__ == '__main__':
    try:

        rospy.init_node('turtlesim_motion_pose', anonymous = True)

        cmd_vel_topic = '/turtle0/cmd_vel'
        velocity_publisher = rospy.Publisher(cmd_vel_topic, Twist, queue_size = 10)

        position_topic = "/turtle0/pose"
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback)

        position_topic_pub = "/turtle0/pose"
        pose_subscriber = rospy.Publisher(position_topic_pub, Pose, queue_size=10)

        cf2_position_topic = "/turtle2/pose"
        pose_subscriber = rospy.Subscriber(cf2_position_topic, Pose, cf2Callback)

        cf3_position_topic = "/turtle3/pose"
        pose_subscriber = rospy.Subscriber(cf3_position_topic, Pose, cf3Callback)

        cf4_position_topic = "/turtle4/pose"
        pose_subscriber = rospy.Subscriber(cf4_position_topic, Pose, cf4Callback)

        time.sleep(2)     

        
        #Frth line
        #Bot R
        # time.sleep(2.0)
        # orientate(1,1)
        # time.sleep(1.0)
        # go_to_goal(1,1)
        # time.sleep(1.0)	

        time.sleep(2.0)
        orientate(10,10)
        time.sleep(0.5)
        go_to_goal(10,10)
        time.sleep(0.5)	
         #Thrd line
        #Top R
        orientate(1,5.5)
        time.sleep(0.5)
        go_to_goal(1,5.5)
        time.sleep(0.5)		
        #Scnd line
        #Top L
        orientate(10,5.5)
        time.sleep(0.5)
        go_to_goal(10,5.5)
        time.sleep(0.5)

        #frst line 
        #Btm L
        orientate(1,1)
        time.sleep(0.5)
        go_to_goal(1,1)
        time.sleep(0.5)
        #rotate(45)
        orientate(9,10)
        time.sleep(0.1)

    except rospy.ROSInterruptException:        
        pass