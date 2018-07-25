# Now, this file ("test.py") is in python terminology a "module". 
# We can import it (as long as it can be found in our PYTHONPATH) 
# Note that the current directory is always in PYTHONPATH, so if use_test is 
# being run from the same directory where test.py lives, you're all set:
from vector import Vector



v1 = Vector([7.887, 4.138])
v2 = Vector([-8.802, 6.776])
v3 = Vector([-5.955, -4.904, -1.874])
v4 = Vector([-4.496, -8.755, 7.103])

v5 = Vector([3.183, -7.627])
v6 = Vector([-2.668, 5.319])
v7 = Vector([7.35, 0.221, 5.188])
v8 = Vector([2.751, 8.259, 3.985])



# print(v1.dot(v2))
# print(v3.dot(v4))

# print(v5.angle_with(v6))
# print(v7.angle_with(v8,True))


v9 = Vector([-7.579, -7.88])
v10 = Vector([22.737, 23.64])

# print(v9.is_parallel_to(v10))
# print(v9.is_orthogonal_to(v10))

v11 = Vector([-2.029, 9.97, 4.172])
v12 = Vector([-9.231, -6.639, -7.245])

# print(v11.is_parallel_to(v12))
# print(v11.is_orthogonal_to(v12))

v13 = Vector([-2.328, -7.284, -1.214])
v14 = Vector([-1.821, 1.072, -2.94])

# print(v13.is_parallel_to(v14))
# print(v13.is_orthogonal_to(v14))

v15 = Vector([3.039, 1.879])
v16 = Vector([0.825, 2.036])

p = v15.projection(v16)
# print(p[0], p[1])


v17 = Vector([-9.88, -3.264, -8.159])
v18 = Vector([-2.155, -9.353, -9.473])

p = v17.projection(v18)
# print(p[0], p[1])

v19 = Vector([3.009, -6.172, 3.692, -2.51])
v20 = Vector([6.404, -9.144, 2.759, 8.718])

p = v19.projection(v20)
print(p[0], p[1])