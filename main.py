#Bài 1 ứng dụng Quản Lí Sinh Viên (CRUD cơ bản)
import csv

def dinh_dang_ten(text:str) -> str:
    return text.strip().title()
def dinh_dang_nganh(text:str) -> str:
    return text.strip().title()

def doc_file_csv():
    student = []
    try:
        with open('student.csv', mode='r',newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                student.append({
                    'MSSV': row['MSSV'],
                    'Họ Tên': dinh_dang_ten(row['Họ Tên']),
                    'Tuổi': int(row['Tuổi']),
                    'Ngành': dinh_dang_nganh(row['Ngành'])
                })
    except FileNotFoundError:
        print(f"File {'student.csv'} không tồn tại.")
    return student
def save_to_csv(students):
    with open('student.csv', mode='w', newline='', encoding='utf-8') as f:
        fieldnames = ['MSSV', 'Họ Tên', 'Tuổi', 'Ngành']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

def them_sinh_vien(students):
    mssv = input("Nhập MSSV: ").strip()
    for sv in students:
        if sv['MSSV'] == mssv:
            print("MSSV đã tồn tại. Không thể thêm sinh viên.")
            return
    name = dinh_dang_ten(input("Nhập Họ Tên: "))
    age = int(input("Nhập Tuổi: ")) 
    major = dinh_dang_nganh(input("Nhập Ngành: "))
    students.append({'MSSV': mssv, 'Họ Tên': name, 'Tuổi': age, 'Ngành': major})
    print("Thêm sinh viên thành công.")
def cap_nhat_sinh_vien(students):
    mssv = input("Nhập MSSV của sinh viên cần cập nhật: ").strip()
    for sv in students:
        if sv['MSSV'] == mssv:
            print(f"Thông tin hiện tại: {sv}")
            name = dinh_dang_ten(input("Nhập Họ Tên mới (bỏ trống để giữ nguyên): ") or sv['Họ Tên'])
            age_input = input("Nhập Tuổi mới (bỏ trống để giữ nguyên): ")
            age = int(age_input) if age_input else sv['Tuổi']
            major = dinh_dang_nganh(input("Nhập Ngành mới (bỏ trống để giữ nguyên): ") or sv['Ngành'])
            sv.update({'Họ Tên': name, 'Tuổi': age, 'Ngành': major})
            print("Cập nhật sinh viên thành công.")
            return
    print("Không tìm thấy sinh viên với MSSV đã nhập.")
def xoa_sinh_vien(students):
    mssv = input("Nhập MSSV của sinh viên cần xóa: ").strip()
    for sv in students:
        if sv['MSSV'] == mssv:
            students.remove(sv)
            print("Xóa sinh viên thành công.")
            return
    print("Không tìm thấy sinh viên với MSSV đã nhập.")
def tim_sinh_vien(students):
    keyword = input("Nhập từ khóa tìm kiếm (MSSV hoặc Họ Tên): ").strip().lower()
    results = [sv for sv in students if keyword in sv['MSSV'].lower() or keyword in sv['Họ Tên'].lower()]
    if results:
        print("Kết quả tìm kiếm:")
        for sv in results:
            print(sv)
    else:
        print("Không tìm thấy sinh viên nào.")
def hien_thi_danh_sach(students):
    if not students:
        print("Danh sách sinh viên trống.")
        return
    print(f"{'MSSV':<10} {'Họ Tên':<30} {'Tuổi':<5} {'Ngành':<20}")
    print("-" * 65)
    for sv in students:
        print(f"{sv['MSSV']:<10} {sv['Họ Tên']:<30} {sv['Tuổi']:<5} {sv['Ngành']:<20}")
def menu():
    students = doc_file_csv()
    if not students: 
        students = doc_file_input()
        if students:  
            save_to_csv(students)
    while True:
        print("\nQuản Lí Sinh Viên")
        print("1. Thêm Sinh Viên")
        print("2. Cập Nhật Sinh Viên")
        print("3. Xóa Sinh Viên")
        print("4. Tìm Kiếm Sinh Viên")
        print("5. Hiển Thị Danh Sách Sinh Viên")
        print("6. Lưu và Thoát")
        choice = input("Chọn một tùy chọn (1-6): ").strip()
        if choice == '1':
            them_sinh_vien(students)
        elif choice == '2':
            cap_nhat_sinh_vien(students)
        elif choice == '3':
            xoa_sinh_vien(students)
        elif choice == '4':
            tim_sinh_vien(students)
        elif choice == '5':
            hien_thi_danh_sach(students)
        elif choice == '6':
            save_to_csv(students)
            print("Dữ liệu đã được lưu. Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    menu()
