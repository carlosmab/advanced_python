# Build a simple program that simulates a race 
# between multiple runners using threads. 
# Each runner should be represented by a separate thread,
# and they should all start running at the same time. 
# The program should print the progress of each runner at 
# regular intervals until they all reach the finish line.


import time
from threading import Thread
import unittest

class TestRaceSimulation(unittest.TestCase):
    
    def test_race_simulation(self):
        runners = ['Runner 1', 'Runner 2', 'Runner 3']
        progress = {runner: 0 for runner in runners}

        def simulate_runner(runner):
            while progress[runner] < 100:
                time.sleep(0.1)
                progress[runner] += 10

        threads = [Thread(target=simulate_runner, args=(runner,)) for runner in runners]
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        for runner, runner_progress in progress.items():
            self.assertEqual(runner_progress, 100, f'{runner} did not reach the finish line')

if __name__ == '__main__':
    unittest.main()