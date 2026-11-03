class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) < len(B):
            A, B = B, A


        l, r = 0, len(B) - 1
        total_len = (len(A) + len(B)) // 2

        while True:
            m = (l + r) // 2
            remains = total_len - m - 2

            A_right = A[remains] if remains >= 0 else float('-infinity')
            A_right_1 = A[remains + 1] if remains + 1 < len(A) else float('infinity')
            B_right = B[m] if m >= 0 else float('-infinity')
            B_right_1 = B[m + 1] if m + 1 < len(B) else float('infinity')

            if A_right <= B_right_1 and B_right <= A_right_1:

                if (len(A) + len(B)) % 2 == 1:
                    return min(B_right_1, A_right_1)
                else:
                    return (max(A_right, B_right) + min(B_right_1, A_right_1)) / 2
            elif B_right > A_right_1:
                r = m - 1
            else:
                l = m + 1