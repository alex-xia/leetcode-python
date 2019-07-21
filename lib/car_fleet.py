'''
N cars are going to the same destination along a one lane road.  The destination is target miles away.

Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i] miles towards the target along the road.

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored - they are assumed to have the same position.

A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.


How many car fleets will arrive at the destination?



Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.

Note:

0 <= N <= 10 ^ 4
0 < target <= 10 ^ 6
0 < speed[i] <= 10 ^ 6
0 <= position[i] < target
All initial positions are different.
'''

class Solution(object):
    def __init__(self):
        self.fleets_cnt = 0

    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        if len(position) == 0:
            return 0
        fleets = {}
        arrived = set()
        for i in xrange(0, len(position)):
            fleet_pos, fleet_speed = position[i], speed[i]
            if fleet_pos >= target:
                arrived.add(fleet_pos)
            else:
                self.addFleetToFleets(fleet_pos, fleet_speed, fleets)

        self.carFleetsRun(target, fleets, len(arrived))
        return self.fleets_cnt


    def carFleetsRun(self, target, fleets, arrived_cnt):
        print target, fleets, arrived_cnt
        if len(fleets) == 0:
            self.fleets_cnt = arrived_cnt
            return
        fleets_new = {}
        arrived = set()
        for fleet_pos in fleets:
            fleet_speed = fleets[fleet_pos]
            fleet_pos_new = fleet_pos + fleet_speed
            if fleet_pos_new >= target:
                arrived.add(1.0 * (target - fleet_pos) / fleet_speed)
            else:
                self.addFleetToFleets(fleet_pos_new, fleet_speed, fleets_new)
        # if len(arrived) > 0:
        #     print '=====' + str(arrived)
        return self.carFleetsRun(target, fleets_new, arrived_cnt + len(arrived))

    def addFleetToFleets(self, fleet_pos, fleet_speed, fleets):
        if fleet_pos in fleets:
            fleets[fleet_pos] = min(fleets[fleet_pos], fleet_speed)
        else:
            fleets[fleet_pos] = fleet_speed


if __name__ == '__main__':
    sol = Solution()
    # print sol.carFleet(12, [10,8,0,5,3], [2,4,1,1,3])
    # print sol.carFleet(10, [8,3,7,4,6,5], [4,4,4,4,4,4])
    print sol.carFleet(20, [6,2,17], [3,9,2])
    # print sol.carFleet(10, [3], [3])