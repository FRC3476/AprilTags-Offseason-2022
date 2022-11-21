from _pynetworktables import NetworkTables

# Will need to set with ip of roboRIO when on the robot
NetworkTables.initialize()
vision_table = NetworkTables.getDefault().getTable("Vision")


def log_pos(tag_id, x, y, z):
    vision_table.getEntry(str(tag_id) + "x").setValue(float(x))
    vision_table.getEntry(str(tag_id) + "y").setValue(float(y))
    vision_table.getEntry(str(tag_id) + "z").setValue(float(z))


def log_looptime(time):
    vision_table.getEntry("Vision_Looptime").setValue(time)


def flush():
    NetworkTables.getDefault().flush()
