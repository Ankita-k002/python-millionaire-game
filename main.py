questions=[
 ["Who is ShahRukh Khan?","WWE Wrestler","Plumber","Actor","Astronaut",3],  # 3 is the index of the correct answer form the list 
 ["What is the Capital of France?","Berlin","Paris","Rome","London",2],
 ["How many states are there in India?","27","28","29","7",2], 
 ["What is the largest planet in our solar system?", "Earth", "Mars", "Jupiter", "Saturn", 3],
 ["Who wrote 'Romeo and Juliet'?", "Charles Dickens", "William Shakespeare", "Mark Twain", "Leo Tolstoy", 2],
 ["What is the boiling point of water at sea level?", "90°C", "100°C", "80°C", "120°C", 2],
 ["Which is the fastest land animal?", "Cheetah", "Lion", "Tiger", "Horse", 1],
 ["What is the currency of Japan?", "Yuan", "Won", "Yen", "Dollar", 3],
 ["Name of the Parliament of Afghanistan?", "Majlis","Congress","Senate","Shora",4],
 ["Pitch is the playing area of which game?","Ragbi","Badminton","Kho-Kho","Kabadi",1],

]

prizes=[500,3000,6000,9000,12000,15000,18000,21000,25500,30000,40000,48000]
i=0

for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    a=int(input("Enter your answer: 1 for a, 2 for b,3 for c,4 for d: "))
    if (question[5]==a):
        print("Correct Answer")
        i+=1
    else:
        print(f"Incorrect, the correct answer is {question[5]}")
        print("Better luck newxt time")
        break
print(f"You won {prizes[i]}")
