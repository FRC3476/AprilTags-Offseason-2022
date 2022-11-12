from _pynetworktables import NetworkTables

NetworkTables.initialize(server="localhost")
vision_table = NetworkTables.getDefault().getTable("Vision")


def log_pos(x, z):
    vision_table.getEntry("x_pos").setValue(float(x))
    vision_table.getEntry("z_pos").setValue(float(z))
