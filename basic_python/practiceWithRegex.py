import re

def finding_Email(text): 
    email = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",text)
    print(email)


finding_Email("""Chào bạn, nếu bạn có bất kỳ câu hỏi nào, vui lòng liên hệ với chúng tôi qua email support@example.com.
Đối với các vấn đề kỹ thuật, bạn có thể gửi yêu cầu đến tech.team@company.org.
Nếu bạn đang tìm kiếm cơ hội hợp tác, hãy gửi email đến partner_sales@business.co.uk.
Ngoài ra, bộ phận nhân sự có thể được liên hệ qua hr-dept@enterprise.net.
Nếu bạn cần hỗ trợ khẩn cấp, hãy thử email cá nhân của tôi: john.doe1990@gmail.com hoặc alice_smith+help@yahoo.com.""")