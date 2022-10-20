from django import forms

from gamesplay.games_play.models import ProfileModel, GameModel


class ProfileModelForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = ProfileModel
        fields = ['email', 'age', 'password']


class GameModelForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = ['title', 'category', 'rating', 'max_level', 'image_url', 'summary']

class GameDeleteForm(GameModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = "__all__"



