data = input()

class Solution():
    def word_count(self, string):
        string = string.strip()
        div_str = string.split()
        count = 0
        for i in div_str:
            count += 1
        return count        

if __name__ == "__main__":
    sol = Solution()
    print(sol.word_count(data))

    #개행에는 " ", n,t 개행들 다너어주어야함 split default에는 다포함됨 
