    def actions(self, state):
        """
        Trả về danh sách các hoạt động:
        0: Lật biến p
        1: Lật biến q
        2: Lật biến r
        """
        return [0, 1, 2]

    #Tạo trạng thái mới sau khi thực hiện hành động
    def result(self, state, action):
        state_list = list(state)
        state_list[action] = not state_list[action]
        return tuple(state_list)