class Solution:
    def simplifyPath(self, path: str) -> str:

        st = []
        l = list(path.split("/"))
        i = 0
        while(i<len(l)) :
            if l[i] == ".." :
                if len(st)>0 :
                    st.pop()
            elif l[i] == "." or l[i]=="":
                pass
            else :
                st += [l[i]]
            i += 1

        news = "/"
        for i in range(0,len(st)) :
            if st[i] != "" :
                news += st[i]
                news += "/"

        if news == "/" :
            return news
        return news[:-1]       