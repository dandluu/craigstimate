
from flask import render_template, request, redirect, url_for, session, current_app as app
from app.forms import InputForm, DataForm
from app.states_region import state_region
from app.model import predict_rent


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm()
    
    form.state.choices = [(k.upper()) for k, v in state_region.items()]


    if request.method == 'POST':
        return redirect(url_for('get_data', state=request.form.get('state')))

    
    context = {
        'form' : form,

    }

    return render_template('index.html', **context)


@app.route('/form', methods=['GET', 'POST'])
def get_data():
    form = DataForm()
    context = {
        'form': form,
    }
    if request.method == 'GET':
        state = request.args.get('state').lower()
        
        if state in state_region:
            display = [i.title() for i in state_region[state]]
            values = [i for i in state_region[state]]
            form.region.choices = list(zip(values, display))
        # print(state)
        
        return render_template('form.html', **context, state=state)
        
    
    if request.method == 'POST':
        
        context = {
            'region' : form.region.data,
            'home_type' : form.home_type.data,
            'squarefeet' : int(form.sqfeet.data),
            'beds' : form.bed.data,
            'baths' : form.bath.data,
            'pets' : form.pet.data,
            'smoke' : form.smoke.data,
            'laundry' : form.laundry.data,
            'parking' : form.parking.data,

        }
        # print(context)

        return redirect(url_for('predict', **context))



@app.route('/predict', methods=['GET', 'POST'])
def predict():
    
    '''
    For Predicting and rendering results on HTML 
    '''

    form = InputForm()
    form.state.choices = [(k.upper()) for k, v in state_region.items()]
    

    def get_key(value):
        for k,v in state_region.items():
            for i in v:
                if  value == i:
                    state_name = k
                    return state_name.upper()

    state_name = get_key(request.args['region'])
    region = request.args['region']
    home_type = request.args['home_type'].lower()
    squarefeet = request.args['squarefeet']
    beds = request.args['beds']
    baths = request.args['baths']
    pets = request.args['pets']
    smoke = request.args['smoke']
    laundry = request.args['laundry'].lower()
    parking = request.args['parking'].lower()
    
    features = [region, home_type, squarefeet,
                beds, baths, pets, smoke, laundry, parking]

    prediction = predict_rent(region, home_type, squarefeet, beds, baths, pets, smoke, laundry, parking)

    
    return render_template('index.html', prediction_text=f'{prediction}', features=features, form=form, state_name=state_name)
