class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        for asteroid in asteroids:
            # If the asteroid is moving to the right (positive), just add it to the stack
            if asteroid > 0:
                stack.append(asteroid)
            else:  # If the asteroid is moving to the left (negative)
                while stack and stack[-1] > 0:  # While there are asteroids moving to the right
                    if stack[-1] < abs(asteroid):  # Current asteroid destroys the previous one
                        stack.pop()
                    elif stack[-1] == abs(asteroid):  # Both asteroids are destroyed
                        stack.pop()
                        break  # No further collisions
                    else:  # Current asteroid is destroyed, previous remains
                        break
                else:  # If there were no asteroids moving to the right or all are destroyed
                    stack.append(asteroid)
        return stack
