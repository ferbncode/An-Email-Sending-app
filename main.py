import smtplib
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class RootApp(App):
    pass
class MainScreen(BoxLayout):
    def next_screen(self):
        self.clear_widgets()
        self.add_widget(NewScreen())
class NewScreen(BoxLayout):
    def prev_screen(self):
        self.clear_widgets()
        self.add_widget(MainScreen())
    def loginScreen(self):
        self.clear_widgets()
        self.add_widget(LogInScreen())
class LogInScreen(BoxLayout):
    def loggedin(self):
        global smtpObj
        smtpObj=smtplib.SMTP('smtp.gmail.com',587)
        em=self.ids['email_id']
        pw=self.ids['password']
        a=smtpObj.ehlo()
        if a[0]==250:
            print("Hello was successful")
        b=smtpObj.starttls()
        if b[0]==220:
            print("TLS encryption is successful")
        c=smtpObj.login(em.text,pw.text)
        if c[0]==235:
            print("Login Successful")
            global email
            email=em.text
        self.clear_widgets()
        self.add_widget(Send_Email())
class Send_Email(BoxLayout):
    def send_email(self):
        recievers=self.ids['reciever']
        sub=self.ids['subject']
        body=self.ids['body']
        checkbox=self.ids['checkbox']
        c=smtpObj.sendmail(email,recievers.text,'Subject:{}\n{}'.format(sub.text,body.text))
        if c=={}:
            print("Email sent")
            checkbox.active=True
            smtpObj.quit()
if __name__=='__main__':
    RootApp().run()
