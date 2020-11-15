import tkinter
import tkinter.messagebox

connecting = []
accounts = []

client_y = 10


class ConnectedUser:
    def __init__(self, user_id, user_pw, y):
        self.id = user_id
        self.pw = user_pw
        self.y = y

        # GUI 버튼들
        self.label_client = None
        self.button_logout = None

    def user_login(self):
        global connecting

        # 접속창에 아이디 추가
        self.label_client = tkinter.Label(server, text=self.id, font=("Times New Roman", 10))
        self.label_client.place(x=10, y=self.y)

        # 접속창에 로그아웃 버튼 추가
        self.button_logout = tkinter.Button(server, text="로그아웃", command=lambda: self.user_logout())
        self.button_logout.place(x=200, y=self.y)

    def user_logout(self):
        global client_y

        self.button_logout.destroy()
        self.label_client.destroy()

        client_y -= 30

        connecting.remove(self)
        tkinter.messagebox.showinfo("로그아웃", f"{self.id}이(가) 로그아웃하였습니다.")
        print(f"{self.id}: 로그아웃시도 - 성공")
        connected_ids = [u.id for u in connecting]
        print(f"접속중인 계정: {str(connected_ids)}\n")

        for user in connecting:
            if user.y > self.y:
                user.go_down()

    def go_down(self):
        self.y -= 30
        self.label_client.place(x=10, y=self.y)
        self.button_logout.place(x=200, y=self.y)


def click_btn_login():
    global client_y, connecting

    # 안전하게 accounts에서 특정 유저 정보 가져옴
    user = next((u for u in accounts if u['id'] == ID.get()), {"id": None, "pw": None})

    # 접속중인 유저의 아이디 배열 가져옴
    connected_ids = [u.id for u in connecting]

    if user['id'] in connected_ids:
        # 로그인 실패 메시지 출력
        tkinter.messagebox.showinfo("로그인", "이미 로그인된 아이디 입니다.")
        print(f"{ID.get()}: 로그인시도 - 이미 로그인됨\n")
    elif user['pw'] == password.get():

        tkinter.messagebox.showinfo("로그인", "로그인을 성공했습니다.")

        client_y += 30
        logined_user = ConnectedUser(user['id'], user['pw'], client_y)

        connecting.append(logined_user)
        logined_user.user_login()

        print(f"{ID.get()}: 로그인시도 - 성공")

        # 접속중 아이디 갱신
        connected_ids = [u.id for u in connecting]
        print(f"접속중인 계정: {str(connected_ids)}\n")
    else:
        # 로그인 실패 메시지 출력
        tkinter.messagebox.showinfo("로그인", "가입 되지 않은 정보 입니다.")
        print(f"{ID.get()}: 로그인시도 - 실패\n")


def click_btn_signup():
    txt_id = ID.get()
    txt_password = password.get()

    if ID.get() in [u['id'] for u in accounts]:
        tkinter.messagebox.showinfo("회원가입", "이미 가입된 계정입니다.")
        print(f"{txt_id}: 회원가입시도 - 실패\n")
    else:
        accounts.append({"id": txt_id, "pw": txt_password})

        tkinter.messagebox.showinfo("회원가입", "회원가입을 완료했습니다!")
        print(f"{txt_id}: 회원가입시도 - 성공\n")


client = tkinter.Tk()

client.title("로그인 화면")
client.geometry("400x200")
client.resizable(False, False)
canvas = tkinter.Canvas(client, width=400, height=200)
canvas.pack()
jumpking = tkinter.PhotoImage(file="shtelo.png")
canvas.create_image(200, 100, image=jumpking)

# UI 셋팅
label_id = tkinter.Label(client, text="ID", font=("Times New Roman", 10))
ID = tkinter.Entry(width=20)

label_password = tkinter.Label(client, text="password", font=("Times New Roman", 10))
password = tkinter.Entry(width=20)

sign_up = tkinter.Button(client, text="회원가입", command=click_btn_signup)
sign_up.place(x=310, y=160)

login = tkinter.Button(client, text="로그인", command=click_btn_login)
login.place(x=310, y=130)

label_id.place(x=10, y=110)
ID.place(x=10, y=130)

label_password.place(x=10, y=150)
password.place(x=10, y=170)

server = tkinter.Tk()

server.title("접속 목록")
server.geometry("300x800")
server.resizable(False, True)

label_list = tkinter.Label(server, text="< 참여자 목록 >", font=("Times New Roman", 10))
label_list.place(x=10, y=10)

client.mainloop()


