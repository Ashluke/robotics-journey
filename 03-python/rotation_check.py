import numpy as np

def R(deg):
    t = np.radians(deg)
    return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])

print(R(90).T)
print(np.allclose(R(90).T, R(-90)))
print(np.allclose(R(-90).T @ R(-90), np.eye(2)), np.linalg.det(R(-90)))