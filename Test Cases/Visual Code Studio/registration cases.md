# N1
## Tittle: Successful Registration with New Credentials

## Description: 
The user registers with new credentials and successfully logs into the system.

## Precondition: 
• The user is on the registration page.

## Postcondition: 
• The user is logged into the system.

## Steps to reproduce:
1. Open the website: https://invu.ge/register
2. Fill in the registration form with the following data:
- First Name: Test
- Last Name: Account
- Email: TestAccount@gmail.com
- Password: Test1234
- Confirm Password: Test1234
3. Click the button: "რეგისტრაცია"

## Expected Result: 
The user successfully registers and is redirected into the system.
    

# N2
## Tittle: Registration with an Existing Email Address

## Description: 
The user attempts to register with an existing email address and receives an appropriate error message.

## Precondition: 
• The user is on the registration page.

## Postcondition: 
• The user cannot complete the registration.

## Steps to reproduce:
1. Open the website: https://invu.ge/register
2. Fill in the registration form with the following data:
- First Name: Test
- Last Name: Account
- Email: TestAccount@gmail.com
- Password: Test1234
- Confirm Password: Test1234
3. Click the button: "რეგისტრაცია"

## Expected Result: 
The system notifies the user that the email address is already in use.



# N3 
## Tittle: Registration with Different Passwords

## Description: 
The user attempts to register using different passwords and receives an appropriate error message.

## Precondition: 
• The user is on the registration page.

## Postcondition: 
• The user cannot complete the registration.

## Steps to reproduce:
1. Open the website: https://invu.ge/register
2. Fill in the registration form with the following data:
- First Name: Test
- Last Name: Account
- Email: testacc@gmail.com
- Password: Test123
- Confirm Password: test1
3. Click the button: "რეგისტრაცია"

## Expected Result: 
The system notifies the user that the passwords do not match.



# N4
## Tittle: Registration with Empty Fields

## Description: 
The user attempts to register with empty fields and receives an appropriate error message.

## Precondition: 
• The user is on the registration page.

## Postcondition: 
• The user cannot complete the registration.

## Steps to reproduce:
1. Open the website: https://invu.ge/register
2. Leave the registration fields empty
3. Click the button: "რეგისტრაცია"

## Expected Result: 
The system notifies the user that all fields are required.


N5
## Tittle: Registration with a Google Account

## Description: 
The user registers with a Google account and successfully logs into the system.

## Precondition: 
• The user is on the registration page.

## Postcondition: 
• The user is logged into the system.

## Steps to reproduce:
1. Open the website: https://invu.ge/register
2. Click the button: "Continue with Google"
3. Select a Google account for registration
4. Complete the registration process using the Google account

## Expected Result: 
The user successfully registers and is redirected into the system.
