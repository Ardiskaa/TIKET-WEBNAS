import smtplib, ssl
import pandas as pd
import time

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

receivers = pd.read_excel('receivers.xlsx', usecols="A, B, C")

sender_email = "invasiudayanatiket3@gmail.com"
password = "tevfogucogvjrkoj"

subject = "D-DAY WEBINAR NASIONAL INFORMATIKA 2023"

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    for i in receivers.index:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["Subject"] = subject

        body = """
        <!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Automata Tiket Webinar</title>

            <style>
                @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500;700;900&display=swap');
                @media (prefers-color-scheme: dark){
                    .section p , .section small{
                        color: black !important;
                    }
                }

                * {
                    font-family: 'Roboto', sans-serif;
                    box-sizing: border-box;
                    padding: 0;
                    margin: 0;
                }

                .container {
                    height: 100vh;
                }

                .header .text {
                    color: white;
                    padding-left: 1.55rem;
                }

                .bodyy {
                    position: relative;
                    top: -2vh;
                }

                .header,
                .footer {
                    background: #dcdce4;
                    background: linear-gradient(90deg, #282624, #8a761a 100%, #00d4ff 0);
                    color: white;
                }

                .section {
                    background: url("https://d33wubrfki0l68.cloudfront.net/static/media/fb1f349208f1d6f59c9a196fdb5dc23cabe80b4e/bg-web.4e83223833905a64c54b.jpg");
                    text-align: justify;
                    line-height: 1.5rem;
                }

                .btn-a {
                    padding: 0.8rem 5rem;
                    background: linear-gradient(90deg, #c9af3b, #6f5f14 100%, #00d4ff 0);
                    color: white !important;
                    border: none;
                    margin: auto !important;
                    text-decoration: none;
                    border-radius: 30px;
                    filter: drop-shadow(4px 4px 4px rgba(0, 0, 0, 0.25));
                }

                .btn-a:hover{
                    opacity: 90%;
                }

                .section-header {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    margin-bottom: 1rem;
                }

                .section-header small {
                    color: gray;
                }

                .footer {
                    text-align: center;
                    color: white;
                    padding-top: 0.5rem;
                    padding-bottom: 0.5rem;
                }
                p{
                    color: black !importt;
                }
            </style>
        </head>

        <body>
            <div class="container">
                <div class="child">
                    <table cellspading='0' cellpading='0' border='0' class='header' width='400px'
                        style='padding: 1rem 3rem; border-left: 2px solid #24200f; border-right: 2px solid #8a761a; border-top-left-radius: 10px !important; border-top-right-radius: 10px !important;'>
                        <tr style="align-items: center;">
                            <td width='90px'>
                                <img src="assets/logowebnas.png"
                                    width="100%" class='ps-4 m-0 p-0 my-auto'>
                            </td>
                            <td width='210px' style='padding-left: 1.5rem;'>
                                <h2>WEBINAR NASIONAL INFORMATIKA</h2>
                                <small>Webinar Nasional</small>
                            </td>
                        </tr>
                    </table>
                    <table class='section' cellspading='0' cellpading='0' border='0' style='padding: 2rem 1.5rem; border-left: 2px solid #f5f5f1; border-right: 2px solid #eaeaf0;'
                        width='400px'>
                        <tr>
                            <td colspan="2" class='bodyy'>
                                <p>
                                    Halo Inovator Muda!🙌
                                </p>
                                <p style='padding-top: 0.5rem;'>
                                    Tidak terasa nih Webinar Nasional Informatika 2023
                                    telah sampai pada hari pelaksanaan. Persiapkan dirimu yaa pada:
                                </p>
                                <p style='padding-top: 0.5rem; text-align: left;'>
                                    📆: <b>Minggu, 14 September 2023</b><br>
                                    🕓: <b>09.00 WITA - selesai</b><br>
                                    🔗: <a href="https://zoom.us/j/97920818097?pwd=NHoyWlQxMHk2QS8wN3NqTFptM2NIdz09">https://zoom.us/j/97920818097?pwd=NHoyWlQxMHk2QS8wN3NqTFptM2NIdz09</a><br>
                                    Meeting ID : 979 2081 8097<br>
                                    Passcode : 732957<br>
                                </p>
                                <p style="padding-top: 0.5rem;">
                                    Nomor Tiket Kamu: <b>Nomor Tiket_Nama</b><br>
                                    Format Nama: <b>Nomor Tiket_Nama</b>
                                </p>
                                <p style="padding-top: 0.5rem; text-align: left;">
                                    Virtual background: <a href="https://bit.ly/VIRTUALBACKGROUNDINVASI2022">https://bit.ly/VIRTUALBACKGROUNDINVASI2022</a><br>
                                    Tata Tertib Peserta: <a href="https://bit.ly/TATATERTIBINVASI2022">https://bit.ly/TATATERTIBINVASI2022</a><br>
                                    Susunan Acara: <a href="https://bit.ly/SUSUNANACARAINVASI2022">https://bit.ly/SUSUNANACARAINVASI2022</a>
                                </p>
                                <p style="padding-top: 0.5rem; text-align: left;">
                                    Dimohon kepada seluruh peserta membaca dan menaati tata tertib tersebut yaa. Terima kasih✨
                                </p>
                                <p style="padding-top: 0.5rem; text-align: left;">
                                    Kami tunggu kehadiranmu, see you!😉🤩<br>
                                    ======================<br>
                                    Webinar Nasional Informatika 2023!<br>
                                </p>
                                <div style="padding-top: 2rem; text-align: center; width: 100%">
                                    <small style = 'color: black !important;'>
                                        <b>
                                            Terdapat kendala? Silakan hubungi contact person berikut.
                                        </b>
                                    </small>

                                </div>
                                <div style='text-align: center; margin-top: 1rem;'>
                                    <a href='https://invasiudayana.com/CpWebnasDanTalkshowInvasi' class='btn-a'>
                                        Contact Person
                                    </a>
                                </div>
                            </td>
                        </tr>
                    </table>
                    <table cellspading='0' class = 'footer' cellpading='0' border='0' width='400px' style = 'border-left: 2px solid #302b12; border-right: 2px solid #8a761a; border-bottom-left-radius: 10px; border-bottom-right-radius: 10px;'>
                        <tr>
                            <td align="center" width = '700px'>
                                <small>&copy; Webinar Nasional informatika 2023</small>
                            </td>
                        </tr>
                    </table>
                </div>
            </div>
        </body>
        </html>
        """

        message.attach(MIMEText(body, "html"))

        # file_send = f"{receivers['nomor'][i]}.png"
        # with open(file_send, "rb") as attachment:
        #     part = MIMEBase("application", "octet-stream")
        #     part.set_payload(attachment.read())

        # encoders.encode_base64(part)

        # part.add_header(
        #     "Content-Disposition",
        #     f"attachment; filename={file_send}"
        # )

        # message.attach(part)
        text = message.as_string()

        server.sendmail(sender_email, receivers['email'][i], text)

        print(f"{receivers['nomor'][i]} - {receivers['email'][i]} send successfully")
        time.sleep(1)
