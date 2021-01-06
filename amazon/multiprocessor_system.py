"""
A multiprocessor system has a certain number of processors.
Each processor has the ability to schedule a limited number of processes in one second.
However, after each scheduling, the processor's ability is reduced to ability/2 rounded down to the nearest number.
Only one processor can work to schedule processes each second.
As an Amazonian you are tasked to find the minimum time required to schedule all the processes in the system
given the processor's abilities and the number of processes.

Example:
Input: num = 5, ability = [3, 1,7,2,4], processes = 15
Output: 4
Explanation:
First, the processor with ability = 7 schedules 7 processes in one second.
Now, ability = [3, 1, 3, 2, 4] because 7 was reduced to floor(7/2).
Second, the processor with ability = 4 is used. After that, ability = [3,1,3,2,2].
Third, the processor with ability = 3 is used. Now, ability = [1, 1, 3, 2, 2].
Finally, the processor with ability 1 is used to schedule the final process.
Each step requires one second of processing time, which adds up to 4.

So, the output is 4.
"""
import heapq


def multiprocessor_system(abilities, processes):
    heap = [-a for a in abilities]
    heapq.heapify(heap)

    steps = 0
    while processes > 0:
        processor = -heapq.heappop(heap)
        processes -= processor
        heapq.heappush(heap, -(processor // 2))
        steps += 1
    return steps


if __name__ == "__main__":
    assert multiprocessor_system([3, 1, 7, 2, 4], 15) == 4
