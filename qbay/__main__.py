from qbay import *
from qbay.models import *

from qbay.controllers import *

"""
This file runs the server at a given port
"""

FLASK_PORT = 8081

if __name__ == "__main__":
    app.run(debug=True, port=FLASK_PORT, host='0.0.0.0')


def main():
    while True:
        selection = input(
            'Welcome. Please type 1 to login. '
            'Or type 2 register. Or type 3 to exit')
        selection = selection.strip()
        if selection == '1':
            user = login_page()
            if user:
                print(f'welcome {user.username}')
                break
            else:
                print('login failed')
        elif selection == '2':
            regsiter_page()
        elif selection == '3':
            user = update_page()
            if user:
                print(f'welcome {user.username}')
                break
            else:
                print('update failed')
        elif selection == '4':
            break


if __name__ == '__main__':
    main()