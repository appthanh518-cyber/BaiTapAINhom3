
import random
from simpleai.search import SearchProblem, hill_climbing


class LogicProblem(SearchProblem):
    def __init__(self, initial_state):
        super().__init__(initial_state)

    # Hàm đánh giá trạng thái
    def value(self, state):
        p, q, r = state

        return (
            int((not p) or q) +
            int((not q) or r) +
            int(p) +
            int(not r)
        )

    # Các hành động có thể thực hiện
    def actions(self, state):
        return [0, 1, 2]

    # Tạo trạng thái mới bằng cách đảo giá trị biến
    def result(self, state, action):
        new_state = list(state)
        new_state[action] = not new_state[action]
        return tuple(new_state)


def hybrid_adaptive_local_search(max_restarts=20):
    best_state = None
    best_value = -1

    # Mức độ thay đổi trạng thái ban đầu
    perturbation = 1

    for restart in range(max_restarts):

        # Khởi tạo trạng thái ngẫu nhiên
        state = tuple(random.choice([True, False])
                      for _ in range(3))

        problem = LogicProblem(state)

        # Hill Climbing
        result = hill_climbing(
            problem,
            iterations_limit=100
        )

        current_state = result.state
        current_value = problem.value(current_state)

        # Lưu trạng thái tốt nhất
        if current_value > best_value:
            best_state = current_state
            best_value = current_value
            perturbation = 1
        else:
            # Tăng mức độ thay đổi khi bị mắc kẹt
            perturbation = min(perturbation + 1, 3)

        # Kiểm tra đã tìm được phản ví dụ chưa
        if best_value == 4:
            break

    return best_state, best_value


# Chạy thuật toán
state, value = hybrid_adaptive_local_search()

print("Trang thai tot nhat:", state)
print("Gia tri danh gia:", value, "/ 4")

if value == 4:
    print("Tim thay phan vi du!")
else:
    print("Khong tim thay phan vi du.")
