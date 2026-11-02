import json
import os
import random

project_name = "K-Bridge"
student_name = "Korean Learner"

file_name = "kbridge_vocabulary.json"

default_vocabulary = {
    "Trường học": {
        "강의실": "Phòng học",
        "도서관": "Thư viện",
        "학교": "Trường học",
        "교실": "Phòng học",
        "친구": "Bạn bè"
    },
    "Đời sống": {
        "가족": "Gia đình",
        "음식": "Món ăn"
    },
    "Công việc": {
        "회사": "Công ty"
    }
}

if os.path.exists(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        vocabulary = json.load(file)
else:
    vocabulary = default_vocabulary.copy()

print("Welcome to", project_name)
print("Your Korean learning journey starts here!")

def save_vocabulary():
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(vocabulary, file, ensure_ascii=False, indent=4)

def show_topics():
    print("\n=== CÁC CHỦ ĐỀ HIỆN CÓ ===")

    topics = list(vocabulary.keys())

    for index, topic in enumerate(topics, start=1):
        print(index, ".", topic)
    
    return topics

def search():
    word = input (
            "Nhập từ tiếng Hàn (Nhập exit để thoát): "
        ).strip()

    if word.upper() == "EXIT" :
            print("Tạm biệt!")
            return
    
    for topic, words in vocabulary.items():
        if word in words:
            print("Chủ đề: ", topic)
            print("Nghĩa tiếng Việt: ", words[word])

    print(word, "chưa có trong từ điển.")

    choice = input(
        "Bạn muốn thêm từ này vào từ điển không? (Có/Không): "
    ).strip()

    if choice.upper() in ("CÓ", "CO"):
            topics = show_topics()

            try:
                option = int(input("Chọn chủ đề: "))

                if 1 <= option <= len(topics):
                    topic = topics[option - 1]
                    meaning = input("Nhập nghĩa tiếng Việt: ").strip()

                    if meaning:
                        vocabulary[topic][word] = meaning
                        save_vocabulary()
                        print("Đã thêm từ mới!")
                    else:
                        print("Nghĩa không được để trống.")
                
                else:
                    print("Chủ đề không hợp lệ!")

            except ValueError:
                print("Vui lòng nhập một số nguyên!")


def show_vocabulary():
    print("\n=== TỪ VỰNG CỦA BẠN ===")

    for topic, words in vocabulary.items():
        print("\n---", topic, "---")

        for index, (word, meaning) in enumerate(words.items(), start=1):
            print(index, ".", word, ":", meaning)
        
    print()

def add_topic():
    while True:
        new_topic = input("Nhập tên chủ đề mới: ").strip()

        if not new_topic:
            print("Chủ đề không được để trống")
            continue

        if new_topic in vocabulary:
            print("Chủ đề đã tồn tại")
            continue

        vocabulary[new_topic] = {}
        save_vocabulary()

        print("Đã thêm chủ đề thành công!")
        break

def add_vocabulary():
    while True:
        topics = show_topics()

        try:
            option = int(input("Chọn chủ đề (Nhập 0 để thoát): "))

            if option == 0:
                break

            if not 1 <= option <= len(topics):
                print("Bạn đã chọn chủ đề không hợp lệ!")
                continue

            topic = topics[option - 1]

            word = input("Nhập từ tiếng Hàn: ").strip()

            if not word:
                print("Từ vựng không được để trống!")
                continue
            
            if any(word in words for words in vocabulary.values()):
                print("Từ vựng đã tồn tại trong từ điển!")
                continue

            meaning = input("Nhập nghĩa tiếng Việt: ").strip()

            if not meaning:
                print("Nghĩa không được để trống!")
                continue

            vocabulary[topic][word] = meaning
            save_vocabulary()

            print("Đã thêm từ mới vào chủ đề", topic, "!")

        except ValueError:
            print("Vui lòng nhập số nguyên!")
    
def quiz():
    all_words = []

    for topic, words in vocabulary.items():
        for word, meaning in words.items():
            all_words.append((word, meaning))
    
    if not all_words:
        print("Từ điển chưa có từ vựng!")
        return

    while True:
        try:
            k = int(input("Số từ bạn muốn kiểm tra: "))

            if k <= 0 :
                print("Số từ cần kiểm tra phải lớn hơn 0")
                continue

            elif k > len(all_words):
                print("Số từ trong từ điển không đủ!")
                continue
                
            questions = random.sample(all_words, k)

            score = 0
            wrong = []
            
            for index, (word, meaning) in enumerate(questions, start=1):
                print(index, ". Từ tiếng Hàn:", word)

                answer = input("Nhập nghĩa tiếng Việt: ").strip()

                if answer.lower() == meaning.lower():
                    score += 1
                else:
                    wrong.append((word, meaning))

            print("Số câu đúng: ", score)
            print("Số câu sai: ", len(wrong))

            if wrong:
                print("\nCác từ bạn trả lời sai:")

                for word, meaning in wrong:
                    print(word, ":", meaning)

            else:
                print("Tuyệt vời! Bạn đã trả lời đúng tất cả!")
                
            choice = input(
                "Bạn muốn tiếp tục hay dừng? (Tiếp tục/ Dừng) "
                ).strip()

            if choice.upper() not in ("TIẾP TỤC", "TIEP TUC"):
                break

        except ValueError:
            print("Vui lòng nhập một số nguyên!")

def main():
    print("\nTổng số từ vựng: ", sum(
        len(words) for words in vocabulary.values()
    ))

    while True:
        print("\n========== K-BRIDGE ==========")
        print("1. Search")
        print("2. Add Vocabulary")
        print("3. List Vocabulary")
        print("4. Quiz")
        print("5. Add Topic")
        print("0. Exit")

        option = input("Chọn chức năng: ").strip()

        if option == "1": search()

        elif option == "2": add_vocabulary()

        elif option == "3": show_vocabulary()
        
        elif option == "4": quiz()

        elif option == "5": add_topic()

        elif option == "0":
            print("Tạm biệt! Hẹn gặp lại.")
            break       

        else: 
            print("Bạn đã nhập lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()



            
