class Solution:
<<<<<<< HEAD
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
=======
    def reverseString(self, s) -> None:
>>>>>>> a39207f6e87896e3752319a47f2ec8e6e92375e0
        time = len(s)/2
        count = 0
        while time >= 1 :
            time -= 1
            temp = s[count]
            s[count] = s[-(count+1)]
            s[-(count+1)] = temp
<<<<<<< HEAD
            count += 1
=======
            count += 1

        return s

test = Solution()
print(test.reverseString(["h","e","l","l","o"]))
>>>>>>> a39207f6e87896e3752319a47f2ec8e6e92375e0
