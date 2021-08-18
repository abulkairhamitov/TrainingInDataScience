# Один из вариантов представления матрицы - список списков

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols

def get_row(A, i):
    return A[i]

def get_column(A, j):
    return [A_i[j] for A_i in A]

# Создание матрицы (entry_fn возвращает требуемое значение элемента с индексами i и j)
def make_matrix(num_rows, num_cols, entry_fn):
    return [entry_fn(i, j) for i in range(num_cols) for j in range(num_rows)]
# # Пример:
# def is_diagonal(i, j):
#     return 1 if i==j else 0
# identity_matrix = make_matrix(5, 5, is_diagonal)
