import datetime
from datetime import date


class Tasks():
    def Total_Inactive_Clients_Outreached():
        # User Input For 5 Common Outcomes After Outreaching An Inactive Client
        Close_Account = int(
            input("Total Clients That Want To Close Their Account: "))
        No_Respopnse = int(
            input("Total Clients That Did Not Respond To Outreach: "))
        Keep_Account = int(
            input("Total Clients That Want To Keep Their Account: "))
        Potential_Client = int(
            input("Total Clients That Are Potential Clients: "))
        Business_Closed = int(
            input("Total Clients That Have Closed Their Business: "))
        # Addition Calculation from All the User Inputed Data
        Total = Close_Account + No_Respopnse + \
            Keep_Account + Potential_Client + Business_Closed
        #The Variable Below Can Have Any Number On The Right Operand 
        Total_Clients_From_Weekly_List = 750
        Remaining_Calls = Total_Clients_From_Weekly_List - Total
        # Final Message Result To Give Progress
        print(date.today())
        print("Inactive Clients Outreached So Far: ", Total)
        print("Remaining Inactive Clients To Outreach : ", Remaining_Calls)
        

    def Total_Sales_Made():
        # User Input For Up To 20 Leads Closed Per Day. The Total Closed Leads Can Be Different Per Pay
        Total_Sale_Amount_1 = int(input("Sale #1 Total: "))
        Total_Sale_Amount_2 = int(input("Sale #2 Total: "))
        Total_Sale_Amount_3 = int(input("Sale #3 Total: "))
        Total_Sale_Amount_4 = int(input("Sale #4 Total: "))
        Total_Sale_Amount_5 = int(input("Sale #5 Total: "))
        Total_Sale_Amount_6 = int(input("Sale #6 Total: "))
        Total_Sale_Amount_7 = int(input("Sale #7 Total: "))
        Total_Sale_Amount_8 = int(input("Sale #8 Total: "))
        Total_Sale_Amount_9 = int(input("Sale #9 Total: "))
        Total_Sale_Amount_10 = int(input("Sale #10 Total: "))
        Total_Sale_Amount_11 = int(input("Sale #11 Total: "))
        Total_Sale_Amount_12 = int(input("Sale #12 Total: "))
        Total_Sale_Amount_13 = int(input("Sale #13 Total: "))
        Total_Sale_Amount_14 = int(input("Sale #14 Total: "))
        Total_Sale_Amount_15 = int(input("Sale #15 Total: "))
        Total_Sale_Amount_16 = int(input("Sale #16 Total: "))
        Total_Sale_Amount_17 = int(input("Sale #17 Total: "))
        Total_Sale_Amount_18 = int(input("Sale #18 Total: "))
        Total_Sale_Amount_19 = int(input("Sale #19 Total: "))
        Total_Sale_Amount_20 = int(input("Sale #20 Total: "))
        
        # Addition Of All Total Amount Of Sales
        a = Total_Sale_Amount_1 + Total_Sale_Amount_2 + Total_Sale_Amount_3
        b = Total_Sale_Amount_4 + Total_Sale_Amount_5 + Total_Sale_Amount_6
        c = Total_Sale_Amount_7 + Total_Sale_Amount_8 + Total_Sale_Amount_9
        d = Total_Sale_Amount_10 + Total_Sale_Amount_11 + Total_Sale_Amount_12
        e = Total_Sale_Amount_13 + Total_Sale_Amount_14 + Total_Sale_Amount_15
        f = Total_Sale_Amount_16 + Total_Sale_Amount_17 + Total_Sale_Amount_18
        g = Total_Sale_Amount_19 + Total_Sale_Amount_20 
        
        # Final Result
        print("As of", date.today())
        print("The Total Sales Made is: ")
        print(a + b + c + d + e + f + g)
        

Tasks.Total_Inactive_Clients_Outreached()
Tasks.Total_Sales_Made()