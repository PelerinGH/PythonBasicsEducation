def sherlockAndAnagrams(s):
    count = 0
    dict = {}
    for i in range(len(s)):
        for j in range(i + 1, len(s)+1):
            ss = list(s[i:j].strip())
            ss.sort()
            ss = "".join(ss)
            print(i,",",j, s[i:j])
            if ss in dict:
                count += dict[ss]
                dict[ss]+=1
                print("good")
            else:
                dict[ss] =1
    return count

print(sherlockAndAnagrams("cdcd"))