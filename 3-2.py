def user_profile(name, surname, birthday, phone, email, city):

    return f" Name - {name} Surname - {surname} Birthday - {birthday} " \
           f"Phone - {phone} Email - {email} City - {city}"
name_var = input("Enter name:")
surname_var = input('Enter surname:')
birthday_var = input('Enter date of birth:')
city_var = input('Enter city:')
phone_var = input('Enter phone number:')
email_var = input('Enter email:')
print('*****************************************')
print(user_profile(name=name_var, surname=surname_var, birthday=birthday_var, city=city_var,
                   phone=phone_var, email=email_var))