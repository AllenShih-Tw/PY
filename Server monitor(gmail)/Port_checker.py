import socket
from datetime import datetime
from email.mime.text import MIMEText
import smtplib
import atexit
import ssl
import os.path



# #### VARIABLES #### #

# list of servers to check with the following items in the
# definitions per-server: ('hostname', 'ssl or plain', portnumber)
SERVER_LIST = [
    ('10.136.226.107', 'ssl', 443)
]
# Globally define these lists as 'empty' for population later.
SRV_DOWN = []
SRV_UP = []
# Email handling items - email addresses
ADMIN_NOTIFY_LIST = ["allendx123@gmail.com", "allendx1995@gmail.com"]
FROM_ADDRESS = "allendx789@gmail.com"
# Valid Priorities for Mail
LOW = 1
NORMAL = 2
HIGH = 3
# accoount check times
# Begin Execution Here
@atexit.register
def count():
    try:
        r = open("count.txt", "r")
        content = r.read()
    except IOError:
        w = open("count.txt", "w")
        w.write("0")
        w.close()


def _exit():
    print("%s  Server Status Checker Now Exiting." % (current_timestamp()))


def current_timestamp():
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")


def send_server_status_report():
    # Init priority - should be NORMAL for most cases, so init it to that.
    priority = NORMAL
    # Init the send_mail flag.  Ideally, we would be sending mail if this function is
    # called, but we need to make sure that there are cases where it's not necessary
    # such as when there are no offline servers.

    if len(SRV_UP) == 0:

        r = open("count.txt", "r")
        content = r.read()
        Icontent = int(content)
        if Icontent < 3:
            Icontent = Icontent+1
            Scontent = str(Icontent)
            w = open("count.txt", "w")
            w.write(Scontent)
            w.close()
            send_mail = True
            up_str = "Servers online: None!  ***THIS IS REALLY BAD!!!***"
        else:
            send_mail = False
            Icontent = Icontent+1
            Scontent = str(Icontent)
            w = open("count.txt", "w")
            w.write(Scontent)
            w.close()

    else:
        send_mail = True
        up_str = "Servers online: " + ", ".join(SRV_UP)

    if len(SRV_DOWN) == 0:
        r = open("count.txt","r")
        content = r.read()
        Icontent = int(content)
        Icontent = 0
        Scontent = str(Icontent)
        w = open("count.txt", "w")
        w.write(Scontent)
        w.close()
        down_str = "Servers down: None!"
        send_mail = False
    else:
        down_str = "Servers down: " + \
            ", ".join(SRV_DOWN) + \
            "   ***CHECK IF SERVERS LISTED ARE REALLY DOWN!***"
        priority = HIGH

    if len(SRV_UP) == len(SERVER_LIST) and len(SRV_DOWN) == 0:
        priority = LOW
    if send_mail:
        body = """Server Status Report - %s

    %s

    %s""" % (current_timestamp(), down_str, up_str)

        # craft msg base
        msg = MIMEText(body)
        msg['Subject'] = "Server Status Report - %s" % (current_timestamp())
        msg['From'] = FROM_ADDRESS
        msg['Sender'] = FROM_ADDRESS  # This is sort of important...

        if priority == LOW:
            # ThunderBird "Lowest", works with Exchange.
            msg['X-Priority'] = '5'
        elif priority == NORMAL:
            # Plain old "Normal". Works with Exchange.
            msg['X-Priority'] = 'Normal'
        elif priority == HIGH:
            # ThunderBird "Highest", works with Exchange.
            msg['X-Priority'] = '1'

        # Initialize SMTP session variable so it has the correct scope
        # within this function, rather than just inside the 'try' statement.
        smtp = None

        try:
            # SMTP is important, so configure it via Google Mail.
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.starttls()
            smtp.login(FROM_ADDRESS, 'Allendx78789')
        except Exception as e:
            print("Could not correctly establish SMTP connection with Google, error was: %s" % (
                e.__str__()))
            exit()

        for destaddr in ADMIN_NOTIFY_LIST:
            # Change 'to' field, so only one shows up in 'To' headers.
            msg['To'] = destaddr

            try:
                # Actually send the email.
                smtp.sendmail(FROM_ADDRESS, destaddr, msg.as_string())
                print("%s  Status email sent to [%s]." % (
                    current_timestamp(), destaddr))
            except Exception as e:
                print("Could not send message, error was: %s" % (e.__str__()))
                continue

        # No more emails, so close the SMTP connection!
        smtp.close()


def main():
    for (srv, mechanism, port) in sorted(SERVER_LIST):
        # [ 'serverhost' , 'ssl' or 'plain' ]
        print(srv, ", ", mechanism, ", ", port)
        try:
            if mechanism == 'plain':
                # Use a plain text connector for this.
                print("%s  Using Plain for [%s]..." %
                      (current_timestamp(), srv))
                socket.create_connection(
                    ("%s.layerbnc.org" % srv, port), timeout=10)
            elif mechanism == 'ssl':
                # We're going to use an SSL connector for this.
                print("%s  Using SSL for [%s]..." % (current_timestamp(), srv))
                ssl.wrap_socket(socket.create_connection(
                    ("%s" % srv, port), timeout=10))
            else:
                print("%s  Invalid mechanism defined for [%s], skipping..." % (
                    current_timestamp(), srv))
                continue
            SRV_UP.append(srv)
            print("%s  %s: UP" % (current_timestamp(), srv))
        except socket.timeout:
            SRV_DOWN.append(srv)
            print("%s  %s: DOWN" % (current_timestamp(), srv))
            continue
        except Exception as err:
            print("An error occurred: %s" % (err.__str__()))
            exit()

    send_server_status_report()  # Create email to send the status notices.

    exit()  # Exit when done


if __name__ == "__main__":
    print("%s  Server Status Checker Running...." % (current_timestamp()))
    main()
