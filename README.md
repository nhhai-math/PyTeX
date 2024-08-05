
# PyTeX

**Liên hệ:**  
Nguyễn Hoàng Hải (hoanghai@hcmut.edu.vn)  
Hoàng Trọng Tấn (httandayonline@gmail.com)

`PyTeX` là một thư viện Python được thiết kế để hỗ trợ xử lý và trích xuất thông tin từ các tệp LaTeX (`.tex`), đặc biệt khi sử dụng với gói `ex_test.sty`. Thư viện này giúp đơn giản hóa việc tạo ngân hàng câu hỏi, trích xuất nội dung, và thực hiện nhiều tác vụ liên quan khác trong quá trình soạn thảo tài liệu.

## Cài đặt

Để cài đặt `PyTeX`, bạn có thể sử dụng lệnh `pip` sau:

```bash
pip install git+https://github.com/nhhai-math/PyTeX.git
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
