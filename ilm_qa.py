"""Questions and answers for Technical Pipeline Director II at ILM.
This module was developed with python 3.10.
Run in a terminal with python 3:
>>> `python -m ilm_qa`
"""
from contextlib import contextmanager
from dataclasses import dataclass
from io import BytesIO
import json

MIN_PR: int = 0
MAX_PR: int = 10


class Command(str):
    pass


@dataclass
class Job:
    command: Command
    priority: int
    next: "Job" = None

    def __post_init__(self):
        assert self.priority in range(MIN_PR, MAX_PR + 1), "`priority` must be an integer value [0, 10]"


class PriorityQueue:
    """A descending order priority queue using a linked list of `Job`,
    where priority 10 is the highest and 0 is lowest.
    """

    def __init__(self):
        self.head: Job = None

    def is_empty(self) -> bool:
        """Check whether the queue is empty.
        """
        return self.head is None

    def enqueue(self, command: Command, priority: int):
        """Insert a command and its priority (an integer value [0,10]) into the queue.
        """
        job = Job(command, priority)
        if self.is_empty():
            self.head = job
        elif priority > self.head.priority:
            job.next = self.head
            self.head = job
        else:
            current = self.head
            while current.next is not None and current.next.priority >= priority:
                current = current.next
            job.next = current.next
            current.next = job

    def dequeue(self) -> Command:
        """Get the command in the queue with the highest priority.
        """
        if self.is_empty():
            return None
        job = self.head
        self.head = self.head.next
        return job.command

    def peek(self) -> Command:
        """Return the highest priority command.
        """
        if self.is_empty():
            return None
        return self.head.command


@contextmanager
def question(question):
    print(question + "\n")
    yield
    print("====================================================\n")


@question("1. Explain Big-O notation in simple terms:")
def answer1():
    print(
        """
    Big-O notation is a conventional way to mathematically describe the performance of a function or algorithm.
    It is commonly used in computer science to give an approximation of the worst-case analysis
    in which an algorithm will grow in space or time, also known as "complexity analysis".
    For example, if we observe the running time of an algorithm to grow linearly with the input size,
    then we say that the algorithm is O(n) or linear.
    If the running time grows quadratically with the input size, then we say that the algorithm is O(n^2) or quadratic.
    Other common growth rates found in complexity analysis are:
    O(1) or constant
    O(log n) or logarithmic
    O(2^n) or exponential
    O(n^3) or cubic
    
    Therefore, algorithms with a very large input size should ideally have a "big O of logn" (i.e. logarithmic) or a "big O of n" 
    (i.e. linear). In contrast, algorithms that are big-O quadratic or exponential would 
    drastically degrade in performance when using large input sizes.
    """
    )


@question("2. What are the most important things to look for when reviewing another team member's code?")
def answer2():
    print(
        """
    The first thing to check in another team member's code is whether it solves the problem at hand 
    or supports a relevant user story (i.e. a goal and acceptance criteria).
    Typically we can do this by running the code using parameters covering the common use cases, 
    as well as some edge cases.
    If the code comes with unit tests, check whether the tests provide sufficient coverage.
    It's also important to examine the code for readability and maintainability, and that it follows
    best practices (such as separation of concerns, encapsulation, etc.). 
    Coding style should follow company's style guide.
    Ideally the code should come with documentation. Sometimes, if the logic is easy enough 
    to follow, documentation could be omitted.
    Any security vulnerabilities should also be flagged.
    If performance could be easily improved somewhere in the code, then that should be pointed out too.
    I believe sometimes it's okay to be pedantic in providing feedback as long as it benefits the goal,
    helps the reviewee produce better quality code, and does not hinder development or release time.
    """
    )


@question(
    "3. Describe a recent interaction with someone who was non-technical."
    "What did you need to communicate and how did you do it?"
)
def answer3():
    print(
        """
     My partner is new to programming and learning R. She asked what a high-level language is, so I explained that it’s a type of 
    programming language that is not understood by a computer’s processor but can be used to give the computer instructions after 
    translating it to a low-level language which it understands. High-level languages, such as R and Python, are are more natural 
    and easier to understand to humans than low-level languages, such as assembly and machine code. Both high-level and low-level 
    languages are alternative ways of giving a computer instructions. 
    I gave her the following analogy:
    Say there’s a blanket factory that can create any pattern you wish. However the factory workers speak a language that very 
    few people outside the factory understand and they are the only ones who can operate the machines. A designer needs to create a 
    blanket but is only fluent in a language that is commonly used outside the factory that the workers don’t understand. They write 
    the instructions for a blanket pattern in the common language and they give them to the factory manager who will translate it into 
    the worker’s language. The instructions can now be understood by the factory workers. In this analogy, the designer’s language is 
    farther from the machine, known as a “high-level language”,  while the worker’s language is closer to the machine, known as the 
    “low-level language”.
    """
    )


@question("4. Implement a simple priority queue.")
def answer4():
    
    commands_stream = BytesIO(
        b'[{"command": "zbe", "priority": 7}, {"command": "lmy", "priority": 10}, {"command": "swc", "priority": 7}, {"command": "jtc", "priority": 2}, {"command": "slg", "priority": 4}, {"command": "rwa", "priority": 10}, {"command": "zln", "priority": 1}, {"command": "ytm", "priority": 6}, {"command": "aou", "priority": 8}, {"command": "uuv", "priority": 3}]'
    )
    commands = json.load(commands_stream)
    print(commands)
    pq = PriorityQueue()

    MAX = len(commands) + 1
    for command in commands[:MAX]:
        (command, priority) = command.values()
        pq.enqueue(command, priority)
        print(f"enqueued: {command!r} (priority {priority})")
    print("\nDequeueing...")
    queued_commands = []
    for _ in range(0, MAX):
        comm = pq.dequeue()
        if comm:
            queued_commands.append(comm)
            print(f"dequeued: {comm!r}")

    expected = ["lmy", "rwa", "aou", "zbe", "swc", "ytm", "slg", "uuv", "jtc", "zln"]
    assert expected == queued_commands, f"Expected order of commands: {expected}; Got: {queued_commands}"


def main():
    answer1()
    answer2()
    answer3()
    answer4()


if __name__ == "__main__":
    main()
