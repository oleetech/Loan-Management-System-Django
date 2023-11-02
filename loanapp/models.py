from django.db import models
from django.contrib.auth.models import User


# User Profile Management
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images', default='default.jpg')
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)
    social_media_links = models.CharField(max_length=255, blank=True)       
    def __str__(self):
        return self.user.username
    
class Customer(models.Model):
    docNo = models.PositiveIntegerField(default=1, unique=True)    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=255)    
    
    def __str__(self):
        return f"{self.docNo}"
    
class CustomersDocument(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/')
    upload_date = models.DateTimeField(auto_now_add=True)  
    def __str__(self):
        return f"{self.customer.docNo}"      

# Loan Product Definition and Configuration
class LoanProduct(models.Model):
    name = models.CharField(max_length=100)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    max_loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name  
    
# Loan Approval Workflow
class Loan(models.Model):
    STATUS_CHOICE = (
        ('1', 'Open'),
        ('2', 'Running'),        
        ('3', 'Closed'),

        
    )    
    stuff = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)    
    product = models.ForeignKey(LoanProduct, on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices=STATUS_CHOICE,default='1')  
    approval_date = models.DateField(blank=True, null=True)
    disbursement_date = models.DateField(blank=True, null=True) 
    
    def save_model(self, request, obj, form, change):
        """Set the `stuff` field to the current user if the user is authenticated."""
        
        if self.status is None:
            

            if request.user.is_authenticated:
                obj.stuff = request.user
            else:
                # Set the `stuff` field to another valid value, such as a default user account.
                obj.stuff = User.objects.get(pk=1)

        super().save_model(request, obj, form, change) 
    
    def __str__(self):
        return str(self.id)  
    
class LoanApproval(models.Model):  
    STATUS_CHOICE = (
    ('1', 'Approved'),
    ('2', 'Not Approved'),        
    ) 
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices=STATUS_CHOICE)


class LoanDistribution(models.Model):  
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    date= models.DateField()   
              
# Loan Repayment Scheduling
class RepaymentSchedule(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    installment_number = models.PositiveIntegerField()
    due_date = models.DateField()
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)   
    
    def __str__(self):
        return str(self.loan)                