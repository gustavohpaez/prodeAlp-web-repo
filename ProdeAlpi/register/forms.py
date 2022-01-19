from django import forms 


class Formulario_Ingreso(forms.Form):
    
    nombre = forms.CharField(label="Nombre", max_length=128)
    apellido = forms.CharField(label="Apellido", max_length=128)
    email = forms.EmailField(label="Email")

    EQUIPOS = (
    ("1", "Boca Juniors"),
    ("2", "River Plate"),
    ("3", "Independiente"),
    ("4", "Racing"),
    ("5", "Def y Justicia"),
    ("6", "Talleres"),
    ("7", "Velez"),
    ("8", "Estuduantes (LP)"),
    ("9", "Colon"),
    ("10", "Huracan"),
    ("11", "Lanus"),
    ("12", "Gimnasia (LP)"),
    ("13", "Union"),
    ("14", "Aldosivi"),
    ("15", "Argentinos"),
    ("16", "Rosario Central"),
    ("17", "Godoy Cruz"),
    ("18", "Platense"),
    ("19", "Newells"),
    ("20", "Banfield"),
    ("21", "San Lorenzo"),
    ("22", "Central Cba (SdE)"),
    ("23", "Patronato"),
    ("24", "Sarmiento (J)"),
    ("25", "Atl Tucuman"),
    ("26", "Arsenal"),

    )

    equipo = forms.ChoiceField(choices = EQUIPOS)
    consulta = forms.BooleanField(label="Trabaja en la empresa?", required=False)
    fecha_inicio = forms.DateField(label="Fecha de inicio",widget=forms.DateInput(attrs={"type": "date"})) 



