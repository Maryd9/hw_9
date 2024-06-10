import time
from pages.registration_page import RegistrationFormPage


def test_student_registration_form():
    registration_page = RegistrationFormPage()
    registration_page.open()
    (
        registration_page
        .fill_first_name('Masha')
        .fill_last_name('Www')
        .fill_user_email('test@gmail.com')
        .fill_gender('Female')
        .fill_user_number('1234456789')
        .fill_day_of_birth('1999', 'May', '11')
        .fill_subject('Maths')
        .fill_hobbies()
        .fill_picture('picture.jpg')
        .fill_current_address('Quitzon Common, South Kraigville')
        .fill_state('NCR')
        .fill_city('Delhi')
        .click_submit()
    )
    registration_page.should_have_registered('Masha Www', 'test@gmail.com', 'Female', '1234456789', '11 May,1999',
                                             'Maths', 'Sports', 'picture.jpg',
                                             'Quitzon Common, South Kraigville', 'NCR Delhi')
