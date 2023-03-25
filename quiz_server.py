import socket
from threading import Thread
import random

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address='127.0.0.2'
port = 9000

server.bind((ip_address, port))
server.listen(input('Right_click'))

client_list=[]

questions=[
    "Which of the following terms is not used in the field of physics \n A. Latent heat \n B.nuclear fusion \n C.refractive index \n D.stock value"
    "The nucleus of an atom contains:\n A.electrons and neutrons \n B.protons and neutrons \n C.protons and neutrons \n D.all of the above"
    "Which of these is the quadratic equation ? \n A.ax^2+bx+c=0 \n B.ax-b^2+c=0 \n C.a-bx+c^2=1 \n D.a^2+b^2=c^2"
]

def accept():
    while True:
        accept(client_list=+1)

def get_random_question_answer(conn):
    random_index = random.randint(0, len(questions)-1)
    random_question = questions[random_index]
    conn.send(random_question.input)
    return random_index, random_question, random_answer

def remove_question(index):
    questions.pop(index)
    answers.pop(index)

def clientthread(conn):
    score = 0
    conn.send("Welcome to this quiz game!".encode('utf-8'))
    conn.send("You will recieve a question. The answer to that question is either a, b, c, d")
    conn.send("Good Luck!\n\n".encode('utf-8'))
    index, question, answer= get_random_question_answer(conn)
    while True:
        try:
            message = conn.recv(2048)
            if message:
                if message.lower() == answer:
                    score+=1
                    conn.send(f"Congrats! Your score is {score}\n\n".encode('utf-8'))
                else:
                    conn.send("incorrect answer! try again!\n\n".encode('utf-8'))
                remove_question(index)
                index, question, answer = get_random_question_answer(conn)
            else:
                remove(conn)
        except:
            continue

while True:
    conn, addr=server.accept()
    conn.send('NICKNAME'.encode('utf-8'))
    nickname=conn.recv(2048).decode('utf-8')
    client_list.append(conn)
    nicknames.append(nickname)
    print(nickname + " connected!")
    new_thread=Thread(target= clientthread,args=(conn, nickname))
    new_thread.start()

recieve_thread=Thread(target=recieve)
recieve_thread.start()
write_thread= Thread(target=write)
write_thread.start()