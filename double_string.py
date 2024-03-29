#take string input
#make double the letters
#print
def double_stinrg(n):
    st = ""
    for i in n:
        st = st+i*2
    return st
n = input("Enter Your text here: ")
print(double_stinrg(n))
