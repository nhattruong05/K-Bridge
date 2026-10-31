import json
import os
import random

project_name = "K-Bridge"
student_name = "Korean Learner"

file_name = "vocabulary.json"

print("Welcome to", project_name)
print("Your Korean learning journey starts here!")

if os.path.exists(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        vocabulary = json.load(file)
else:
    vocabulary = {
        "강의실" : "Phòng học",
        "도서관" : "Thư viện",
        "학교" : "Trường học",
        "교실" : "Phòng học",
        "친구" : "Bạn bè"
    }

print("Từ vựng hiện có là ", len(vocabulary), "từ")

def save_vocabulary():
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(vocabulary, file, ensure_ascii=False, indent=4)

def search():
    word = input (
            "Nhập từ tiếng Hàn (Nếu muốn thoát, vui lòng nhập exit): "
        ).strip()

    if word.upper() == "EXIT" :
            print("Tạm biệt!")

    elif word in vocabulary:
            print("Nghĩa tiếng Việt: ", vocabulary[word])

    else :
        print(word ,"chưa có trong từ điển")
        tmp = input(
            "Bạn muốn thêm từ này vào từ điển không? (Có/Không) : "
        ).strip()

        if tmp.upper() in ("CÓ", "CO"):
            meaning = input("Nghĩa tiếng Việt: ").strip()
            if meaning:
                vocabulary[word] = meaning
                save_vocabulary()
                print("Đã thêm từ mới!")
            else:
                print("Nghĩa không được để trống.")
        else: 
                print("Bạn chưa thêm từ mới!")

def List():
    print("\n=== TỪ VỰNG CỦA BẠN ===")
    for index, word in enumerate(vocabulary, start=1):
        print(index,".", word, ":", vocabulary[word])
        
    print("\n")

def add():
    while True:
        word = input("Nhập từ tiếng Hàn bạn muốn thêm: ").strip()
        meaning = input("Nhập nghĩa tiếng Việt: ").strip()
        
        if not word or not meaning:
            print("Từ vựng và nghĩa không được để trống!")
            continue
        if word in vocabulary:
            print("Từ này đã có trong từ điển!")
            continue

        vocabulary[word] = meaning
        save_vocabulary()
        print("Đã thêm từ mới!")
        choice = input(
            "Bạn muốn tiếp tục thêm từ vựng mới không? (Có/Không): "
        ).strip()
        if choice.upper() in ("CÓ", "CO"):
            continue
        else:
            break
    
def quiz():
    words = list(vocabulary.keys())

    while True:
        try:
            k = int(input("Số từ bạn muốn kiểm tra: "))

            if k <= 0 :
                print("Số từ cần kiểm tra phải lớn hơn 0")
                continue

            elif k > len(vocabulary):
                print("Số từ trong từ điển không đủ!")
                continue
                
            else: 
                questions = random.sample(words, k)
                score = 0
                wrong = []
                
                for index, word in enumerate(questions, start=1):
                    print(index, ". Từ tiếng Hàn:", word)
                    answer = input("Nhập nghĩa tiếng Việt: ").strip()
                    if answer.lower() == vocabulary[word].lower():
                        score += 1
                    else:
                        wrong.append((word, vocabulary[word]))

                print("Số câu đúng: ", score)
                print("Số câu sai: ", len(wrong))

                if wrong:
                    print("\nCác từ bạn trả lời sai:")
                    for word, meaning in wrong:
                        print(word, ":", meaning)

                else:
                    print("Tuyệt vời! Bạn đã trả lời đúng tất cả!")
                    
                tmp = input("Bạn muốn tiếp tục hay dừng? (Tiếp tục/ Dừng) ")

                if tmp.upper() in ("TIẾP TỤC", "TIEP TUC"):
                    continue
                else : break

        except ValueError:
            print("Vui lòng nhập một số nguyên!")

def main():
    while True:
        option = input("Chọn chức năng (Search/Add/List/Exit/Quiz): ").strip()

        if option.upper() == "SEARCH": search()

        elif option.upper() == "ADD": add()

        elif option.lower() == "list": List()
        
        elif option.upper() == "QUIZ": quiz()

        elif option.upper() == "EXIT":
            print("Tạm biệt!")
            break       

        else: 
            print("Bạn đã nhập sai!")

if __name__ == "__main__":
    main()



            
