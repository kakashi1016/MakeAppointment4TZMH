# -*- coding:utf-8 -*-
__author__ = 'Qian'


from MyHandlers.Demo import DemoHandler
from MyHandlers.ClinicAppointment import LoginHandler,ValidateHandler,ChooseDroctorHandler

url=[
    (r'/', DemoHandler),
    (r'/Login/', LoginHandler),
    (r'/PatientValidate/', ValidateHandler),
    (r'/ChooseDoctor/', ChooseDroctorHandler),
    (r'/MakeAppointment/', ChooseDroctorHandler),

    ]