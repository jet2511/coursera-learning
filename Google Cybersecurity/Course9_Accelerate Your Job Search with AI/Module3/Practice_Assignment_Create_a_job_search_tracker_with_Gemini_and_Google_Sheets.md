# Practice Assignment: Create a Job Search Tracker with Gemini and Google Sheets

## 📌 Tóm Tắt Bài Tập Thực Hành
- **Mục tiêu:** Tạo và tùy chỉnh bảng theo dõi quá trình tìm việc (*Job Search Tracker*) trên Google Sheets bằng cách sử dụng mẫu (*template*) kết hợp với sự hỗ trợ của Gemini AI.
- **Quy trình thực hiện:**
  1. Mở [Job Search Tracker Template](https://docs.google.com/spreadsheets/d/1JaZnPViRdu6EyMMOZC5Sltg-Y6lCTpjhYcjJ8AIfxQ0/template/preview) và chọn *Use Template* để tạo bản sao cá nhân.
  2. Chọn 1 vị trí tuyển dụng thực tế và điền thông tin cơ bản (Tên công ty, vị trí, link JD).
  3. Sử dụng Gemini để tóm tắt mô tả công việc (JD) trong 2–3 câu với prompt:
     - `Summarize the following job description in 2–3 sentences: [dán nội dung JD]`
     - Copy kết quả vào cột **"Job Description Notes"**.
  4. Nghiên cứu thông tin công ty (Website, LinkedIn, tin tức) và dùng Gemini trích xuất điểm nổi bật với prompt:
     - `Extract the main points about [Tên công ty]’s recent projects from the following article: [dán bài báo]`
     - Copy kết quả vào cột **"Company Research Notes"**.
  5. Lưu các prompt hiệu quả vào *AI Prompt Library*.
  6. Lưu bảng theo dõi vào *Job Search Portfolio* để duy trì và cập nhật liên tục.

---

## 📝 Gợi Ý Trả Lời Chi Tiết (Nộp Bài Coursera)

### Question 1:
> **Prompt:** Customize the tracker template and continue to use it in your ongoing job search. Thinking about your personal job search style and the types of roles you're targeting, what's one specific customization you might make to the tracker? Why do you feel this personalization will make the tracker even more effective for you?

#### 💡 Gợi ý trả lời (Tiếng Anh - Dùng để nộp bài):
One specific customization I would make to the job search tracker is adding a dedicated **"Technical Stack & Required Tools"** column alongside a **"Skill Match & Gap Analysis"** column.

Since I am targeting roles in Cybersecurity (such as Entry-Level Cybersecurity Analyst or SOC Analyst), job postings often emphasize specific technical tools, operating systems, and security frameworks (e.g., Splunk, Wireshark, Linux, Python, ISO 27001). Adding these columns allows me to:
1. Quickly map out the exact security toolsets and requirements for each position.
2. Identify any technical skill gaps that I need to quickly brush up on before an interview.

This personalization makes the tracker significantly more effective for me because cybersecurity roles vary widely in technical scope. Tracking specific toolsets ensures I focus my preparation time efficiently and tailor my interview responses to match the hiring team's exact tech stack.

---

### Question 2:
> **Prompt:** Now that you're more familiar with AI's capabilities, can you envision other ways AI could help you populate or maintain your job search tracker, beyond the examples in this activity?

#### 💡 Gợi ý trả lời (Tiếng Anh - Dùng để nộp bài):
Beyond summarizing job descriptions and extracting company research points, I can envision several advanced ways AI could help populate and maintain my job search tracker:

1. **Tailored Interview Question Generation:** I can provide Gemini with the summarized JD and company research notes from my tracker and ask it to predict 5–10 customized technical and behavioral interview questions specific to that role.
2. **Automated Follow-Up & Thank-You Drafts:** Based on the interview dates and contact details logged in my tracker, I can prompt Gemini to generate personalized follow-up emails and post-interview thank-you notes.
3. **Automated Data Population via Apps Script:** Using Google Apps Script connected with the Gemini API, I could automatically parse saved job webpage links or interview invitation emails to auto-fill new rows in Google Sheets, eliminating manual data entry.
4. **Salary & Industry Benchmarking:** I can ask Gemini to analyze market salary ranges and compensation packages for specific job titles and locations, helping me evaluate and negotiate job offers more strategically.
