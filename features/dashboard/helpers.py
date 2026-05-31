from features.staffs.models import Staff
from features.departments.models import Department
from features.documents.models import Document


def getStaffCount():
    return Staff.objects.count()

def getDepartmentCount():
    return Department.objects.count()

def getDocumentCount():
    return Document.objects.count()