import openai

# GPT-3.5 modelining API kalit so'zini o'rnating
api_key = "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"

# OpenAI API-ga ulanish
openai.api_key = api_key

# Savolni berish
question = "List the 10 largest countries by land area"

# ChatGPT ga so'rov yuborish
response = openai.Completion.create(
    engine="text-davinci-003",  # Foydalanmoqchi bo'lgan model (masalan, "text-davinci-003")
    prompt=question,
    max_tokens=1000,  # Javobda maksimal belgi soni
    n=1,  # Nechta javob variantini qaytarish (faqat 1 ta)
    stop=None,  # Javobni to'xtatish uchun so'zlarni kiritish (masalan, "Qiziqarli bo'lmang", "Yana bir savolim bor", ...)
)
print(response)

# Javobni olish
answer = response.choices[0].text.strip()

# Javobni chop etish
print("ChatGPT javobi:", answer)