# assignmnet

Collection Url:
https://www.getpostman.com/collections/60f8bed43b1edc59e73f


Data Base Tables

| Table Name                     | Purpose                                                                                    |
| ------------------------------ | ------------------------------------------------------------------------------------------ |
| notes                          | To Store comments                                                                          |
| users                          | To Store user related information                                                          |

Table Schema:

Enums:

CommentHeirarchy:
  INDIVIDUAL = 1
  PARENT = 2
  CHILD = 3

1. Notes
    {
      id: <integer: <auto-inc>,
      comments: <TextField>,
      parent_comment: <Foreign Key: Self>,
      commented_by: <Foreign Key: User>,
      comment_date: <DateTimeField>,
      modified_by: <Foreign Key: User>,
      modified_on: <DateTimeField>,
      comment_heirarchy: <EnumField>
    }

2. Users
    {
      id: <integer: <auto-inc>,
      name: <Charfield>,
      email: <Charfiled>,
      mobile_number: <Charfield>
    }

API


1. Get Comments
    URL => /notes/list/
    METHOD => GET
    Response => {...
    }

2.
    URL => /notes/add/
    METHOD => POST and PUT
    request => {...}
    RESPONSE => {...}

3.
    URL => /note/delete/
    METHOD => POST
    Request => {
      ...
    }

