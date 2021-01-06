"""
Each aircraft should be assigned two shipping routes at once: one forward route and one return route.
Due to the complex scheduling of flight plans,all aircraft have a fixed maximum operating travel distance,
and cannot be scheduled to fly a shipping route that requires more travel distance than the prescribed
maximum operating travel distance.
The goal of the system is to optimize the total operating travel distance of a given aircraft.
A forward/return shipping route pair is considered to be “optimal” if there does not exist another pair that
has a higher operating travel distance than this pair, and also has a total less than or equal to the maximum operating
travel distance of the aircraft.

For example, if the aircraft has a maximum operating travel distance of 3000 miles,
a forward/return shipping route pair using a total of 2900 miles would be optimal
if there does not exist a pair that uses a total operating travel distance of 3000 miles,
but would not be considered optimal if such a pair did exist.
Your task is to write an algorithm to optimize the sets of forward/return shipping route pairs
that allow the aircraft to be optimally utilized, given a list of forward shipping routes and a list of return shipping routes.

Ex:
maxTravelDist=7000
forwardRouteList=[[1,2000][2,4000][3,6000]]
returnRouteList=[[1,2000]]
Output: [[2,1]]

Ex:
maxTravelDist=10000
forwardRouteList=[[1,3000][2,5000][3,7000],[4,10000]
returnRouteList=[[1,2000][2,3000][3,4000][4,5000]]
Output: [[2,4],[3,2]]
"""


def air_route(forward_list, return_list, max_distance):
    diffDist = {}

    forward_list = sorted(forward_list, key=lambda x: x[1])
    return_list = sorted(return_list, key=lambda x: x[1])
    fl, rr = 0, len(return_list) - 1

    while fl < len(forward_list) and rr >= 0:
        diff = max_distance - (forward_list[fl][1] + return_list[rr][1])
        if diff >= 0:
            if diff not in diffDist:
                diffDist[diff] = []
            diffDist[diff].append([forward_list[fl][0], return_list[rr][0]])
            fl += 1
        else:
            rr -= 1

    return diffDist[min(diffDist)]


if __name__ == "__main__":

    f = [[1, 2000], [2, 4000], [3, 6000]]
    r = [[1, 2000]]
    print(air_route(f, r, 7000))  # [2, 1]

    f = [[1, 3000], [2, 5000], [3, 7000], [4, 10000]]
    r = [[1, 2000], [2, 3000], [3, 4000], [4, 5000]]

    print(air_route(f, r, 10000))  # [2, 4], [3, 2]
