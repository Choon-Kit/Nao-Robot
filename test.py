import sys
import os

print(str(sys.path))

dir_path = os.path.dirname(os.path.realpath(__file__))
print("current working dir: %s\n\n" % dir_path)

lib_path = "C:\Users\choki\Desktop\Nao\sra-project-template\pynaoqi-python2.7-2.8.5.10-win64-vs2015-20181203_210310\lib"
package_path = lib_path + "\python2.7\Lib\site-packages"
sys.path.insert(0, lib_path)
sys.path.insert(0, package_path)


print(str(sys.path))

from naoqi import ALProxy
postureProxy = ALProxy("ALRobotPosture", "192.168.54.252", 9559)
postureProxy.goToPosture("StandZero", 1.0)
print postureProxy.getPostureFamily()


# tts = ALProxy("ALTextToSpeech", "192.168.54.252", 9559)
# tts.say("Good Morning, Take Care and see you next time")