
# PyTeX

**Liên hệ:**  
Nguyễn Hoàng Hải, Trường Đại học Bách Khoa - ĐHQG-HCM, email: hoanghai@hcmut.edu.vn

Hoàng Trọng Tấn, email: httandayonline@gmail.com

Nhóm trao đổi: https://www.facebook.com/groups/pytex

`PyTeX` là một thư viện Python được thiết kế để hỗ trợ xử lý và trích xuất thông tin từ các tệp LaTeX (`.tex`), đặc biệt khi sử dụng với gói `ex_test.sty`. Thư viện này giúp đơn giản hóa việc tạo ngân hàng câu hỏi, trích xuất nội dung, và thực hiện nhiều tác vụ liên quan khác trong quá trình soạn thảo tài liệu.

## Cài đặt

Để cài đặt `PyTeX`, bạn có thể sử dụng lệnh `pip` thông qua `git` với dòng lệnh sau trên Terminal:

```bash
pip install git+https://github.com/nhhai-math/PyTeX.git
```
Cách khác là tải tệp `MyTeX.py` về theo đường dẫn sau rồi lưu tệp này chung với `main.py` đang soạn.
```bash
https://github.com/nhhai-math/PyTeX/blob/main/PyTeX/PyTeX.py
```
## Lọc câu hỏi

Dưới đây là ví dụ minh họa cách sử dụng `PyTeX` để lọc câu hỏi từ tệp dữ liệu `.tex`

### Tìm kiếm theo ID câu hỏi
```python
import PyTeX

# Đường dẫn đến tệp LaTeX của bạn
file_path = 'DuongDan/TepCuaBan.tex'

# Đọc nội dung của tệp LaTeX
with open(file_path, 'r', encoding='utf-8') as file:
    data = file.read()

# Tạo ngân hàng câu hỏi từ dữ liệu đã đọc
questions_bank = PyTeX.get_bank(data)

# Lọc câu hỏi theo một ID cụ thể
ID = "1D7N1-4"
questions_found = questions_bank.find_by_id(ID)
print(questions_found)
```
Một vài cú pháp tìm kiếm theo ID:

- `ID = "1D7N1-[45]"`: Tìm câu hỏi với ID có dạng Toán là 4 hoặc 5.
- `ID = "1D7N1-."`: Tìm tất cả câu hỏi với dạng bất kỳ.
- `ID = "1D...-."`: Tìm tất cả câu hỏi lớp 11 phần Đại số.
### Tìm kiếm theo loại câu hỏi (tự luận, trả lời ngắn, đúng/sai, trắc nghiệm 4 phương án)
```python
import PyTeX

# Đường dẫn đến tệp LaTeX của bạn
file_path = 'DuongDan/TepCuaBan.tex'

# Đọc nội dung của tệp LaTeX
with open(file_path, 'r', encoding='utf-8') as file:
    data = file.read()

# Tạo ngân hàng câu hỏi từ dữ liệu đã đọc
questions_bank = PyTeX.get_bank(data)

#Lọc câu hỏi theo loại câu hỏi
loai = "choice"
questions_found = questions_bank.find_by_type(loai)
print(questions_found)
```

Cú pháp tìm kiếm theo loại câu hỏi:

- `loai = "longans"`: Tìm câu hỏi tự luận.
- `loai = "shortans"`: Tìm câu hỏi trả lời ngắn.
- `loai = "choiceTF"`: Tìm câu hỏi đúng/sai.
- `loai = "choice"`: Tìm câu hỏi trắc nghiệm 4 phương án.
