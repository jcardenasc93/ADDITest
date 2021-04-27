""" Module to run processes in parallel """

from threading import Thread


class ParallelProcessing:
    """ Class implementation for handle parallel excecutions """

    def __init__(self, *tasks):
        self._tasks = tasks

    def run_tasks_in_parallel(self):
        """ This method runs tasks in parallel
        and join the responses
        """
        # Run tasks
        self.processes = []
        for task in self._tasks:
            process = Thread(target=task)
            process.start()
            self.processes.append(process)
        self.wait_for_completion()

    def wait_for_completion(self):
        # Join executions
        for process in self.processes:
            process.join()
