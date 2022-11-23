from typing import List


class Solution:
    def get_matrix_column(self, matrix, start, end) -> List[List[int]]:
        return [row[start:end+1] for row in matrix]

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # min_path = 10e4

        def min_path_start_end(matrix: List[List[int]], min_path: int) -> int:
            first_matrix = matrix[0]
            print(first_matrix)

            if len(matrix) == 1:
                return min(first_matrix)
            else:
                current = 0
                for c in range(len(first_matrix)):
                    current += first_matrix[c]
                    current += min_path_start_end(
                        self.get_matrix_column(
                            matrix[1:], 0 if c-1 < 0 else c -
                            1, len(first_matrix) -
                            1 if c == len(first_matrix) else c+1
                        ), current
                    )

                    print(c, current)

                    if current < min_path:
                        min_path = current
                    else:
                        current = 0
                return min_path

        return min_path_start_end(matrix, 10e4)


print(Solution().minFallingPathSum([[1, 3, 5], [7, 9, 2], [6, 8, 1]]))
