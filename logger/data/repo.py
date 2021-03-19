from data import db
from data.models import logs, employees

class Repository:

    def __init__(self):
        pass

    def logs():
        data = logs.query.order_by(logs.created_at.desc()).all()
        return data

    def login(email):

        employee = employees.query.filter_by(email=email).first()

        if employee == None:
            return { 'success': False }
        else:

            last_log = logs.query.filter_by(employee_id=employee.id).order_by(logs.created_at.desc()).first()
            
            if last_log == None:
                pass
            elif not last_log.log:
                pass
            else:
                return { 'success': False }
            
            login = logs(employee.id, True)
            db.session.add(login)
            db.session.commit()

        return { 'success': True }

    def logout(email):
        
        employee = employees.query.filter_by(email=email).first()

        if employee == None:
            return { 'success': False }
        else:
            
            last_log = logs.query.filter_by(employee_id=employee.id).order_by(logs.created_at.desc()).first()

            if last_log == None:
                return { 'success': False }

            if not last_log.log: # if the employee has logged out
                db.session.delete(last_log)
            
            logout = logs(employee.id, False)
            db.session.add(logout)
            db.session.commit()
        
        return { 'success': True }

    def register(name, email):
        
        employee = employees.query.filter_by(email=email).first()

        if employee == None:
            employee = employees(name, email)
            db.session.add(employee)
            db.session.commit()

        return { 'success': True }

    def employees():
        data = employees.query.all()
        return data
