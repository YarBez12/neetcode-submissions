class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        leftAsteroids = []
        for asteroid in asteroids:
            if asteroid > 0:
                leftAsteroids.append(asteroid)
                continue
            prev = asteroid
            while leftAsteroids and leftAsteroids[-1] > 0 and prev < 0:
                if abs(leftAsteroids[-1]) > abs(prev):
                    break
                if abs(leftAsteroids[-1]) == abs(prev):
                    leftAsteroids.pop()
                    break
                leftAsteroids.pop()
            else:
                leftAsteroids.append(asteroid)
        return leftAsteroids

        