# Droits d'auteur : HUSSON CONSULTING SAS - Liberasys
# 2016/09
# Donne en licence selon les termes de l EUPL V.1.1 (EUPL : European Union Public Licence)
# Voir EUPL V1.1 ici : http://ec.europa.eu/idabc/eupl.html
import sys
import getopt
import serial
import copy

from decode_pmepmi import LecturePortSerie



########################################################################
# MAIN
########################################################################


try:
                               
    lien_serie = serial.Serial(port = '/dev/ttyUSB0',
                               baudrate = 1200,
                               #baudrate = 4800,
                               #baudrate = 9600,
                               #baudrate = 19200,
                               #baudrate = 38400,
                               #baudrate = 57600,
                               #baudrate = 115200,
                               bytesize=serial.SEVENBITS,
                               #bytesize=serial.EIGHTBITS,
                               parity=serial.PARITY_EVEN,
                               stopbits=serial.STOPBITS_ONE,
                               #stopbits=serial.STOPBITS_ONE_POINT_FIVE,
                               xonxoff=False,
                               rtscts=False,
                               dsrdtr=False,
                               timeout=1)
    print("Port serie initialise")
except serial.SerialException, e:
    print("Probleme avec le port serie : " + str(e))

# Callback appele quand un octet est recu sur le port serie
def cb_nouvel_octet_recu(octet_recu):
    sys.stdout.write(octet_recu)
    sys.stdout.flush()

# Lecture sur port serie
# instanciation thread serie
lecture_serie = LecturePortSerie(lien_serie, cb_nouvel_octet_recu)
# lancement thread
lecture_serie.run()

