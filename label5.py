from tkinter import *

root = Tk()
photo = PhotoImage(file="kitten.png")
w = Label(root, image=photo, justify="left").pack(side="right")
message="""삶이 그대를 속일지라도
슬퍼하거나 노하지 말라!
우리 곁에는 언제나 고양이,
강아지, 참새, 까지, 덕새,
도마뱀, 햄스터, 사슴벌레가 있으니.
모든 것은 순간적인 것, 지나가는 것이니
그리고 지나가는 것은 훗날 소중하게 되리니.

야옹
"""
w2 = Label(root, padx = 10, text=message).pack(side="left")

root.mainloop()