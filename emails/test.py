
# coding=utf-8
import smtplib
from email.mime.text import MIMEText

msg_from = '2639049615@qq.com'  # 发送方邮箱
passwd = 'fbalrvvagtexdijg'  # 填入发送方邮箱的授权码
msg_to = '529635881@qq.com'  # 收件人邮箱

subject = "python1709邮件"  # 主题
content = '<html><body><h1>Hello</h1>' \
    '<p>send by <a href="http://www.python.org">Python</a><img src="test.png"/>...</p>' \
    '</body></html>'# 正文
msg = MIMEText(content,'html','utf-8')
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to
try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 邮件服务器及端口号
    s.login(msg_from, passwd)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print("发送成功")
except smtplib.SMTPException as e:
    print("发送失败")
finally:
    s.quit()