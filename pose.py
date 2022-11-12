# Offsets for each tag around the field to make their orgins at the same place and normalize them
# Format is (X_OFFSET, X_NORMALIZATION, Y_OFFSET, Y_NORMALIZATION, Z_OFFSET, Z_NORMALIZATION)
import network

offset_map = {
    0: (.08, .17, .18, .29, 0, .8),
    1: (0, 0, 0, 0, 0, 0),
    2: (0, 0, 0, 0, 0, 0),
    3: (0, 0, 0, 0, 0, 0)
}


# Find coordinates of tag (normalized to 0-1) (Orgin is left, bottom, far)
def normalize_pose(detection):
    offsets = offset_map[detection.tag_id]
    x_pos = (detection.pose_t[0] + offsets[0]) / offsets[1]
    y_pos = (detection.pose_t[1] + offsets[2]) / offsets[3]
    z_pos = (detection.pose_t[2] + offsets[4]) / offsets[5]

    # Temporary non-gyro pose, must be parallel to tag 0
    if detection.tag_id == 0:
        network.log_pos(x_pos, z_pos)

    return x_pos, y_pos, z_pos
