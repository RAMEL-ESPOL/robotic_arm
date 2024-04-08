#! /usr/bin/env python3

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import numpy as np
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
from moveit_commander.conversions import pose_to_list
import math

# Altura del lapiz
global pen 
pen = 0.22

#El paso que habrá entre una coordenada y la siguiente a la hora de escribir
global t
t = 0.01

#Altura máxima a la que llegará cada letra en Y
global y_h 
y_h = 0.225

#Tamaño de cada letra en ancho y alto
global size
size = 0.05

#Espacio entre cada letra
global space
space = 0.01

def home():
    # We get the joint values from the group and change some of the values:
    joint_goal = group.get_current_joint_values()
    joint_goal[0] = 0
    joint_goal[1] = 0
    joint_goal[2] = 0
    joint_goal[3] = 0
    joint_goal[4] = 0
    joint_goal[5] = 0

    # The go command can be called with joint values, poses, or without any
    # parameters if you have already set the pose or joint target for the group
    group.go(joint_goal, wait=True)
    rospy.loginfo("The robotic arm is at home position.")

def loginfog(msg: str):
    rospy.loginfo("\033[92m%s\033[0m" % msg)

def print_plan(w: list, s: str):
    message = "\n--------------------------------------------------------------"
    for i in range(len(w)):
        message += """
Pose {0}:\n{1}
--------------------------------------------------------------""".format( i , w[i])
    
    rospy.loginfo(message)
    loginfog("Drawing a " + s)

def plan_circle( center_x : float , center_y : float , r : float , theta_o : float  , theta_f : float , wpose, circle_waypoints : list , sentido_x : bool, sentido_y : bool):
    if (sentido_x and sentido_y):
        for theta in range(theta_o, theta_f + 1, 2):
            wpose.position.y = center_y + r*math.sin(theta*math.pi/180)
            wpose.position.x = center_x + r*math.cos(theta*math.pi/180)
            circle_waypoints.append(copy.deepcopy(wpose))
    elif (not(sentido_x) and sentido_y):
        for theta in range(theta_o, theta_f + 1, 2):
            wpose.position.y = center_y + r*math.sin(theta*math.pi/180)
            wpose.position.x = center_x - r*math.cos(theta*math.pi/180)
            circle_waypoints.append(copy.deepcopy(wpose))
    elif (sentido_x and not(sentido_y)):
        for theta in range(theta_o, theta_f + 1, 2):
            wpose.position.y = center_y - r*math.sin(theta*math.pi/180)
            wpose.position.x = center_x + r*math.cos(theta*math.pi/180)
            circle_waypoints.append(copy.deepcopy(wpose))
    else:
        for theta in range(theta_o, theta_f + 1, 2):
            wpose.position.y = center_y - r*math.sin(theta*math.pi/180)
            wpose.position.x = center_x - r*math.cos(theta*math.pi/180)
            circle_waypoints.append(copy.deepcopy(wpose))

    return circle_waypoints, wpose

def plan_A(wpose, waypoints : list):

    wpose.position.y -= size
    waypoints.append(copy.deepcopy(wpose))    

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    

    wpose.position.y += size
    waypoints.append(copy.deepcopy(wpose))    

    wpose.position.x += size
    waypoints.append(copy.deepcopy(wpose))    

    wpose.position.y -= size
    waypoints.append(copy.deepcopy(wpose))    

    wpose.position.y += size/2
    waypoints.append(copy.deepcopy(wpose))    

    wpose.position.x -= size
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.z = pen + 0.05
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.y  = y_h
    wpose.position.x += size + space
    waypoints.append(copy.deepcopy(wpose))

    return (waypoints, wpose)


def plan_B(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    


    return (waypoints, wpose)


def plan_C(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    


    return (waypoints, wpose)


def plan_D(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    


    return (waypoints, wpose)


def plan_E(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    


    return (waypoints, wpose)


def plan_F(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    


    return (waypoints, wpose)


def plan_G(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    


    return (waypoints, wpose)


def plan_H(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    


    return (waypoints, wpose)


def plan_I(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.x += size
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.x -= size/2
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.y -= size
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.x += size/2
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.x -= size
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.z = pen + 0.05
    waypoints.append(copy.deepcopy(wpose))

    wpose.position.y = y_h
    wpose.position.x += size + space
    waypoints.append(copy.deepcopy(wpose))

    return (waypoints, wpose)


def plan_J(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    


    return (waypoints, wpose)


def plan_K(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    


    return (waypoints, wpose)


def plan_L(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    


    return (waypoints, wpose)


def plan_M(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    


    return (waypoints, wpose)


def plan_N(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    


    return (waypoints, wpose)


def plan_O(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    


    return (waypoints, wpose)


def plan_P(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    


    return (waypoints, wpose)


def plan_Q(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    


    return (waypoints, wpose)


def plan_R(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    


    return (waypoints, wpose)


def plan_S(wpose, waypoints : list):

    wpose.position.x += size
    waypoints.append(copy.deepcopy(wpose))    

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    

    wpose.position.x -= size
    waypoints.append(copy.deepcopy(wpose))    

    wpose.position.y -= size/2
    waypoints.append(copy.deepcopy(wpose))    

    wpose.position.x += size
    waypoints.append(copy.deepcopy(wpose))    
    
    wpose.position.y -= size/2
    waypoints.append(copy.deepcopy(wpose))    

    wpose.position.x -= size
    waypoints.append(copy.deepcopy(wpose))    
    
    wpose.position.z = pen + 0.05
    waypoints.append(copy.deepcopy(wpose))    
    
    wpose.position.x += size + space
    wpose.position.y = y_h
    waypoints.append(copy.deepcopy(wpose))    
    
    
    return (waypoints, wpose)


def plan_T(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    


    return (waypoints, wpose)


def plan_U(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    


    return (waypoints, wpose)


def plan_V(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    


    return (waypoints, wpose)


def plan_W(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    


    return (waypoints, wpose)


def plan_X(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    


    return (waypoints, wpose)


def plan_Y(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    


    return (waypoints, wpose)


def plan_Z(wpose, waypoints : list):

    wpose.position.z = pen
    waypoints.append(copy.deepcopy(wpose))    

    wpose.position.x += size
    waypoints.append(copy.deepcopy(wpose))    

    wpose.position.y -= size
    wpose.position.x -= size
    waypoints.append(copy.deepcopy(wpose))    

    wpose.position.x += size
    waypoints.append(copy.deepcopy(wpose))    
    
    wpose.position.z = pen + 0.05
    waypoints.append(copy.deepcopy(wpose))    
    
    wpose.position.x += space
    wpose.position.y = y_h
    waypoints.append(copy.deepcopy(wpose))    

    return (waypoints, wpose)


#By executing this file we can make the robot move to several preconfigured positions in Cartesian coordinates, in the order in which they are in the file
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('planing_node', anonymous=True)
rate = rospy.Rate(10)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()    
group = moveit_commander.MoveGroupCommander("arm_group")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)

home()
# Calling ``stop()`` ensures that there is no residual movement
group.stop()
word = input("Write the word you want the robotic arm write: ").upper()
if (((space + size)*len(word)) <= 0.5):
    waypoints = []

    x_i = -1*(len(word)/2 * (size + space))#Cálculo de la posición inicial del lápiz
    print(x_i)
    #Moviendo lápiz a la posición inicial
    wpose = group.get_current_pose().pose
    wpose.position.x = x_i
    wpose.position.y = y_h
    wpose.position.z = pen + 0.05
    waypoints.append(copy.deepcopy(wpose))    

    for w in word:
        rospy.logerr(w)
        (waypoints, wpose) = (plan_A(wpose,waypoints) if w == "A" else
                             (plan_B(wpose,waypoints) if w == "B" else
                             (plan_C(wpose,waypoints) if w == "C" else
                             (plan_D(wpose,waypoints) if w == "D" else
                             (plan_E(wpose,waypoints) if w == "E" else
                             (plan_F(wpose,waypoints) if w == "F" else
                             (plan_G(wpose,waypoints) if w == "G" else
                             (plan_H(wpose,waypoints) if w == "H" else
                             (plan_I(wpose,waypoints) if w == "I" else
                             (plan_J(wpose,waypoints) if w == "J" else
                             (plan_K(wpose,waypoints) if w == "K" else
                             (plan_L(wpose,waypoints) if w == "L" else
                             (plan_M(wpose,waypoints) if w == "M" else
                             (plan_N(wpose,waypoints) if w == "N" else
                             (plan_O(wpose,waypoints) if w == "O" else
                             (plan_P(wpose,waypoints) if w == "P" else
                             (plan_Q(wpose,waypoints) if w == "Q" else
                             (plan_R(wpose,waypoints) if w == "R" else
                             (plan_S(wpose,waypoints) if w == "S" else
                             (plan_T(wpose,waypoints) if w == "T" else
                             (plan_U(wpose,waypoints) if w == "U" else
                             (plan_V(wpose,waypoints) if w == "V" else
                             (plan_W(wpose,waypoints) if w == "W" else
                             (plan_X(wpose,waypoints) if w == "X" else
                             (plan_Y(wpose,waypoints) if w == "Y" else
                             (plan_Z(wpose,waypoints) if w == "Z" else []))))))))))))))))))))))))))
        
    plan  = group.compute_cartesian_path(waypoints, t, 0.0)[0]

    display_trajectory = moveit_msgs.msg.DisplayTrajectory()
    display_trajectory.trajectory_start = robot.get_current_state()
    display_trajectory.trajectory.append(plan)
    # Publish
    display_trajectory_publisher.publish(display_trajectory)

    group.execute(plan, wait=True)
    rospy.loginfo("Planning succesfully executed.\n")
else:
    rospy.logerr("The word has too many letters.")
home()
