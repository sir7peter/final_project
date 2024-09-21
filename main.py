# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
from datetime import date
import changeImage
import supplier_image_upload
import run
import reports
import emails

def main(argv):
    images = r'C:\Users\pedro\OneDrive\Documents\Python Google Course\course6_module4\supplier-data\images'
    text = r'C:\Users\pedro\OneDrive\Documents\Python Google Course\course6_module4\supplier-data\descriptions'
    #changeImage.converter(images)
    #supplier_image_upload.upload(images)
    data = run.process_data(text)
    #run.json_file(data,text)
    today = date.today()
    additional_info = '<br/>'.join('name: ' + item['name'] + '<br/>' +
                                   'weight: ' + str(item['weight']) + ' lbs'
                                   + '<br/>' for item in data)
    report_param = {'filename': text + '\\' + 'processed.pdf'
                    ,'title': 'Processed Update on '+today.strftime('%B %d, %Y')
                    ,'paragraph': additional_info}
    reports.generate_report(report_param['filename'],report_param['title'], report_param['paragraph'])

    email_param = {'sender': 'automation@example.com'
                   ,'recipient': 'student@example.com'
                   ,'subject': 'Upload Completed - Online Fruit Store'
                   , 'body': 'All fruits are uploaded to our website successfully. '
                             'A detailed list is attached to this email.'
                   , 'attach': report_param['filename']}
    message = emails.generate_email(email_param['sender'], email_param['recipient'], email_param['subject']
                          ,email_param['body'],email_param['attach'])
    emails.send_email(message)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(sys.argv)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
