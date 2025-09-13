# Chatbot Quán Cà Phê (Rule-Based)

## Giới thiệu

Dự án này là một chatbot rule-based cho quán cà phê, xây dựng bằng Python và Gradio. Chatbot trả lời các câu hỏi về menu, giờ mở cửa, địa chỉ, giá cả, dịch vụ, v.v.

## Yêu cầu hệ thống

- Python >= 3.7
- Các thư viện trong `requirements.txt` (Gradio, difflib)

## Cài đặt

1. Tải mã nguồn về máy.
2. Cài đặt thư viện:
   ```bash
   pip install -r requirements.txt
   ```

## Sử dụng

Chạy ứng dụng bằng lệnh:

```bash
python main.py
```

Giao diện web sẽ xuất hiện, bạn có thể nhập câu hỏi vào ô chat.

## Các rule (luật trả lời)

Chatbot sử dụng các rule cố định để trả lời:

| Từ khóa    | Trả lời                                                                          |
| ---------- | -------------------------------------------------------------------------------- |
| menu       | Quán có: cà phê đen, cà phê sữa, latte, cappuccino, trà đào, trà sữa, bánh ngọt. |
| giờ        | Quán mở từ 7h sáng đến 10h tối mỗi ngày.                                         |
| địa chỉ    | Số 1, Đường Võ Văn Ngân, P. Thủ Đức, TP. Hồ Chí Minh.                            |
| cà phê đen | Cà phê đen giá 25.000đ.                                                          |
| cà phê sữa | Cà phê sữa giá 30.000đ.                                                          |
| latte      | Latte giá 40.000đ.                                                               |
| cappuccino | Cappuccino giá 45.000đ.                                                          |
| trà đào    | Trà đào giá 35.000đ.                                                             |
| trà sữa    | Trà sữa giá 35.000đ.                                                             |
| bánh       | Quán có bánh ngọt các loại, giá từ 20.000đ đến 35.000đ.                          |
| wifi       | Quán có Wi-Fi miễn phí, pass sẽ in trên hóa đơn.                                 |
| ship       | Quán có dịch vụ giao hàng qua GrabFood và ShopeeFood.                            |

## Từ đồng nghĩa (synonyms)

Chatbot tự động ánh xạ các từ đồng nghĩa về từ chính để tăng độ chính xác:

| Từ đồng nghĩa | Từ chính   |
| ------------- | ---------- |
| thời gian     | giờ        |
| mấy giờ       | giờ        |
| hoạt động     | giờ        |
| ở đâu         | địa chỉ    |
| chỗ nào       | địa chỉ    |
| cafe          | cà phê     |
| cafe sữa      | cà phê sữa |
| coffee        | cà phê     |
| ship hàng     | ship       |
| giao hàng     | ship       |
| trà           | trà đào    |
| dessert       | bánh       |

## Quy tắc hoạt động

1. Nếu câu hỏi chứa từ khóa chính, chatbot trả lời theo rule.
2. Nếu không khớp, chatbot dùng fuzzy matching để gợi ý gần đúng.
3. Nếu vẫn không tìm thấy, chatbot sẽ trả lời gợi ý các chủ đề có thể hỏi.
4. Lịch sử hội thoại được lưu lại trên giao diện.

## Ví dụ sử dụng

- "Quán mở cửa lúc mấy giờ?" → Quán mở từ 7h sáng đến 10h tối mỗi ngày.
- "Có bánh không?" → Quán có bánh ngọt các loại, giá từ 20.000đ đến 35.000đ.
- "Ship hàng qua đâu?" → Quán có dịch vụ giao hàng qua GrabFood và ShopeeFood.
- "Wi-Fi pass là gì?" → Quán có Wi-Fi miễn phí, pass sẽ in trên hóa đơn.

## Giao diện

Ứng dụng sử dụng Gradio, giao diện web đơn giản gồm:

- Khung chat hiển thị hội thoại
- Ô nhập câu hỏi
- Nút gửi và nút xóa hội thoại

## Đóng góp

Mọi đóng góp vui lòng gửi pull request hoặc liên hệ qua email bên dưới.

## Liên hệ

- Email: your-email@example.com

## Giấy phép

Dự án phát hành theo giấy phép MIT.
