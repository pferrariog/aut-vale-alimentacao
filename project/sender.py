from datetime import date
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from glob import glob
from os.path import expanduser
from os.path import join
from pathlib import Path
from shutil import move
from smtplib import SMTP


def mail_sender(username: str, password: str, message: str, order_date: str, to: list) -> None:
    """Send email to managers"""
    # Get files to send
    pdf_files = manipulate_downloaded_files()

    # Create the message object
    msg = MIMEMultipart()
    msg["Subject"] = f"Vale alimentação - {order_date}"
    msg["From"] = username
    msg["To"] = ", ".join(to)
    msg.attach(MIMEText(message))

    # Get attachments
    for file in pdf_files:
        part = MIMEBase("application", "octet-stream")
        with open(file, "rb") as f:
            part.set_payload(f.read())
        encoders.encode_base64(part)
        current_file = Path(__file__).parent / file
        part.add_header("Content-Disposition", "attachment", filename=current_file.name)
        msg.attach(part)

    # Send email
    smtp = SMTP(host="smtp.gmail.com", port=587)
    smtp.starttls()
    smtp.login(username, password)
    smtp.sendmail(username, to, msg.as_string())
    smtp.quit()


def manipulate_downloaded_files() -> list:
    """Move the files to input folder"""
    pdf_files = []
    current_month = date.today().strftime("%Y-%m")
    download_path = rf"{expanduser('~')}\Downloads\*"
    files_in_execution = glob(download_path)
    for file in files_in_execution:
        if "Cartoes_Incluidos" in file or "Boleto Ticket Alimentação" in file:
            filename = file.split("\\")[-1]
            new_file_name = join(f"./input/{current_month}", filename)
            move(file, new_file_name)
            pdf_files.append(new_file_name)
    return pdf_files


if __name__ == "__main__":
    manipulate_downloaded_files()
    mail_sender("", "", "", "", [""])
