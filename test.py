from pyseneye.sud import SUDevice, Action

d = SUDevice()

d.action(Action.ENTER_INTERACTIVE_MODE)
s = d.action(Action.SENSOR_READING)
print(s.ph)

print(s.nh3)

print(s.temperature)

#d.action(Action.LEAVE_INTERACTIVE_MODE)
#d.close()

