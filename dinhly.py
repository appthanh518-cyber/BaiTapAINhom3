'''
import random

from simpleai.search import SearchProblem
from simpleai.search.local import hill_climbing


class BaiToanLogic(SearchProblem):

    def __init__(self, trangThaiBanDau):
        self.initial_state = trangThaiBanDau

    # 0: thay đổi p
    # 1: thay đổi q
    # 2: thay đổi r
    def actions(self, state):
        return [0, 1, 2]

    # Đổi giá trị 0 <-> 1
    def result(self, state, action):
        trangThaiMoi = list(state)

        trangThaiMoi[action] = 1 - trangThaiMoi[action]

        return tuple(trangThaiMoi)

    # Hàm đánh giá:
    # Đếm số constraint đúng
    def value(self, state):

        p, q, r = state

        C1 = (p == 0 or q == 1)
        C2 = (q == 0 or r == 1)
        C3 = (p == 1)
        C4 = (r == 0)

        diem = 0

        if C1:
            diem += 1

        if C2:
            diem += 1

        if C3:
            diem += 1

        if C4:
            diem += 1

        return diem


def kiemTraConstraint(state):

    p, q, r = state

    C1 = (p == 0 or q == 1)
    C2 = (q == 0 or r == 1)
    C3 = (p == 1)
    C4 = (r == 0)

    return C1, C2, C3, C4


def main():

    diemTotNhat = -1
    trangThaiTotNhat = None

    # Chạy nhiều lần với trạng thái ban đầu ngẫu nhiên
    for lan in range(10):

        trangThaiBanDau = (
            random.randint(0, 1),
            random.randint(0, 1),
            random.randint(0, 1)
        )

        baiToan = BaiToanLogic(trangThaiBanDau)

        ketQua = hill_climbing(
            baiToan,
            iterations_limit=100
        )

        # SimpleAI trả về SearchNodeValueOrdered
        # nên lấy trạng thái bằng .state
        trangThai = ketQua.state

        diem = baiToan.value(trangThai)

        print("Lần", lan + 1)
        print("Trạng thái ban đầu:", trangThaiBanDau)
        print("Trạng thái tìm được:", trangThai)
        print("Điểm:", diem, "/ 4")
        print()

        if diem > diemTotNhat:
            diemTotNhat = diem
            trangThaiTotNhat = trangThai

    print("========== KẾT QUẢ ==========")

    p, q, r = trangThaiTotNhat

    print("p =", p)
    print("q =", q)
    print("r =", r)

    C1, C2, C3, C4 = kiemTraConstraint(trangThaiTotNhat)

    print("\nCác constraint:")

    print("C1 = NOT p OR q:", C1)
    print("C2 = NOT q OR r:", C2)
    print("C3 = p:", C3)
    print("C4 = NOT r:", C4)

    print("\nSố constraint đúng:",
          diemTotNhat, "/ 4")

    if diemTotNhat == 4:
        print("Tìm được nghiệm thỏa mãn CNF.")
    else:
        print("Không tìm được nghiệm thỏa mãn toàn bộ CNF.")
        print("CNF vô nghiệm theo chứng minh Resolution.")


if __name__ == "__main__":
    main()

'''

from simpleai.search import SearchProblem, hill_climbing

# 1. & 2. Mô hình hóa bài toán & Xây dựng lớp SearchProblem kế thừa từ SimpleAI
class CNFLocalSearch(SearchProblem):
    def __init__(self, initial_state):
        # Trạng thái ban đầu là bộ giá trị (p, q, r) gồm các giá trị True/False
        super().__init__(initial_state=initial_state)

    def actions(self, state):
        # Hành động: Đảo ngược giá trị chân lý của một biến bất kỳ (0: biến p, 1: biến q, 2: biến r)
        return [0, 1, 2]

    def result(self, state, action):
        # Tạo trạng thái lân cận sau khi lật giá trị của biến tại vị trí action
        state_list = list(state)
        state_list[action] = not state_list[action]
        return tuple(state_list)

    def value(self, state):
        # 3. Xây dựng hàm đánh giá: Tính số lượng mệnh đề CNF được thỏa mãn
        p, q, r = state
        
        # 4 mệnh đề CNF từ phần chứng minh phản chứng:
        # C1: ¬p ∨ q (p -> q)
        # C2: ¬q ∨ r (q -> r)
        # C3: p      (giả thiết p)
        # C4: ¬r     (phủ định kết luận r)
        clauses = [
            (not p or q),
            (not q or r),
            p,
            not r
        ]
        
        # Trả về số lượng clause nhận giá trị True (tối đa là 4)
        return sum(1 for clause in clauses if clause)

if __name__ == "__main__":
    print("=" * 65)
    print("DEMO GIẢI BÀI TOÁN CNF BẰNG LOCAL SEARCH (HILL CLIMBING - SIMPLEAI)")
    print("=" * 65)
    print("Hệ mệnh đề CNF:")
    print("  - C1: ¬p ∨ q")
    print("  - C2: ¬q ∨ r")
    print("  - C3: p")
    print("  - C4: ¬r")
    print("(Lưu ý: Do tập mệnh đề này vô nghiệm - minh chứng bằng phản chứng ở phần trên,")
    print(" thuật toán Hill Climbing sẽ dừng ở cực đại cục bộ đạt số clause thỏa mãn cao nhất).\n")

    # 6. Kiểm thử thuật toán: Chạy qua tất cả 8 trạng thái ban đầu có thể có của không gian tìm kiếm
    initial_states = [
        (False, False, False),
        (False, False, True),
        (False, True, False),
        (False, True, True),
        (True, False, False),
        (True, False, True),
        (True, True, False),
        (True, True, True),
    ]

    for idx, init_state in enumerate(initial_states, 1):
        # 5. Cài đặt Local Search sử dụng thuật toán hill_climbing từ SimpleAI
        problem = CNFLocalSearch(initial_state=init_state)
        result_node = hill_climbing(problem)
        
        # Lấy state thực tế từ SearchNode để tránh lỗi unpack
        best_state = result_node.state
        max_satisfied = problem.value(best_state)

        print(f"Lần chạy {idx}:")
        print(f"  * Trạng thái ban đầu: p={init_state[0]}, q={init_state[1]}, r={init_state[2]}")
        print(f"  * Trạng thái tối ưu tìm được: p={best_state[0]}, q={best_state[1]}, r={best_state[2]}")
        print(f"  * Số clause thỏa mãn: {max_satisfied} / 4")
        print("-" * 65)