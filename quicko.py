import turtle
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font
import random
import PIL.Image
import PIL.ImageTk
import time
import smtplib, ssl


global is_main_page_destroyed
is_main_page_destroyed = False

def quicko():
    
    def another_menu_page():
        global is_second_main_page_destroyed
        is_second_main_page_destroyed = False
        
        global second_main_page
        treats_menu_page.destroy()
        second_main_page = tk.Tk()
        second_main_page.geometry("600x800")
        second_main_page.title("")
        quicko_second_main_page = PIL.Image.open(r'main_page.png')
        resized_quicko_second_main_page = quicko_second_main_page.resize((600, 800))
    
        img = PIL.ImageTk.PhotoImage(resized_quicko_second_main_page)
        quicko_second_main_page_label = tk.Label(image = img)
        quicko_second_main_page_label.image = img 
        quicko_second_main_page_label.pack()
        quicko_second_main_page_photo = PIL.ImageTk.PhotoImage(file=r'main_page.png')
    
    
        # Beverages button
    
        beverages_button_image = PIL.ImageTk.PhotoImage(file = r'beverages.png')
        beverages_button = tk.Button(second_main_page, image = beverages_button_image,
                                 highlightthickness = 0, bd = 0, command = beverages_page)
        beverages_button.pack()
        beverages_button.place(x = 47, y = 368)
        
        main_page.mainloop()
        
    
    def beverages_page():
        
        def beverage_item_added_successfully():
            messagebox.showinfo("", "Beverage added to cart")
        
        def my_profile_page_for_beverages():
            beverages_menu_page.destroy()
            my_profile_page = tk.Tk()
            my_profile_page.geometry("600x800")
            my_profile_page.title("")
            my_profile_page_image_open = PIL.Image.open(r'my_profile.png')
            resized_my_profile_page = my_profile_page_image_open.resize((600, 800))
            img_my_profile = PIL.ImageTk.PhotoImage(resized_my_profile_page)
            my_profile_page_label = tk.Label(image = img_my_profile)
            my_profile_page_label.image = img_my_profile
            my_profile_page_label.pack()
            my_profile_page.mainloop()
        
        def my_cart_page_for_beverages():
            
            def thank_you_page():
            
                my_cart_page.destroy()
                thank_you_page = tk.Tk()
                thank_you_page.geometry("600x800")
                thank_you_page.title("")
                thank_you_page_image_open = PIL.Image.open(r'thank_you_page.png')
                resized_thank_you_page = thank_you_page_image_open.resize((600, 800))
                img_thank_you_page = PIL.ImageTk.PhotoImage(resized_thank_you_page)
                thank_you_page_label = tk.Label(image = img_thank_you_page)
                thank_you_page_label.image = img_thank_you_page
                thank_you_page_label.pack()
                thank_you_page_label.mainloop()
            
            
            beverages_menu_page.destroy()
            global my_cart_page
            my_cart_page = tk.Tk()
            my_cart_page.geometry("600x800")
            my_cart_page.title("")
            my_cart_page_image_open = PIL.Image.open(r'my_cart_page.png')
            resized_my_cart_page = my_cart_page_image_open.resize((600, 800))
            img_my_cart = PIL.ImageTk.PhotoImage(resized_my_cart_page)
            my_cart_page_label = tk.Label(image = img_my_cart)
            my_cart_page_label.image = img_my_cart
            my_cart_page_label.pack()
        
            # Pay now button
            pay_now_button_image = PIL.ImageTk.PhotoImage(file=r'pay_now_button.png')
            pay_now_button = tk.Button(my_cart_page, image = pay_now_button_image,
                                 highlightthickness = 0, bd = 0, command = thank_you_page)
            pay_now_button.pack()
            pay_now_button.place(x = 200, y = 729)
        
            my_cart_page.mainloop()
            
        global is_main_page_destroyed
        global is_second_main_page_destroyed
        
        if is_second_main_page_destroyed == False:
            second_main_page.destroy()
            is_second_main_page_destroyed = True
        
        elif is_main_page_destroyed == False:
            main_page.destroy()
            is_main_page_destroyed = True
        
        
            
        global beverages_menu_page
        beverages_menu_page = tk.Tk()
        beverages_menu_page.geometry("600x800")
        beverages_menu_page.title("")
        beverages_page = PIL.Image.open(r'beverages_page.png')
        resized_beverages_page = beverages_page.resize((600, 800))
        img_beverage = PIL.ImageTk.PhotoImage(resized_beverages_page)
        beverages_page_label = tk.Label(image = img_beverage)
        beverages_page_label.image = img_beverage
        beverages_page_label.pack()
        
        #My profile button
        
        my_profile_button_image = PIL.ImageTk.PhotoImage(file=r'my_profile_button.png')
        my_profile_button = tk.Button(beverages_menu_page, image = my_profile_button_image,
                                 highlightthickness = 0, bd = 0, command = my_profile_page_for_beverages)
        my_profile_button.pack()
        my_profile_button.place(x = 540, y = 29)
        
        
        #My cart button
        my_cart_button_image = PIL.ImageTk.PhotoImage(file=r'my_cart_button.png')
        my_cart_button = tk.Button(beverages_menu_page, image = my_cart_button_image,
                                 highlightthickness = 0, bd = 0, command = my_cart_page_for_beverages)
        my_cart_button.pack()
        my_cart_button.place(x = 470, y = 22)
        
        
        #Add a beverage button
        
        add_beverage_button_image = PIL.ImageTk.PhotoImage(file=r'plus_symbol.png')
        add_beverage_button = tk.Button(beverages_menu_page, image = add_beverage_button_image,
                                 highlightthickness = 0, bd = 0, command = beverage_item_added_successfully)
        add_beverage_button.pack()
        add_beverage_button.place(x = 132, y = 470)
        beverages_menu_page.mainloop()
        
        
    def treats_page():
        global treats_menu_page
        
        def treat_item_added_successfully():
            messagebox.showinfo("", "Item added to cart")
        
        def my_profile_page_for_treats():
            treats_menu_page.destroy()
            my_profile_page = tk.Tk()
            my_profile_page.geometry("600x800")
            my_profile_page.title("")
            my_profile_page_image_open = PIL.Image.open(r'my_profile.png')
            resized_my_profile_page = my_profile_page_image_open.resize((600, 800))
            img_my_profile = PIL.ImageTk.PhotoImage(resized_my_profile_page)
            my_profile_page_label = tk.Label(image = img_my_profile)
            my_profile_page_label.image = img_my_profile
            my_profile_page_label.pack()
            my_profile_page.mainloop()
            
            
        
        def my_cart_page_for_treats():
            
            def thank_you_page():
            
                my_cart_page.destroy()
                thank_you_page = tk.Tk()
                thank_you_page.geometry("600x800")
                thank_you_page.title("")
                thank_you_page_image_open = PIL.Image.open(r'thank_you_page.png')
                resized_thank_you_page = thank_you_page_image_open.resize((600, 800))
                img_thank_you_page = PIL.ImageTk.PhotoImage(resized_thank_you_page)
                thank_you_page_label = tk.Label(image = img_thank_you_page)
                thank_you_page_label.image = img_thank_you_page
                thank_you_page_label.pack()
                thank_you_page_label.mainloop()
            
            
            treats_menu_page.destroy()
            global my_cart_page
            my_cart_page = tk.Tk()
            my_cart_page.geometry("600x800")
            my_cart_page.title("")
            my_cart_page_image_open = PIL.Image.open(r'my_cart_page.png')
            resized_my_cart_page = my_cart_page_image_open.resize((600, 800))
            img_my_cart = PIL.ImageTk.PhotoImage(resized_my_cart_page)
            my_cart_page_label = tk.Label(image = img_my_cart)
            my_cart_page_label.image = img_my_cart
            my_cart_page_label.pack()
        
            # Pay now button
            pay_now_button_image = PIL.ImageTk.PhotoImage(file=r'pay_now_button.png')
            pay_now_button = tk.Button(my_cart_page, image = pay_now_button_image,
                                 highlightthickness = 0, bd = 0, command = thank_you_page)
            pay_now_button.pack()
            pay_now_button.place(x = 200, y = 729)
        
            my_cart_page.mainloop()
        
        
        main_page.destroy()
        treats_menu_page = tk.Tk()
        treats_menu_page.geometry("600x800")
        treats_menu_page.title("")
        treats_page = PIL.Image.open(r'treats_page.png')
        resized_treats_page = treats_page.resize((600, 800))
        img_treats = PIL.ImageTk.PhotoImage(resized_treats_page)
        treats_page_label = tk.Label(image = img_treats)
        treats_page_label.image = img_treats
        treats_page_label.pack()
        
        #My profile button
        my_profile_button_image = PIL.ImageTk.PhotoImage(file=r'my_profile_button.png')
        my_profile_button = tk.Button(treats_menu_page, image = my_profile_button_image,
                                 highlightthickness = 0, bd = 0, command = my_profile_page_for_treats)
        my_profile_button.pack()
        my_profile_button.place(x = 540, y = 29)
        
        
        #My cart button
        my_cart_button_image = PIL.ImageTk.PhotoImage(file=r'my_cart_button.png')
        my_cart_button = tk.Button(treats_menu_page, image = my_cart_button_image,
                                 highlightthickness = 0, bd = 0, command = my_cart_page_for_treats)
        my_cart_button.pack()
        my_cart_button.place(x = 470, y = 29)
        
        
        #Add item button
        add_item_button_image = PIL.ImageTk.PhotoImage(file=r'plus_symbol.png')
        add_item_button = tk.Button(treats_menu_page, image = add_item_button_image,
                                 highlightthickness = 0, bd = 0, command = treat_item_added_successfully)
        add_item_button.pack()
        add_item_button.place(x = 134, y = 718)
        
        
        back_button_image = PIL.ImageTk.PhotoImage(file=r'back_button.png')
        back_button = tk.Button(treats_menu_page, image = back_button_image,
                                 highlightthickness = 0, bd = 0, command = another_menu_page, relief = "flat")
        back_button.pack()
        back_button.place(x = 47, y = 368)
        
        
        treats_menu_page.mainloop()
        
        
        
    def my_profile_page():
        
        main_page.destroy()
        my_profile_page = tk.Tk()
        my_profile_page.geometry("600x800")
        my_profile_page.title("")
        my_profile_page_image_open = PIL.Image.open(r'my_profile.png')
        resized_my_profile_page = my_profile_page_image_open.resize((600, 800))
        img_my_profile = PIL.ImageTk.PhotoImage(resized_my_profile_page)
        my_profile_page_label = tk.Label(image = img_my_profile)
        my_profile_page_label.image = img_my_profile
        my_profile_page_label.pack()
        my_profile_page.mainloop()
        
        
    
    def my_cart_page():
        
        def thank_you_page():
            
            my_cart_page.destroy()
            thank_you_page = tk.Tk()
            thank_you_page.geometry("600x800")
            thank_you_page.title("")
            thank_you_page_image_open = PIL.Image.open(r'thank_you_page.png')
            resized_thank_you_page = thank_you_page_image_open.resize((600, 800))
            img_thank_you_page = PIL.ImageTk.PhotoImage(resized_thank_you_page)
            thank_you_page_label = tk.Label(image = img_thank_you_page)
            thank_you_page_label.image = img_thank_you_page
            thank_you_page_label.pack()
            thank_you_page_label.mainloop()
            
        
        main_page.destroy()
        global my_cart_page
        my_cart_page = tk.Tk()
        my_cart_page.geometry("600x800")
        my_cart_page.title("")
        my_cart_page_image_open = PIL.Image.open(r'my_cart_page.png')
        resized_my_cart_page = my_cart_page_image_open.resize((600, 800))
        img_my_cart = PIL.ImageTk.PhotoImage(resized_my_cart_page)
        my_cart_page_label = tk.Label(image = img_my_cart)
        my_cart_page_label.image = img_my_cart
        my_cart_page_label.pack()
        
        # Pay now button
        pay_now_button_image = PIL.ImageTk.PhotoImage(file=r'pay_now_button.png')
        pay_now_button = tk.Button(my_cart_page, image = pay_now_button_image,
                                 highlightthickness = 0, bd = 0, command = thank_you_page)
        pay_now_button.pack()
        pay_now_button.place(x = 200, y = 729)
        
        my_cart_page.mainloop()
        
        
    #global main_page
    
    main_page = tk.Tk()
    main_page.geometry("600x800")
    main_page.title("")
    quicko_main_page = PIL.Image.open(r'main_page.png')
    resized_quicko_main_page = quicko_main_page.resize((600, 800))
    
    img = PIL.ImageTk.PhotoImage(resized_quicko_main_page)
    quicko_main_page_label = tk.Label(image = img)
    quicko_main_page_label.image = img 
    quicko_main_page_label.pack()
    quicko_main_page_photo = PIL.ImageTk.PhotoImage(file=r'main_page.png')
    
    
    # Beverages button
    
    beverages_button_image = PIL.ImageTk.PhotoImage(file=r'beverages.png')
    beverages_button = tk.Button(main_page, image = beverages_button_image,
                                 highlightthickness = 0, bd = 0, command = beverages_page, relief = "flat")
    beverages_button.pack()
    beverages_button.place(x = 47, y = 368)
    
    
    # Treats button
    
    treats_button_image = PIL.ImageTk.PhotoImage(file=r'treats.png')
    treats_button = tk.Button(main_page, image = treats_button_image,
                                 highlightthickness = 0, bd = 0, command = treats_page)
    treats_button.pack()
    treats_button.place(x = 250, y = 379)
    
    
    # My Profile button
    
    my_profile_button_image = PIL.ImageTk.PhotoImage(file=r'my_profile_button.png')
    my_profile_button = tk.Button(main_page, image = my_profile_button_image,
                                 highlightthickness = 0, bd = 0, command = my_profile_page)
    my_profile_button.pack()
    my_profile_button.place(x = 540, y = 29)
    
    
    # My Cart button
    
    my_cart_button_image = PIL.ImageTk.PhotoImage(file=r'my_cart_button.png')
    my_cart_button = tk.Button(main_page, image = my_cart_button_image,
                                 highlightthickness = 0, bd = 0, command = my_cart_page)
    my_cart_button.pack()
    my_cart_button.place(x = 440, y = 29)
    


    main_page.mainloop()


quicko()
