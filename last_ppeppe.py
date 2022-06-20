from tkinter import *
import tkinter.ttk
import webbrowser as w
from tkinter import messagebox
import time
import winsound

#-------------------------------------------------
def python_site_url():
    w.open("https://www.python.org/")

def python_install_youtube():
    w.open("https://www.youtube.com/watch?v=bM5eBHz7QJg")

#-------------------------------------------------
def cmd(cmd_txt):
    string=cmd_txt.get("1.0", END)
    exec(string)

#-------------------------------------------------

def click():
    for i in range(1,101):
        time.sleep(0.01)
        p_var.set(i)
        progressbar1.update()
        
#-------------------------------------------------
def chapter_info():
    info = Tk()
    info.title("Chapter 정보")
    info.geometry("400x550-150+10")
    info.resizable(False, False) 
    
    info_frame=Frame(info, bd=1, relief="flat")
    info_frame.pack(expand=True, fill="both")
    
    canvas_info=Canvas(info_frame, width=500, height=600, bg="white")
    canvas_info.place(x=-10, y=0)
    canvas_info.create_rectangle(0, 30, 410, 60, fill="#124e8c", outline="#124e8c", width=7)
    canvas_info.create_rectangle(0, 75, 410, 85, fill="#ffe760", outline="#ffe760", width=4)
    canvas_info.create_text(210, 120, text="Chatper 정보", font=("DungGeunMo", 30 , "bold"), fill="black")
    canvas_info.create_text(179, 180, text="Chatper 0 : Install", font=("나눔스퀘어라운드", 15 , "bold"), fill="black")
    canvas_info.create_text(180, 210, text="Chatper 1 : 자료형", font=("나눔스퀘어라운드", 15 , "bold"), fill="black")
    canvas_info.create_text(180, 240, text="Chatper 2 : 연산자", font=("나눔스퀘어라운드", 15 , "bold"), fill="black")
    canvas_info.create_text(180, 270, text="Chatper 3 : 조건문", font=("나눔스퀘어라운드", 15 , "bold"), fill="black")
    canvas_info.create_text(180, 300, text="Chatper 4 : 반복문", font=("나눔스퀘어라운드", 15 , "bold"), fill="black")
    canvas_info.create_text(180, 330, text="Chatper 5 : 문자열", font=("나눔스퀘어라운드", 15 , "bold"), fill="black")
    canvas_info.create_text(189, 360, text="Chatper 6 : 자료구조", font=("나눔스퀘어라운드", 15 , "bold"), fill="black")
    canvas_info.create_text(170, 390, text="Chatper 7 : 함수", font=("나눔스퀘어라운드", 15 , "bold"), fill="black")
    canvas_info.create_text(202, 420, text="Chatper 8 : 파일 입출력", font=("나눔스퀘어라운드", 15 , "bold"), fill="black")
    canvas_info.create_text(211, 450, text="Chatper 9 : 파일 예외처리", font=("나눔스퀘어라운드", 15 , "bold"), fill="black")
    canvas_info.create_text(185, 480, text="Chatper 10 : 클래스", font=("나눔스퀘어라운드", 15 , "bold"), fill="black")
    canvas_info.create_text(210, 510, text="Chatper 11 : 모듈, 패키지", font=("나눔스퀘어라운드", 15 , "bold"), fill="black")

    info.mainloop( )

#-------------------------------------------------
def transport(before, after):
    before.pack_forget()
    after.pack(expand=True, fill="both")
def transport_exit_i(before, after, canvases):
    global i
    transport_list_back(canvases[i], canvases[0])

    i=0
    before.pack_forget()
    after.pack(expand=True, fill="both")
def transport_exit_j(before, after, canvases):
    global j

    transport_chapter_list_back(canvases[j], canvases[0])

    j=0
    before.pack_forget()
    after.pack(expand=True, fill="both")

#-------------------------------------------------
def transport_canvas(before, after):
    before.place_forget()
    after.place(x=0, y=60)

i=0
def transport_list_next(before, after):
    global i
    transport_canvas(before, after)
    i=i+1

def transport_list_back(before, after):
    global i
    if i > 0:
        transport_canvas(before, after)
        i=i-1

#-------------------------------------------------
def transport_chapter_canvas(before, after):
    before.place_forget()
    after.place(x=140, y=60)

j=0
def transport_chapter_list_next(before, after):
    global j
    transport_chapter_canvas(before, after)
    j=j+1

def transport_chapter_list_back(before, after):
    global j
    if j > 0:
        transport_chapter_canvas(before, after)
        j=j-1

#-------------------------------------------------
def freq(o, s):
    if s == 'do':
        return 524*2**o
    elif s == 're':
        return 587*2**o
    elif s == 'mi':
        return 659*2**o
    elif s == 'fa':
        return 698*2**o
    elif s == 'sol':
        return 784*2**o
    elif s == 'ra':
        return 880*2**o
    elif s == 'si':
        return 988*2**o

#-------------------------------------------------
def melody1():
    t=700
    d=80
    winsound.Beep(freq(0,'do'), int(0.6*t-d))
    winsound.Beep(freq(0,'mi'), int(0.6*t-d))
    winsound.Beep(freq(0,'sol'), int(0.6*t-d))

#-------------------------------------------------
def melody2():
    t=700
    d=80
    winsound.Beep(freq(0,'si'), 600)
    winsound.Beep(freq(0,'si'), 600)

#-------------------------------------------------
def chg_to_img1(event):
    p_label_1.config(image=ppeppe_photo1)

def chg_to_img2(event):
    p_label_1.config(image=ppeppe_photo2)

#-------------------------------------------------

def judge(quiz_root, order, q_answer, k, data, quiz_title):
    if order==q_answer:
        melody1()
        messagebox.showinfo(title="정답", message="맞았습니다. ")
        quiz_root.destroy()
        if (k+1)<len(data['question']):
            quiz(data, quiz_title, k+1)
    else:
        melody2()
        messagebox.showinfo(title="오답", message="틀렸습니다. ")

def quiz(data, quiz_title, k):
    quiz_root=Tk()
    quiz_root.wm_attributes("-topmost", 1)
    
    quiz_root.geometry("800x450-10+10")
    quiz_root.title(quiz_title)
    quiz_root.resizable(False, False)
    quiz_root.config(bg="white")
    
    title = Label(quiz_root, text="QUIZ", width=50, bg="#124e8c", fg="white", font=("ariel", 20, "bold"))
    title.place(x=0, y=2)
    
    question_label=Label(quiz_root, text=data['question'][k], width=60, font=('ariel', 17, 'bold'), anchor='w', bg="white")
    question_label.place(x=60, y=80)
    
    btn1=Button(quiz_root, text=data['options'][k][0], width=50, font=('ariel', 15, 'bold'), anchor='w', command=lambda:judge(quiz_root, 1, data['answer'][k],k, data, quiz_title))
    btn1.place(x=50, y=150)
    btn1=Button(quiz_root, text=data['options'][k][1], width=50, font=('ariel', 15, 'bold'), anchor='w', command=lambda:judge(quiz_root, 2, data['answer'][k],k, data, quiz_title))
    btn1.place(x=50, y=200)
    btn1=Button(quiz_root, text=data['options'][k][2], width=50, font=('ariel', 15, 'bold'), anchor='w', command=lambda:judge(quiz_root, 3, data['answer'][k], k, data, quiz_title))
    btn1.place(x=50, y=250)
    btn1=Button(quiz_root, text=data['options'][k][3], width=50, font=('ariel', 15, 'bold'), anchor='w', command=lambda:judge(quiz_root, 4, data['answer'][k], k, data, quiz_title))
    btn1.place(x=50, y=300)
    
    quiz_root.mainloop()

datatype_quiz_dic = {'question': ['Q1. 다음 중 변수의 이름으로 옳지 않은 것은?', 'Q2. 다음 중 자료형에 대한 설명으로 옳지 않은 것은?'], 'answer': [3, 3], 'options': [['123data',
                                                                                                                       '_data', 'data*', 'Data'], ['int: 정수형 자료형은 양의 정수, 음의 정수, 0을 대입할 수 있다.', 'float: 실수형에는 허수가 아닌 모든 실수가 저장된다.', 'string: 문자열은 공백을 포함할 수 없다.', 'bool: 불 자료형은 참, 거짓을 의미한다.']]}
operator_quiz_dic = {'question': ['Q1. 거듭제곱을 나타내는 산술 연산자를 고르시오. ', 'Q2. 왼쪽 변수에서 오른쪽 값을 나눈 나머지의 결과를 왼쪽 변수에\n 할당하는 대입 연산자를 고르시오.'], 'answer': [2, 1], 'options': [['*',
                                                                                                             '**', '***', '//'], ['%=', '**=', '//=', '/=']]}
conditional_quiz_dic = {'question': ["Q1. 다음 조건문 중 올바른 조건문을 고르시오.",
                     "Q2. 조건문에 대해 옳지 않은 설명을 고르시오."], 'answer': [3, 2], 'options': [['if money', 'if money;', 'if money():', 'if money();'], ['들여쓰기는 같아야 한다.', '중괄호를 무조건 써야 한다.', 'elif는 여러 개 해도 상관없다.', 'if 조건문 뒤에 반드시 콜론(:)이 붙는다.']]}
loop_quiz_dic = {'question': ["Q1. 다음 중 for문으로 5번 반복하는 방법으로 올바른 것은?",
                     "Q2. 다음 보기 중 나머지와 다른 하나는 무엇인가?"
                     ], 'answer': [3, 3], 'options': [['for j in range(5, 11):', 'for j in range(5, 0):', 'for j in range(20, 30, 2):', 'for j in range(1, 10, 1):'], ['for i in range(5): print(i)', 'for i in range(0, 5): print(i)', 'for i in range(1, 5): print(i)', 'for i in range(0, 5, 1): print(i)']]}

string_quiz_dic = {'question': ['Q1. 문자열에 대한 설명으로 옳지 않은 것을 고르시오.', 'Q2. 문자열을 리스트로 쪼개는 메서드를 고르시오.'], 'answer': [3, 4], 'options': [['문자열도 슬라이싱이 가능하다.',
                                                                                                             '문자열은 인덱싱이 가능하다.', 'split 메서드는 괄호가 필요없다.', 'len() 메서드를 통해서 문자열의 길이를 알 수 있다.'], ['strip', 'len', 'replace', 'split']]}
datastructure_quiz_dic = {'question': ['Q1. list 내장함수 중에서 데이터들을 알파벳 \n순서대로 정렬하는 내장함수로 올바른 것은?', "Q2. 다음 중 파이썬 실행의 결과 값으로 틀린 것은?"], 'answer': [1, 2], 'options': [
    ['sort()', 'sorted()', 'place()', 'replace()'], ['pow(2, 4)는 16이다.', 'list(range(5, 10))은 [5, 6, 7, 8, 9, 10]이다.', 'tuple("abs"는 (\'a\', \'b\', \'c\')이다.', 'type("school")은 < class \'str\'>이다.']]}

function_quiz_dic = {'question': ["Q1.함수를 만들 때 사용하는 예약어는? ",
                     "Q2. 다음 중 매개변수가 없는 kait 라는 이름의 함수를 호출하는 방법은?",
                     ], 'answer': [3, 3], 'options': [['make',
                                                       'define', 'def', 'fun'], ['def kait', 'kait', 'kait()', 'kait[]']]}

inputoutput_quiz_dic = {'question': ['Q1. 읽기용을 나타내는 파일 모드 매개변수를 고르시오.', 'Q2. 파일 입력 관련 함수가 아닌 것을 고르시오.'], 'answer': [1, 4], 'options': [['r',
                                                                                                             'w', 'a', 't'], ['read()', 'readline', 'readlines', 'writelines()']]}
exception_quiz_dic = {'question': ['Q1. 예외처리에서 사용되지 않는 것을 고르시오.', 'Q2. 예외처리에 대해서 옳지 않은 것을 고르시오.'], 'answer': [1, 1], 'options': [['expect',
                                                                                                             'try', 'except', 'else'], ['예외처리를 하면 예외처리 안의 모든 문장이 실행된다.', 'try를 통해서 오류가 발생할 수 있는 문장을 쓴다.', 'except를 통해서 오류가 발생할 경우 실행할 문장을 쓴다.', 'else를 통해서 오류가 없을 때 실행할 문장을 쓴다.']]}
class_quiz_dic = {'question': ['Q1. 다음 중 클래스의 정의로 옳은 것은?', 'Q2. 다음 중 올바른 생성자를 고르시오.'], 'answer': [2, 1], 'options': [['파이썬에서만 제공되는 특별한 기능이다.',
                                                                                                             '객체지향 프로그래밍의 핵심 개념이다.', '클래스와 필드는 동일한 용어이다.', '클래스 안에는 변수를 포함할 수 있는데, 이를 메서드라고 한다.'], ['__init__', '__init', '__init()__', '__init()']]}
module_quiz_dic = {'question': ['Q1. import의 사용법은?', 'Q2. 다음 중 모듈의 종류가 다른 하나를 고르시오.'], 'answer': [1, 4], 'options': [['import 모듈이름',    
'import 모듈함수', 'import 함수', 'import 모듈'], ['math', 'urlib.request', 'random', 'numpy.random']]}

#-------------------------------------------------

window=Tk()
window.title("PPePPe : Python Program Education")
window.geometry("1000x700+10+10")
window.resizable(False, False) 

#-------------------------------------------------

# start_frame 정보 (1st)
start_frame=Frame(window, bd=1, relief="flat")
start_frame.pack(expand=True, fill="both")

back_photo_1=PhotoImage(file="photo/start_back.png")
b_label_1=Label(start_frame, image=back_photo_1)
b_label_1.pack(expand=True, fill="both")

ppeppe_photo1=PhotoImage(file="photo/ppeppe1.png")
ppeppe_photo2=PhotoImage(file="photo/ppeppe2.png")
p_label_1=Label(start_frame, image=ppeppe_photo1)
p_label_1.place(x=310, y=170)  
p_label_1.bind("<Enter>", chg_to_img2)
p_label_1.bind("<Leave>", chg_to_img1)

start_btn_1=Button(start_frame, text="START", width=7, height=1, font=("DungGeunMo", 50 , "bold"), fg="white", bg="#124e8c", command=lambda:transport(start_frame, main_menu_frame))
start_btn_1.place(x=380, y=550)

Quiz_btn_1=Button(start_frame, text="Quiz", width=7, height=1, font=("DungGeunMo", 30 , "bold"), bg="#ffe760", command=lambda:transport(start_frame, quiz_menu_frame))
Quiz_btn_1.place(x=700, y=550)

ex_btn_1=Button(start_frame, text="How", width=5, font=("DungGeunMo", 18), fg="white", bg="#377bc0", command=lambda:transport(start_frame, ex_frame))
ex_btn_1.place(x=870, y=584)

t_label_1=Label(start_frame, text="3조 청일점이조", font=("DungGeunMo", 20 , "bold"), bg="white")
t_label_1.place(x=700, y=630)

#------------------------------------------------------------------------------------------------------------------------------------------------------------

back_photo_0=PhotoImage(file="photo/ex_back.png")
ex_frame=Frame(window, bd=1, relief="flat")

b_label_0=Label(ex_frame, image=back_photo_0)
b_label_0.pack(expand=True, fill="both")

t_label_0=Label(ex_frame, text="PPePPe : Python Program Education", font=("DungGeunMo", 30 , "bold"), bg="white", fg="#0e2e50")
t_label_0.place(x=158, y=310)
t_label_0=Label(ex_frame, text="✔ 이 프로그램은 Python을 기반으로 초보자들을 위한", font=("나눔바름펜", 20 , "bold"), bg="white", fg="black")
t_label_0.place(x=200, y=370)
t_label_0=Label(ex_frame, text="  Python언어 기초 교육 프로그램입니다.", font=("나눔바름펜", 20 , "bold"), bg="white", fg="black")
t_label_0.place(x=227, y=410)
t_label_0=Label(ex_frame, text="- Menu에서 Install부터 Chapter11까지 순서대로 학습해보세요!", font=("나눔바름펜", 20 , "bold"), bg="white", fg="#0f4175")
t_label_0.place(x=100, y=465)
t_label_0=Label(ex_frame, text="- 학습을 다 한 후엔 Quiz 버튼을 눌러 각 Chapter 별 문제를 풀어보세요.", font=("나눔바름펜", 20 , "bold"), bg="white", fg="#0f4175")
t_label_0.place(x=100, y=505)
t_label_0=Label(ex_frame, text="- Info 버튼을 누르면 각 Chapter의 정보를 확인할 수 있습니다.", font=("나눔바름펜", 20 , "bold"), bg="white", fg="#0f4175")
t_label_0.place(x=100, y=545)

pre_btn_0=Button(ex_frame, text="◀ BACK", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport(ex_frame, start_frame))
pre_btn_0.place(x=0, y=120)

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# main_menu_frame 정보 (2nd)
back_photo_2=PhotoImage(file="photo/menu_back.png")
main_menu_frame=Frame(window, bd=1, relief="flat")

b_label_2=Label(main_menu_frame, image=back_photo_2)
b_label_2.pack(expand=True, fill="both")

t_label_2=Label(main_menu_frame, text="MENU", font=("DungGeunMo", 60 , "bold"), bg="white")
t_label_2.place(x=420,y=100)

btn1_2=Button(main_menu_frame, text="INSTALL", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#124e8c", command=lambda:transport(main_menu_frame, install_frame))
btn1_2.place(x=70, y=240)

btn2_2=Button(main_menu_frame, text="Chapter1", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#377bc0", command=lambda:transport(main_menu_frame, chapter_1_frame))
btn2_2.place(x=70, y=340)

btn3_2=Button(main_menu_frame, text="Chapter2", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#377bc0", command=lambda:transport(main_menu_frame, chapter_2_frame))
btn3_2.place(x=70, y=440)

btn4_2=Button(main_menu_frame, text="Chapter3", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#377bc0", command=lambda:transport(main_menu_frame, chapter_3_frame))
btn4_2.place(x=290, y=240)

btn5_2=Button(main_menu_frame, text="Chapter4", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#377bc0", command=lambda:transport(main_menu_frame, chapter_4_frame))
btn5_2.place(x=290, y=340)

btn6_2=Button(main_menu_frame, text="Chapter5", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#377bc0", command=lambda:transport(main_menu_frame, chapter_5_frame))
btn6_2.place(x=290, y=440)

btn7_2=Button(main_menu_frame, text="Chapter6", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#377bc0", command=lambda:transport(main_menu_frame, chapter_6_frame))
btn7_2.place(x=510, y=240)

btn8_2=Button(main_menu_frame, text="Chapter7", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#377bc0", command=lambda:transport(main_menu_frame, chapter_7_frame))
btn8_2.place(x=510, y=340)

btn9_2=Button(main_menu_frame, text="Chapter8", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#377bc0", command=lambda:transport(main_menu_frame, chapter_8_frame))
btn9_2.place(x=510, y=440)

btn10_2=Button(main_menu_frame, text="Chapter9", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#377bc0", command=lambda:transport(main_menu_frame, chapter_9_frame))
btn10_2.place(x=730, y=240)

btn11_2=Button(main_menu_frame, text="Chapter10", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#377bc0", command=lambda:transport(main_menu_frame, chapter_10_frame))
btn11_2.place(x=730, y=340)

btn12_2=Button(main_menu_frame, text="Chapter11", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#377bc0", command=lambda:transport(main_menu_frame, chapter_11_frame))
btn12_2.place(x=730, y=440)

pre_btn_2=Button(main_menu_frame, text="◀ BACK", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport(main_menu_frame, start_frame))
pre_btn_2.place(x=0, y=120)

pre_btn_2=Button(main_menu_frame, text="🗨 info", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=chapter_info)
pre_btn_2.place(x=884, y=120)

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# quiz_menu_frame 정보 (3rd)
back_photo_3=PhotoImage(file="photo/Quiz_back.png")
quiz_menu_frame=Frame(window, bd=1, relief="flat")

b_label_3=Label(quiz_menu_frame, image=back_photo_3)
b_label_3.pack(expand=True, fill="both")

btn1_3=Button(quiz_menu_frame, text="Hello", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#124e8c", command=lambda:transport(quiz_menu_frame, install_frame))
btn1_3.place(x=70, y=300)

btn2_3=Button(quiz_menu_frame, text="Chapter1", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#377bc0", command=lambda:quiz(datatype_quiz_dic,"Data Type Quiz", 0))
btn2_3.place(x=70, y=400)

btn3_3=Button(quiz_menu_frame, text="Chapter2", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#377bc0", command=lambda:quiz(operator_quiz_dic,"Operator Quiz", 0))
btn3_3.place(x=70, y=500)

btn4_3=Button(quiz_menu_frame, text="Chapter3", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#377bc0", command=lambda:quiz(conditional_quiz_dic,"Conditional Quiz", 0))
btn4_3.place(x=290, y=300)

btn5_3=Button(quiz_menu_frame, text="Chapter4", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#377bc0", command=lambda:quiz(loop_quiz_dic, "Loop Quiz", 0))
btn5_3.place(x=290, y=400)

btn6_3=Button(quiz_menu_frame, text="Chapter5", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#377bc0", command=lambda:quiz(string_quiz_dic, "String Quiz", 0))
btn6_3.place(x=290, y=500)

btn7_3=Button(quiz_menu_frame, text="Chapter6", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#377bc0", command=lambda:quiz(datastructure_quiz_dic,"Data Structure Quiz", 0))
btn7_3.place(x=510, y=300)

btn8_3=Button(quiz_menu_frame, text="Chapter7", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#377bc0", command=lambda:quiz(function_quiz_dic, "Fuction Quiz", 0))
btn8_3.place(x=510, y=400)

btn9_3=Button(quiz_menu_frame, text="Chapter8", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#377bc0", command=lambda:quiz(inputoutput_quiz_dic, "Input Output Quiz", 0))
btn9_3.place(x=510, y=500)

btn10_3=Button(quiz_menu_frame, text="Chapter9", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#377bc0", command=lambda:quiz(exception_quiz_dic, "Exception Quiz", 0))
btn10_3.place(x=730, y=300)

btn11_3=Button(quiz_menu_frame, text="Chapter10", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#377bc0", command=lambda:quiz(class_quiz_dic, "Class Quiz", 0))
btn11_3.place(x=730, y=400)

btn12_3=Button(quiz_menu_frame, text="Chapter11", width=9, height=1, font=("DungGeunMo", 30 , "bold"), fg="white", bg="#377bc0", command=lambda:quiz(module_quiz_dic, "Module and Package Quiz", 0))
btn12_3.place(x=730, y=500)

pre_btn_3=Button(quiz_menu_frame, text="◀ BACK", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport(quiz_menu_frame, start_frame))
pre_btn_3.place(x=0, y=120)

pre_btn_3=Button(quiz_menu_frame, text="🗨 info", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=chapter_info)
pre_btn_3.place(x=884, y=120)

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# install_frame 정보 (4rd)
back_photo_chpater=PhotoImage(file="photo/interface_back.png")
install_frame=Frame(window, bd=1, relief="flat")
install_frame.config(bg="white")

ppe_photo=PhotoImage(file="photo/ppe.png")
install_1=PhotoImage(file="install_photo/1.png")
install_2=PhotoImage(file="install_photo/2.png")
install_3=PhotoImage(file="install_photo/3.png")
install_4=PhotoImage(file="install_photo/4.png")
install_5=PhotoImage(file="install_photo/5.png")
install_6=PhotoImage(file="install_photo/6.png")
install_7=PhotoImage(file="install_photo/7.png")
install_8=PhotoImage(file="install_photo/8.png")
install_9=PhotoImage(file="photo/install_ppeppe.png")
install_10=PhotoImage(file="install_photo/9.png")

# install_frame canvas_1 정보
canvas_4_1=Canvas(install_frame, width=1000, height=700, bg="#c8e9f3")
canvas_4_1.place(x=0, y=60)
photo_4_1=canvas_4_1.create_image(290, 300, image=install_1)
text_4=canvas_4_1.create_text(765, 130, text="그럼 지금부터 파이썬을 설치해볼까요?", fill="black", font=("나눔바른펜", 20 , "bold"))
text_4=canvas_4_1.create_text(765, 170, text="아래의 링크를 클릭해서 들어갑시다.", fill="black", font=("나눔바른펜", 20 , "bold"))
btn4_1_1 = Button(canvas_4_1, text="https://www.python.org/", width=25, height=1, font=("DungGeunMo", 13), fg="white", bg="#2a6fb6", command=python_site_url)
btn4_1_1.place(x=650, y=195)
text_4=canvas_4_1.create_text(765, 250, text="혹시 이해가 안된다면 위의", fill="black", font=("나눔바른펜", 20 , "bold"))
text_4=canvas_4_1.create_text(765, 290, text="링크를 클릭해서 따라가 봅시다.", fill="black", font=("나눔바른펜", 20 , "bold"))
btn4_1_2 = Button(canvas_4_1, text="https://www.youtube.com/watch?v=bM5eBHz7QJg", width=45, height=1, font=("DungGeunMo", 13), fg="white", bg="#2a6fb6", command=python_install_youtube)
btn4_1_2.place(x=565, y=320)
photo_4_1=canvas_4_1.create_image(765, 450, image=install_9)

# install_frame canvas_2 정보
canvas_4_2=Canvas(install_frame, width=1000, height=700, bg="#c8e9f3")
photo_4_2=canvas_4_2.create_image(300, 250, image=install_2)
photo_4_2=canvas_4_2.create_image(720, 250, image=install_3)
text_4=canvas_4_2.create_text(500, 500, text="Downloads를 누른 후, 컴퓨터 사양에 맞게 클릭!", fill="black", font=("나눔바른펜", 25 , "bold"))
text_4=canvas_4_2.create_text(500, 550, text="최근 버전의 64bit 클릭하여 원하는 위치에 설치", fill="black", font=("나눔바른펜", 25 , "bold"))

# install_frame canvas_3 정보
canvas_4_3=Canvas(install_frame, width=1000, height=700, bg="#c8e9f3")
photo_4_3=canvas_4_3.create_image(500, 270, image=install_4)
text_4=canvas_4_3.create_text(500, 530, text="아랫부분의 두 가지를 체크하여 Install Now 를 클릭!", fill="black", font=("나눔바른펜", 25 , "bold"))

# install_frame canvas_4 정보
canvas_4_4=Canvas(install_frame, width=1000, height=700, bg="#c8e9f3")
photo_4_4=canvas_4_4.create_image(500, 130, image=install_5)
photo_4_4=canvas_4_4.create_image(500, 350, image=install_6)
text_4=canvas_4_4.create_text(500, 500, text="Documentation을 체크한 후 next 클릭!", fill="black", font=("나눔바른펜", 25 , "bold"))
text_4=canvas_4_4.create_text(500, 540, text="Associate files with Python~을 체크, Install 을 클릭!", fill="black", font=("나눔바른펜", 25 , "bold"))

# install_frame canvas_5 정보
p_var=DoubleVar()
canvas_4_5=Canvas(install_frame, width=1000, height=700, bg="#c8e9f3")
progressbar1 = tkinter.ttk.Progressbar(canvas_4_5, maximum=100, length=200, mode="determinate", variable=p_var)
progressbar1.place(x=380, y=470)
btn4_5 = Button(canvas_4_5, text="click", width=5, height=1, font=("DungGeunMo", 13), fg="white", bg="#2a6fb6", command=click)
btn4_5.place(x=600, y=470)

photo_4_5=canvas_4_5.create_image(500, 140, image=install_7)
photo_4_5=canvas_4_5.create_image(500, 360, image=install_8)
text_4=canvas_4_5.create_text(500, 530, text="설치 완료!!!", fill="black", font=("나눔바른펜", 25 , "bold"))
text_4=canvas_4_5.create_text(500, 570, text="그럼 입력 해볼까요?", fill="black", font=("나눔바른펜", 25 , "bold"))

canvas_4_6=Canvas(install_frame, width=1000, height=700, bg="#c8e9f3")
canvas_4_6.create_rectangle(0,30,1000,50, fill="#124e8c", outline="#124e8c", width=7)
photo_4_6=canvas_4_6.create_image(510, 150, image=install_10)
txt4_6=Text(canvas_4_6, width=50, height=10)
txt4_6.place(x=300, y=250)
btn4_6=Button(canvas_4_6, text="click", width=5, height=1, font=("DungGeunMo", 15), fg="white", bg="#2a6fb6", command=lambda:cmd(txt4_6))
btn4_6.place(x=660, y=250)
text_4=canvas_4_6.create_text(500, 450, text="print("'"Hello World!"'")를 적어볼까요?", fill="black", font=("나눔바른펜", 25 , "bold"))
text_4=canvas_4_6.create_text(500, 490, text="다 적었으면 click을 눌러주세요!", fill="black", font=("나눔바른펜", 25 , "bold"))
text_4=canvas_4_6.create_text(500, 550, text="Hello World! 라는 문구가 출력됩니다 :)", fill="#0f4175", font=("나눔바른펜", 25 , "bold"))
text_4=canvas_4_6.create_text(500, 610, text="Exit로 나가 Chapter 1로 넘어가주세요", fill="#0f4175", font=("나눔바른펜", 15 , "bold"))

install_canvas_list=[]
install_canvas_list.append(canvas_4_1)
install_canvas_list.append(canvas_4_2)
install_canvas_list.append(canvas_4_3)
install_canvas_list.append(canvas_4_4)
install_canvas_list.append(canvas_4_5)
install_canvas_list.append(canvas_4_6)

#--------------------------------------

exit_btn_4=Button(install_frame, text="EXIT", width=7, height=1, font=("DungGeunMo", 26 , "bold"), fg="white", bg="#124e8c", command=lambda:transport_exit_i(install_frame, main_menu_frame, install_canvas_list))
exit_btn_4.place(x=0, y=0)

Quiz_btn_4=Button(install_frame, text="Quiz", width=7, height=1, font=("DungGeunMo", 26 , "bold"), bg="#ffe760", command=lambda:transport(install_frame, quiz_menu_frame))
Quiz_btn_4.place(x=860, y=0)

pre_btn_4=Button(install_frame, text="◀ BACK", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_list_back(install_canvas_list[i], install_canvas_list[i-1]))
pre_btn_4.place(x=0, y=654)

next_btn_4=Button(install_frame, text="NEXT ▶", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_list_next(install_canvas_list[i], install_canvas_list[i+1]))
next_btn_4.place(x=886, y=654)

title_label_4=Label(install_frame,  text="INSTALL", font=("DungGeunMo", 33 , "bold"), bg="white", padx=5, pady=5)
title_label_4.place(x=150,y=0)

date_label_4=Label(install_frame, text=time.strftime('%Y.%m.%d', time.localtime(time.time())), font=("DungGeunMo", 18), bg="white", padx=5, pady=5)
date_label_4.place(x=720, y=18)

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# chapter_1_frame 정보 (5th)
chapter_1_frame=Frame(window, bd=1, relief="flat")
chapter_1_frame.config(bg="white")

level_1_photo=PhotoImage(file="photo/level_1.png")
chpater_1_1=PhotoImage(file="chapter_1_photo/1.png")
chpater_1_2=PhotoImage(file="chapter_1_photo/2.png")
chpater_1_3=PhotoImage(file="chapter_1_photo/3.png")
chpater_1_4=PhotoImage(file="chapter_1_photo/4.png")
chpater_1_5=PhotoImage(file="chapter_1_photo/5.png")
chpater_1_6=PhotoImage(file="chapter_1_photo/6.png")
chpater_1_7=PhotoImage(file="chapter_1_photo/7.png")
chpater_1_8=PhotoImage(file="chapter_1_photo/8.png")

label_5=Label(chapter_1_frame, image=level_1_photo)
label_5.place(x=0, y=60)  
t_label_5=Label(chapter_1_frame, text="beginning", font=("DungGeunMo", 20), fg="#0f4175", bg="white")
t_label_5.place(x=5, y=210)
t_label_5=Label(chapter_1_frame, text="level", font=("DungGeunMo", 25), fg="#0f4175", bg="white")
t_label_5.place(x=25, y=240)

# chapter_1_frame canvas_1 정보
canvas_5_1=Canvas(chapter_1_frame, width=1000, height=700, bg="#c8e9f3")
canvas_5_1.place(x=140, y=60)
photo_5_1=canvas_5_1.create_image(290, 210, image=chpater_1_1)
photo_5_1=canvas_5_1.create_image(690, 210, image=chpater_1_2)
text_5=canvas_5_1.create_text(440, 350, text="변수란 데이터를 제공하는 공간입니다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_1.create_text(440, 390, text="쉽게 생각하면 변수는 데이터를 담는 상자입니다.", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_1.create_text(440, 430, text="데이터가 다르면 상자의 모양과 크기도 달라집니다!", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_1.create_text(440, 470, text="수학에서의 대수(x)와 비슷한 개념이라고 생각해도 괜찮습니다", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_1.create_text(440, 610, text="Chapter 1에 오신 걸 환영합니다 :)", fill="#0f4175", font=("나눔바른펜", 17 , "bold"))

# chapter_1_frame canvas_2 정보
canvas_5_2=Canvas(chapter_1_frame, width=1000, height=700, bg="#c8e9f3")
photo_5_2=canvas_5_2.create_image(440, 210, image=chpater_1_3)
text_5=canvas_5_2.create_text(440, 350, text="int는 integer의 약자로, 일반적인 정수의 자료형입니다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_2.create_text(440, 390, text="float은 floating-point의 약자로 실수의 자료형입니다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_2.create_text(440, 430, text="str은 string의 약자로, “ ”나 ‘ ’로 이루어진 문자열의 자료형입니다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_2.create_text(440, 470, text="bool은 boolean의 약자로, True와 False로 이루어진 참, 거짓의 자료형입니다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_2.create_text(440, 510, text="(data type = 자료형 = 데이터형)", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))

# chapter_1_frame canvas_3정보
canvas_5_3=Canvas(chapter_1_frame, width=1000, height=700, bg="#c8e9f3")
photo_5_3=canvas_5_3.create_image(440, 110, image=chpater_1_4)
text_5=canvas_5_3.create_text(440, 200, text="변수는 ‘변수명=저장할 값’과 같은 형태로 사용 가능합니다.", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_3.create_text(440, 240, text="우리는 오른쪽에서 왼쪽으로 보면 됩니다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_3.create_text(440, 280, text="오른쪽 값을 왼쪽의 변수에 대입합니다. (저장)", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_3.create_text(440, 320, text="‘=’는 대입 연산자입니다.", fill="black", font=("나눔바른펜", 20 , "bold"))
txt5_3=Text(canvas_5_3, width=50, height=5)
txt5_3.place(x=230, y=350)
btn5_3=Button(canvas_5_3, text="click", width=5, height=1, font=("DungGeunMo", 15), fg="white", bg="#2a6fb6", command=lambda:cmd(txt5_3))
btn5_3.place(x=600, y=350)
text_5=canvas_5_3.create_text(440, 460, text="sum=3; print("'"%d"'"% sum)을 적어볼까요?", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_3.create_text(440, 500, text="다 적었으면 click을 눌러주세요!", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_3.create_text(440, 540, text="3 이 출력됩니다 :)", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))

# chapter_1_frame canvas_4 정보
canvas_5_4=Canvas(chapter_1_frame, width=1000, height=700, bg="#c8e9f3")
canvas_5_4.create_rectangle(0,30,1000,50, fill="#124e8c", outline="#124e8c", width=7)
text_5=canvas_5_4.create_text(440, 110, text="< 변수 주의사항 >", fill="#0f4175", font=("나눔바른펜", 30 , "bold"))
canvas_5_4.create_rectangle(200, 150, 670, 530, fill="white", outline="#124e8c", width=5)
text_5=canvas_5_4.create_text(440, 200, text="✔ 변수명은 숫자로 시작하지 않는다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_4.create_text(440, 235, text="ex) 123data (x)", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_4.create_text(440, 280, text="✔ 대소문자를 구분한다. ", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_4.create_text(440, 315, text="ex) data != Data", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_4.create_text(440, 360, text="✔ _를 제외한 특수문자를 사용하지 않는다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_4.create_text(440, 395, text="ex) _data (O),  data* (X)", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_4.create_text(440, 440, text="✔ 파이썬에 지정된 키는 사용하지 않는다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_4.create_text(440, 475, text="ex) print (x)", fill="black", font=("나눔바른펜", 20 , "bold"))

# chapter_1_frame canvas_5 정보
canvas_5_5=Canvas(chapter_1_frame, width=1000, height=700, bg="#c8e9f3")
photo_5_5=canvas_5_5.create_image(440, 150, image=chpater_1_5)
text_5=canvas_5_5.create_text(440, 280, text="✔ print 함수", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_5.create_text(440, 320, text="- 출력하고 싶은 정보를 출력하는 함수", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_5.create_text(440, 360, text="- 형태: print(출력 정보)", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_5.create_text(440, 440, text="✔ input 함수", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_5.create_text(440, 480, text="- 입력하고 싶은 정보를 출력하는 함수", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_5.create_text(440, 520, text="- ( ) 안에 문자열이 존재하면 출력 가능", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_5.create_text(440, 560, text="- 형태: 변수=input( )", fill="black", font=("나눔바른펜", 20 , "bold"))

# chapter_1_frame canvas_6 정보
canvas_5_6=Canvas(chapter_1_frame, width=1000, height=700, bg="#c8e9f3")
photo_5_6=canvas_5_6.create_image(440, 180, image=chpater_1_6)
text_5=canvas_5_6.create_text(440, 300, text="✔ type 함수", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_6.create_text(440, 340, text="- 데이터 타입을 알려주는 함수", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_6.create_text(440, 380, text="- 형태: type(정보)", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_6.create_text(440, 420, text="- 출력: <type '데이터 타입'>", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_6.create_text(440, 500, text="(# : 주석 - 코드에 대한 설명, 코드에 영향X)", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))

# chapter_1_frame canvas_7 정보
canvas_5_7=Canvas(chapter_1_frame, width=1000, height=700, bg="#c8e9f3")
photo_5_7=canvas_5_7.create_image(440, 180, image=chpater_1_7)
text_5=canvas_5_7.create_text(440, 300, text="✔ 형변환 함수", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_7.create_text(440, 340, text="- int( ) : 다른 데이터형을 정수로 변환", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_7.create_text(440, 380, text="- float( ) : 다른 데이터형을 실수로 변환", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_7.create_text(440, 420, text="- str( ) : 다른 데이터형을 문자열로 변환", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_7.create_text(440, 500, text="(단, int, float는 ( )안에 문자가 있다면 오류 발생)", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))

# chapter_1_frame canvas_8 정보
canvas_5_8=Canvas(chapter_1_frame, width=1000, height=700, bg="#c8e9f3")
photo_5_8=canvas_5_8.create_image(440, 180, image=chpater_1_8)
txt5_8=Text(canvas_5_8, width=50, height=5)
txt5_8.place(x=230, y=350)
btn5_8=Button(canvas_5_8, text="click", width=5, height=1, font=("DungGeunMo", 15), fg="white", bg="#2a6fb6", command=lambda:cmd(txt5_8))
btn5_8.place(x=600, y=350)
text_5=canvas_5_8.create_text(440, 460, text="지금까지 배운 input 함수와 type 함수를 이용해볼까요?", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_8.create_text(440, 500, text="위의 그림에 있는 대로 한 번 따라해볼까요?", fill="black", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_8.create_text(440, 540, text="y=10, type <'int'>가 출력됩니다 :)", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_5=canvas_5_8.create_text(440, 610, text="Exit로 나가 Chapter 2로 넘어가주세요", fill="#0f4175", font=("나눔바른펜", 15 , "bold"))

chapter_1_canvas_list=[]
chapter_1_canvas_list.append(canvas_5_1)
chapter_1_canvas_list.append(canvas_5_2)
chapter_1_canvas_list.append(canvas_5_3)
chapter_1_canvas_list.append(canvas_5_4)
chapter_1_canvas_list.append(canvas_5_5)
chapter_1_canvas_list.append(canvas_5_6)
chapter_1_canvas_list.append(canvas_5_7)
chapter_1_canvas_list.append(canvas_5_8)

#--------------------------------------

exit_btn_5=Button(chapter_1_frame, text="EXIT", width=7, height=1, font=("DungGeunMo", 26 , "bold"), fg="white", bg="#124e8c", command=lambda:transport_exit_j(chapter_1_frame, main_menu_frame, chapter_1_canvas_list))
exit_btn_5.place(x=0, y=0)

Quiz_btn_5=Button(chapter_1_frame, text="Quiz", width=7, height=1, font=("DungGeunMo", 26 , "bold"), bg="#ffe760", command=lambda:transport(chapter_1_frame, quiz_menu_frame))
Quiz_btn_5.place(x=860, y=0)

pre_btn_5=Button(chapter_1_frame, text="◀ BACK", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_chapter_list_back(chapter_1_canvas_list[j], chapter_1_canvas_list[j-1]))
pre_btn_5.place(x=140, y=654)

next_btn_5=Button(chapter_1_frame, text="NEXT ▶", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_chapter_list_next(chapter_1_canvas_list[j], chapter_1_canvas_list[j+1]))
next_btn_5.place(x=886, y=654)

title_label_5=Label(chapter_1_frame, text="CHAPTER 1 : 자료형", font=("DungGeunMo", 33 , "bold"), bg="white", padx=5, pady=5)
title_label_5.place(x=150,y=0)

date_label_5=Label(chapter_1_frame, text=time.strftime('%Y.%m.%d', time.localtime(time.time())), font=("DungGeunMo", 18), bg="white", padx=5, pady=5)
date_label_5.place(x=720, y=18)

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# chapter_2_frame 정보 (6th)
chapter_2_frame=Frame(window, bd=1, relief="flat")
chapter_2_frame.config(bg="white")

chpater_2_1=PhotoImage(file="chapter_2_photo/1.png")
chpater_2_2=PhotoImage(file="chapter_2_photo/2.png")
chpater_2_3=PhotoImage(file="chapter_2_photo/3.png")
chpater_2_4=PhotoImage(file="chapter_2_photo/4.png")
chpater_2_5=PhotoImage(file="chapter_2_photo/5.png")
chpater_2_6=PhotoImage(file="chapter_2_photo/6.png")
chpater_2_7=PhotoImage(file="chapter_2_photo/7.png")

label_6=Label(chapter_2_frame, image=level_1_photo)
label_6.place(x=0, y=60)  
t_label_6=Label(chapter_2_frame, text="beginning", font=("DungGeunMo", 20), fg="#0f4175", bg="white")
t_label_6.place(x=5, y=210)
t_label_6=Label(chapter_2_frame, text="level", font=("DungGeunMo", 25), fg="#0f4175", bg="white")
t_label_6.place(x=25, y=240)

# chapter_2_frame canvas_1 정보
canvas_6_1=Canvas(chapter_2_frame, width=1000, height=700, bg="#c8e9f3")
canvas_6_1.place(x=140, y=60)
photo_6_1=canvas_6_1.create_image(440, 210, image=chpater_2_1)
text_6=canvas_6_1.create_text(440, 370, text="연산자에는 산술 연산자, 비교 연산자,", fill="black", font=("나눔바른펜", 20 , "bold"))
text_6=canvas_6_1.create_text(440, 410, text="논리 연산자, 대입 연산자, 비트 연산자가 있습니다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_6=canvas_6_1.create_text(440, 450, text="연산자를 이용하여 다양한 수식을 계산하고 만들 수 있습니다!", fill="black", font=("나눔바른펜", 20 , "bold"))
text_6=canvas_6_1.create_text(440, 490, text="각 연산자에 대해 한 번 알아볼까요?", fill="black", font=("나눔바른펜", 20 , "bold"))
text_6=canvas_6_1.create_text(440, 610, text="Chapter 2에 오신 걸 환영합니다 :)", fill="#0f4175", font=("나눔바른펜", 17 , "bold"))

# chapter_2_frame canvas_2 정보
canvas_6_2=Canvas(chapter_2_frame, width=1000, height=700, bg="#c8e9f3")
canvas_6_2.create_rectangle(0,30,1000,50, fill="#124e8c", outline="#124e8c", width=7)
text_6=canvas_6_2.create_text(440, 150, text="✔ 산술 연산자", fill="#0f4175", font=("나눔바른펜", 30 , "bold"))
photo_6_2=canvas_6_2.create_image(440, 350, image=chpater_2_2)

# chapter_2_frame canvas_3 정보
canvas_6_3=Canvas(chapter_2_frame, width=1000, height=700, bg="#c8e9f3")
canvas_6_3.create_rectangle(0,30,1000,50, fill="#124e8c", outline="#124e8c", width=7)
text_6=canvas_6_3.create_text(440, 100, text="✔ 비교 연산자", fill="#0f4175", font=("나눔바른펜", 30 , "bold"))
photo_6_3=canvas_6_3.create_image(440, 315, image=chpater_2_3)
text_6=canvas_6_3.create_text(440, 530, text="비교 연산자에 의해 도출되는 값은 bool (True, False)입니다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_6=canvas_6_3.create_text(440, 570, text="값이 참이면 True, 거짓이면 False를 반환합니다.", fill="black", font=("나눔바른펜", 20 , "bold"))

# chapter_2_frame canvas_4 정보
canvas_6_4=Canvas(chapter_2_frame, width=1000, height=700, bg="#c8e9f3")
canvas_6_4.create_rectangle(0,30,1000,50, fill="#124e8c", outline="#124e8c", width=7)
text_6=canvas_6_4.create_text(440, 150, text="✔ 논리 연산자", fill="#0f4175", font=("나눔바른펜", 30 , "bold"))
photo_6_4=canvas_6_4.create_image(440, 330, image=chpater_2_4)
text_6=canvas_6_4.create_text(440, 500, text="논리 연산자에 의해 도출되는 값은 bool (True, False)입니다.", fill="black", font=("나눔바른펜", 20 , "bold"))

# chapter_2_frame canvas_5 정보
canvas_6_5=Canvas(chapter_2_frame, width=1000, height=700, bg="#c8e9f3")
canvas_6_5.create_rectangle(0,30,1000,50, fill="#124e8c", outline="#124e8c", width=7)
text_6=canvas_6_5.create_text(440, 120, text="✔ 대입 연산자", fill="#0f4175", font=("나눔바른펜", 30 , "bold"))
photo_6_5=canvas_6_5.create_image(440, 370, image=chpater_2_5)

# chapter_2_frame canvas_6 정보
canvas_6_6=Canvas(chapter_2_frame, width=1000, height=700, bg="#c8e9f3")
canvas_6_6.create_rectangle(0,30,1000,50, fill="#124e8c", outline="#124e8c", width=7)
text_6=canvas_6_6.create_text(440, 150, text="✔ 비트 연산자", fill="#0f4175", font=("나눔바른펜", 30 , "bold"))
photo_6_6=canvas_6_6.create_image(440, 330, image=chpater_2_6)
text_6=canvas_6_6.create_text(440, 500, text="정수를 2진수로 변환한 후 각 자리의 비트끼리 연산 수행합니다.", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))

# chapter_2_frame canvas_7 정보
canvas_6_7=Canvas(chapter_2_frame, width=1000, height=700, bg="#c8e9f3")
canvas_6_7.create_rectangle(0,30,1000,50, fill="#124e8c", outline="#124e8c", width=7)
text_6=canvas_6_7.create_text(440, 100, text="✔ 연산자 우선순위", fill="#0f4175", font=("나눔바른펜", 30 , "bold"))
photo_6_7=canvas_6_7.create_image(440, 330, image=chpater_2_7)
text_6=canvas_6_7.create_text(440, 560, text="연산자 우선순위를 모를 땐 ( )를 활용하여 우선순위를 정하면 됩니다!", fill="black", font=("나눔바른펜", 20 , "bold"))
canvas_6_8=Canvas(chapter_2_frame, width=1000, height=700, bg="#c8e9f3")
text_6=canvas_6_8.create_text(440, 610, text="Exit로 나가 Chapter 3로 넘어가주세요", fill="#0f4175", font=("나눔바른펜", 15 , "bold"))

chapter_2_canvas_list=[]
chapter_2_canvas_list.append(canvas_6_1)
chapter_2_canvas_list.append(canvas_6_2)
chapter_2_canvas_list.append(canvas_6_3)
chapter_2_canvas_list.append(canvas_6_4)
chapter_2_canvas_list.append(canvas_6_5)
chapter_2_canvas_list.append(canvas_6_6)
chapter_2_canvas_list.append(canvas_6_7)

#--------------------------------------

exit_btn_6=Button(chapter_2_frame, text="EXIT", width=7, height=1, font=("DungGeunMo", 26 , "bold"), fg="white", bg="#124e8c", command=lambda:transport_exit_j(chapter_2_frame, main_menu_frame, chapter_2_canvas_list))
exit_btn_6.place(x=0, y=0)

Quiz_btn_6=Button(chapter_2_frame, text="Quiz", width=7, height=1, font=("DungGeunMo", 26 , "bold"), bg="#ffe760", command=lambda:transport(chapter_2_frame, quiz_menu_frame))
Quiz_btn_6.place(x=860, y=0)

pre_btn_6=Button(chapter_2_frame, text="◀ BACK", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_chapter_list_back(chapter_2_canvas_list[j], chapter_2_canvas_list[j-1]))
pre_btn_6.place(x=140, y=654)

next_btn_6=Button(chapter_2_frame, text="NEXT ▶", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_chapter_list_next(chapter_2_canvas_list[j], chapter_2_canvas_list[j+1]))
next_btn_6.place(x=886, y=654)

title_label_6=Label(chapter_2_frame,  text="CHAPTER 2 : 연산자", font=("DungGeunMo", 33 , "bold"), bg="white", padx=5, pady=5)
title_label_6.place(x=150,y=0)

date_label_6=Label(chapter_2_frame, text=time.strftime('%Y.%m.%d', time.localtime(time.time())), font=("DungGeunMo", 18), bg="white", padx=5, pady=5)
date_label_6.place(x=720, y=18)

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# chapter_3_frame 정보 (7th)
chapter_3_frame=Frame(window, bd=1, relief="flat")
chapter_3_frame.config(bg="white")

chpater_3_1=PhotoImage(file="chapter_3_photo/1.png")
chpater_3_2=PhotoImage(file="chapter_3_photo/2.png")
chpater_3_3=PhotoImage(file="chapter_3_photo/3.png")
chpater_3_4=PhotoImage(file="chapter_3_photo/4.png")

label_7=Label(chapter_3_frame, image=level_1_photo)
label_7.place(x=0, y=60)  
t_label_7=Label(chapter_3_frame, text="beginning", font=("DungGeunMo", 20), fg="#0f4175", bg="white")
t_label_7.place(x=5, y=210)
t_label_7=Label(chapter_3_frame, text="level", font=("DungGeunMo", 25), fg="#0f4175", bg="white")
t_label_7.place(x=25, y=240)

# chapter_3_frame canvas_1 정보
canvas_7_1=Canvas(chapter_3_frame, width=1000, height=700, bg="#c8e9f3")
canvas_7_1.place(x=140, y=60)
canvas_7_1.create_rectangle(0,50,1000,70, fill="#124e8c", outline="#124e8c", width=7)
photo_7_1=canvas_7_1.create_image(270, 330, image=chpater_3_1)
text_7=canvas_7_1.create_text(550, 150, text="✔ if문", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_7=canvas_7_1.create_text(550, 220, text="   if (조건식): ", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_1.create_text(550, 260, text="       실행할 문장", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_1.create_text(585, 350, text="- 조건식이 참이면 ", fill="black", font=("나눔바른펜", 19 , "bold"))
text_7=canvas_7_1.create_text(595, 390, text="  문장을 실행하고,", fill="black", font=("나눔바른펜", 19 , "bold"))
text_7=canvas_7_1.create_text(590, 430, text="- 조건식이 거짓이면", fill="black", font=("나눔바른펜", 19 , "bold"))
text_7=canvas_7_1.create_text(630, 470, text="  문장을 실행하지 않는다.", fill="black", font=("나눔바른펜", 19 , "bold"))
text_7=canvas_7_1.create_text(440, 610, text="Chapter 3에 오신 걸 환영합니다 :)", fill="#0f4175", font=("나눔바른펜", 17 , "bold"))

# chapter_3_frame canvas_2 정보 
canvas_7_2=Canvas(chapter_3_frame, width=1000, height=700, bg="#c8e9f3")
canvas_7_2.create_rectangle(0,50,1000,70, fill="#124e8c", outline="#124e8c", width=7)
photo_7_2=canvas_7_2.create_image(270, 330, image=chpater_3_2)
text_7=canvas_7_2.create_text(650, 150, text="✔ if-else문", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_7=canvas_7_2.create_text(610, 220, text="   if (조건식): ", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_2.create_text(615, 260, text="       실행할 문장 1", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_2.create_text(580, 300, text="   else : ", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_2.create_text(615, 340, text="       실행할 문장 2", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_2.create_text(645, 420, text="- 조건식이 참이면 ", fill="black", font=("나눔바른펜", 18 , "bold"))
text_7=canvas_7_2.create_text(660, 460, text="  문장 1을 실행하고,", fill="black", font=("나눔바른펜", 18 , "bold"))
text_7=canvas_7_2.create_text(650, 500, text="- 조건식이 거짓이면", fill="black", font=("나눔바른펜", 18 , "bold"))
text_7=canvas_7_2.create_text(660, 540, text="  문장 2를 실행한다.", fill="black", font=("나눔바른펜", 18 , "bold"))

# chapter_3_frame canvas_3 정보 
canvas_7_3=Canvas(chapter_3_frame, width=1000, height=700, bg="#c8e9f3")
canvas_7_3.create_rectangle(0,20,1000,40, fill="#124e8c", outline="#124e8c", width=7)
photo_7_3=canvas_7_3.create_image(280, 330, image=chpater_3_3)
text_7=canvas_7_3.create_text(630, 80, text="✔ 중첩 if문", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_7=canvas_7_3.create_text(600, 150, text="   if (조건식1): ", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_3.create_text(605, 190, text="       if (조건식2):", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_3.create_text(610, 230, text="           실행할 문장 1", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_3.create_text(575, 270, text="       else :", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_3.create_text(610, 310, text="           실행할 문장 2", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_3.create_text(570, 350, text="   else : ", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_3.create_text(605, 390, text="       실행할 문장 3", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_3.create_text(680, 450, text="- 조건식 1이 참이면 조건식 2를 판별하여,", fill="black", font=("나눔바른펜", 15 , "bold"))
text_7=canvas_7_3.create_text(635, 490, text="  참이면 문장 1을 실행하고,", fill="black", font=("나눔바른펜", 15 , "bold"))
text_7=canvas_7_3.create_text(645, 530, text="  거짓이면 문장 2를 실행한다. ", fill="black", font=("나눔바른펜", 15 , "bold"))
text_7=canvas_7_3.create_text(670, 570, text="- 조건식 1이 참이면 문장 3을 실행한다.", fill="black", font=("나눔바른펜", 15 , "bold"))

# chapter_3_frame canvas_4 정보 
canvas_7_4=Canvas(chapter_3_frame, width=1000, height=700, bg="#c8e9f3")
canvas_7_4.create_rectangle(0,50,1000,70, fill="#124e8c", outline="#124e8c", width=7)
photo_7_4=canvas_7_4.create_image(280, 330, image=chpater_3_3)
text_7=canvas_7_4.create_text(670, 110, text="✔ if-elif-else문", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_7=canvas_7_4.create_text(600, 180, text="   if (조건식1): ", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_4.create_text(605, 220, text="       실행할 문장 1", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_4.create_text(605, 260, text="   elif (조건식2): ", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_4.create_text(605, 300, text="       실행할 문장 2", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_4.create_text(570, 340, text="   else : ", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_4.create_text(605, 380, text="       실행할 문장 3", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_4.create_text(680, 450, text="- 조건식 1이 참이면 문장 1을 실행하고,", fill="black", font=("나눔바른펜", 15 , "bold"))
text_7=canvas_7_4.create_text(680, 490, text="  거짓이면 elif의 조건식 2을 판별하여,", fill="black", font=("나눔바른펜", 15 , "bold"))
text_7=canvas_7_4.create_text(640, 530, text="- 참이면 문장 2를 실행하고", fill="black", font=("나눔바른펜", 15 , "bold"))
text_7=canvas_7_4.create_text(650, 570, text="  거짓이면 문장 3을 실행한다.", fill="black", font=("나눔바른펜", 15 , "bold"))

# chapter_3_frame canvas_5 정보 
canvas_7_5=Canvas(chapter_3_frame, width=1000, height=700, bg="#c8e9f3")
canvas_7_5.create_rectangle(0,30,1000,50, fill="#124e8c", outline="#124e8c", width=7) 
text_7=canvas_7_5.create_text(440, 110, text="< 조건문 주의사항 >", fill="#0f4175", font=("나눔바른펜", 30 , "bold"))
canvas_7_5.create_rectangle(150, 150, 750, 530, fill="white", outline="#124e8c", width=5)
text_7=canvas_7_5.create_text(350, 200, text="✔ 조건문에는 연산자를 사용한다.", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_5.create_text(455, 240, text="- 비교연산자(<,>,==,!=,>=,<=), 논리연산자(and, or, not)", fill="black", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_5.create_text(327, 280, text="✔ 들여쓰기에 주의해야 한다.", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_5.create_text(295, 320, text="- Spacebar*4 == Tab", fill="black", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_5.create_text(370, 360, text="- 둘을 혼용해서는 안 되고 하나만 사용", fill="black", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_5.create_text(315, 400, text="- Spacebar*4를 권장한다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_5.create_text(353, 440, text="✔ 조건문 다음 콜론(:)을 써야 한다.", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_5.create_text(290, 480, text="ex) if (a>5) :", font=("나눔바른펜", 20 , "bold"))
text_7=canvas_7_5.create_text(440, 610, text="Exit로 나가 Chapter 4로 넘어가주세요", fill="#0f4175", font=("나눔바른펜", 15 , "bold"))

chapter_3_canvas_list=[]
chapter_3_canvas_list.append(canvas_7_1)
chapter_3_canvas_list.append(canvas_7_2)
chapter_3_canvas_list.append(canvas_7_3)
chapter_3_canvas_list.append(canvas_7_4)
chapter_3_canvas_list.append(canvas_7_5)

#--------------------------------------

exit_btn_7=Button(chapter_3_frame, text="EXIT", width=7, height=1, font=("DungGeunMo", 26 , "bold"), fg="white", bg="#124e8c", command=lambda:transport_exit_j(chapter_3_frame, main_menu_frame, chapter_3_canvas_list))
exit_btn_7.place(x=0, y=0)

Quiz_btn_7=Button(chapter_3_frame, text="Quiz", width=7, height=1, font=("DungGeunMo", 26 , "bold"), bg="#ffe760", command=lambda:transport(chapter_3_frame, quiz_menu_frame))
Quiz_btn_7.place(x=860, y=0)

pre_btn_7=Button(chapter_3_frame, text="◀ BACK", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_chapter_list_back(chapter_3_canvas_list[j], chapter_3_canvas_list[j-1]))
pre_btn_7.place(x=140, y=654)

next_btn_7=Button(chapter_3_frame, text="NEXT ▶", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_chapter_list_next(chapter_3_canvas_list[j], chapter_3_canvas_list[j+1]))
next_btn_7.place(x=886, y=654)

title_label_7=Label(chapter_3_frame,  text="CHAPTER 3 : 조건문", font=("DungGeunMo", 33 , "bold"), bg="white", padx=5, pady=5)
title_label_7.place(x=150,y=0)

date_label_7=Label(chapter_3_frame, text=time.strftime('%Y.%m.%d', time.localtime(time.time())), font=("DungGeunMo", 18), bg="white", padx=5, pady=5)
date_label_7.place(x=720, y=18)

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# chapter_4_frame 정보 (8th)
chapter_4_frame=Frame(window, bd=1, relief="flat")
chapter_4_frame.config(bg="white")

level_2_photo=PhotoImage(file="photo/level_2.png")
chpater_4_1=PhotoImage(file="chapter_4_photo/1.png")
chpater_4_2=PhotoImage(file="chapter_4_photo/2.png")
chpater_4_3=PhotoImage(file="chapter_4_photo/3.png")
chpater_4_4=PhotoImage(file="chapter_4_photo/4.png")
chpater_4_5=PhotoImage(file="chapter_4_photo/5.png")
chpater_4_6=PhotoImage(file="chapter_4_photo/6.png")

label_8=Label(chapter_4_frame, image=level_2_photo)
label_8.place(x=0, y=60)  
t_label_8=Label(chapter_4_frame, text="intermediate", font=("DungGeunMo", 16), fg="#0f4175", bg="white")
t_label_8.place(x=0, y=210)
t_label_8=Label(chapter_4_frame, text="level", font=("DungGeunMo", 23), fg="#0f4175", bg="white")
t_label_8.place(x=25, y=235)

# chapter_4_frame canvas_1 정보
canvas_8_1=Canvas(chapter_4_frame, width=1000, height=700, bg="#c8e9f3")
canvas_8_1.place(x=140, y=60)
canvas_8_1.create_rectangle(0,50,1000,70, fill="#124e8c", outline="#124e8c", width=7)
photo_8_1=canvas_8_1.create_image(240, 290, image=chpater_4_1)
text_8=canvas_8_1.create_text(550, 150, text="✔ while문", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_8=canvas_8_1.create_text(550, 220, text="  while 조건식: ", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_8=canvas_8_1.create_text(550, 260, text="       실행할 문장1", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_8=canvas_8_1.create_text(550, 300, text="       실행할 문장2", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_8=canvas_8_1.create_text(585, 360, text="- 조건식이 참일 동안 ", fill="black", font=("나눔바른펜", 19 , "bold"))
text_8=canvas_8_1.create_text(600, 400, text="  계속해서 while문 안의", fill="black", font=("나눔바른펜", 19 , "bold"))
text_8=canvas_8_1.create_text(590, 440, text="  문장1, 2를 반복한다.", fill="black", font=("나눔바른펜", 19 , "bold"))
text_8=canvas_8_1.create_text(645, 480, text="- 조건식이 True이면 무한루프이다.", fill="black", font=("나눔바른펜", 19 , "bold"))
text_8=canvas_8_1.create_text(440, 610, text="Chapter 4에 오신 걸 환영합니다 :)", fill="#0f4175", font=("나눔바른펜", 17 , "bold"))

# chapter_4_frame canvas_2 정보
canvas_8_2=Canvas(chapter_4_frame, width=1000, height=700, bg="#c8e9f3")
canvas_8_2.create_rectangle(0,50,1000,70, fill="#124e8c", outline="#124e8c", width=7)
photo_8_2=canvas_8_2.create_image(240, 290, image=chpater_4_2)
text_8=canvas_8_2.create_text(640, 150, text="✔ while문 - 무한루프", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_8=canvas_8_2.create_text(550, 220, text="  while True: ", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_8=canvas_8_2.create_text(550, 260, text="       실행할 문장1", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_8=canvas_8_2.create_text(550, 300, text="       실행할 문장2", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_8=canvas_8_2.create_text(605, 360, text="- 조건식이 계속 참이어서 ", fill="black", font=("나눔바른펜", 19 , "bold"))
text_8=canvas_8_2.create_text(605, 400, text="  계속해서 while문 안의", fill="black", font=("나눔바른펜", 19 , "bold"))
text_8=canvas_8_2.create_text(615, 440, text="  문장1, 2를 무한 반복한다.", fill="black", font=("나눔바른펜", 19 , "bold"))
text_8=canvas_8_2.create_text(600, 480, text="- 무한루프 : 무한히 반복", fill="black", font=("나눔바른펜", 19 , "bold"))
text_8=canvas_8_2.create_text(640, 520, text="- break를 통해 빠져나갈 수 있다.", fill="black", font=("나눔바른펜", 19 , "bold"))
text_8=canvas_8_2.create_text(650, 560, text="- continue를 통해 계속 할 수 있다.", fill="black", font=("나눔바른펜", 19 , "bold"))

# chapter_4_frame canvas_3 정보
canvas_8_3=Canvas(chapter_4_frame, width=1000, height=700, bg="#c8e9f3")
canvas_8_3.create_rectangle(0,50,1000,70, fill="#124e8c", outline="#124e8c", width=7)
canvas_8_3.create_rectangle(200, 170, 700, 290, fill="white", outline="#124e8c", width=5)
text_8=canvas_8_3.create_text(440, 130, text="✔ for문", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_8=canvas_8_3.create_text(440, 190, text="  for 변수 in range (시작값, 끝값+1, 증가값): ", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_8=canvas_8_3.create_text(380, 230, text="       실행할 문장1", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_8=canvas_8_3.create_text(380, 270, text="       실행할 문장2", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_8=canvas_8_3.create_text(430, 330, text="- 변수가 시작값부터 끝값+1 까지", fill="black", font=("나눔바른펜", 19 , "bold"))
text_8=canvas_8_3.create_text(460, 370, text="  증가값만큼 증가하여 for문 안에 있는", fill="black", font=("나눔바른펜", 19 , "bold"))
text_8=canvas_8_3.create_text(390, 410, text="  문장1, 2를 반복한다.", fill="black", font=("나눔바른펜", 19 , "bold"))
text_8=canvas_8_3.create_text(355, 480, text="= range( ) 함수", fill="#0f4175", font=("나눔바른펜", 19 , "bold"))
text_8=canvas_8_3.create_text(470, 520, text="- 숫자 리스트를 자동으로 생성해주는 함수", fill="black", font=("나눔바른펜", 19 , "bold"))
text_8=canvas_8_3.create_text(470, 560, text="ex) range(0, 10) : 0부터 10까지 리스트", fill="black", font=("나눔바른펜", 19 , "bold"))

# chapter_4_frame canvas_4 정보
canvas_8_4=Canvas(chapter_4_frame, width=1000, height=700, bg="#c8e9f3")
canvas_8_4.create_rectangle(0,50,1000,70, fill="#124e8c", outline="#124e8c", width=7)
canvas_8_4.create_rectangle(200, 190, 710, 350, fill="white", outline="#124e8c", width=5)
text_8=canvas_8_4.create_text(440, 130, text="✔ 중첩 for문", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_8=canvas_8_4.create_text(440, 210, text="  for 변수1 in range (시작값, 끝값+1, 증가값): ", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_8=canvas_8_4.create_text(440, 250, text="          for 변수2 in range (시작값, 끝값+1, 증가값):", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_8=canvas_8_4.create_text(360, 290, text="      실행할 문장1", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_8=canvas_8_4.create_text(300, 330, text="      실행할 문장2", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_8=canvas_8_4.create_text(400, 400, text="- 변수가 시작값부터 끝값+1 까지", fill="black", font=("나눔바른펜", 19 , "bold"))
text_8=canvas_8_4.create_text(465, 440, text="  증가값만큼 증가하여 for 1이 1번 돌아갈 동안", fill="black", font=("나눔바른펜", 19 , "bold"))
text_8=canvas_8_4.create_text(405, 480, text="  for 2가 시작값부터 끝값+1까지", fill="black", font=("나눔바른펜", 19 , "bold"))
text_8=canvas_8_4.create_text(460, 520, text="  문장 2를 계속 반복한 후 문장 1을 반복한다.", fill="black", font=("나눔바른펜", 19 , "bold"))
text_8=canvas_8_4.create_text(420, 580, text="- 총 변수1 * 변수2 번 동안 반복한다.", fill="black", font=("나눔바른펜", 19 , "bold"))

# chapter_4_frame canvas_5 정보
canvas_8_5=Canvas(chapter_4_frame, width=1000, height=700, bg="#c8e9f3")
canvas_8_5.create_rectangle(0,50,1000,70, fill="#124e8c", outline="#124e8c", width=7)
photo_8_5_1=canvas_8_5.create_image(230, 320, image=chpater_4_3)
photo_8_5_2=canvas_8_5.create_image(630, 320, image=chpater_4_4)
text_8=canvas_8_5.create_text(235, 150, text="✔ break", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_8=canvas_8_5.create_text(635, 150, text="✔ continue", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_8=canvas_8_5.create_text(235, 490, text="- 반복문 탈출", fill="black", font=("나눔바른펜", 19 , "bold"))
text_8=canvas_8_5.create_text(635, 490, text="- 반복문 진행", fill="black", font=("나눔바른펜", 19 , "bold"))

# chapter_4_frame canvas_6 정보 
canvas_8_6=Canvas(chapter_4_frame, width=1000, height=700, bg="#c8e9f3")
canvas_8_6.create_rectangle(0,50,1000,70, fill="#124e8c", outline="#124e8c", width=7)
photo_8_6_1=canvas_8_6.create_image(230, 310, image=chpater_4_5)
photo_8_6_2=canvas_8_6.create_image(630, 310, image=chpater_4_6)
text_8=canvas_8_6.create_text(235, 130, text="✔ break", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_8=canvas_8_6.create_text(635, 130, text="✔ continue", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_8=canvas_8_6.create_text(235, 490, text="- hap이 1000이상이면 반복문 탈출", fill="black", font=("나눔바른펜", 19 , "bold"))
text_8=canvas_8_6.create_text(635, 490, text="- i가 3의 배수면 뛰어넘고 반복문 진행", fill="black", font=("나눔바른펜", 19 , "bold"))
text_8=canvas_8_6.create_text(440, 610, text="Exit로 나가 Chapter 5로 넘어가주세요", fill="#0f4175", font=("나눔바른펜", 15 , "bold"))

chapter_4_canvas_list=[]
chapter_4_canvas_list.append(canvas_8_1)
chapter_4_canvas_list.append(canvas_8_2)
chapter_4_canvas_list.append(canvas_8_3)
chapter_4_canvas_list.append(canvas_8_4)
chapter_4_canvas_list.append(canvas_8_5)
chapter_4_canvas_list.append(canvas_8_6)

#--------------------------------------

exit_btn_8=Button(chapter_4_frame, text="EXIT", width=7, height=1, font=("DungGeunMo", 26 , "bold"), fg="white", bg="#124e8c", command=lambda:transport_exit_j(chapter_4_frame, main_menu_frame, chapter_4_canvas_list))
exit_btn_8.place(x=0, y=0)

Quiz_btn_8=Button(chapter_4_frame, text="Quiz", width=7, height=1, font=("DungGeunMo", 26 , "bold"), bg="#ffe760", command=lambda:transport(chapter_4_frame, quiz_menu_frame))
Quiz_btn_8.place(x=860, y=0)

pre_btn_8=Button(chapter_4_frame, text="◀ BACK", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_chapter_list_back(chapter_4_canvas_list[j], chapter_4_canvas_list[j-1]))
pre_btn_8.place(x=140, y=654)

next_btn_8=Button(chapter_4_frame, text="NEXT ▶", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_chapter_list_next(chapter_4_canvas_list[j], chapter_4_canvas_list[j+1]))
next_btn_8.place(x=886, y=654)

title_label_8=Label(chapter_4_frame,  text="CHAPTER 4 : 반복문", font=("DungGeunMo", 33 , "bold"), bg="white", padx=5, pady=5)
title_label_8.place(x=150,y=0)

date_label_8=Label(chapter_4_frame, text=time.strftime('%Y.%m.%d', time.localtime(time.time())), font=("DungGeunMo", 18), bg="white", padx=5, pady=5)
date_label_8.place(x=720, y=18)

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# chapter_5_frame 정보 (9th)
chapter_5_frame=Frame(window, bd=1, relief="flat")
chapter_5_frame.config(bg="white")

chpater_5_1=PhotoImage(file="chapter_5_photo/1.png")
chpater_5_2=PhotoImage(file="chapter_5_photo/2.png")
chpater_5_3=PhotoImage(file="chapter_5_photo/3.png")
chpater_5_4=PhotoImage(file="chapter_5_photo/4.png")
chpater_5_5=PhotoImage(file="chapter_5_photo/5.png")
chpater_5_6=PhotoImage(file="chapter_5_photo/6.png")
chpater_5_7=PhotoImage(file="chapter_5_photo/7.png")
chpater_5_8=PhotoImage(file="chapter_5_photo/8.png")

label_9=Label(chapter_5_frame, image=level_2_photo)
label_9.place(x=0, y=60)  
t_label_9=Label(chapter_5_frame, text="intermediate", font=("DungGeunMo", 16), fg="#0f4175", bg="white")
t_label_9.place(x=0, y=210)
t_label_9=Label(chapter_5_frame, text="level", font=("DungGeunMo", 24), fg="#0f4175", bg="white")
t_label_9.place(x=25, y=235)

# chapter_5_frame canvas_1 정보
canvas_9_1=Canvas(chapter_5_frame, width=1000, height=700, bg="#c8e9f3")
canvas_9_1.place(x=140, y=60)
photo_9_1=canvas_9_1.create_image(435, 200, image=chpater_5_1)
text_9=canvas_9_1.create_text(440, 70, text="✔ 문자열", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_9=canvas_9_1.create_text(390, 330, text="- 문자열 : 문자들의 집합, 리스트(배열)", fill="black", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_1.create_text(280, 400, text="= 문자열 인덱싱", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_1.create_text(390, 440, text="- 문자열 자체를 문자의 리스트로 보고,", fill="black", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_1.create_text(445, 480, text="  순서대로 0부터 인덱스로 삼아 접근 가능합니다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_1.create_text(480, 520, text="- 인덱스는 뒤에서부터 -1, -2, ...로도 나타낼 수 있습니다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_1.create_text(440, 610, text="Chapter 5에 오신 걸 환영합니다 :)", fill="#0f4175", font=("나눔바른펜", 17 , "bold"))

# chapter_5_frame canvas_2 정보
canvas_9_2=Canvas(chapter_5_frame, width=1000, height=700, bg="#c8e9f3")
photo_9_2=canvas_9_2.create_image(220, 300, image=chpater_5_2)
text_9=canvas_9_2.create_text(560, 120, text="✔ 문자열 슬라이싱", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_9=canvas_9_2.create_text(630, 180, text="- 대입 연산자를 사용해 변수에 문자열 할당", fill="black", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_2.create_text(598, 240, text="- [2:4]는 2~4 번째까지 잘라줍니다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_2.create_text(590, 280, text="- [:4]는 1~4 번째까지 잘라줍니다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_2.create_text(590, 320, text="- [2:]는 2~마지막까지 잘라줍니다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_2.create_text(595, 380, text="= [m:n]은 배열의 인덱스를 이용하여", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_2.create_text(586, 420, text="   m~n번째까지 범위를 지정한 후,", fill="black", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_2.create_text(550, 460, text="   지정한 만큼 잘라줍니다.", fill="black", font=("나눔바른펜", 20 , "bold"))

# chapter_5_frame canvas_3 정보
canvas_9_3=Canvas(chapter_5_frame, width=1000, height=700, bg="#c8e9f3")
photo_9_3=canvas_9_3.create_image(240, 300, image=chpater_5_3)
text_9=canvas_9_3.create_text(590, 120, text="✔ 문자열 연결", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_9=canvas_9_3.create_text(640, 180, text="- '+' 연산자를 통해 문자열을 연결", fill="black", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_3.create_text(653, 220, text="- '+' 사용하면 공백 없이 문자열 연결", fill="black", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_3.create_text(618, 260, text="- 문자열 사이 공백을 넣어 '+'", fill="black", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_3.create_text(645, 300, text="  연결하면 문자열 사이 공백 추가", fill="black", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_3.create_text(602, 340, text="- ','를 통해 문자열을 연결", fill="black", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_3.create_text(650, 380, text="- ',' 사용하면 공백 있이 문자열 연결", fill="black", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_3.create_text(660, 420, text="- 문자열을 연결하여 다른 변수에 대입", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))

# chapter_5_frame canvas_4 정보
canvas_9_4=Canvas(chapter_5_frame, width=1000, height=700, bg="#c8e9f3")
photo_9_2=canvas_9_4.create_image(200, 190, image=chpater_5_4)
text_9=canvas_9_4.create_text(480, 80, text="✔ 문자열 루프", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_9=canvas_9_4.create_text(500, 130, text="- for문을 통해 루프 사용", fill="black", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_4.create_text(480, 170, text="- for i in string에서", fill="black", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_4.create_text(510, 210, text="  string은 인덱스 i를 증가'", fill="black", font=("나눔바른펜", 20 , "bold"))
photo_9_2=canvas_9_4.create_image(275, 460, image=chpater_5_5)
text_9=canvas_9_4.create_text(620, 380, text="✔ 문자열 포함", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_9=canvas_9_4.create_text(635, 440, text="- 'in'을 통해 문자열 안에", fill="black", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_4.create_text(650, 480, text="   단어의 존재 여부 확인 가능", fill="black", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_4.create_text(670, 520, text="- 값은 bool(True, False)로 도출", fill="black", font=("나눔바른펜", 20 , "bold"))

# chapter_5_frame canvas_5 정보
canvas_9_5=Canvas(chapter_5_frame, width=1000, height=700, bg="#c8e9f3")
text_9=canvas_9_5.create_text(440, 80, text="✔ 문자열 메서드", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_9=canvas_9_5.create_text(440, 130, text="문자열 메서드를 통해 다양하게 문자열 활용", fill="black", font=("나눔바른펜", 20 , "bold"))
photo_9_5=canvas_9_5.create_image(440, 370, image=chpater_5_6)

# chapter_5_frame canvas_6 정보
canvas_9_6=Canvas(chapter_5_frame, width=1000, height=700, bg="#c8e9f3")
canvas_9_6.create_rectangle(0,30,1000,50, fill="#124e8c", outline="#124e8c", width=7)
text_9=canvas_9_6.create_text(200, 100, text="✔ 문자열 메서드 예시", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
photo_9_6=canvas_9_6.create_image(220, 240, image=chpater_5_7)
photo_9_6=canvas_9_6.create_image(220, 440, image=chpater_5_8)
text_9=canvas_9_6.create_text(550, 180, text="= len( ) : 문자열의 길이", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_6.create_text(610, 220, text="- 빈칸도 문자로 취급하고 길이 센다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_6.create_text(565, 300, text="= replace( ) : 문자열 변경", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_6.create_text(600, 400, text="= split( ) : 문자열 공백 단위 분할", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_6.create_text(630, 440, text="= split("'"문자"'") : 문자열 문자 단위 분할", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_9=canvas_9_6.create_text(440, 610, text="Exit로 나가 Chapter 6로 넘어가주세요", fill="#0f4175", font=("나눔바른펜", 15 , "bold"))

chapter_5_canvas_list=[]
chapter_5_canvas_list.append(canvas_9_1)
chapter_5_canvas_list.append(canvas_9_2)
chapter_5_canvas_list.append(canvas_9_3)
chapter_5_canvas_list.append(canvas_9_4)
chapter_5_canvas_list.append(canvas_9_5)
chapter_5_canvas_list.append(canvas_9_6)

#--------------------------------------

exit_btn_9=Button(chapter_5_frame, text="EXIT", width=7, height=1, font=("DungGeunMo", 26 , "bold"), fg="white", bg="#124e8c", command=lambda:transport_exit_j(chapter_5_frame, main_menu_frame, chapter_5_canvas_list))
exit_btn_9.place(x=0, y=0)

Quiz_btn_9=Button(chapter_5_frame, text="Quiz", width=7, height=1, font=("DungGeunMo", 26 , "bold"), bg="#ffe760", command=lambda:transport(chapter_5_frame, quiz_menu_frame))
Quiz_btn_9.place(x=860, y=0)

pre_btn_9=Button(chapter_5_frame, text="◀ BACK", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_chapter_list_back(chapter_5_canvas_list[j], chapter_5_canvas_list[j-1]))
pre_btn_9.place(x=140, y=654)

next_btn_9=Button(chapter_5_frame, text="NEXT ▶", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_chapter_list_next(chapter_5_canvas_list[j], chapter_5_canvas_list[j+1]))
next_btn_9.place(x=886, y=654)

title_label_9=Label(chapter_5_frame,  text="CHAPTER 5 : 문자열", font=("DungGeunMo", 33 , "bold"), bg="white", padx=5, pady=5)
title_label_9.place(x=150,y=0)

date_label_9=Label(chapter_5_frame, text=time.strftime('%Y.%m.%d', time.localtime(time.time())), font=("DungGeunMo", 18), bg="white", padx=5, pady=5)
date_label_9.place(x=720, y=18)

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# chapter_6_frame 정보 (10th)
chapter_6_frame=Frame(window, bd=1, relief="flat")
chapter_6_frame.config(bg="white")

label_10=Label(chapter_6_frame, image=level_2_photo)
label_10.place(x=0, y=60)  
t_label_10=Label(chapter_6_frame, text="intermediate", font=("DungGeunMo", 16), fg="#0f4175", bg="white")
t_label_10.place(x=0, y=210)
t_label_10=Label(chapter_6_frame, text="level", font=("DungGeunMo", 24), fg="#0f4175", bg="white")
t_label_10.place(x=25, y=235)

chpater_6_1=PhotoImage(file="chapter_6_photo/1.png")
chpater_6_2=PhotoImage(file="chapter_6_photo/2.png")
chpater_6_3=PhotoImage(file="chapter_6_photo/3.png")
chpater_6_4=PhotoImage(file="chapter_6_photo/4.png")
chpater_6_5=PhotoImage(file="chapter_6_photo/5.png")
chpater_6_6=PhotoImage(file="chapter_6_photo/6.png")
chpater_6_7=PhotoImage(file="chapter_6_photo/7.png")
chpater_6_8=PhotoImage(file="chapter_6_photo/8.png")

# chapter_6_frame canvas_1 정보
canvas_10_1=Canvas(chapter_6_frame, width=1000, height=700, bg="#c8e9f3")
canvas_10_1.place(x=140, y=60)
photo_10_1=canvas_10_1.create_image(435, 200, image=chpater_6_1)
text_10=canvas_10_1.create_text(440, 40, text="✔ 리스트(list)", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_10=canvas_10_1.create_text(440, 360, text="= 리스트 : 서로 다른 데이터형을 순서대로 묶은 집합(= 배열)", fill="#0e2e50", font=("나눔바른펜", 20 , "bold"))
text_10=canvas_10_1.create_text(435, 400, text="- 인덱스를 통해 리스트 안의 데이터로 접근할 수 있습니다!", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_10=canvas_10_1.create_text(320, 450, text="  ex) aa=[10, 20, 30, 40]", fill="black", font=("나눔바른펜", 20 , "bold"))
text_10=canvas_10_1.create_text(435, 490, text="      aa[0]=10, aa[1]=20, aa[2]=30, aa[3]=40", fill="black", font=("나눔바른펜", 20 , "bold"))
text_10=canvas_10_1.create_text(355, 550, text="  ex) bb=[10, 'python', '파이썬']", fill="black", font=("나눔바른펜", 20 , "bold"))
text_10=canvas_10_1.create_text(440, 610, text="Chapter 6에 오신 걸 환영합니다 :)", fill="#0f4175", font=("나눔바른펜", 17 , "bold"))

# chapter_6_frame canvas_2 정보
canvas_10_2=Canvas(chapter_6_frame, width=1000, height=700, bg="#c8e9f3")
photo_10_2=canvas_10_2.create_image(440, 210, image=chpater_6_2)
canvas_10_2.create_rectangle(0,30,1000,50, fill="#124e8c", outline="#124e8c", width=7)
text_10=canvas_10_2.create_text(410, 380, text="✔ 리스트 인덱싱 : 양수와 음수 모두 접근 가능", fill="#0e2e50", font=("나눔바른펜", 20 , "bold"))
text_10=canvas_10_2.create_text(380, 420, text="- 양수와 음수에 대한 규약은 없습니다.", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_10=canvas_10_2.create_text(450, 460, text="- 문자열 슬라이싱처럼 리스트도 슬라이싱 가능합니다.", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_10=canvas_10_2.create_text(370, 510, text="  ex) 인덱싱 : aa[0] = aa[-4] = 10", fill="black", font=("나눔바른펜", 20 , "bold"))
text_10=canvas_10_2.create_text(368, 560, text="  ex) 슬라이싱 : aa[ :2] = [10, 20]", fill="black", font=("나눔바른펜", 20 , "bold"))
text_10=canvas_10_2.create_text(440, 580, text=" ", fill="black", font=("나눔바른펜", 20 , "bold"))

# chapter_6_frame canvas_3 정보
canvas_10_3=Canvas(chapter_6_frame, width=1000, height=700, bg="#c8e9f3")
canvas_10_3.create_rectangle(0,30,1000,50, fill="#124e8c", outline="#124e8c", width=7)
photo_10_3=canvas_10_3.create_image(440, 350, image=chpater_6_3)
text_10=canvas_10_3.create_text(440, 90, text="✔ 리스트 메서드", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))

# chapter_6_frame canvas_4 정보
canvas_10_4=Canvas(chapter_6_frame, width=1000, height=700, bg="#c8e9f3")
photo_10_4=canvas_10_4.create_image(440, 250, image=chpater_6_4)
txt_10=canvas_10_4.create_text(440, 60, text="= 리스트 메서드 예시 =", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
txt10_4=Text(canvas_10_4, width=50, height=10)
txt10_4.place(x=230, y=420)
btn10_4=Button(canvas_10_4, text="click", width=5, height=1, font=("DungGeunMo", 15), fg="white", bg="#2a6fb6", command=lambda:cmd(txt5_8))
btn10_4.place(x=600, y=420)
text_10=canvas_10_4.create_text(440, 590, text="위의 그림에 있는 대로 한 번 따라해볼까요?", fill="black", font=("나눔바른펜", 20 , "bold"))

# chapter_6_frame canvas_5 정보
canvas_10_5=Canvas(chapter_6_frame, width=1000, height=700, bg="#c8e9f3")
photo_10_5=canvas_10_5.create_image(440, 190, image=chpater_6_5)
text_10=canvas_10_5.create_text(440, 30, text="✔ 튜플(tuple)", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_10=canvas_10_5.create_text(440, 350, text="= 튜플 : 서로 다른 데이터형을 순서대로 묶은 집합(= 리스트)", fill="#0e2e50", font=("나눔바른펜", 20 , "bold"))
text_10=canvas_10_5.create_text(435, 390, text="- 인덱스를 통해 리스트 안의 데이터로 접근할 수 있습니다!", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_10=canvas_10_5.create_text(415, 430, text="- 리스트는 [ ], 튜플은 ( ) 사용 (튜플은 소괄호 생략O)", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_10=canvas_10_5.create_text(318, 470, text="- 튜플은 값 변경X, 읽기 전용 자료", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_10=canvas_10_5.create_text(350, 520, text="  ex) tt = (10, 20, 30, 40)", fill="black", font=("나눔바른펜", 20 , "bold"))
text_10=canvas_10_5.create_text(388, 560, text="      인덱싱 : tt[0] = tt[-4] = 10", fill="black", font=("나눔바른펜", 20 , "bold"))
text_10=canvas_10_5.create_text(388, 600, text="      슬라이싱 : tt[ :2] = (10, 20)", fill="black", font=("나눔바른펜", 20 , "bold"))


# chapter_6_frame canvas_6 정보
canvas_10_6=Canvas(chapter_6_frame, width=1000, height=700, bg="#c8e9f3")
photo_10_6=canvas_10_6.create_image(440, 150, image=chpater_6_6)
text_10=canvas_10_6.create_text(440, 50, text="✔ 딕셔너리(dictionary)", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_10=canvas_10_6.create_text(430, 250, text="= 딕셔너리 : 키(Key)와 값(Value)의 쌍으로 구성된 집합", fill="#0e2e50", font=("나눔바른펜", 20 , "bold"))
text_10=canvas_10_6.create_text(360, 290, text="- 딕셔너리는 순서가 없어 순서대로 구성X", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_10=canvas_10_6.create_text(440, 330, text="- 키와 값은 사용자가 지정하는 것으로 반대로 해도 상관X", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_10=canvas_10_6.create_text(438, 390, text="- 접근 : student['학번'] = 1000 (인덱싱 지원X)", fill="black", font=("나눔바른펜", 20 , "bold"))
text_10=canvas_10_6.create_text(370, 430, text="- 변경 : student['학번'] = '2000'", fill="black", font=("나눔바른펜", 20 , "bold"))
text_10=canvas_10_6.create_text(428, 470, text="- 추가 : student['연락처'] = '010-1111-2222'", fill="black", font=("나눔바른펜", 20 , "bold"))
text_10=canvas_10_6.create_text(352, 510, text="- 변경 : del(student['학과'])", fill="black", font=("나눔바른펜", 20 , "bold"))
text_10=canvas_10_6.create_text(440, 570, text="* 결과 : {'학번' : 2000, '이름' : '홍길동, '연락처' : '010-1111-2222'}", fill="black", font=("나눔바른펜", 20 , "bold"))

# chapter_6_frame canvas_7 정보
canvas_10_7=Canvas(chapter_6_frame, width=1000, height=700, bg="#c8e9f3")
photo_10_7=canvas_10_7.create_image(440, 190, image=chpater_6_7)
photo_10_8=canvas_10_7.create_image(440, 480, image=chpater_6_8)
text_10=canvas_10_7.create_text(440, 50, text="✔ 딕셔너리 메서드", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_10=canvas_10_7.create_text(440, 330, text="= 딕셔너리 메서드 예시 =", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_10=canvas_10_7.create_text(440, 610, text="Exit로 나가 Chapter 7로 넘어가주세요", fill="#0f4175", font=("나눔바른펜", 15 , "bold"))

chapter_6_canvas_list=[]
chapter_6_canvas_list.append(canvas_10_1)
chapter_6_canvas_list.append(canvas_10_2)
chapter_6_canvas_list.append(canvas_10_3)
chapter_6_canvas_list.append(canvas_10_4)
chapter_6_canvas_list.append(canvas_10_5)
chapter_6_canvas_list.append(canvas_10_6)
chapter_6_canvas_list.append(canvas_10_7)

#--------------------------------------

exit_btn_10=Button(chapter_6_frame, text="EXIT", width=7, height=1, font=("DungGeunMo", 26 , "bold"), fg="white", bg="#124e8c", command=lambda:transport_exit_j(chapter_6_frame, main_menu_frame, chapter_6_canvas_list))
exit_btn_10.place(x=0, y=0)

Quiz_btn_10=Button(chapter_6_frame, text="Quiz", width=7, height=1, font=("DungGeunMo", 26 , "bold"), bg="#ffe760", command=lambda:transport(chapter_6_frame, quiz_menu_frame))
Quiz_btn_10.place(x=860, y=0)

pre_btn_10=Button(chapter_6_frame, text="◀ BACK", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_chapter_list_back(chapter_6_canvas_list[j], chapter_6_canvas_list[j-1]))
pre_btn_10.place(x=140, y=654)

next_btn_10=Button(chapter_6_frame, text="NEXT ▶", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_chapter_list_next(chapter_6_canvas_list[j], chapter_6_canvas_list[j+1]))
next_btn_10.place(x=886, y=654)

title_label_10=Label(chapter_6_frame,  text="CHAPTER 6 : 자료구조", font=("DungGeunMo", 33 , "bold"), bg="white", padx=5, pady=5)
title_label_10.place(x=150,y=0)

date_label_10=Label(chapter_6_frame, text=time.strftime('%Y.%m.%d', time.localtime(time.time())), font=("DungGeunMo", 18), bg="white", padx=5, pady=5)
date_label_10.place(x=720, y=18)

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# chapter_7_frame 정보 (11th)
chapter_7_frame=Frame(window, bd=1, relief="flat")
chapter_7_frame.config(bg="white")

label_11=Label(chapter_7_frame, image=level_2_photo)
label_11.place(x=0, y=60)  
t_label_11=Label(chapter_7_frame, text="intermediate", font=("DungGeunMo", 16), fg="#0f4175", bg="white")
t_label_11.place(x=0, y=210)
t_label_11=Label(chapter_7_frame, text="level", font=("DungGeunMo", 23), fg="#0f4175", bg="white")
t_label_11.place(x=25, y=235)

chpater_7_1=PhotoImage(file="chapter_7_photo/1.png")
chpater_7_2=PhotoImage(file="chapter_7_photo/2.png")
chpater_7_3=PhotoImage(file="chapter_7_photo/3.png")
chpater_7_4=PhotoImage(file="chapter_7_photo/4.png")
chpater_7_5=PhotoImage(file="chapter_7_photo/5.png")
chpater_7_6=PhotoImage(file="chapter_7_photo/6.png")
chpater_7_7=PhotoImage(file="chapter_7_photo/7.png")

# chapter_7_frame canvas_1 정보
canvas_11_1=Canvas(chapter_7_frame, width=1000, height=700, bg="#c8e9f3")
canvas_11_1.place(x=140, y=60)
text_11=canvas_11_1.create_text(440, 50, text="✔ 함수(function)", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
photo_11_1=canvas_11_1.create_image(440, 220, image=chpater_7_1)
text_11=canvas_11_1.create_text(430, 390, text="= 함수 : 입력값을 가지고 어떤 일을 수행한 다음, 그 결과값을 내놓음", fill="#0e2e50", font=("나눔바른펜", 20 , "bold"))
text_11=canvas_11_1.create_text(435, 430, text="- 입력값 → 함수 → 결과값", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_11=canvas_11_1.create_text(430, 470, text="- def 함수명 (매개변수) :", fill="black", font=("나눔바른펜", 20 , "bold"))
text_11=canvas_11_1.create_text(410, 510, text="      수행할 문장 1", fill="black", font=("나눔바른펜", 20 , "bold"))
text_11=canvas_11_1.create_text(410, 550, text="      수행할 문장 2", fill="black", font=("나눔바른펜", 20 , "bold"))
text_11=canvas_11_1.create_text(440, 610, text="Chapter 7에 오신 걸 환영합니다 :)", fill="#0f4175", font=("나눔바른펜", 17 , "bold"))

# chapter_7_frame canvas_2 정보
canvas_11_2=Canvas(chapter_7_frame, width=1000, height=700, bg="#c8e9f3")
canvas_11_2.create_rectangle(0,30,1000,50, fill="#124e8c", outline="#124e8c", width=7)
text_11=canvas_11_2.create_text(440, 110, text="✔ 변수", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
photo_11_2=canvas_11_2.create_image(440, 280, image=chpater_7_2)
text_11=canvas_11_2.create_text(430, 460, text="= 변수 : 계속 변하는 값, 그 값을 저장하는 공간", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_11=canvas_11_2.create_text(412, 500, text="- 지역 변수 : 한정된 지역(함수)에서만 사용", fill="black", font=("나눔바른펜", 20 , "bold"))
text_11=canvas_11_2.create_text(383, 540, text="- 전역 변수 : 프로그램 전체에서 사용", fill="black", font=("나눔바른펜", 20 , "bold"))

# chapter_7_frame canvas_3 정보
canvas_11_3=Canvas(chapter_7_frame, width=1000, height=700, bg="#c8e9f3")
text_11=canvas_11_3.create_text(250, 50, text="1. 입력값 O 함수", fill="#0e2e50", font=("나눔바른펜", 25 , "bold"))
text_11=canvas_11_3.create_text(600, 50, text="2. 입력값 X 함수", fill="#0e2e50", font=("나눔바른펜", 25 , "bold"))
photo_11_3=canvas_11_3.create_image(250, 330, image=chpater_7_3)
photo_11_4=canvas_11_3.create_image(600, 330, image=chpater_7_4)

# chapter_7_frame canvas_4 정보
canvas_11_4=Canvas(chapter_7_frame, width=1000, height=700, bg="#c8e9f3")
text_11=canvas_11_4.create_text(280, 90, text="3. 결과값 O 함수", fill="#0e2e50", font=("나눔바른펜", 25 , "bold"))
text_11=canvas_11_4.create_text(630, 90, text="4. 결과값 X 함수", fill="#0e2e50", font=("나눔바른펜", 25 , "bold"))
photo_11_5=canvas_11_4.create_image(280, 330, image=chpater_7_5)
photo_11_6=canvas_11_4.create_image(630, 330, image=chpater_7_6)

# chapter_7_frame canvas_5 정보
canvas_11_5=Canvas(chapter_7_frame, width=1000, height=700, bg="#c8e9f3")
canvas_11_5.create_rectangle(0,30,1000,50, fill="#124e8c", outline="#124e8c", width=7)
text_11=canvas_11_5.create_text(440, 110, text="< 함수 유의사항 >", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
canvas_11_5.create_rectangle(180, 150, 690, 530, fill="white", outline="#124e8c", width=5)
text_11=canvas_11_5.create_text(440, 200, text="✔ 매개변수를 지정할 수 있다.", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_11=canvas_11_5.create_text(440, 235, text="ex) sum = add(a=5, b=3)", fill="black", font=("나눔바른펜", 20 , "bold"))
text_11=canvas_11_5.create_text(440, 280, text="✔ 함수의 결괏값은 언제나 하나다.", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_11=canvas_11_5.create_text(440, 315, text="ex) return sum;(O) return ssum;(X)", fill="black", font=("나눔바른펜", 20 , "bold"))
text_11=canvas_11_5.create_text(440, 360, text="✔ 매개변수에 초깃값 미리 설정할 수 있다.", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_11=canvas_11_5.create_text(440, 395, text="ex) def say_myself(name, old, man=True): ", fill="black", font=("나눔바른펜", 20 , "bold"))
text_11=canvas_11_5.create_text(440, 440, text="✔ 지역변수, 전역변수에 유의한다.", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_11=canvas_11_5.create_text(440, 475, text="ex) 지역 : a, 전역 : global a", fill="black", font=("나눔바른펜", 20 , "bold"))

# chapter_7_frame canvas_6 정보
canvas_11_6=Canvas(chapter_7_frame, width=1000, height=700, bg="#c8e9f3")
canvas_11_6.create_rectangle(0,50,1000,70, fill="#124e8c", outline="#124e8c", width=7)
photo_11_6=canvas_11_6.create_image(250, 350, image=chpater_7_7)
text_11=canvas_11_6.create_text(610, 160, text="✔ global 명령어", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_11=canvas_11_6.create_text(610, 220, text="- 함수 밖에 선언된 변수를", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_11=canvas_11_6.create_text(635, 260, text="  함수 안에서 직접적으로 사용", fill="black", font=("나눔바른펜", 20 , "bold"))
text_11=canvas_11_6.create_text(620, 300, text="- 외부 변수에 종속적인 함수", fill="black", font=("나눔바른펜", 20 , "bold"))
text_11=canvas_11_6.create_text(550, 390, text="- global 변수", fill="#0e2e50", font=("나눔바른펜", 20 , "bold"))
text_11=canvas_11_6.create_text(560, 430, text="  ex) global a", fill="black", font=("나눔바른펜", 20 , "bold"))
text_11=canvas_11_6.create_text(440, 610, text="Exit로 나가 Chapter 8로 넘어가주세요", fill="#0f4175", font=("나눔바른펜", 15 , "bold"))

chapter_7_canvas_list=[]
chapter_7_canvas_list.append(canvas_11_1)
chapter_7_canvas_list.append(canvas_11_2)
chapter_7_canvas_list.append(canvas_11_3)
chapter_7_canvas_list.append(canvas_11_4)
chapter_7_canvas_list.append(canvas_11_5)
chapter_7_canvas_list.append(canvas_11_6)

#--------------------------------------

exit_btn_11=Button(chapter_7_frame, text="EXIT", width=7, height=1, font=("DungGeunMo", 26 , "bold"), fg="white", bg="#124e8c", command=lambda:transport_exit_j(chapter_7_frame, main_menu_frame, chapter_7_canvas_list))
exit_btn_11.place(x=0, y=0)

Quiz_btn_11=Button(chapter_7_frame, text="Quiz", width=7, height=1, font=("DungGeunMo", 26 , "bold"), bg="#ffe760", command=lambda:transport(chapter_7_frame, quiz_menu_frame))
Quiz_btn_11.place(x=860, y=0)

pre_btn_11=Button(chapter_7_frame, text="◀ BACK", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_chapter_list_back(chapter_7_canvas_list[j], chapter_7_canvas_list[j-1]))
pre_btn_11.place(x=140, y=654)

next_btn_11=Button(chapter_7_frame, text="NEXT ▶", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_chapter_list_next(chapter_7_canvas_list[j], chapter_7_canvas_list[j+1]))
next_btn_11.place(x=886, y=654)

title_label_11=Label(chapter_7_frame,  text="CHAPTER 7 : 함수", font=("DungGeunMo", 33 , "bold"), bg="white", padx=5, pady=5)
title_label_11.place(x=150,y=0)

date_label_11=Label(chapter_7_frame, text=time.strftime('%Y.%m.%d', time.localtime(time.time())), font=("DungGeunMo", 18), bg="white", padx=5, pady=5)
date_label_11.place(x=720, y=18)

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# chapter_8_frame 정보 (12th)
chapter_8_frame=Frame(window, bd=1, relief="flat")
chapter_8_frame.config(bg="white")

level_3_photo=PhotoImage(file="photo/level_3.png")

label_12=Label(chapter_8_frame, image=level_3_photo)
label_12.place(x=0, y=60)  
t_label_12=Label(chapter_8_frame, text="advanced", font=("DungGeunMo", 20), fg="#0f4175", bg="white")
t_label_12.place(x=10, y=210)
t_label_12=Label(chapter_8_frame, text="level", font=("DungGeunMo", 25), fg="#0f4175", bg="white")
t_label_12.place(x=25, y=240)

chpater_8_1=PhotoImage(file="chapter_8_photo/1.png")
chpater_8_2=PhotoImage(file="chapter_8_photo/2.png")
chpater_8_3=PhotoImage(file="chapter_8_photo/3.png")
chpater_8_4=PhotoImage(file="chapter_8_photo/4.png")
chpater_8_5=PhotoImage(file="chapter_8_photo/5.png")
chpater_8_6=PhotoImage(file="chapter_8_photo/6.png")

# chapter_8_frame canvas_1 정보
canvas_12_1=Canvas(chapter_8_frame, width=1000, height=700, bg="#c8e9f3")
canvas_12_1.place(x=140, y=60)
canvas_12_1.create_rectangle(0,30,1000,50, fill="#124e8c", outline="#124e8c", width=7)
text_12=canvas_12_1.create_text(440, 120, text="✔ 파일 입출력", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
photo_12_1=canvas_12_1.create_image(440, 280, image=chpater_8_1)
text_12=canvas_12_1.create_text(440, 430, text="= 파일 입출력 : 파일을 통한 입출력 방식", fill="#124e8c", font=("나눔바른펜", 20 , "bold"))
text_12=canvas_12_1.create_text(432, 470, text="- 파일을 생성한 후, 파일의 내용을 변경할 수 있습니다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_12=canvas_12_1.create_text(440, 510, text="- 파일의 내용을 변경하고 저장한 후 종료할 수 있습니다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_12=canvas_12_1.create_text(440, 610, text="Chapter 8에 오신 걸 환영합니다 :)", fill="#0f4175", font=("나눔바른펜", 17 , "bold"))

# chapter_8_frame canvas_2 정보
canvas_12_2=Canvas(chapter_8_frame, width=1000, height=700, bg="#c8e9f3")
canvas_12_2.create_rectangle(0,30,1000,50, fill="#124e8c", outline="#124e8c", width=7)
canvas_12_2.create_rectangle(200, 135, 680, 190, fill="white", outline="#124e8c", width=5)
photo_12_2=canvas_12_2.create_image(440, 450, image=chpater_8_2)
text_12=canvas_12_2.create_text(440, 100, text="1. 파일 생성하기(열기)", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_12=canvas_12_2.create_text(440, 160, text="파일 객체 = open(파일 이름, 파일 모드)", fill="#124e8c", font=("나눔바른펜", 20 , "bold"))
text_12=canvas_12_2.create_text(437, 230, text="- 읽기용 : f = open("'"test.txt"'", 'r')", fill="black", font=("나눔바른펜", 20 , "bold"))
text_12=canvas_12_2.create_text(440, 270, text="- 쓰기용 : f = open("'"test.txt"'", 'w')", fill="black", font=("나눔바른펜", 20 , "bold"))

# chapter_8_frame canvas_3 정보
canvas_12_3=Canvas(chapter_8_frame, width=1000, height=700, bg="#c8e9f3")
canvas_12_3.create_rectangle(0,30,1000,50, fill="#124e8c", outline="#124e8c", width=7)
text_12=canvas_12_3.create_text(440, 100, text="2. 파일 읽고 쓰기", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
photo_12_3=canvas_12_3.create_image(440, 210, image=chpater_8_3)
photo_12_4=canvas_12_3.create_image(440, 440, image=chpater_8_4)

# chapter_8_frame canvas_4 정보
canvas_12_4=Canvas(chapter_8_frame, width=1000, height=700, bg="#c8e9f3")
canvas_12_4.create_rectangle(0,30,1000,50, fill="#124e8c", outline="#124e8c", width=7)
canvas_12_4.create_rectangle(300, 145, 580, 200, fill="white", outline="#124e8c", width=5)
text_12=canvas_12_4.create_text(440, 100, text="3. 파일 닫기", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_12=canvas_12_4.create_text(440, 170, text="파일 객체.close( )", fill="#124e8c", font=("나눔바른펜", 20 , "bold"))
text_12=canvas_12_4.create_text(440, 230, text="- f.close( )", fill="black", font=("나눔바른펜", 20 , "bold"))
photo_12_5=canvas_12_4.create_image(440, 420, image=chpater_8_5)

# chapter_8_frame canvas_5 정보
canvas_12_5=Canvas(chapter_8_frame, width=1000, height=700, bg="#c8e9f3")
canvas_12_5.create_rectangle(0,30,1000,50, fill="#124e8c", outline="#124e8c", width=7)
canvas_12_5.create_rectangle(200, 155, 680, 210, fill="white", outline="#124e8c", width=5)
text_12=canvas_12_5.create_text(440, 110, text="✔ with문", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_12=canvas_12_5.create_text(440, 180, text="with open(파일명, 파일모드) as 파일 객체", fill="#124e8c", font=("나눔바른펜", 20 , "bold"))
text_12=canvas_12_5.create_text(421, 260, text="- 파일을 open 하면 항상 close 해줍니다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_12=canvas_12_5.create_text(440, 300, text="- 파일을 열고 닫는 것을 자동으로 처리합니다.", fill="black", font=("나눔바른펜", 20 , "bold"))
photo_12_6=canvas_12_5.create_image(440, 420, image=chpater_8_6)
text_12=canvas_12_5.create_text(440, 610, text="Exit로 나가 Chapter 9로 넘어가주세요", fill="#0f4175", font=("나눔바른펜", 15 , "bold"))

chapter_8_canvas_list=[]
chapter_8_canvas_list.append(canvas_12_1)
chapter_8_canvas_list.append(canvas_12_2)
chapter_8_canvas_list.append(canvas_12_3)
chapter_8_canvas_list.append(canvas_12_4)
chapter_8_canvas_list.append(canvas_12_5)

#--------------------------------------

exit_btn_12=Button(chapter_8_frame, text="EXIT", width=7, height=1, font=("DungGeunMo", 26 , "bold"), fg="white", bg="#124e8c", command=lambda:transport_exit_j(chapter_8_frame, main_menu_frame, chapter_8_canvas_list))
exit_btn_12.place(x=0, y=0)

Quiz_btn_12=Button(chapter_8_frame, text="Quiz", width=7, height=1, font=("DungGeunMo", 26 , "bold"), bg="#ffe760", command=lambda:transport(chapter_8_frame, quiz_menu_frame))
Quiz_btn_12.place(x=860, y=0)

pre_btn_12=Button(chapter_8_frame, text="◀ BACK", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_chapter_list_back(chapter_8_canvas_list[j], chapter_8_canvas_list[j-1]))
pre_btn_12.place(x=140, y=654)

next_btn_12=Button(chapter_8_frame, text="NEXT ▶", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_chapter_list_next(chapter_8_canvas_list[j], chapter_8_canvas_list[j+1]))
next_btn_12.place(x=886, y=654)

title_label_12=Label(chapter_8_frame,  text="CHAPTER 8 : 입출력", font=("DungGeunMo", 33 , "bold"), bg="white", padx=5, pady=5)
title_label_12.place(x=150,y=0)

date_label_12=Label(chapter_8_frame, text=time.strftime('%Y.%m.%d', time.localtime(time.time())), font=("DungGeunMo", 18), bg="white", padx=5, pady=5)
date_label_12.place(x=720, y=18)

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# chapter_9_frame 정보 (13th)
chapter_9_frame=Frame(window, bd=1, relief="flat")
chapter_9_frame.config(bg="white")

label_13=Label(chapter_9_frame, image=level_3_photo)
label_13.place(x=0, y=60)  
t_label_13=Label(chapter_9_frame, text="advanced", font=("DungGeunMo", 20), fg="#0f4175", bg="white")
t_label_13.place(x=10, y=210)
t_label_13=Label(chapter_9_frame, text="level", font=("DungGeunMo", 25), fg="#0f4175", bg="white")
t_label_13.place(x=25, y=240)

chpater_9_1=PhotoImage(file="chapter_9_photo/1.png")
chpater_9_2=PhotoImage(file="chapter_9_photo/2.png")
chpater_9_3=PhotoImage(file="chapter_9_photo/3.png")
chpater_9_4=PhotoImage(file="chapter_9_photo/4.png")

# chapter_9_frame canvas_1 정보
canvas_13_1=Canvas(chapter_9_frame, width=1000, height=700, bg="#c8e9f3")
canvas_13_1.place(x=140, y=60)
canvas_13_1.create_rectangle(0,50,1000,70, fill="#124e8c", outline="#124e8c", width=7)
text_13=canvas_13_1.create_text(440, 115, text="✔ 예외처리", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
photo_13_1=canvas_13_1.create_image(440, 250, image=chpater_9_1)
text_13=canvas_13_1.create_text(440, 380, text="= 예외처리 : 예상치 못한 상황 발생을 대비해 실행할 동작 미리 지정", fill="#0f4175", font=("나눔바른펜", 20 , "bold"))
text_13=canvas_13_1.create_text(440, 440, text="- 파일 입출력 시, 파일을 열 수 없는 경우가 있습니다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_13=canvas_13_1.create_text(408, 480, text="- 오류가 나서 프로그램이 종료될 수 있습니다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_13=canvas_13_1.create_text(385, 520, text="- 이 때, 예외처리를 이용하면 프로그램의", fill="black", font=("나눔바른펜", 20 , "bold"))
text_13=canvas_13_1.create_text(365, 560, text="  비정상적 종료를 막을 수 있습니다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_13=canvas_13_1.create_text(440, 610, text="Chapter 9에 오신 걸 환영합니다 :)", fill="#0f4175", font=("나눔바른펜", 17 , "bold"))

# chapter_9_frame canvas_2 정보
canvas_13_2=Canvas(chapter_9_frame, width=1000, height=700, bg="#c8e9f3")
photo_13_2=canvas_13_2.create_image(230, 310, image=chpater_9_2)
photo_13_3=canvas_13_2.create_image(650, 340, image=chpater_9_3)
text_13=canvas_13_2.create_text(230, 60, text="✔ try-except", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_13=canvas_13_2.create_text(650, 60, text="✔ try-except-else", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))

# chapter_9_frame canvas_3 정보
canvas_13_3=Canvas(chapter_9_frame, width=1000, height=700, bg="#c8e9f3")
canvas_13_3.create_rectangle(0,50,1000,70, fill="#124e8c", outline="#124e8c", width=7)
text_13=canvas_13_3.create_text(440, 120, text="✔ 예외처리 예시", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
photo_13_3=canvas_13_3.create_image(440, 370, image=chpater_9_4)
text_13=canvas_13_3.create_text(440, 610, text="Exit로 나가 Chapter 10로 넘어가주세요", fill="#0f4175", font=("나눔바른펜", 15 , "bold"))

chapter_9_canvas_list=[]
chapter_9_canvas_list.append(canvas_13_1)
chapter_9_canvas_list.append(canvas_13_2)
chapter_9_canvas_list.append(canvas_13_3)

#--------------------------------------

exit_btn_13=Button(chapter_9_frame, text="EXIT", width=7, height=1, font=("DungGeunMo", 26 , "bold"), fg="white", bg="#134e8c", command=lambda:transport_exit_j(chapter_9_frame, main_menu_frame, chapter_9_canvas_list))
exit_btn_13.place(x=0, y=0)

Quiz_btn_13=Button(chapter_9_frame, text="Quiz", width=7, height=1, font=("DungGeunMo", 26 , "bold"), bg="#ffe760", command=lambda:transport(chapter_9_frame, quiz_menu_frame))
Quiz_btn_13.place(x=860, y=0)

pre_btn_13=Button(chapter_9_frame, text="◀ BACK", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_chapter_list_back(chapter_9_canvas_list[j], chapter_9_canvas_list[j-1]))
pre_btn_13.place(x=140, y=654)

next_btn_13=Button(chapter_9_frame, text="NEXT ▶", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_chapter_list_next(chapter_9_canvas_list[j], chapter_9_canvas_list[j+1]))
next_btn_13.place(x=886, y=654)

title_label_13=Label(chapter_9_frame,  text="CHAPTER 9 : 예외처리", font=("DungGeunMo", 33 , "bold"), bg="white", padx=5, pady=5)
title_label_13.place(x=150,y=0)

date_label_13=Label(chapter_9_frame, text=time.strftime('%Y.%m.%d', time.localtime(time.time())), font=("DungGeunMo", 18), bg="white", padx=5, pady=5)
date_label_13.place(x=720, y=18)

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# chapter_10_frame 정보 (14th)
chapter_10_frame=Frame(window, bd=1, relief="flat")
chapter_10_frame.config(bg="white")

label_14=Label(chapter_10_frame, image=level_3_photo)
label_14.place(x=0, y=60) 
t_label_14=Label(chapter_10_frame, text="advanced", font=("DungGeunMo", 20), fg="#0f4175", bg="white")
t_label_14.place(x=10, y=210)
t_label_14=Label(chapter_10_frame, text="level", font=("DungGeunMo", 25), fg="#0f4175", bg="white")
t_label_14.place(x=25, y=240)

chpater_10_1=PhotoImage(file="chapter_10_photo/1.png")
chpater_10_2=PhotoImage(file="chapter_10_photo/2.png")
chpater_10_3=PhotoImage(file="chapter_10_photo/3.png")
chpater_10_4=PhotoImage(file="chapter_10_photo/4.png")
chpater_10_5=PhotoImage(file="chapter_10_photo/5.png")
chpater_10_6=PhotoImage(file="chapter_10_photo/6.png")
chpater_10_7=PhotoImage(file="chapter_10_photo/7.png")
chpater_10_8=PhotoImage(file="chapter_10_photo/8.png")

# chapter_10_frame canvas_1 정보
canvas_14_1=Canvas(chapter_10_frame, width=1000, height=700, bg="#c8e9f3")
canvas_14_1.place(x=140, y=60)
photo_14_1=canvas_14_1.create_image(440, 470, image=chpater_10_1)
text_14=canvas_14_1.create_text(440, 50, text="✔ 클래스(class)", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_14=canvas_14_1.create_text(387, 100, text="= 클래스 : 사용자가 정의하는 자료형", fill="#0e2e50", font=("나눔바른펜", 20 , "bold"))
text_14=canvas_14_1.create_text(440, 140, text="- 공통된 특성을 한 번에 정의하고 공유하여 사용", fill="black", font=("나눔바른펜", 20 , "bold"))
text_14=canvas_14_1.create_text(382, 180, text="- 공통된 특성 : 멤버 변수, 멤버 함수", fill="black", font=("나눔바른펜", 20 , "bold"))
text_14=canvas_14_1.create_text(450, 250, text="= 객체 : 클래스에 의해 만들어지는 실제 사용 변수", fill="#0e2e50", font=("나눔바른펜", 20 , "bold"))
text_14=canvas_14_1.create_text(453, 290, text="- 코드 안에서 실질적으로 사용하는 실체(인스턴스)", fill="black", font=("나눔바른펜", 20 , "bold"))
text_14=canvas_14_1.create_text(428, 330, text="- 클래스를 통해 객체가 생성되면 메모리 할당", fill="black", font=("나눔바른펜", 20 , "bold"))
text_14=canvas_14_1.create_text(440, 610, text="Chapter 10에 오신 걸 환영합니다 :)", fill="#0f4175", font=("나눔바른펜", 17 , "bold"))

# chapter_10_frame canvas_2 정보
canvas_14_2=Canvas(chapter_10_frame, width=1000, height=700, bg="#c8e9f3")
canvas_14_2.create_rectangle(0,30,1000,50, fill="#124e8c", outline="#124e8c", width=7)
text_14=canvas_14_2.create_text(440, 100, text="✔ 클래스 예시", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
photo_14_2=canvas_14_2.create_image(440, 350, image=chpater_10_2)

# chapter_10_frame canvas_3 정보
canvas_14_3=Canvas(chapter_10_frame, width=1000, height=700, bg="#c8e9f3")
text_14=canvas_14_3.create_text(440, 50, text="= 클래스 예시 =", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
photo_14_8=canvas_14_3.create_image(440, 250, image=chpater_10_8)
txt14_3=Text(canvas_14_3, width=50, height=10)
txt14_3.place(x=230, y=420)
btn14_3=Button(canvas_14_3, text="click", width=5, height=1, font=("DungGeunMo", 15), fg="white", bg="#2a6fb6", command=lambda:cmd(txt14_3))
btn14_3.place(x=600, y=420)
text_14=canvas_14_3.create_text(440, 590, text="위의 그림에 있는 대로 한 번 따라해볼까요?", fill="black", font=("나눔바른펜", 20 , "bold"))

# chapter_10_frame canvas_4 정보
canvas_14_4=Canvas(chapter_10_frame, width=1000, height=700, bg="#c8e9f3")
canvas_14_4.create_rectangle(0,60,1000,80, fill="#124e8c", outline="#124e8c", width=7)
text_14=canvas_14_4.create_text(440, 150, text="✔ 클래스 사용 단계", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
photo_14_4=canvas_14_4.create_image(440, 390, image=chpater_10_4)

# chapter_10_frame canvas_5 정보
canvas_14_5=Canvas(chapter_10_frame, width=1000, height=700, bg="#c8e9f3")
canvas_14_5.create_rectangle(300, 135, 580, 185, fill="white", outline="#124e8c", width=5)
text_14=canvas_14_5.create_text(440, 50, text="✔ 클래스 생성자", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_14=canvas_14_5.create_text(440, 160, text="def __init__(self)", fill="#124e8c", font=("나눔바른펜", 20 , "bold"))
text_14=canvas_14_5.create_text(440, 100, text="= 생성자 : 인스턴스 생성 시, 멤버 변수를 초기화", fill="#0e2e50", font=("나눔바른펜", 20 , "bold"))
photo_14_4=canvas_14_5.create_image(440, 400, image=chpater_10_4)

# chapter_10_frame canvas_6 정보
canvas_14_6=Canvas(chapter_10_frame, width=1000, height=700, bg="#c8e9f3")
canvas_14_6.create_rectangle(300, 135, 580, 185, fill="white", outline="#124e8c", width=5)
text_14=canvas_14_6.create_text(440, 50, text="✔ 클래스 소멸자", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_14=canvas_14_6.create_text(440, 160, text="__del__( )", fill="#124e8c", font=("나눔바른펜", 20 , "bold"))
text_14=canvas_14_6.create_text(440, 100, text="= 소멸자 : 인스턴스 삭제 시, 자동으로 호출", fill="#0e2e50", font=("나눔바른펜", 20 , "bold"))
photo_14_5=canvas_14_6.create_image(440, 400, image=chpater_10_5)

# chapter_10_frame canvas_7 정보
canvas_14_7=Canvas(chapter_10_frame, width=1000, height=700, bg="#c8e9f3")
text_14=canvas_14_7.create_text(440, 50, text="✔ 클래스 상속", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_14=canvas_14_7.create_text(440, 100, text="= 상속 : 기존 클래스를 물려받는 파생 클래스를 만드는 것", fill="#0e2e50", font=("나눔바른펜", 20 , "bold"))
text_14=canvas_14_7.create_text(375, 140, text="- 공통된 특성을 물려받아 그대로 사용, 변경", fill="black", font=("나눔바른펜", 20 , "bold"))
text_14=canvas_14_7.create_text(302, 180, text="- 상위-하위, 부모-자식 관계", fill="black", font=("나눔바른펜", 20 , "bold"))
photo_14_6=canvas_14_7.create_image(440, 400, image=chpater_10_6)

# chapter_10_frame canvas_8 정보
canvas_14_8=Canvas(chapter_10_frame, width=1000, height=700, bg="#c8e9f3")
canvas_14_8.create_rectangle(0,20,1000,40, fill="#124e8c", outline="#124e8c", width=7)
text_14=canvas_14_8.create_text(440, 80, text="✔ 클래스 상속 예시", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
photo_14_8=canvas_14_8.create_image(440, 350, image=chpater_10_7)
text_14=canvas_14_8.create_text(440, 610, text="Exit로 나가 Chapter 10로 넘어가주세요", fill="#0f4175", font=("나눔바른펜", 15 , "bold"))

chapter_10_canvas_list=[]
chapter_10_canvas_list.append(canvas_14_1)
chapter_10_canvas_list.append(canvas_14_2)
chapter_10_canvas_list.append(canvas_14_3)
chapter_10_canvas_list.append(canvas_14_4)
chapter_10_canvas_list.append(canvas_14_5)
chapter_10_canvas_list.append(canvas_14_6)
chapter_10_canvas_list.append(canvas_14_7)
chapter_10_canvas_list.append(canvas_14_8)

#--------------------------------------

exit_btn_14=Button(chapter_10_frame, text="EXIT", width=7, height=1, font=("DungGeunMo", 26 , "bold"), fg="white", bg="#144e8c", command=lambda:transport_exit_j(chapter_10_frame, main_menu_frame, chapter_10_canvas_list))
exit_btn_14.place(x=0, y=0)

Quiz_btn_14=Button(chapter_10_frame, text="Quiz", width=7, height=1, font=("DungGeunMo", 26 , "bold"), bg="#ffe760", command=lambda:transport(chapter_10_frame, quiz_menu_frame))
Quiz_btn_14.place(x=860, y=0)

pre_btn_14=Button(chapter_10_frame, text="◀ BACK", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_chapter_list_back(chapter_10_canvas_list[j], chapter_10_canvas_list[j-1]))
pre_btn_14.place(x=140, y=654)

next_btn_14=Button(chapter_10_frame, text="NEXT ▶", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_chapter_list_next(chapter_10_canvas_list[j], chapter_10_canvas_list[j+1]))
next_btn_14.place(x=886, y=654)

title_label_14=Label(chapter_10_frame,  text="CHAPTER 10 : 클래스", font=("DungGeunMo", 33 , "bold"), bg="white", padx=5, pady=5)
title_label_14.place(x=150,y=0)

date_label_14=Label(chapter_10_frame, text=time.strftime('%Y.%m.%d', time.localtime(time.time())), font=("DungGeunMo", 18), bg="white", padx=5, pady=5)
date_label_14.place(x=720, y=18)

#------------------------------------------------------------------------------------------------------------------------------------------------------------

# chapter_11_frame 정보 (15th)
chapter_11_frame=Frame(window, bd=1, relief="flat")
chapter_11_frame.config(bg="white")

label_15=Label(chapter_11_frame, image=level_3_photo)
label_15.place(x=0, y=60) 
t_label_15=Label(chapter_11_frame, text="advanced", font=("DungGeunMo", 20), fg="#0f4175", bg="white")
t_label_15.place(x=10, y=210)
t_label_15=Label(chapter_11_frame, text="level", font=("DungGeunMo", 25), fg="#0f4175", bg="white")
t_label_15.place(x=25, y=240)

chpater_11_1=PhotoImage(file="chapter_11_photo/1.png")
chpater_11_2=PhotoImage(file="chapter_11_photo/2.png")
chpater_11_3=PhotoImage(file="chapter_11_photo/3.png")

# chapter_11_frame canvas_1 정보
canvas_15_1=Canvas(chapter_11_frame, width=1000, height=700, bg="#c8e9f3")
canvas_15_1.place(x=140, y=60)
text_15=canvas_15_1.create_text(440, 50, text="✔ 모듈(module)", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
text_15=canvas_15_1.create_text(440, 100, text="= 모듈 : 함수, 변수, 클래스의 집합", fill="#0e2e50", font=("나눔바른펜", 20 , "bold"))
text_15=canvas_15_1.create_text(440, 150, text="- 다른 파이썬 프로그램에서 불러와 사용할 수 있게 만든 파이썬 파일", fill="black", font=("나눔바른펜", 20 , "bold"))
text_15=canvas_15_1.create_text(300, 210, text="- 표준 모듈 : 파이썬에서 제공하는 모듈", fill="black", font=("나눔바른펜", 20 , "bold"))
text_15=canvas_15_1.create_text(350, 250, text="- 사용자 정의 모듈 : 직접 만들어서 사용하는 모듈", fill="black", font=("나눔바른펜", 20 , "bold"))
text_15=canvas_15_1.create_text(445, 290, text="- 서드 파티 모듈 : 파이썬이 아닌 외부 회사나 단체에서 제공하는 모듈", fill="black", font=("나눔바른펜", 20 , "bold"))
photo_15_1=canvas_15_1.create_image(440, 440, image=chpater_11_1)
text_15=canvas_15_1.create_text(440, 610, text="Chapter 11에 오신 걸 환영합니다 :)", fill="#0f4175", font=("나눔바른펜", 17 , "bold"))

# chapter_11_frame canvas_2 정보
canvas_15_2=Canvas(chapter_11_frame, width=1000, height=700, bg="#c8e9f3")
canvas_15_2.create_rectangle(0,30,1000,50, fill="#124e8c", outline="#124e8c", width=7)
text_15=canvas_15_2.create_text(440, 100, text="✔ 모듈 import", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
canvas_15_2.create_rectangle(170, 140, 710, 280, fill="white", outline="#124e8c", width=5)
text_15=canvas_15_2.create_text(368, 170, text="- import 모듈이름", fill="#124e8c", font=("나눔바른펜", 20 , "bold"))
text_15=canvas_15_2.create_text(440, 210, text="- from 모듈이름 import 모듈함수", fill="#124e8c", font=("나눔바른펜", 20 , "bold"))
text_15=canvas_15_2.create_text(405, 250, text="- from 모듈이름 import *", fill="#124e8c", font=("나눔바른펜", 20 , "bold"))
text_15=canvas_15_2.create_text(440, 340, text="- import : 현재 디렉터리에 있는 파일이나 파이썬 라이브러리가", fill="black", font=("나눔바른펜", 20 , "bold"))
text_15=canvas_15_2.create_text(435, 380, text="           저장된 디렉터리에 있는 모듈만 불러올 수 있다.", fill="black", font=("나눔바른펜", 20 , "bold"))
text_15=canvas_15_2.create_text(385, 450, text="- 파이썬 라이브러리 : 파이썬을 설치할 때 자동으로 ", fill="black", font=("나눔바른펜", 20 , "bold"))
text_15=canvas_15_2.create_text(430, 480, text="                     설치되는 파이썬 모듈 (= 표준모듈)", fill="black", font=("나눔바른펜", 20 , "bold"))

# chapter_11_frame canvas_3 정보
canvas_15_3=Canvas(chapter_11_frame, width=1000, height=700, bg="#c8e9f3")
canvas_15_3.create_rectangle(0,30,1000,50, fill="#124e8c", outline="#124e8c", width=7)
text_15=canvas_15_3.create_text(440, 100, text="✔ 모듈 예시", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
photo_15_2=canvas_15_3.create_image(440, 360, image=chpater_11_2)

# chapter_11_frame canvas_4 정보
canvas_15_4=Canvas(chapter_11_frame, width=1000, height=700, bg="#c8e9f3")
text_15=canvas_15_4.create_text(440, 50, text="✔ 패키지(package)", fill="#0e2e50", font=("나눔바른펜", 30 , "bold"))
canvas_15_4.create_rectangle(170, 190, 710, 290, fill="white", outline="#124e8c", width=5)
text_15=canvas_15_4.create_text(440, 100, text="= 패키지 : 모듈의 집합 (= 폴더)", fill="#0e2e50", font=("나눔바른펜", 20 , "bold"))
text_15=canvas_15_4.create_text(440, 150, text="- 모듈을 주제별로 분리할 때 주로 사용", fill="black", font=("나눔바른펜", 20 , "bold"))
text_15=canvas_15_4.create_text(440, 220, text="- from 패키지명.모듈명 import 함수", fill="#124e8c", font=("나눔바른펜", 20 , "bold"))
text_15=canvas_15_4.create_text(425, 260, text="- from 패키지명.모듈명 import *", fill="#124e8c", font=("나눔바른펜", 20 , "bold"))
photo_15_3=canvas_15_4.create_image(440, 440, image=chpater_11_3)
text_14=canvas_15_4.create_text(440, 610, text="모두 완료했습니다. 수고하셨습니다! :)", fill="#0f4175", font=("나눔바른펜", 15 , "bold"))

chapter_11_canvas_list=[]
chapter_11_canvas_list.append(canvas_15_1)
chapter_11_canvas_list.append(canvas_15_2)
chapter_11_canvas_list.append(canvas_15_3)
chapter_11_canvas_list.append(canvas_15_4)

#--------------------------------------

exit_btn_15=Button(chapter_11_frame, text="EXIT", width=7, height=1, font=("DungGeunMo", 26 , "bold"), fg="white", bg="#154e8c", command=lambda:transport_exit_j(chapter_11_frame, main_menu_frame, chapter_11_canvas_list))
exit_btn_15.place(x=0, y=0)

Quiz_btn_15=Button(chapter_11_frame, text="Quiz", width=7, height=1, font=("DungGeunMo", 26 , "bold"), bg="#ffe760", command=lambda:transport(chapter_11_frame, quiz_menu_frame))
Quiz_btn_15.place(x=860, y=0)

pre_btn_15=Button(chapter_11_frame, text="◀ BACK", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_chapter_list_back(chapter_11_canvas_list[j], chapter_11_canvas_list[j-1]))
pre_btn_15.place(x=150, y=654)

next_btn_15=Button(chapter_11_frame, text="NEXT ▶", width=7, height=1, font=("DungGeunMo", 20 , "bold"), fg="white", bg="#2a6fb6", command=lambda:transport_chapter_list_next(chapter_11_canvas_list[j], chapter_11_canvas_list[j+1]))
next_btn_15.place(x=886, y=654)

title_label_15=Label(chapter_11_frame,  text="CHAPTER 11 : 모듈", font=("DungGeunMo", 33 , "bold"), bg="white", padx=5, pady=5)
title_label_15.place(x=150,y=0)

date_label_15=Label(chapter_11_frame, text=time.strftime('%Y.%m.%d', time.localtime(time.time())), font=("DungGeunMo", 18), bg="white", padx=5, pady=5)
date_label_15.place(x=720, y=18)

#------------------------------------------------------------------------------------------------------------------------------------------------------------

window.mainloop()