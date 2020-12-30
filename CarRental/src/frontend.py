from tkinter import *
from tkinter import ttk, font



class MainPage:
    def __init__(self, root):
        x = '1150'
        y = '650'


        # --------------------------- FONTS ---------------------------
        label_frame_font    = font.Font(family='times', weight='bold', size=20)
        label_font          = font.Font(family='times', weight='bold', size=12)



        # --------------------------- GUI Variables ---------------------------
        c_name  = StringVar()
        c_phone = StringVar()

        v_vehicleID     = StringVar()
        v_description   = StringVar()
        v_car_type      = StringVar()
        v_car_year      = StringVar()
        v_category      = StringVar()

        r_custID        = StringVar()
        r_vehicleID     = StringVar()
        r_order_date    = StringVar()
        r_pay_date      = StringVar()
        r_start_date    = StringVar()
        r_return_date   = StringVar()
        r_quantity      = StringVar()
        r_rental_type   = StringVar()
        r_total         = StringVar()

        rate_car_type   = StringVar()
        rate_category   = StringVar()
        rate_weekly     = StringVar()
        rate_daily      = StringVar()



        # --------------------------- CALL BACKS ---------------------------
        def on_insert_click():
            pass
            
        def on_view_click():
            pass

        def on_delete_click():
            pass

        def on_update_click():
            pass

        def display_data():
            pass


        # --------------------------- MAIN WINDOW ---------------------------
        self.root = root
        self.root.title('Covid Car Rental')
        self.root.geometry('%sx%s+0+0' % (x,y))
        self.root.config(bg = 'white') 



        # --------------------------- FRAMES AND CANVAS ---------------------------
        self.canvas         = Canvas(self.root, bg='ghost white')
        self.data_frame     = LabelFrame(self.root, bg='ghost white', bd =1, text='Output', font=label_frame_font)        

        self.main_frame     = Frame(self.canvas, bg='ghost white', bd=1, width=100, height=100)

        self.customer_frame = LabelFrame(self.main_frame, bg='ghost white', bd=1, font=label_frame_font, relief=GROOVE, text='Customer')
        self.vehicle_frame  = LabelFrame(self.main_frame, bg='ghost white', bd=1, font=label_frame_font, relief=GROOVE, text='Vehicle')
        self.rental_frame   = LabelFrame(self.main_frame, bg='ghost white', bd=1, font=label_frame_font, relief=GROOVE, text='Rental')
        self.rate_frame     = LabelFrame(self.main_frame, bg='ghost white', bd=1, font=label_frame_font, relief=GROOVE, text='Rate')

        self.canvas         .grid(row=0, column=0, rowspan=8, columnspan=3)
        self.canvas         .create_window((0,0), window=self.main_frame, anchor='nw')

        self.main_frame     .grid(row=0, column=2)
        self.data_frame     .grid(row=0, column=4, padx=100, rowspan=4, columnspan=4)

        self.customer_frame .grid(row=0, column=1, padx=10, pady=10)
        self.vehicle_frame  .grid(row=1, column=1, padx=10, pady=10)
        self.rental_frame   .grid(row=2, column=1, padx=10, pady=10)
        self.rate_frame     .grid(row=3, column=1, padx=10, pady=10)



        # --------------------------- OUTPUT TABLE AND SCROLLBARS ---------------------------
        self.y_scroll           = Scrollbar(self.data_frame, orient=VERTICAL)
        self.x_scroll           = Scrollbar(self.data_frame, orient=HORIZONTAL)
        self.listbox            = Listbox(self.data_frame, 
                                            xscrollcommand=self.x_scroll.set, yscrollcommand=self.y_scroll.set,
                                            width=85, height=35)

        self.y_scroll['command'] = self.listbox.yview
        self.x_scroll['command'] = self.listbox.xview

        self.listbox            .grid(row=0, column=0, sticky=NSEW)
        self.y_scroll           .grid(row=0, column=1, sticky=NS)
        self.x_scroll           .grid(row=1, column=0, sticky=EW)

        # Canvas Scrollbar
        self.scrollbar                  = Scrollbar(self.canvas, command=self.canvas.yview, orient=VERTICAL)
        self.canvas['yscrollcommand']   = self.scrollbar.set

        self.main_frame.bind('<Configure>', 
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox('all')
            )
        )

        self.scrollbar  .grid(row=0, column=0, sticky=NS)



        # --------------------------- CUSTOMER ---------------------------

        # LABELS
        self.lbc_name       = Label(self.customer_frame, font=label_font, text='Name:', bg='ghost white', justify=RIGHT)
        self.lbc_phone      = Label(self.customer_frame, font=label_font, text='Phone:', bg='ghost white', justify=RIGHT)

        # ENTRY BOXES
        self.ec_name        = Entry(self.customer_frame, font=label_font, textvariable=c_name , width=40)
        self.ec_phone       = Entry( self.customer_frame, font=label_font, textvariable=c_phone , width=40 )

        # BUTTONS
        self.btnc_search    = Button(self.customer_frame, text='Search', font=label_font, bd=4, command=on_view_click)
        self.btnc_insert    = Button(self.customer_frame, text='Insert', font=label_font, bd=4, command=on_insert_click)
        self.btnc_delete    = Button(self.customer_frame, text='Delete', font=label_font, bd=4, command=on_delete_click)
        self.btnc_update    = Button(self.customer_frame, text='Update', font=label_font, bd=4, command=on_update_click) 

        # PLACEMENT OF CUSTOMER WIDGETS in self.customer_frame
        self.lbc_name       .grid(row=0, column=0, padx=2, pady=1)
        self.lbc_phone      .grid(row=1, column=0, padx=2, pady=1)

        self.ec_name        .grid(row=0, column=1, padx=4, pady=2, columnspan=3)
        self.ec_phone       .grid(row=1, column=1, padx=4, pady=2, columnspan=3)
        
        self.btnc_search    .grid(row=2, column=0, sticky=NSEW, padx=2, pady=1)
        self.btnc_insert    .grid(row=2, column=1, sticky=NSEW, padx=2, pady=1)
        self.btnc_delete    .grid(row=2, column=2, sticky=NSEW, padx=2, pady=1)
        self.btnc_update    .grid(row=2, column=3, sticky=NSEW, padx=2, pady=1)
        


        # --------------------------- VEHICLE --------------------------- 

        # LABELS 
        self.lbv_id             = Label(self.vehicle_frame, font=label_font, text='Vehicle ID:', bg='ghost white',  justify=RIGHT)
        self.lbv_description    = Label(self.vehicle_frame, font=label_font, text='Description:', bg='ghost white', justify=RIGHT)
        self.lbv_car_year       = Label(self.vehicle_frame, font=label_font, text='Car Year:', bg='ghost white',    justify=RIGHT)
        self.lbv_car_type       = Label(self.vehicle_frame, font=label_font, text='Car Type:', bg='ghost white',    justify=RIGHT)
        self.lbv_category       = Label(self.vehicle_frame, font=label_font, text='Category:', bg='ghost white',    justify=RIGHT)

        # ENTRY BOX
        self.ev_id              = Entry(self.vehicle_frame, font=label_font, textvariable=v_vehicleID,   width=40)
        self.ev_description     = Entry(self.vehicle_frame, font=label_font, textvariable=v_description, width=40)
        self.ev_car_type        = Entry(self.vehicle_frame, font=label_font, textvariable=v_car_type,    width=40)
        self.ev_car_year        = Entry(self.vehicle_frame, font=label_font, textvariable=v_car_year,    width=40)
        self.ev_category        = Entry(self.vehicle_frame, font=label_font, textvariable=v_category,    width=40)

        # BUTTONS
        self.btnv_search        = Button(self.vehicle_frame, text='Search', font=label_font, bd=4, command=on_view_click)
        self.btnv_insert        = Button(self.vehicle_frame, text='Insert', font=label_font, bd=4, command=on_insert_click)
        self.btnv_delete        = Button(self.vehicle_frame, text='Delete', font=label_font, bd=4, command=on_delete_click)
        self.btnv_update        = Button(self.vehicle_frame, text='Update', font=label_font, bd=4, command=on_update_click)

        # PLACEMENT OF VEHICLE WIDGETS IN self.vehicle_frame
        self.lbv_id             .grid(row=0, column=0, padx=2, pady=1)
        self.lbv_description    .grid(row=1, column=0, padx=2, pady=1)
        self.lbv_car_year       .grid(row=2, column=0, padx=2, pady=1)
        self.lbv_car_type       .grid(row=3, column=0, padx=2, pady=1)
        self.lbv_category       .grid(row=4, column=0, padx=2, pady=1)

        self.ev_id              .grid(row=0, column=1, padx=4, pady=2, columnspan=3)
        self.ev_description     .grid(row=1, column=1, padx=4, pady=2, columnspan=3)
        self.ev_car_year        .grid(row=2, column=1, padx=4, pady=2, columnspan=3)
        self.ev_car_type        .grid(row=3, column=1, padx=4, pady=2, columnspan=3)
        self.ev_category        .grid(row=4, column=1, padx=4, pady=2, columnspan=3)

        self.btnv_search        .grid(row=5, column=0, sticky=NSEW, padx=2, pady=1)
        self.btnv_insert        .grid(row=5, column=1, sticky=NSEW, padx=2, pady=1)
        self.btnv_delete        .grid(row=5, column=2, sticky=NSEW, padx=2, pady=1)
        self.btnv_update        .grid(row=5, column=3, sticky=NSEW, padx=2, pady=1)



        # --------------------------- RENTAL ---------------------------

        # LABELS
        self.lbr_custID         = Label(self.rental_frame, font=label_font, text='Customer ID:', bg='ghost white')
        self.lbr_vehicleID      = Label(self.rental_frame, font=label_font, text='Vehicle ID:' , bg='ghost white')
        self.lbr_order_date     = Label(self.rental_frame, font=label_font, text='Order Date:' , bg='ghost white')
        self.lbr_pay_date       = Label(self.rental_frame, font=label_font, text='Pay Date:'   , bg='ghost white')
        self.lbr_start_date     = Label(self.rental_frame, font=label_font, text='Start Date:' , bg='ghost white')
        self.lbr_return_date    = Label(self.rental_frame, font=label_font, text='Return Date:', bg='ghost white')
        self.lbr_quantity       = Label(self.rental_frame, font=label_font, text='Quantity:'   , bg='ghost white')
        self.lbr_rental_type    = Label(self.rental_frame, font=label_font, text='Rental Type:', bg='ghost white')
        self.lbr_total          = Label(self.rental_frame, font=label_font, text='Total:'      , bg='ghost white')

        # ENTRY BOXES
        self.er_custID          = Entry(self.rental_frame, font=label_font, textvariable=r_custID     , width=40)
        self.er_vehicleID       = Entry(self.rental_frame, font=label_font, textvariable=r_vehicleID  , width=40)
        self.er_order_date      = Entry(self.rental_frame, font=label_font, textvariable=r_order_date , width=40)
        self.er_pay_date        = Entry(self.rental_frame, font=label_font, textvariable=r_pay_date   , width=40)
        self.er_start_date      = Entry(self.rental_frame, font=label_font, textvariable=r_start_date , width=40)
        self.er_return_date     = Entry(self.rental_frame, font=label_font, textvariable=r_return_date, width=40)
        self.er_quantity        = Entry(self.rental_frame, font=label_font, textvariable=r_quantity   , width=40)
        self.er_rental_type     = Entry(self.rental_frame, font=label_font, textvariable=r_rental_type, width=40)
        self.er_total           = Entry(self.rental_frame, font=label_font, textvariable=r_total      , width=40)

        # BUTTONS
        self.btnr_search        = Button(self.rental_frame, text='Search', font=label_font, bd=4, command=on_view_click)
        self.btnr_insert        = Button(self.rental_frame, text='Insert', font=label_font, bd=4, command=on_insert_click)
        self.btnr_delete        = Button(self.rental_frame, text='Delete', font=label_font, bd=4, command=on_delete_click)
        self.btnr_update        = Button(self.rental_frame, text='Update', font=label_font, bd=4, command=on_update_click)

        # PLACEMENT OF RENTAL WIDGETS in self.rental_frame
        self.lbr_custID         .grid(row=0, column=0, padx=2, pady=1)
        self.lbr_vehicleID      .grid(row=1, column=0, padx=2, pady=1)
        self.lbr_order_date     .grid(row=2, column=0, padx=2, pady=1)
        self.lbr_pay_date       .grid(row=3, column=0, padx=2, pady=1)
        self.lbr_start_date     .grid(row=4, column=0, padx=2, pady=1)
        self.lbr_return_date    .grid(row=5, column=0, padx=2, pady=1)
        self.lbr_quantity       .grid(row=6, column=0, padx=2, pady=1)
        self.lbr_rental_type    .grid(row=7, column=0, padx=2, pady=1)
        self.lbr_total          .grid(row=8, column=0, padx=2, pady=1)

        self.er_custID          .grid(row=0, column=1, padx=4, pady=2, columnspan=3)
        self.er_vehicleID       .grid(row=1, column=1, padx=4, pady=2, columnspan=3)
        self.er_order_date      .grid(row=2, column=1, padx=4, pady=2, columnspan=3)
        self.er_pay_date        .grid(row=3, column=1, padx=4, pady=2, columnspan=3)
        self.er_start_date      .grid(row=4, column=1, padx=4, pady=2, columnspan=3)
        self.er_return_date     .grid(row=5, column=1, padx=4, pady=2, columnspan=3)
        self.er_quantity        .grid(row=6, column=1, padx=4, pady=2, columnspan=3)
        self.er_rental_type     .grid(row=7, column=1, padx=4, pady=2, columnspan=3)
        self.er_total           .grid(row=8, column=1, padx=4, pady=2, columnspan=3)

        self.btnr_search        .grid(row=9, column=0, sticky=NSEW, padx=2, pady=1)
        self.btnr_insert        .grid(row=9, column=1, sticky=NSEW, padx=2, pady=1)
        self.btnr_delete        .grid(row=9, column=2, sticky=NSEW, padx=2, pady=1)
        self.btnr_update        .grid(row=9, column=3, sticky=NSEW, padx=2, pady=1)



        # --------------------------- RATE ---------------------------
        
        # LABEL
        # Add labels to self.rate_frame the different labels are: 'Car Type', 'Category', 'Weekly', and 'Daily'
        # background color of the labels should be 'ghost white'
        # font should be label_font 
        # self.lbr_custIDr        = Label(self.rate_frame, font=label_font, text='Customer ID:', bg='ghost white')
        # self.lbr_vehicleIDr      = Label(self.rate_frame, font=label_font, text='Vehicle ID:' , bg='ghost white')
        # self.lbr_order_dater     = Label(self.rate_frame, font=label_font, text='Order Date:' , bg='ghost white')
        # l = Label(self.rate_frame, text="Hello", font="-size 50")
        # l.grid()

        # l = Label(self.rate_frame, text="Hello", font="-size 50")
        # l.grid()

        # l = Label(self.rate_frame, text="Hello", font="-size 50")
        # l.grid()
        # # self.lbr_custIDr.grid()
        # self.lbr_vehicleIDr.grid()
        # self.lbr_order_dater.grid()

        # ENTRY BOXES
        # Add entries to the self.rate_frame next to the labels
        # Font should be equal to label_font
        # background color should be 'ghost white'
        # width should be 40 characters
        # assign a special variable (look at 'GUI Variables')


        # BUTTONS
        # PLACEMENT OF RATE WIDGETS IN self.rate_frame



if __name__ == '__main__':
    root = Tk()
    application = MainPage(root)
    root.mainloop()
