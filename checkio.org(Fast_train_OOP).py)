from typing import List

class Train:
    def __init__(self,speed,distance):
        self.speed = speed
        self.distance = distance
    def __repr__(self):
        return "S:{}-D:{}".format(self.speed,self.distance)

    def create_new_trains(self) -> list:
        new_trains = []
        for speed_change in (-1,0,1):
            new_speed = self.speed + speed_change
            if new_speed <= 0: continue
            end_distance = self.distance + new_speed
            if end_distance > target_distance: continue
            if end_distance == target_distance and new_speed > 1: continue
            for current_distance in range(self.distance+1,end_distance+1):
                if new_speed > speed_limit[current_distance]:
                    break
            else:
                new_trains.append(Train(new_speed,end_distance))
        return new_trains


def fast_train(sections) -> int:
    global speed_limit, target_distance
    speed_limit = ["*"] # Anchored
    for track_length,track_speedlimit in sections:
        speed_limit += [track_speedlimit]*track_length
    target_distance = len(speed_limit) - 1

    time_elapsed = 0
    trains = [Train(0,0)]
    while True:
        time_elapsed += 1
        new_trains = []
        for train in trains:
            new_trains += train.create_new_trains()
        trains = new_trains[:]
        if any(train.distance == target_distance for train in trains):
            return time_elapsed


if __name__ == '__main__':

    assert fast_train([(4, 3)]) == 3
    assert fast_train([(9, 10)]) == 5
    assert fast_train([(5, 5), (4, 2)]) == 6
    print("Coding complete? Click 'Check' to earn cool rewards!")
