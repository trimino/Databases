from tkinter import *
from tkinter import ttk, font



class MainPage:
    def __init__(self, root):
        x = '1100'
        y = '700'


        # FONTS 
        label_frame_font    = font.Font(family='times', weight='bold', size=20)
        label_font          = font.Font(family='times', weight='bold', size=12)

        # GUI Variables 
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



        # CALL BACKS 
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


        # MAIN WINDOW 
        self.root = root
        self.root.title('Covid Car Rental')
        self.root.geometry('%sx%s+0+0' % (x,y))
        self.root.config(bg = 'white') 



        # FRAMES AND CANVAS
        main_frame      = Frame(self.root, bg='ghost white', bd=1)
        data_frame      = LabelFrame(self.root, bg='ghost white', bd =1, text='Output', font=label_frame_font)

        canvas          = Canvas(main_frame, bg='ghost white', width=600, height=700)

        customer_frame  = LabelFrame(canvas, bg='ghost white', bd=1, font=label_frame_font, relief=GROOVE, text='Customer')
        vehicle_frame   = LabelFrame(canvas, bg='ghost white', bd=1, font=label_frame_font, relief=GROOVE, text='Vehicle')
        rental_frame    = LabelFrame(canvas, bg='ghost white', bd=1, font=label_frame_font, relief=GROOVE, text='Rental')
        rate_frame      = LabelFrame(canvas, bg='ghost white', bd=1, font=label_frame_font, relief=GROOVE, text='Rate')

        main_frame      .grid()
        data_frame      .grid(row=0, column=1, padx=75, rowspan=4, columnspan=4)
        canvas          .grid(row=0, column=0, rowspan=3, columnspan=3)
        #customer_frame  .grid(row=0, column=0, padx=10, pady=10)
        # # vehicle_frame   .grid(row=1, column=0, padx=10, pady=10)
        # # rental_frame    .grid(row=2, column=0, padx=10, pady=10)
        # # rate_frame      .grid(row=3, column=0, padx=10, pady=10)

        canvas.create_window(625, 0, window=customer_frame)
        # canvas.create_window(200, 200, window=vehicle_frame)
        # canvas.create_window(500, 500, window=rental_frame)
        # canvas.create_window(900, 900, window=rate_frame)



        # OUTPUT TABLE AND SCROLLBARS (For data_frame and the canvas)
        # self.y_scroll = Scrollbar(data_frame, orient=VERTICAL)
        # self.x_scroll = Scrollbar(data_frame, orient=HORIZONTAL)

        # self.listbox = Listbox(data_frame, 
        #                         xscrollcommand=self.x_scroll.set, yscrollcommand=self.y_scroll.set,
        #                         width=85, height=35)

        # self.y_scroll['command'] = self.listbox.yview
        # self.x_scroll['command'] = self.listbox.xview

        # self.listbox.grid(row=0, column=0, sticky=NSEW)
        # self.y_scroll.grid(row=0, column=1, sticky=NS)
        # self.x_scroll.grid(row=1, column=0, sticky=EW)

        # self.ef_y_scroll = Scrollbar(canvas, orient=VERTICAL, command=canvas.yview)
        # self.ef_y_scroll.grid(row=0, column=5, sticky=NS)
        # canvas['yscrollcommand'] = self.ef_y_scroll.set
        # canvas.configure( scrollregion=(0, 0, 200, 1000))



        # CUSTOMER LABELS, ENTRY AND BUTTONS
        self.lbc_name   = Label(customer_frame, font=label_font, text='Name:', bg='ghost white', justify=RIGHT)
        self.lbc_phone  = Label(customer_frame, font=label_font, text='Phone:', bg='ghost white', justify=RIGHT)

        self.ec_name    = Entry(customer_frame, font=label_font, textvariable=c_name , width=40)
        self.ec_phone   = Entry( customer_frame, font=label_font, textvariable=c_phone , width=40 )

        self.btnc_search = Button(customer_frame, text='Search', font=label_font, bd=4, command=on_view_click)
        self.btnc_insert = Button(customer_frame, text='Insert', font=label_font, bd=4, command=on_insert_click)
        self.btnc_delete = Button(customer_frame, text='Delete', font=label_font, bd=4, command=on_delete_click)
        self.btnc_update = Button(customer_frame, text='Update', font=label_font, bd=4, command=on_update_click) 

        self.lbc_name   .grid(row=0, column=0, padx=2, pady=1)
        self.lbc_phone  .grid(row=1, column=0, padx=2, pady=1)
        self.ec_name    .grid(row=0, column=1, padx=4, pady=2, columnspan=3)
        self.ec_phone   .grid(row=1, column=1, padx=4, pady=2, columnspan=3)

        self.btnc_search.grid(row=2, column=0, sticky=NSEW, padx=2, pady=1)
        self.btnc_insert.grid(row=2, column=1, sticky=NSEW, padx=2, pady=1)
        self.btnc_delete.grid(row=2, column=2, sticky=NSEW, padx=2, pady=1)
        self.btnc_update.grid(row=2, column=3, sticky=NSEW, padx=2, pady=1)
        


        # VEHICLE LABEL, ENTRY AND BUTTONS
        self.lbv_id          = Label(vehicle_frame, font=label_font, text='Vehicle ID:', bg='ghost white', justify=RIGHT)
        self.lbv_description = Label(vehicle_frame, font=label_font, text='Description:', bg='ghost white', justify=RIGHT)
        self.lbv_car_year    = Label(vehicle_frame, font=label_font, text='Car Year:', bg='ghost white', justify=RIGHT)
        self.lbv_car_type    = Label(vehicle_frame, font=label_font, text='Car Type:', bg='ghost white', justify=RIGHT)
        self.lbv_category    = Label(vehicle_frame, font=label_font, text='Category:', bg='ghost white', justify=RIGHT)

        self.ev_id              = Entry(vehicle_frame, font=label_font, textvariable=v_vehicleID,   width=40)
        self.ev_description     = Entry(vehicle_frame, font=label_font, textvariable=v_description, width=40)
        self.ev_car_type        = Entry(vehicle_frame, font=label_font, textvariable=v_car_type,    width=40)
        self.ev_car_year        = Entry(vehicle_frame, font=label_font, textvariable=v_car_year,    width=40)
        self.ev_category        = Entry(vehicle_frame, font=label_font, textvariable=v_category,    width=40)

        self.btnv_search = Button(vehicle_frame, text='Search', font=label_font, bd=4, command=on_view_click)
        self.btnv_insert = Button(vehicle_frame, text='Insert', font=label_font, bd=4, command=on_insert_click)
        self.btnv_delete = Button(vehicle_frame, text='Delete', font=label_font, bd=4, command=on_delete_click)
        self.btnv_update = Button(vehicle_frame, text='Update', font=label_font, bd=4, command=on_update_click)

        self.lbv_id         .grid(row=0, column=0, padx=2, pady=1)
        self.lbv_description.grid(row=1, column=0, padx=2, pady=1)
        self.lbv_car_year   .grid(row=2, column=0, padx=2, pady=1)
        self.lbv_car_type   .grid(row=3, column=0, padx=2, pady=1)
        self.lbv_category   .grid(row=4, column=0, padx=2, pady=1)
        self.ev_id          .grid(row=0, column=1, padx=4, pady=2, columnspan=3)
        self.ev_description .grid(row=1, column=1, padx=4, pady=2, columnspan=3)
        self.ev_car_year    .grid(row=2, column=1, padx=4, pady=2, columnspan=3)
        self.ev_car_type    .grid(row=3, column=1, padx=4, pady=2, columnspan=3)
        self.ev_category    .grid(row=4, column=1, padx=4, pady=2, columnspan=3)

        self.btnv_search.grid(row=5, column=0, sticky=NSEW, padx=2, pady=1)
        self.btnv_insert.grid(row=5, column=1, sticky=NSEW, padx=2, pady=1)
        self.btnv_delete.grid(row=5, column=2, sticky=NSEW, padx=2, pady=1)
        self.btnv_update.grid(row=5, column=3, sticky=NSEW, padx=2, pady=1)



        # RENTAL LABELS, ENTRY AND BUTTONS
        self.lbr_custID         = Label(rental_frame, font=label_font, text='Customer ID:', bg='ghost white')
        self.lbr_vehicleID      = Label(rental_frame, font=label_font, text='Vehicle ID:' , bg='ghost white')
        self.lbr_order_date     = Label(rental_frame, font=label_font, text='Order Date:' , bg='ghost white')
        self.lbr_pay_date       = Label(rental_frame, font=label_font, text='Pay Date:'   , bg='ghost white')
        self.lbr_start_date     = Label(rental_frame, font=label_font, text='Start Date:' , bg='ghost white')
        self.lbr_return_date    = Label(rental_frame, font=label_font, text='Return Date:', bg='ghost white')
        self.lbr_quantity       = Label(rental_frame, font=label_font, text='Quantity:'   , bg='ghost white')
        self.lbr_rental_type    = Label(rental_frame, font=label_font, text='Rental Type:', bg='ghost white')
        self.lbr_total          = Label(rental_frame, font=label_font, text='Total:'      , bg='ghost white')

        self.er_custID        = Entry(rental_frame, font=label_font, textvariable=r_custID     , width=40)
        self.er_vehicleID     = Entry(rental_frame, font=label_font, textvariable=r_vehicleID  , width=40)
        self.er_order_date    = Entry(rental_frame, font=label_font, textvariable=r_order_date , width=40)
        self.er_pay_date      = Entry(rental_frame, font=label_font, textvariable=r_pay_date   , width=40)
        self.er_start_date    = Entry(rental_frame, font=label_font, textvariable=r_start_date , width=40)
        self.er_return_date   = Entry(rental_frame, font=label_font, textvariable=r_return_date, width=40)
        self.er_quantity      = Entry(rental_frame, font=label_font, textvariable=r_quantity   , width=40)
        self.er_rental_type   = Entry(rental_frame, font=label_font, textvariable=r_rental_type, width=40)
        self.er_total         = Entry(rental_frame, font=label_font, textvariable=r_total      , width=40)

        self.btnr_search = Button(rental_frame, text='Search', font=label_font, bd=4, command=on_view_click)
        self.btnr_insert = Button(rental_frame, text='Insert', font=label_font, bd=4, command=on_insert_click)
        self.btnr_delete = Button(rental_frame, text='Delete', font=label_font, bd=4, command=on_delete_click)
        self.btnr_update = Button(rental_frame, text='Update', font=label_font, bd=4, command=on_update_click)

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

        self.btnr_search.grid(row=9, column=0, sticky=NSEW, padx=2, pady=1)
        self.btnr_insert.grid(row=9, column=1, sticky=NSEW, padx=2, pady=1)
        self.btnr_delete.grid(row=9, column=2, sticky=NSEW, padx=2, pady=1)
        self.btnr_update.grid(row=9, column=3, sticky=NSEW, padx=2, pady=1)



        # RATE LABEL, ENTRY AND BUTTONS
        # Add labels to rate_frame the different labels are: 'Car Type', 'Category', 'Weekly', and 'Daily'
        # background color of the labels should be 'ghost white'
        # font should be label_font 
        self.lbrate_car_type = Label(rate_frame, font=label_font, text='Car Type:', bg='ghost white')
        self.lbrate_category = Label(rate_frame, font=label_font, text='Category:', bg='ghost white')
        self.lbrate_weekly   = Label(rate_frame, font=label_font, text='Weekly:'  , bg='ghost white')
        self.lbrate_daily    = Label(rate_frame, font=label_font, text='Daily:'    , bg='ghost white')


        # Add entries to the rate_frame next to the labels
        # Font should be equal to label_font
        # background color should be 'ghost white'
        # width should be 40 characters
        # assign a special variable (look at 'GUI Variables')


        # show on the screen by using the grid()
        self.lbrate_car_type.grid( row=0, column=0, padx=2, pady=2 )
        self.lbrate_category.grid( row=1, column=0, padx=2, pady=2 )
        self.lbrate_weekly  .grid( row=2, column=0, padx=2, pady=2 )
        self.lbrate_daily   .grid( row=3, column=0, padx=2, pady=2 )

if __name__ == '__main__':
    root = Tk()
    application = MainPage(root)
    root.mainloop()