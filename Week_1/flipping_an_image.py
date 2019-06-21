# Flipping An Imagine:
# Flip a matrix horizontally, then invert it

class Solution:
	# flip(A): Reverses each row in A matrix
    def flip(self, A: List[List[int]]) -> None:
        for row in range(len(A)):
            for col in range(int(len(A[0])/2)):
                rev_col = len(A[0]) - 1 - col
                A[row][col], A[row][rev_col] =  A[row][rev_col], A[row][col]
    # invert(A): Swaps 0's and 1's in a matrix
    def invert(self, A: List[List[int]]) -> None:
        for row in range(len(A)):
            for col in range(int(len(A[0]))):
                A[row][col] = 1 if A[row][col] == 0 else 0
    # flipAndInvertImage: Flips, then inverts matrix A.       
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        self.flip(A)
        self.invert(A)
        return A
        