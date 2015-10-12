# -*- coding:utf-8 -*-


__author__ = 'Qian'


from MyHandlers.Demo import DemoHandler
from MyHandlers.ClinicAppointment import LoginHandler,ValidateHandler,ChooseDroctorHandler, TestHandler
from MyHandlers import AjaxHandler
url=[
    (r'/', DemoHandler),
    (r'/Login/', LoginHandler),
    (r'/PatientValidate/', ValidateHandler),
    (r'/ChooseDoctor/', ChooseDroctorHandler),
    (r'/MakeAppointment/', ChooseDroctorHandler),


    (r'/MakeAppointment/', ChooseDroctorHandler),
    (r'/Test/', TestHandler),


    (r'/Ajax/getPatientsInfo/', AjaxHandler.PatientInfoAjaxHandler),
    (r'/Ajax/getDEPT/',AjaxHandler.DepartmentAjaxHandler ),
    (r'/Ajax/getDoctor/',AjaxHandler.DoctorAjaxHandler ),
    (r'/Ajax/getClinicTime/',AjaxHandler.ClinicTimeAjaxHandler ),


    ]
