# Load the PicoBorg Reverse library
import PicoBorgRev

# Load the standard time library
import time

# Setup the PicoBorg Reverse so it is ready to use
PBR = PicoBorgRev.PicoBorgRev()
PBR.Init()

# Reset the EPO flag to enable motors
PBR.ResetEpo()

# Determine the maximum power output
# In this case 6V motors from a 10x AA rechargeable (1.2 V) pack
maxPower = 6.0 / 12.0

# Run motor 1 forwards at full power
# for 5 seconds, then stop motor 1
PBR.SetMotor1(1.0 * maxPower)
time.sleep(5.0)
PBR.SetMotor1(0)

# Run motor 2 forwards at half power
# for 5 seconds, then stop motor 2
PBR.SetMotor2(0.5 * maxPower)
time.sleep(5.0)
PBR.SetMotor2(0)

# Run motors 3 and 4 backwards at 3/4 power
# for ten seconds, then stop all motors
PBR.SetMotor3(-0.75 * maxPower)
PBR.SetMotor4(-0.75 * maxPower)
time.sleep(10.0)
PBR.MotorsOff()

# Run all motors forwards at half power
# for ten seconds, then stop all motors
PBR.SetMotors(0.5 * maxPower)
time.sleep(10.0)
PBR.MotorsOff()