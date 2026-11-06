from simpleai.search import SearchProblem

class SATProblem(SearchProblem):
    """
    Lớp bài toán kế thừa từ SearchProblem của thư viện SimpleAI
    Mô hình hóa bài toán kiểm tra tính thỏa mãn CNF bằng Tìm kiếm cục bộ (Local Search).
    """

    def __init__(self, initial_state=None):
        """
        Khởi tạo bài toán với trạng thái ban đầu.
        Trạng thái biểu diễn dưới dạng tuple 3 phần tử bool: (p, q, r)
        """
        # Nếu không truyền trạng thái ban đầu, mặc định chọn (False, False, False)
        if initial_state is None:
            initial_state = (False, False, False)

        # Gọi hàm khởi tạo của lớp cha SearchProblem trong SimpleAI
        super().__init__(initial_state=initial_state)

        # Lưu danh sách 4 mệnh đề CNF dưới dạng hàm lambda nhận vào (p, q, r)
        # C1: ~p OR q
        # C2: ~q OR r
        # C3: p
        # C4: ~r
        self.clauses = [
            lambda p, q, r: (not p) or q,
            lambda p, q, r: (not q) or r,
            lambda p, q, r: p,
            lambda p, q, r: not r
        ]

    def actions(self, state):
        """
        Tạo các hành động lân cận: Chọn 1 trong 3 biến (p, q, r) để đảo giá trị (flip).
        Hành động đại diện bởi chỉ số biến: 0 -> lật p, 1 -> lật q, 2 -> lật r.
        """
        return [0, 1, 2]

    def result(self, state, action):
        """
        Trả về trạng thái mới sau khi thực hiện hành động 'action' (lật giá trị biến).
        """
        state_list = list(state)
        # Đảo giá trị bool tại chỉ số action
        state_list[action] = not state_list[action]
        return tuple(state_list)

    def value(self, state):
        """
        Hàm đánh giá (Objective Value): Đếm số clause CNF thỏa mãn (nhận giá trị True).
        Giá trị tối đa đạt được là 4 (nếu thỏa mãn tất cả clause).
        """
        p, q, r = state
        return sum(1 for clause in self.clauses if clause(p, q, r))