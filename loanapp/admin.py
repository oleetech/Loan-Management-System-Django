from django.contrib import admin
from django import forms
# Register your models here.

from .models import UserProfile
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    
    list_display = ['user', 'image']
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    image_tag.short_description = 'Image'  
    
    
from .models import Customer
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'docNo': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance.pk:
            last_order = Customer.objects.order_by('-docNo').first()
            if last_order:
                next_order_number = last_order.docNo + 1
            else:
                next_order_number = 1

            self.initial['docNo'] = next_order_number
                    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin): 
    list_display = ['docNo','first_name', 'last_name']    
    form= CustomerForm  
    
from .models import CustomersDocument
class CustomersDocumentForm(forms.ModelForm):
    class Meta:
        model = CustomersDocument
        fields = '__all__'

                    
@admin.register(CustomersDocument)
class CustomersDocumentAdmin(admin.ModelAdmin): 
    list_display = ['customer','title', 'file']    
    form= CustomersDocumentForm     
    
    
from .models import LoanProduct
class LoanProductForm(forms.ModelForm):
    class Meta:
        model = LoanProduct
        fields = '__all__'

                    
@admin.register(LoanProduct)
class LoanProductAdmin(admin.ModelAdmin): 
    list_display = ['name','interest_rate', 'max_loan_amount']    
    form= LoanProductForm       
    
    
from .models import Loan
class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['stuff','customer','product','status', 'approval_date']    
    form= LoanForm         



from .models import LoanApproval
class LoanApprovalForm(forms.ModelForm):
    class Meta:
        model = LoanApproval
        fields = '__all__'
@admin.register(LoanApproval)
class LoanApprovalAdmin(admin.ModelAdmin):
    list_display = ['loan', 'status']
    form = LoanApprovalForm



from .models import LoanDistribution
class LoanDistributionForm(forms.ModelForm):
    class Meta:
        model = LoanDistribution
        fields = '__all__'

@admin.register(LoanDistribution)
class LoanDistributionAdmin(admin.ModelAdmin):
    list_display = ['loan', 'date']
    form = LoanDistributionForm



from .models import RepaymentSchedule
class RepaymentScheduleForm(forms.ModelForm):
    class Meta:
        model = RepaymentSchedule
        fields = '__all__'

@admin.register(RepaymentSchedule)
class RepaymentScheduleAdmin(admin.ModelAdmin):
    list_display = ['loan', 'installment_number', 'due_date', 'amount_due']
    form = RepaymentScheduleForm 
