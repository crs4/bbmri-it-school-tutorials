import datetime
import socket
import uuid

from hl7apy.parser import parse_message


def query(host, port):
    msg = \
        'MSH|^~\&|PDQ_Consumer|Consumer_Facility|PDQ_Supplier|Supplier_Facility|20250707103000||QBP^Q22^QBP_Q21|123456|T|2.5.1\r' \
        'QPD|Q22^Find Candidates^HL7|QRY12345|@PID.5.1.1^Smith~@PID.5.2^Amy\r' \
        'RCP|I|10^RD'
    # establish the connection
    parsed_message = parse_message(msg)
    parsed_message.msh.sending_application = 'BBMRI-IT-SCHOOL-APP'
    parsed_message.msh.sending_facility = 'BBMRI-IT-SCHOOL-PDQ-CONS'
    parsed_message.msh.receiving_application = 'ARS_APP'
    parsed_message.msh.receiving_facility = 'ARS_PDQ_SUPPL'
    parsed_message.msh.date_time_of_message = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    parsed_message.msh.msh_10 = str(uuid.uuid4())
    parsed_message.qpd.qpd_1 = "IHE PDQ Query"
    parsed_message.qpd.qpd_2 = str(uuid.uuid4())
    parsed_message.qpd.qpd_3 = 'Q22^Find Candidates^HL7'

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((host, port))
        # send the message
        sock.sendall(parsed_message.to_mllp().encode('UTF-8'))
        # receive the answer
        received = sock.recv(1024 * 1024)
        return received
    finally:
        sock.close()


if __name__ == '__main__':
    res = query('localhost', 6662)
    print("Received response: ")
    print(repr(res))
