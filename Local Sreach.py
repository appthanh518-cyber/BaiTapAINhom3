
from simpleai.search import SearchProblem, hill_climbing


class LogicProblem(SearchProblem):

    def __init__(self):
        super().__init__((True, False, True))

    # Ham danh gia trang thai
    def value(self, state):
        p, q, r = state

        return (
            int((not p) or q) +
            int((not q) or r) +
            int(p) +
            int(not r)
        )

    # Cac hanh dong thay doi gia tri p, q, r
    def actions(self, state):
        return [0, 1, 2]

    # Tao trang thai moi
    def result(self, state, action):
        new_state = list(state)
        new_state[action] = not new_state[action]
        return tuple(new_state)


# Khoi tao bai toan
problem = LogicProblem()

# Tim kiem bang Hill Climbing
result = hill_climbing(problem, iterations_limit=100)

# Xuat ket qua
p, q, r = result.state

print("=== KET QUA HILL CLIMBING ===")
print("p =", p)
print("q =", q)
print("r =", r)

print("Gia tri ham danh gia:",
      problem.value(result.state), "/ 4")

# Kiem tra ket qua
if problem.value(result.state) == 4:
    print("Tim thay phan vi du.")
    print("Dinh ly khong duoc chung minh.")
else:
    print("Khong tim thay phan vi du.")
    print("Can kiem chung toan bo khong gian trang thai.")

