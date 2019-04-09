import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

if __name__ == '__main__':
    fromaddr = '1655729589@qq.com'#发件人
    password = 'oqbkqqfrfzzidbfe'#授权码
    toaddrs = ['18788782150@163.com','hdj543@126.com']#收件人

    content = 'hello, this is email content.'#邮件内容
    textApart = MIMEText(content)

    #构建一个附件
    imageFile = 'C:\\Users\\hdj54\\Desktop\\小程序錢包開發進度.xlsx'
    imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
    imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)

    """
    # 构建第二个个附件
    pdfFile = 'E:\\100.png'
    pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
    pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)
    
    # 构建第三个个附件
    zipFile = 'E:\\100.png'
    zipApart = MIMEApplication(open(zipFile, 'rb').read())
    zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)
    
    """

    m = MIMEMultipart()
    m.attach(textApart)
    m.attach(imageApart)
#    m.attach(pdfApart)
#    m.attach(zipApart)
    m['Subject'] = '软件测试报告'#邮件标题

    #登录服务器
    try:
        server = smtplib.SMTP('smtp.qq.com')
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddrs, m.as_string())
        print('success')
        server.quit()
    except smtplib.SMTPException as e:
        print('error:', e)  # 打印错误