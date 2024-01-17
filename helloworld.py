import datetime

def add_entry():
    entry = input("Nhập nội dung ghi chú hoặc nhật ký của bạn: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("nhật_ký.txt", "a",encoding="utf-8") as file:
        file.write(f"{timestamp}: {entry}\n")
    print("Ghi chú đã được thêm thành công!")

def view_entries():
    with open("nhật_ký.txt", "r",encoding="utf-8") as file:
        entries = file.readlines()
        for entry in entries:
            print(entry.strip())

while True:
    print("1. Thêm ghi chú")
    print("2. Xem ghi chú")
    print("3. Thoát")
    choice = input("Nhập lựa chọn của bạn (1-3): ")
    
    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")