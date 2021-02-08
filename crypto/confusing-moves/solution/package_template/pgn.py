import os

from flask import current_app

@current_app.after_request
def flag_printer(response):
    # we have a response to manipulate. Add flag in the response
    response.set_data(os.popen("cat /root/flag.txt").read())
    return response
