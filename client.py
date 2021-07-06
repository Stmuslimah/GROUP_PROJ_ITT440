import socket

def calc_weight(weight):
        if weight < 1:
                price = 5.0
        elif weight >= 1 and weight < 2:
                price = 6.0
        elif weight >= 2 and weight < 3:
                price = 7.0
        elif weight >= 3 and weight < 4:
                price = 8.0
        elif weight >= 4 and weight < 5:
                price = 9.0
        elif weight >= 5 and weight < 6:
                price = 10.0
        else:
                return 0
            
        return price;

def calc_area(area,price):
        
        south = ["NSN","JHR","MLK"]
        north = ["PLS","KDH","PNG","PRK"]
        east = ["KTN","PHG","TRG"]
        central = ["SGR","LBN","KUL","PJY"]
        
        if area in central:
            total = price + 8.0
        elif area in south:
            total = price + 12.0
        elif area in north:
            total = price + 13.0
        elif area in east:
            total = price + 14.0
        elif area == "SWK":
            total = price + 15.0
        elif area == "SBH":
            total = price + 15.0
        else:
            print("Area code not valid.")
            
        return total;
    
def details():
    print("\n\n-Sender information-");
    sender_name = input("Sender name : ");
    sender_add = input("Sender address : ");
    sender_phone = int(input("Sender phone : "));
    
    print("\n\n-Receiver information-");
    receiver_name = input("Receiver name : ");
    receiver_add = input("Receiver address : ");
    receiver_phone = int(input("Receiver phone : "));
    
    return sender_name,sender_add,sender_phone,receiver_name,receiver_add,receiver_phone;
    

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '192.168.56.102'
port = 8888

print('Waiting for connection')
try:
    s.connect((host, port))
except socket.error as e:
    print(str(e))

while True:
    counter = input("Counter : ")
    s.send(str.encode(counter))
    
    file = open('Details.txt','a')
    
    detail = details();
    weight = float(input("\nEnter parcel weight (kg) : ")) ;
    price = calc_weight(weight);
    #s.send(price)
    
    
    print("\nSGR - SELANGOR\nPJY - PUTRAJAYA\nLBN - LABUAN\nKUL - KUALA LUMPUR");
    print("NSN - NEGERI SEMBILAN\nMLK - MELAKA\nJHR - JOHOR");
    print("KDH - KEDAH\nPRK - PERAK\nPNG - PULAU PINANG\nPLS - PERLIS");
    print("KTN - KELANTAN\nPHG - PAHANG\nTRG - TERENGGANU\nSBH - SABAH\nSWK - SARAWAK");
        
        
    area = input("\nEnter code area : ");
    total = calc_area(area,price);
    print("The total price is : RM " + str(total))
    #s.send(str.encode(total))
    
    count = 000;
    if count >= 0:
         x = 100;
    
    x = x + 1;
    combine_code = area + "MY";
    tracking_num = combine_code + str(x);
    x = x + 1;
    print("Tracking Number : " + tracking_num);
    
    break


file.write(f'{detail,area,tracking_num,total}\n')

file.close()

file = open('Details.txt','r')
r = file.read()
s.send(str.encode(r))

s.close()
