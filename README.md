# Hopeless Opus  | ISTE Manipal | Acumen
Hopeless Opus is an online event organised by Acumen, ISTE Manipal in the national level technical festival TechTatva.
Hopeless Opus is a choice-based story based game, where people are supposed to answer aptitude questions to advance further in the story. The choice a person makes in the story based question decides the number of aptitude questions the player answers after that, and also decides the path on which the user goes on.
# Starting the development server
**Step 1:**  Initialize the virtual environment and activate it

`python -m venv env` `source env/bin/activate` (for windows replace bin by Scripts)

**Step 2:** Install the dependencies

`pip install -r requirments.txt` 
(Make sure that the working directory is the same as requirements.txt file)

**Step3 :** Start the development server

`python manage.py runserver`

**Note that if you are using a different database than the SQLite database, you need to change the database setting in settings.py and run the migrations**

# Database Schema for important tables
#### Levels
|  Name | Type   | Description |
| ------------ | ------------ |------------ |
| level  | Integer Field  | Represents the maximum aptitude questions one has to answer on choosing this. This should be unique.|
|  description | Character field  | One word description such as good, medium, bad|
|  points | Integer field  |  Maximum points one gets for choosing this path|

#### Story Questions
|  Name | Type   | Description |
| ------------ | ------------ |------------ |
| question_number  | Integer Field  | Self-explanatory  |
|  question | TextFied  | The text of the question  |

#### Story Options
|  Name | Type   | Description |
| ------------ | ------------ |------------ |
|  question | Foreign key to Story question   | Self-explanatory  |
| level  | Foreign key to level  | Self-explanatory   |
|option  | Text Field  | The text of the option  |
| on_chosen  | Integer Field   | The question number to which a user goes to when he chooses this option |

# Important Files
1. **utils.py  within game app :** This has helper functions to check for end of day and also to get rank of a user.  The **DAYS **Dictionary is designed in such a way that it is self-explanatory. Also,** BRANCHES** is a list of all branched questions. The DAYS dictionary has a key called **branches**, which can be used for keeping a record. It is not used anywhere in evaluating anything.
2. **send_userid_mail.py within user app**:  This is a Django management command, which is used for sending mails to all participants who haven't updated their UserIds yet. To use this, we need to run the command `python manage.py send_userid_mail`. To know more about custom management commands, [click here](https://docs.djangoproject.com/en/3.1/howto/custom-management-commands/ "click here") or [here](https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html "here")


