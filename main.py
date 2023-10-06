from dbhelper import DBHelper

def main():
    db=DBHelper()
    while True:
        print("*********WELCOME**********")
        print()
        print("PRESS 1 to insert new user")
        print("PRESS 2 to display all user")
        print("PRESS 3 delete user")
        print("PRESS 4 to update user")
        print("PRESS 5 to exit program")
        print()
        try:
            choice=int(input())
            if choice==1:
                #insert_user
                uid=int(input("Enter user id:"))
                username=input("Enter the Name:")
                userphone=input("Enter user Phone:")
                db.insert_user(uid,username,userphone)
                pass
            elif choice==2:
                #Display User
                db.fetch_all()
                pass
            elif choice==3:
                #Delete User
                userid=int(input("Enter the User Id to Which you want to Delete ?"))
                db.delete_user(userid)
                pass
            elif choice==4:
                #Update user
                uid=int(input("Enter user id:"))
                Newname=input("Enter the New name:")
                Newphone=input("Enter user New phone:")
                db.update_user(uid,Newname,Newphone)
                pass
            elif choice==5:
                break
            else:
                print("Invlid Input ! Try again ")
        except Exception as e:
            print(e)
            print("Invalid Details ! Try again")


if __name__=="__main__":
    main()




#main coding


'''helper.insert_user(1322,"Kamal","8565454")
helper.insert_user(452,"Sam","67877798")
helper.insert_user(145,"Shyam","76767978")
helper.insert_user(1432,"Sundar","3647676")
helper.insert_user(1332,"Navin","734787878")'''

#helper.fetch_all()
#helper.delete_user(452)
#helper.fetch_all()
#helper.update_user(1432,'Venkat','1234678')

