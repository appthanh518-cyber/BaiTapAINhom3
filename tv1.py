class SATProblemModel:
    def __init__(self):
        self.variables = ['p', 'q', 'r']
        self.clauses = [
            ('p', 'q', 'r'),
            ('~p', 'q'),
            ('~q', 'r'),
            ('~r', '~p')
        ]

    def get_variables(self):
        return self.variables

    def get_clauses(self):
        return self.clauses

    def display_cnf(self):
        formatted_clauses = []
        for clause in self.clauses:
            str_clause = " ∨ ".join([lit.replace('~', '¬') for lit in clause])
            formatted_clauses.append(f"({str_clause})")
        
        cnf_str = " ∧ ".join(formatted_clauses)
        print("BÀI TOÁN LOGIC ĐÃ ĐƯỢC MÔ HÌNH HÓA (CNF)")
        print(f"Các biến logic: {self.variables}")
        print(f"Danh sách các Clause: {self.clauses}")
        print(f"Biểu thức CNF dạng toán học: {cnf_str}")


if __name__ == "__main__":
    model = SATProblemModel()
    
    model.display_cnf()
    
    variables = model.get_variables()
    clauses = model.get_clauses()