
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

## Ví dụ sử dụng

Dưới đây là ví dụ minh họa cách sử dụng `PyTeX` để làm việc với các tệp LaTeX:

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

# Kiểm tra và hiển thị nội dung của câu hỏi đầu tiên trong danh sách tìm được
if questions_found:
    question = questions_found[0]
    print(question['content'])
else:
    print("Không tìm thấy câu hỏi với ID này.")
```

Một vài cú pháp tìm kiếm theo ID:

- `ID = "1D7N1-[45]"`: Tìm câu hỏi với ID có dạng 4 hoặc 5.
- `ID = "1D7N1-."`: Tìm tất cả câu hỏi với định dạng toán.
- `ID = "1D...-."`: Tìm tất cả câu hỏi lớp 11 phần Đại số.
