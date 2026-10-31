class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [] # [pos, speed]
        car_fleets = []
        for i in range(len(position)):
            pos_speed.append([position[i], speed[i]])

        pos_speed = sorted(pos_speed)[::-1]

        for car in pos_speed:
            if car_fleets and car_fleets[-1] >= (target - car[0]) / car[1]:
                pass
            else: 
                car_fleets.append((target - car[0]) / car[1])

        return len(car_fleets)
