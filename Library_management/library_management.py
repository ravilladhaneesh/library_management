class library_management:

    reg_mem=[]
    books_avail={"ponniyin selvan":1,"hello":1,"kite":1}

    def register_member(self,mem_id,reg_date):
        
        self.mem_id=mem_id
        self.reg_date=reg_date


        if self.mem_id in self.reg_mem:

            s=str(self.mem_id)+" already registered  "

            return s

        else:
            library_management.reg_mem.append(mem_id)

            s=str(self.mem_id)+" is registerd into library on "+str(self.reg_date)

            return s

    def cancel_membership(self,mem_id):

        self.mem_id=mem_id

        if self.mem_id in library_management.reg_mem :

            library_management.reg_mem.remove(self.mem_id)

            s=str(self.mem_id)+" is successfully removed"

            return s

        else:
            s=str(self.mem_id)+ " is not a registered member"

            return s

    def search_a_book(self,book_name):
        self.book_name=book_name

        if self.book_name in library_management.books_avail:

            s="' "+str(self.book_name)+" ' is available "
        
            return s
        else:
            s="' " +str(self.book_name)+ " ' is not availabLE"

            return s

    def retrieve_book(self,mem_id,book_name,reg_date):
        
        self.mem_id=mem_id
        self.book_name=book_name
        self.reg_date=reg_date

        if self.mem_id in library_management.reg_mem:

            if self.book_name in library_management.books_avail :
                if library_management.books_avail[self.book_name]==1:

                    library_management.books_avail[self.book_name]-=1

                    s="' "+str(self.book_name)+" ' is issued to "+str(self.mem_id)

                    return s
                else:
                    s="' "+str(self.book_name)+"' not available at present"

                    return s
            else:
                s="' "+str(self.book_name)+" ' not found"

                return s

        else:

            s=self.mem_id+" is not a  registered member"

            return s
                

    def return_book(self,book_name,return_date):

        self.book_name=book_name
        self.return_date=return_date

        if self.book_name in library_management.books_avail:
            if library_management.books_avail[self.book_name]==0:

                s="' "+self.book_name+" ' returned successfully"

                library_management.books_avail[self.book_name]=1
                return s

            else:
                s="' "+self.book_name+" ' not issued "
        else:
            s="' "+self.book_name+" ' not found"

            return s
            

lib_obj=library_management()

l=[]

print("1. REGISTER A USER   ---FORMAT: OPERATION_ID , MEMBER_ID , DATE_OF_REGISTRATION ")
print("2. REMOVE MEMBERSHIP ---FORMAT: OPERATION_ID , MEMBER_ID ")
print("3. SERACH A BOOK     ---FORMAT: OPERATION_ID , BOOK_NAME ")
print('4. ISSUE A BOOK      ---FORMAT: OPERATION_ID , MEMBER_ID , BOOK_NAME , DATE_OF_ISSUE ')
print("5. RETURN THE BOOK   ---FORMAT: OPERATION_ID , BOOK_NAME , DATE_OF_RETURN ")
print()
print("------------------------ENTER '99' TO EXIT-------------------------------")
print()



while(True):

    inp=input().split(",")
    
    if inp[0]=="99":
        break

    #inp[1]=library_management()
    
    if inp[0]=='1' and len(inp)==3:
        l.append(lib_obj.register_member(inp[1],inp[2]))

    elif inp[0]=='2' :
        l.append(lib_obj.cancel_membership(inp[1]))

    elif inp[0]=='3':
        l.append(lib_obj.search_a_book(inp[1]))

    elif inp[0]=='4':
        l.append(lib_obj.retrieve_book(inp[1],inp[2],inp[3]))

    elif inp[0]=='5':
        l.append(lib_obj.return_book(inp[1],inp[2]))

print()
print("------------------------------------------------------------------------")
print()
for i in l:
    print(i)
    







            
