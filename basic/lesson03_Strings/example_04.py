# --- TRƯỜNG HỢP 1: Gán lại biến (Không dùng để định nghĩa mutable/immutable) ---
my_list = [1, 2, 3]
print(f"List ban đầu: {my_list} | Ô nhớ: {hex(id(my_list))}")

my_list = [] # Bạn đang tạo ra một chiếc hộp rỗng mới tinh!
print(f"Sau khi gán = []: {my_list} | Ô nhớ: {hex(id(my_list))} -> (Địa chỉ THAY ĐỔI)")


# --- TRƯỜNG HỢP 2: Sửa đổi tại chỗ (Đây mới là bằng chứng của MUTABLE) ---
my_list2 = [1, 2, 3]
print(f"\nList 2 ban đầu: {my_list2} | Ô nhớ: {hex(id(my_list2))}")

my_list2.clear() # Xóa sạch phần tử bên trong chiếc hộp cũ
print(f"Sau khi .clear(): {my_list2} | Ô nhớ: {hex(id(my_list2))} -> (Địa chỉ GIỮ NGUYÊN!)")
