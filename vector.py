from math import sqrt, acos, pi
from decimal import Decimal, getcontext

getcontext().prec = 30

def replace_if_within_tolerance(val, compared_against, tolerance = 1e-10):
        if abs(val - compared_against) < tolerance: return compared_against
        else: return val

class Vector(object):
    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
    NO_UNIQUE_PARALLEL_COMPONENT_MSG = 'not unique parallel'
    NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG = 'not unique orthogonal'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        return Vector([(a + b) for (a,b) in zip(self.coordinates, v.coordinates)])
        # sum = []
        # for index, elem in enumerate(self.coordinates):
            # sum.append(v.coordinates[index] + elem)
        # return Vector(sum)

    def minus(self, v):
        return Vector([(a - b) for (a,b) in zip(self.coordinates, v.coordinates)])

    def times_scalar(self, a):
        return Vector([Decimal(a) * i for i in self.coordinates])

    def magnitude(self):
        sum_of_coordinates =  sum([i**2 for i in self.coordinates])
        return Decimal(sqrt(sum_of_coordinates))

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal('1.0')/magnitude)

        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    # inner product, or dot product of v1 and v2:
    # v1.v2 = ||v1|| * ||v2|| * cos(theta)
    # theta is the smaller angle between the two vectors
    # because -1 <= cos(theta) <= 1:
    # Cauchy-Schwarz Inequality:
    # |v1.v2| <= ||v1|| * ||v2||
    def dot(self, v):
        return sum([a*b for a,b in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = v.normalized()
            #Capture within range of dot product to be within 1 & -1
            u1u2dot = replace_if_within_tolerance(u1.dot(u2),1)
            u1u2dot = replace_if_within_tolerance(u1.dot(u2),-1)
            theta_in_rad = acos(u1u2dot)

            if in_degrees:
                degrees_per_radian = 180. / pi
                return theta_in_rad * degrees_per_radian
            else:
                return theta_in_rad

        except Exception as e:
            if str(e == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG):
                raise Exception('Cannot compute and angle with the zero vector')
            else:
                raise e

    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    def is_parallel_to(self, v):
        return (self.is_zero() or
                v.is_zero() or
                self.angle_with(v) == 0 or
                self.angle_with(v) == pi)
        # u1 = self.normalized()
        # u2 = v.normalized()
        # print(u1, u2)
        # return u1 == u2

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance
    
    # v projection into b:
    # v = v_parallel + v_orthogonal
    # ||v_parallel|| = ||v||cos(theta)
    # ||v_parallel|| = v . ub

    def projection(self, b):
        ub = b.normalized()
        v_parallel_mag = self.dot(ub)

        v_parallel = ub.times_scalar(v_parallel_mag)
        vT = self.minus(v_parallel)

        return v_parallel, vT

    def component_orthogonal_to(self, basis):
        try:
            projection = self.component_parallel_to(basis)
            return self.minus(projection)
        
        except Exception as e:
            if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
                raise Exception(self.NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
            else:
                raise e
    
    def component_parallel_to(self, basis):
        try:
            u = basis.normalized()
            weight = self.dot(u)
            return u.times_scalar(weight)
        
        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
            else:
                raise e