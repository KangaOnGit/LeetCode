class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Intuition:
            Compute Arrival time of Each Car
            Number of Fleet = len(set(Arrival Time))
                            -> Same time will be same fleet, else different

        Problem: Once a car catches up, it becomes a fleet no matter what
            I.e: position=[10,8,0,5,3]
                    speed=[2,4,1,1,3]
                    Car at 5 and 3 has same position after time t = 1
                        -> They become a fleet regardless
                        (Takes Largest Arrival Time)
        Fix: Just sort them by Position for the simplest Solution
            Create a Stack of Arrival Time(s)
            When a new car has arrival time t:
                - If t is smaller than the fleet behind it, it forms a new fleet.
                - If t is larger than or equal to the fleet behind it, that fleet will
                    eventually catch this car, so the fleet behind disappears and inherits t
                        (Largest Arrival Time)
            Pop all fleets that merge into the current car/fleet.
            The remaining stack contains exactly the surviving fleets.
        """
        # O(nlogn) Time
        car = sorted([(p, s)for p, s in zip(position, speed)])
        stack = []
        for p, s in car:
            t = (target - p)/s # Compute Arrival Time
            # If Arrival Time is larger than previous Car
            while len(stack) > 0 and t >= stack[-1]:
                # Merge them into a Single Fleet
                stack.pop()
            stack.append(t) # Take Largest Arrival Time
        return len(stack)