from django_enumfield.enum import Enum


class CommentHeirarchy(Enum):
    INDIVIDUAL = 1
    PARENT = 2
    CHILD = 3

    labels = {
        INDIVIDUAL: 'Individual',
        PARENT: 'Parent',
        CHILD: 'Child'
    }
