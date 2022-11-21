# Offsets for each tag around the field to make their orgins at the same place and normalize them
# Format is (X_OFFSET, X_NORMALIZATION, Y_OFFSET, Y_NORMALIZATION, Z_OFFSET, Z_NORMALIZATION)

offset_map = {
    -1: (0, 1, 0, 1, 0, 1),
    0: (0, 1, 0, 1, 0, 1),
    1: (0, 1, 0, 1, 0, 1),
    2: (0, 1, 0, 1, 0, 1),
    3: (0, 1, 0, 1, 0, 1),
    4: (0, 1, 0, 1, 0, 1)
}

offset_map.setdefault(-1)


# Find coordinates of tag (normalized to 0-1) (Orgin is left, bottom, far)
def normalize_pose(detection):
    offsets = offset_map[detection.tag_id]

    x_pos = (detection.pose_t[0] + offsets[0]) / offsets[1]
    y_pos = (detection.pose_t[1] + offsets[2]) / offsets[3]
    z_pos = (detection.pose_t[2] + offsets[4]) / offsets[5]

    return round(float(x_pos), 3), round(float(y_pos), 3), round(float(z_pos), 3)
