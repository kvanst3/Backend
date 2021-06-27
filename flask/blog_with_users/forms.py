from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, InputRequired, URL, Email
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class CreateRegisterForm(FlaskForm):
    name = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[Email(), DataRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Register")


class CreateLoginForm(FlaskForm):
    email = StringField("Email", validators=[Email(), DataRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Let me in!")


class CreateCommentForm(FlaskForm):
    comment = CKEditorField("Your comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")