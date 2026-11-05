# LOCAL SEARCH

## 1. Local Search

Cài đặt thuật toán tìm kiếm cục bộ (Local Search), sử dụng trạng thái lân cận để tìm kiếm và cải thiện lời giải hiện tại.

Quá trình thực hiện:

- Khởi tạo trạng thái ban đầu.
- Sinh các trạng thái lân cận.
- Đánh giá và lựa chọn trạng thái tốt hơn.
- Lặp lại quá trình tìm kiếm cho đến khi đạt điều kiện dừng.

## 2. Hybrid Adaptive Local Search

Cài đặt thuật toán tìm kiếm cục bộ kết hợp cơ chế thích nghi (Hybrid Adaptive Local Search), nhằm cải thiện khả năng tìm kiếm và hạn chế tình trạng mắc kẹt tại cực trị địa phương.

Thuật toán tập trung vào:

- Khám phá các trạng thái lân cận.
- Điều chỉnh chiến lược tìm kiếm theo quá trình thực hiện.
- Cải thiện chất lượng lời giải.
- Tăng khả năng thoát khỏi vùng tìm kiếm không hiệu quả.

## 3. Source Code

| File                              | Nội dung                                 |
| --------------------------------- | ---------------------------------------- |
| `Local Sreach.py`                 | Thuật toán Local Search cơ bản.          |
| `Hybrid Adaptive Local Search.py` | Thuật toán Hybrid Adaptive Local Search. |

## 4. Cách chạy

```bash
python "Local Sreach.py"
```

```bash
python "Hybrid Adaptive Local Search.py"
```


