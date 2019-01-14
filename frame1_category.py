def frame1_header(frame,p1,p2,p3,row_number):
    objects = []
    head1 = Label(frame,text="Category",font=("ariel",15,"bold"),bd=8)
    head1.grid(row=row_number,column=0)
    head2 = Label(f1,text=p1,font=("ariel",15,"bold"),bd=8)
    head2.grid(row=row_number,column=1)
    head3 = Label(f1,text=p2,font=("ariel",15,"bold"),bd=8)
    head3.grid(row=row_number,column=2)
    head4 = Label(f1,text=p3,font=("ariel",15,"bold"),bd=8)
    head4.grid(row=row_number,column=3)
    head5 = Label(f1,text="Category Winner",font=("ariel",15,"bold"),bd=8)
    head5.grid(row=row_number,column=4)

    objects.append(head1)
    objects.append(head2)
    objects.append(head3)
    objects.append(head4)
    objects.append(head5)

    return objects

def create_row(cat,s1,s2,s3,winner,row_number):
    objects = []
    obj1 = Label(f1,text=cat,bd=8)
    obj1.grid(row=row_number,column=0)
    obj2 = Label(f1,text=str(s1),bd=8)
    obj2.grid(row=row_number,column=1)
    obj3= Label(f1,text=str(s2),bd=8)
    obj3.grid(row=row_number,column=2)
    obj4=Label(f1,text=str(s3),bd=8)
    obj4.grid(row=row_number,column=3)
    obj5= Label(f1,text=str(winner),bd=8)
    obj5.grid(row=row_number,column=4)
    objects.append(obj1)
    objects.append(obj2)
    objects.append(obj3)
    objects.append(obj4)
    objects.append(obj5)
    return objects 