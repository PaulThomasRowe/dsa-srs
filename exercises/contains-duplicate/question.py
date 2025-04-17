class Example:
    def __init__(self, input, output):
        self.input = input
        self.output = output

class Link:
    def __init__(self, description: str = None, link: str):
        self.description = description
        self.link = link

class Question:
    def  __init__(self, leetcode_number: int = None, name: str, description: str, examples: list[Example], contraints: list[str], hints: list[str], links: list[Link], solutions: list[str], best_solution str = None):
        self.leetcode_number = leetcode_number
        self.name = name
        self.description = description
        self.examples = examples
        self.constraints = constraints
        self.hints = hints
        self.links = links
        self.solutions = solutions
        self.best_solution = best_solution

lcn = None
n = "Contains Duplicate"
d = "Given an integer array nums, return true if any value appears more than once in the array, otherwise return false."
e1 = Example([1,2,3,3], true)
e2 = Example([1,2,3,4], false)
e = [e1,e2]
c = None
h1 = "A brute force solution would be to check every element against every other element in the array. This would be an O(n^2) solution. Can you think of a better way?"
h2 = "Is there a way to check if an element is a duplicate without comparing it to every other element? Maybe there's a 资料 structure that is useful here."
h3 = "We can use a hash data structure like a hash set or hash map to store elements we've already seen. This will allow us to check if an element is a duplicate in constant time."
h = [h1, h2, h3]
l1 = "https://neetcode.io/problems/duplicate-integer"
l = [l1]
#TBD
s = None
bs = None

q = Question(leetcode_number=lcn, name=n, description=d, examples=e, constraints=c, hints=h, links=l, solutions=s, best_solution=bs)
