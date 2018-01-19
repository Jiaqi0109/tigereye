from flask import request

from tigereye.api import ApiView
from tigereye.helper.code import Code
from tigereye.models.hall import Hall
from tigereye.models.seat import Seat
from tigereye.extensions.validator import Validator


class HallView(ApiView):

    @Validator(hid=int)
    def seats(self):
        hid = request.args.get('hid')
        hall = Hall.get(hid)
        if not hall:
            return Code.hall_dose_not_exist, request.args
        hall.seats = Seat.query.filter_by(hid=hid).all()
        return hall
