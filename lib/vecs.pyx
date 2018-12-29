import numpy as np
cimport numpy as np
from libc.math cimport sqrt, pi, atan2, sin, cos, acos
from tqdm import tqdm
import pygame


cdef double angle_between(np.ndarray[double, ndim=1] v1,
                          np.ndarray[double, ndim=1] v2):
    return acos(dot(v1, v2) / (norm(v1)*norm(v2)))

def py_angle_between(v1, v2):
    return angle_between(v1, v2)

cdef double dot(np.ndarray[double, ndim=1] v1,
                np.ndarray[double, ndim=1] v2):
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]


cdef double cross(np.ndarray[double, ndim=1] v1,
                  np.ndarray[double, ndim=1] v2):
    cdef double theta = angle_between(v1, v2)
    return norm(v1) * norm(v2) * sin(theta)


cdef double rad2deg(double angle):
    return angle * 180/pi


cdef double deg2rad(double angle):
    return angle * pi/180


cdef np.ndarray[double, ndim=1] mat_vec_dot(np.ndarray[double, ndim=2] matrix,
                                            np.ndarray[double, ndim=1] vec):
    cdef np.ndarray[double, ndim=1] v_new = np.zeros(3).astype(np.float64)
    v_new[0] = dot(matrix[0], vec)
    v_new[1] = dot(matrix[1], vec)
    v_new[2] = dot(matrix[2], vec)
    return v_new


cdef double norm(np.ndarray[double, ndim=1] vec):
    return sqrt(dot(vec, vec))


cdef np.ndarray[double, ndim=1] c_normalize(np.ndarray[double, ndim=1] vec):
    cdef double N = norm(vec)
    if N != 0:
        return vec_scale(vec, 1/N)
    else:
        return np.zeros(3).astype(np.float64)

def normalize(vec):
    return c_normalize(vec)


cdef np.ndarray[double, ndim=1] vec_add(np.ndarray[double, ndim=1] v1,
                                        np.ndarray[double, ndim=1] v2):
    cdef np.ndarray[double, ndim=1] v_return = np.zeros(3).astype(np.float64)
    v_return[0] = v1[0] + v2[0]
    v_return[1] = v1[1] + v2[1]
    v_return[2] = v1[2] + v2[2]
    return v_return


cdef np.ndarray[double, ndim=1] vec_sub(np.ndarray[double, ndim=1] v1,
                                        np.ndarray[double, ndim=1] v2):
    cdef np.ndarray[double, ndim=1] v_return = np.zeros(3).astype(np.float64)
    v_return[0] = v1[0] - v2[0]
    v_return[1] = v1[1] - v2[1]
    v_return[2] = v1[2] - v2[2]
    return v_return


cdef np.ndarray[double, ndim=1] vec_scale(np.ndarray[double, ndim=1] vec,
                                          double scale):
    cdef np.ndarray[double, ndim=1] v_return = np.zeros(3).astype(np.float64)
    v_return[0] = scale * vec[0]
    v_return[1] = scale * vec[1]
    v_return[2] = scale * vec[2]
    return v_return


cdef double dist2(np.ndarray[double, ndim=1] v1,
                  np.ndarray[double, ndim=1] v2):
    return (v1[0]-v2[0])**2 + (v1[1]-v2[1])**2 + (v1[2]-v2[2])**2


cdef np.ndarray[double, ndim=1] c_vector(double x, double y, double z):
    cdef np.ndarray[double, ndim=1] v = np.array([x, y, z]).astype(np.float64)
    return v

def vector(x=0.0, y=0.0, z=0.0):
    return c_vector(x, y, z)


"""
cdef np.ndarray[double, ndim=1] line_plane_intersection(np.ndarray[double, ndim=1] p0,
                                                        np.ndarray[double, ndim=1] l,
                                                        np.ndarray[double, ndim=1] l0,
                                                        np.ndarray[double, ndim=1] n):
    cdef double numerator
    cdef double denominator
    cdef np.ndarray[double, ndim=1] diff = vec_sub(p0, l0)

    numerator = dot(diff, n)
    denominator = dot(l, n)

    if denominator != 0:
        # one intersection point
"""
