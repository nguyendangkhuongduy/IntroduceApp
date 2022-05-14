from rest_framework import permissions

employer_role = 'employer'
recruiter_role = 'recruiter'


def check_role(user, role):
    group = None
    if user.groups.exists():
        group = user.groups.first()

        return group.name == role
    else:
        return False


class IsEmployerUser(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return check_role(user=request.user, role=employer_role)


class IsRecruiterUser(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return check_role(user=request.user, role=recruiter_role)




