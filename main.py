import gradio as gr
from difflib import get_close_matches

rules = {
    "menu": "Quán có: cà phê đen, cà phê sữa, latte, cappuccino, trà đào, trà sữa, bánh ngọt.",
    "giờ": "Quán mở từ 7h sáng đến 10h tối mỗi ngày.",
    "địa chỉ": "Số 1, Đường Võ Văn Ngân, P. Thủ Đức, TP. Hồ Chí Minh.",
    "cà phê đen": "Cà phê đen giá 25.000đ.",
    "cà phê sữa": "Cà phê sữa giá 30.000đ.",
    "latte": "Latte giá 40.000đ.",
    "cappuccino": "Cappuccino giá 45.000đ.",
    "trà đào": "Trà đào giá 35.000đ.",
    "trà sữa": "Trà sữa giá 35.000đ.",
    "bánh": "Quán có bánh ngọt các loại, giá từ 20.000đ đến 35.000đ.",
    "wifi": "Quán có Wi-Fi miễn phí, pass sẽ in trên hóa đơn.",
    "ship": "Quán có dịch vụ giao hàng qua GrabFood và ShopeeFood."
}

# Từ đồng nghĩa → ánh xạ về từ chính
synonyms = {
    "thời gian": "giờ",
    "mấy giờ": "giờ",
    "hoạt động": "giờ",
    "ở đâu": "địa chỉ",
    "chỗ nào": "địa chỉ",
    "cafe": "cà phê",
    "cafe sữa": "cà phê sữa",
    "coffee": "cà phê",
    "ship hàng": "ship",
    "giao hàng": "ship",
    "trà": "trà đào",  # nếu chỉ nói "trà" → gợi ý trà đào
    "dessert": "bánh"
}

# Fallback gợi ý
available_keywords = ", ".join(rules.keys())

# Hàm xử lý chatbot
def chatbot_response(user_input, history=[], context=""):
    text = user_input.lower().strip()
    response = None

    # Thay từ đồng nghĩa thành từ chính
    for syn, target in synonyms.items():
        if syn in text:
            text = text.replace(syn, target)

    # 1. Tìm trực tiếp trong rules
    for keyword, ans in rules.items():
        if keyword in text:
            response = ans
            context = keyword
            break

    # 2. Fuzzy matching
    if response is None:
        keywords = list(rules.keys())
        matches = get_close_matches(text, keywords, n=1, cutoff=0.7)
        if matches:
            matched = matches[0]
            response = f"Bạn có muốn hỏi về '{matched}' không?\n{rules[matched]}"
            context = matched
        # else:
        #     # 3. Fallback
        #     if context:
        #         response = f"Bạn đang hỏi tiếp về '{context}':\n{rules[context]}"
        #     else:
        #         response = f"Xin lỗi, tôi chưa có thông tin cho câu hỏi này. Bạn có thể hỏi: {available_keywords}."
        else:
        # 3. Fallback (không lặp lại context cũ nếu không có gì gần đúng)
            response = f"Xin lỗi, tôi chưa có thông tin cho câu hỏi này. Bạn có thể hỏi: {available_keywords}."
            context = ""  # reset context để tránh lặp lại

    history.append((user_input, response))
    return history, history, context, ""

# Giao diện Gradio
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# ☕ Chatbot Quán Cà Phê (Rule-Based)")
    gr.Markdown("Hỏi tôi về **menu, giờ mở cửa, địa chỉ, giá cà phê, trà, bánh, ship hàng...**")

    chatbot = gr.Chatbot(height=400)
    with gr.Row():
        msg = gr.Textbox(placeholder="Nhập câu hỏi...", show_label=False, scale=8)
        send = gr.Button("Gửi", scale=2)
    clear = gr.Button("Xóa hội thoại")

    state = gr.State("")  # lưu ngữ cảnh

    send.click(chatbot_response, [msg, chatbot, state], [chatbot, chatbot, state, msg])
    msg.submit(chatbot_response, [msg, chatbot, state], [chatbot, chatbot, state, msg])
    clear.click(lambda: (None, None, "", ""), None, [chatbot, chatbot, state, msg], queue=False)

if __name__ == "__main__":
    demo.launch()
