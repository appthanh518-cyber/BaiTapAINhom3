# LOCAL SEARCH & HYBRID ADAPTIVE LOCAL SEARCH

## 1. Local Search

Local Search là thuật toán tìm kiếm cục bộ, bắt đầu từ một trạng thái ban đầu và liên tục tìm kiếm các trạng thái lân cận để cải thiện chất lượng lời giải.

**Quy trình hoạt động:**
- Khởi tạo trạng thái ban đầu.
- Sinh các trạng thái lân cận.
- Đánh giá và lựa chọn trạng thái tốt hơn.
- Tiếp tục tìm kiếm cho đến khi đạt điều kiện dừng.

**Hạn chế:**
- Dễ mắc kẹt tại cực trị địa phương.
- Khả năng khám phá không gian tìm kiếm còn hạn chế.
- Có thể dừng tại một lời giải chưa tối ưu.
- Hiệu quả phụ thuộc nhiều vào trạng thái khởi tạo và chiến lược lựa chọn lân cận.

## 2. Hybrid Adaptive Local Search

Local Search cơ bản có ưu điểm về sự đơn giản và tốc độ, tuy nhiên khả năng tìm kiếm có thể bị hạn chế khi gặp những vùng không gian có nhiều cực trị địa phương.

Vì vậy, Hybrid Adaptive Local Search được xây dựng nhằm kết hợp và điều chỉnh chiến lược tìm kiếm trong quá trình thực hiện.

Mục tiêu chính:
- Hạn chế tình trạng mắc kẹt tại cực trị địa phương.
- Tăng khả năng khám phá không gian trạng thái.
- Cải thiện chất lượng lời giải.
- Nâng cao khả năng thích nghi với từng giai đoạn tìm kiếm.

## 3. So sánh hai thuật toán

| Tiêu chí | Local Search | Hybrid Adaptive Local Search |
|---|---|---|
| Cực trị địa phương | Dễ mắc kẹt | Hướng đến hạn chế |
| Khám phá không gian | Hạn chế | Tăng cường |
| Khả năng thích nghi | Thấp | Cao hơn |
| Chất lượng lời giải | Có thể chưa tối ưu | Hướng đến lời giải tốt hơn |
| Chiến lược tìm kiếm | Cơ bản | Kết hợp và điều chỉnh |
| Khả năng tiếp tục tìm kiếm | Có thể dừng sớm | Hướng đến giảm tình trạng dừng sớm |

## 4. Source Code

| File | Nội dung |
|---|---|
| `Local_Search.py` | Cài đặt thuật toán Local Search cơ bản. |
| `Hybrid Adaptive Local Search.py` | Cài đặt thuật toán Hybrid Adaptive Local Search. |

## 5. Cách chạy

**Local Search:**

```bash
python "Local_Search.py"
```

**Hybrid Adaptive Local Search:**

```bash
python "Hybrid Adaptive Local Search.py"
```
