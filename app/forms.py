import flask_wtf
import wtforms


class Form(flask_wtf.FlaskForm):
    ask = wtforms.StringField("Your question is: ", [wtforms.validators.required(),
                                                     wtforms.validators.Length(min=3, max=180)])
    submit = wtforms.SubmitField("Ask")
