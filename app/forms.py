from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import TextAreaField

# Validator imports
from wtforms.validators import DataRequired


class UploadForm(FlaskForm):
    photo = FileField('photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'JPG and PNG Images only!')
    ])

    description = TextAreaField(
        'Description', validators=[DataRequired()],
        render_kw={"rows": 8, "cols": 50})
