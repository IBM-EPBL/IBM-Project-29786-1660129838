import ibm_db
hostname=""
uid=""
pwd=""
driver="{IBM DB2 ODBC DRIVER}"
db="bludb"
port=""
protocol="TCPIP"
cert="Certificate.crt"
dsn=(
     "DATABASE={0};"
     "HOSTNAME={1};"
     "PORT={2};"
     "UID={3};"
     "SECURITY=SSL;"
     "SSLServerCertificate={4};"
     "PWD={5};"
     ).format(db,hostname,port,uid,cert,pwd)
print(dsn)
try:
    db2=ibm_db.connect(dsn,"","")
    print("connected to data base")
except:
    print("Unable to connect",ibm_db.conn_errormsg())
