from data import db

class employees(db.Model):
    
    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(100))
    email   = db.Column(db.String(100))

    employees_logs = db.relationship('logs', backref='employee', lazy=True)

    def __init__(self, name, email):
        self.name   = name
        self.email  = email

    def __str__(self):
        return {
            'id'    : self.id,
            'name'  : self.name,
            'email' : self.email
        }

class logs(db.Model):

    id          = db.Column(db.Integer, primary_key=True)
    log         = db.Column(db.Boolean, default=True)
    created_at  = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at  = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)

    def __init__(self, employee_id, log):
        self.employee_id    = employee_id
        self.log            = log

    def __str__(self):
        return {
            'id'            : self.id,
            'log'           : self.log,
            'created_at'    : self.created_at,
            'updated_at'    : self.updated_at,
            'employee_id'   : self.employee_id,
            'name'          : self.employee.name,
            'email'         : self.employee.email
        }
