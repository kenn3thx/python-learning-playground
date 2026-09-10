# 1. Khởi tạo một danh sách (List) ban đầu
my_list = [1, 2, 3]
print(f"1. Danh sách ban đầu: {my_list}      | Địa chỉ ô nhớ (Hex): {hex(id(my_list))}")

# 2. Thay đổi phần tử đầu tiên (Sửa số 1 thành số 99)
my_list[0] = 99
print(f"2. Sau khi sửa phần tử: {my_list}     | Địa chỉ ô nhớ (Hex): {hex(id(my_list))}")

# 3. Thêm một phần tử mới vào cuối danh sách
my_list.append(4)
print(f"3. Sau khi thêm phần tử: {my_list}  | Địa chỉ ô nhớ (Hex): {hex(id(my_list))}")
