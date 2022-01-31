from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.select_place_to_go('Bariloche')
        bot.select_dates(check_in_date='2022-02-15', check_out_date='2022-02-20')
        bot.select_guests(2)
        bot.click_search()
        bot.apply_filters()
        bot.refresh()
        bot.reports_results()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You are trying to run the bot from command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '    set PATH=%PATH%;C:path-to-your-folder \n \n'
            'Linux: \n'
            '    PATH=$PATH:/path/toyour/folder/ \n'
        )
    else:
        raise
