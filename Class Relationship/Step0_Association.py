# How to identify association:
# 1. is one object just using another
# Yes -> possibly association
# 2. If object A is destroyed, can B still exist?
# Yes -> Association/Aggregation
# No -> Composition
# 3. Does A create B?
# Yes -> Not association
# No -> Association/Aggregation

# Example 1: Simple Unidirectional Association
# Scenario: Order -> PaymentGateway
class PaymentGateway:
    def pay(self, amount:float):
        print(f"Paid ${amount}")
    
class Order:
    def __init__(self, gateway: PaymentGateway):
        self.gateway = gateway
    
    def checkout(self):
        self.gateway.pay(100)

# why this is association:
# 1. order uses paymentgateway
# 2. paymentgateway can exist without order
# 3. paymentgateway does not know about order
# 4. no object owns the other

# Example 2: Bidirectional association
# Scenario: Student -> Teacher
class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)

class Student:
    def __init__(self, name):
        self.name = name
        self.teacher = None # Association
    
    def assign_teacher(self, teacher: Teacher):
        self.teacher = teacher
        teacher.add_student(self)
# Why this is association:
# 1. student can exist without a teacher
# 2. teacher can exist without students
# 3. they only reference each other
# 4. lifecycles are independent