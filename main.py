import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)
            
    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            all_balls = self.contents.copy()
            self.contents = []
            return all_balls
        drawn_balls = []
        for _ in range(num_balls):
            ball_index = random.randrange(len(self.contents))
            drawn_balls.append(self.contents.pop(ball_index))
            
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_counts = {}
        for ball in drawn_balls:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1
        success = True
        for color, count in expected_balls.items():
            if color not in drawn_counts or drawn_counts[color] < count:
                success = False
                break
                
        if success:
            success_count += 1
            
    return success_count / num_experiments